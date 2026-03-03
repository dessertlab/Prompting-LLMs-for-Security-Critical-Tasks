import importlib.util
import inspect
import pandas as pd
import pyshark
import os
import ast
import subprocess
from scapy.all import *
import tomllib
import ipaddress

from utils.mappings import *

#Funzione per creare pacchetti a partire dai dati
def is_valid_ipv4(addr):
    try:
        ipaddress.IPv4Address(addr)
        return True
    except:
        return False
        
def create_pkt(py_file, case):
    try:
        if not (is_valid_ipv4(case['src']) and is_valid_ipv4(case['dst'])):
            print(f"[WARNING] IP non validi: src={case['src']}, dst={case['dst']} — passo oltre")
            return None    
    
            pkt = None
            
        if py_file == "test4":
            pkt = IP(src=case['src'], dst=case['dst']) / \
                  UDP(sport=case['sport'], dport=case['dport']) / \
                  DNS(
                      id=case['id'],
                      qr=case['qr'],
                      qdcount=1,
                      ancount=1,
                      qd=None,
                      an=DNSRR(
                          rrname=case['rrname'],
                          ttl=case['ttl'],
                          rdata=case['rdata']
                      )
                  )
                      
        elif py_file == "dev5":          
            pkt = IP(src=case['src'], dst=case['dst']) / \
                  UDP(sport=case['sport'], dport=case['dport']) / \
                  DNS(
                      id=1, qr=1, aa=1, qdcount=1, ancount=1,
                      rcode=case['rcode'],
                      qd=DNSQR(qname=case['qname']),
                      an=DNSRR(rrname=case['qname'], rdata=case['rdata'])
                  )
        elif py_file == "train55":          
            pkt = IP(src=case["src"], dst=case["dst"], ttl=case["ttl"]) / ICMP()
        
        err = ""                
        return pkt, err
    except Exception as e:
        err = f"[ERROR] Errore nella creazione del pacchetto con case={case}: {e}"
        return None, err


#Funzione per estrarre gli input da file toml
def load_test_cases_from_toml(py_file):
    toml_file_name = f"{os.path.splitext(py_file)[0]}_config.toml"
    toml_path = os.path.join("config", toml_file_name)
    
    if not os.path.exists(toml_path):
        raise FileNotFoundError(f"File di configurazione {toml_path} non trovato.")

    with open(toml_path, "rb") as f:
        data = tomllib.load(f)

    if not data:
        raise ValueError(f"{toml_path} è vuoto o non valido.")

    key = next(iter(data))
    data_block = data[key]

    sub_key = None
    if isinstance(data_block, dict):
        sub_key = next(iter(data_block))
        test_cases = data_block[sub_key]
    else:
        test_cases = data_block

    if not isinstance(test_cases, list):
        if sub_key:
            raise ValueError(f"{key} -> {sub_key} non è una lista")
        else:
            raise ValueError(f"{key} non è una lista")

    return test_cases

def format_toml(list_items):
    lines = []
    for item in list_items:
        if isinstance(item, (tuple, list)):
            lines.append(f"({', '.join(str(v) for v in item)})")
        else:
            lines.append(f"({item})")
    return "[" + ", ".join(lines) + "]"


#Salvataggio su excel
def save_results(results, py_file, output_path):
    os.makedirs(output_path, exist_ok=True)
    df = pd.DataFrame(results)
    df.to_excel(f"{output_path}/{py_file}.xlsx", index=False)
    print(f"Risultati salvati in {output_path}/{py_file}.xlsx\n")
    
    
#Funzione per estrarre tutte le versioni da uno scipt
def extract_functions(file_path, script_names, class_name=None):
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if class_name:
        Class = getattr(module, class_name)
        target = Class
    else:
        target = module

    functions_to_test = {
        name: func for name, func in inspect.getmembers(target, inspect.isfunction)
        if any(sn in name for sn in script_names)
    }

    with open(file_path, "r") as file:
        source = file.read()
    tree = ast.parse(source)

    ordered_function_names = []
    if class_name:
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and item.name in functions_to_test:
                        ordered_function_names.append(item.name)
    else:
        ordered_function_names = [
            node.name for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name in functions_to_test
        ]

    return {name: functions_to_test[name] for name in ordered_function_names}, (Class if class_name else module)


#Funzione per estrarre i nomi delle funzioni
def get_script_names(file_name):
    script_name = os.path.basename(file_name)
    return SCRIPT_FUNCTIONS.get(script_name, [None])
   
    
#Funzione per estrarre i nomi delle classi
def get_class_name(script_name):
    return SCRIPT_CLASSES.get(script_name, None)


#Funzione per dati gps leggibili
def extract_gps_info(exif_data):
    if not exif_data or not isinstance(exif_data, dict):
        return "No Exif data found."
    gps_info = exif_data.get("GPSInfo") or exif_data.get(34853)  
    if gps_info:
        return f"GPS Info: {gps_info}"
    else:
        return "No Exif data found."


def format_output(output):
    if isinstance(output, list):
        return "\n".join([str(item) for item in output])
    return str(output)


#Funzione per capire se le funzioni prendono path o pcap 
def input_type(func):
    try:
        source = inspect.getsource(func)
        if "pyshark" in source:
            return "path"
        elif "rdpcap" in source:
            return "scapy"
        elif "open(" in source: 
            return "path"
        else:
            return "reader"
    except Exception:
        return "path"


#Funzione per rimuovere SSH key
def ssh_key_remove(py_file):
    if py_file == "train7":
        subprocess.run(
            [
            "ssh-keygen",
            "-f", "/home/unina/.ssh/known_hosts",
            "-R", "[127.0.0.1]:2222"
            ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        )
    elif py_file == "train58":
        subprocess.run(
            [
                "ssh-keygen",
                "-f", "/home/unina/.ssh/known_hosts",
                "-R", "127.0.0.1"
            ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        )    
    else:
        subprocess.run(["ssh-keygen", "-R", "ssh-container", "-f", "/root/.ssh/known_hosts"])

