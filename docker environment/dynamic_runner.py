import pandas as pd
import subprocess
import time
from utils.initialization_functions import *
import os
import sys

df = pd.read_excel("containers_list.xlsx")
df.columns = df.columns.str.strip().str.lower()  

#clean_all()

# Ottieni UID e GID dell'utente corrente
my_uid = os.getuid()
my_gid = os.getgid()

# Imposta variabili d'ambiente
os.environ['MYUID'] = str(my_uid)
os.environ['MYGID'] = str(my_gid)


# Preleva il parametro da linea di comando
if len(sys.argv) < 2 or sys.argv[1] not in ["1", "2", "3", "4", "5"]:
    sys.exit(1)

test_param = sys.argv[1]

if test_param == "1":
    output_dir = "./output_og"
    vp_dir = "./VP-Dataset_og"
    data_dir = "./resources/data/data_og"
    coverage_dir = "./coverage_og"
elif test_param == "2":
    output_dir = "./output_Llama-3_1"
    vp_dir= "./VP-Dataset_Llama-3_1"
    data_dir = "./resources/data/data_Llama-3_1"
    coverage_dir = "./coverage_Llama-3_1"
elif test_param == "3":
    output_dir = "./output_GPT-4o"
    vp_dir= "./VP-Dataset_GPT-4o"
    data_dir = "./resources/data/data_GPT-4o"
    coverage_dir = "./coverage_GPT-4o"
elif test_param == "4":
    output_dir = "./output_Phi-3_5"
    vp_dir= "./VP-Dataset_Phi-3_5"
    data_dir = "./resources/data/data_Phi-3_5"
    coverage_dir = "./coverage_Phi-3_5"
elif test_param == "5":
    output_dir = "./output_Qwen-2_5"
    vp_dir= "./VP-Dataset_Qwen-2_5"
    data_dir = "./resources/data/data_Qwen-2_5"
    coverage_dir = "./coverage_Qwen-2_5"    
       
else:
    raise ValueError(f"Parametro TEST_PARAM non valido: {test_param}")
if not os.path.isdir(vp_dir):
    raise FileNotFoundError(f"La directory {vp_dir} non esiste")


for _, row in df.iterrows():
    script_name = row["script_py"]
    use_docker = str(row["docker"]).strip().lower() == "yes"
    status = "OK"
    container_field = str(row.get("container_name", "")).strip()

    # Multi-container
    containers = [c.strip() for c in container_field.split(",") if c.strip()] if use_docker else []
    output = ""
    
    try:
        for container in containers:
            print(f"➡️  Avvio container: {container}")
            subprocess.run(["docker", "start", container], check=True)
        if containers:
            time.sleep(3)
            
        #Per questi script c'è bisogno di catturare i pacchetti inviati    
        if script_name in ["train10", "train30", "train34", "dev6"]:
            if script_name == "train10":           
                docker_command = [
                    "docker", "run", "--rm", "-d", "-it",
                    "--name", "udp_listener",
                    "--network", "udp_net",
                    "--ip", "192.168.99.2",
                    "-v", f"{os.getcwd()}/resources/data/{script_name}:/data",
                    "alpine",
                    "sh", "-c", "apk update && apk add tcpdump && timeout 170 tcpdump -i any port 514 -w /data/capture.pcap"
                ]
            
            if script_name == "train30":           
                docker_command = [
                    "docker", "run", "--rm", "-d", "-it",
                    "--name", "udp_listener",
                    "--network", "udp_net",
                    "--ip", "192.168.99.2",
                    "-v", f"{os.getcwd()}/resources/data/{script_name}:/data",
                    "kalilinux/kali-rolling",
                    "bash", "-c",
                    "echo 'Acquire::AllowInsecureRepositories \"true\";' > /etc/apt/apt.conf.d/99insecure && "
                    "apt update && "
                    "apt install -y --allow-unauthenticated tcpdump && "
                    "timeout 100 tcpdump -U -i any port 518 or port 635 -w /data/capture.pcap"
                ]
    
            if script_name == "train34":           
                docker_command = [
                    "docker", "run", "--rm", "-d", "-it",
                    "--name", "udp_listener",
                    "--network", "udp_net",
                    "--ip", "192.168.99.2",
                    "-v", f"{os.getcwd()}/resources/data/{script_name}:/data",
                    "debian:latest",
                    "bash", "-c",
                    "apt update && apt install -y tcpdump && "
                    "timeout 170 tcpdump -U -i any port 513 -nn -X -w /data/capture.pcap"
                ]

            if script_name == "dev6":           
                docker_command = [
                    "docker", "run", "--rm", "-d", "-it",
                    "--name", "udp_listener",
                    "--network", "udp_net",
                    "--ip", "192.168.99.2",
                    "-v", f"{os.getcwd()}/resources/data/{script_name}:/data",
                    "kalilinux/kali-rolling",
                    "bash", "-c",
                    "echo 'Acquire::AllowInsecureRepositories \"true\";' > /etc/apt/apt.conf.d/99insecure && "
                    "apt update && "
                    "apt install -y --allow-unauthenticated tcpdump && "
                    "timeout 170 tcpdump -U -i any port 7 or port 10080 -X -w /data/capture.pcap"
                ]

            subprocess.run(docker_command, check=True)
            time.sleep(5)
            
        env = os.environ.copy()
        env["TEST_PARAM"] = test_param
        env["COVERAGE_ID"] = script_name
        env["OUTPUT_DIR"] = output_dir
        env["VP_DIR"] = vp_dir
        env["DATA_DIR"] = data_dir
        env["COVERAGE_DIR"] = coverage_dir
        
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(data_dir , exist_ok=True)
        os.makedirs(coverage_dir , exist_ok=True)
            
        print(f"▶️  Eseguo script: {script_name}")      
        subprocess.run(["docker", "compose", "-f", "docker-sandbox.yml", "up", f"{script_name}"], check=True, env=env)

    except subprocess.CalledProcessError as e:
        print(f"❌ Errore eseguendo {script_name}: {e}")
        status = "Errore"


    finally:
        if script_name in ["train10", "train30", "train34", "dev6"]:
            subprocess.run(["docker", "wait", "udp_listener"])
            
        status = subprocess.run(["docker", "ps", "-q"], capture_output=True, text=True)
        container_ids = status.stdout.strip().split("\n")
        container_ids = [cid for cid in container_ids if cid]
        
        if container_ids:
            subprocess.run(["docker", "stop"] + container_ids, check=True)
        print()
        
subprocess.run("sudo chown -R $USER:$USER ./", shell=True)
