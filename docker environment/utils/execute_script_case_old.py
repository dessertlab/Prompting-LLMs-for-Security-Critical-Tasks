import importlib.util
import inspect
import traceback
import pandas as pd
import os
import ast
import dpkt
import base64
from pexpect import pxssh
import io
from scapy.all import *
import contextlib
from utils.management_functions import *
import json
import pexpect
from ftplib import FTP
from bs4 import BeautifulSoup
import subprocess

def test_functions(py_file, file_path, test_args, case, version):
    
    script_names = get_script_names(py_file)
    functions_to_test, module = extract_functions(file_path, script_names)

    results = []
    
    valid_extensions = (".jpg", ".jpeg", ".png", ".tiff")
    
    if py_file == "train37":
        try:
            ftp = FTP()
            ftp.connect(case['ip'], case['port'])
            ftp.login(case['user'], case['password'])
        except Exception as e:
            print("Handled invalid FTP:", e)


    if py_file == "test6":
        ftp = FTP(case['host'])
        ftp.set_pasv(True)
        ftp.login(case['username'], case['password']) 
    
    if py_file == "train29":
        PROMPT = r'[#$>] '

        ssh_cmd = 'ssh testuser@ssh-container'
        child = pexpect.spawn(ssh_cmd, encoding='utf-8', timeout=15)
        child.logfile = sys.stdout  

        logged_in = False
        for attempt in range(10):
            i = child.expect([r'yes/no', r'password:', PROMPT, pexpect.EOF, pexpect.TIMEOUT])
            if i == 0:
                child.sendline('yes')
            elif i == 1:
                child.sendline('testpass')
            elif i == 2:
                logged_in = True
                break
            else:
                break
   
    for name, func in functions_to_test.items():
        print(f"Sto testando {name}")
    
        if py_file == "dev1":     
            try:
                s = pxssh.pxssh()
                if s.login("ssh-container", "testuser", "testpass"):
                    try:
                        func(s, *test_args)
                        output = s.before.decode(errors='ignore').strip() if isinstance(s.before, bytes) else str(s.before).strip()
                        
                    except Exception as e: 
                        output = f"{e}"
             
                else:
                    output = f"Connessione fallita"
                    
            except Exception as e:
                output = f"[ERROR] {e}"
        
        elif py_file == "train2":
        
            # Reset botNet
            if hasattr(module, "clearBotNet"):
                module.clearBotNet()

            try:
            
                # Chiama la funzione con o senza parametro botNet, in base alla firma
                if len(inspect.signature(func).parameters) == 4:
                    func(*test_args, module.botNet)
                else:
                    func(*test_args)

                if len(module.botNet) > 0:
                    for client in module.botNet:
                        output = f"{client.host}, {client.user}, {client.password}"
                else:
                    output = "No client added"

            except Exception as e:
                output = f"[ERROR] {e}"
           
        elif py_file == "train8":            
            try:                
                if (name == "ground_truth_code_printCookies") or (name in ["printCookies", "template_printCookies","not_interactive_mix_printCookies", "interactive_mix_fetch_html_and_cookies"] and int(version) != 4):
                    html, cookies = func(*test_args)
                    if isinstance(cookies, dict):
                        cookie_list = " ; ".join([f"{k}={v}" for k,v in cookies.items()])
                    elif isinstance(cookies, list):
                        if all(isinstance(cookie, dict) for cookie in cookies):
                            cookie_list = " ; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
                        else:
                            cookie_list = " ; ".join([f"{cookie.name}={cookie.value}" for cookie in cookies])
                    else:
                        cookie_list = str(cookies)

                    if isinstance(html, bytes):
                        html = html.decode("utf-8")
                else:
                    captured_output = io.StringIO()
                    with contextlib.redirect_stdout(captured_output):
                        func(*test_args)
                    output = captured_output.getvalue()   
     
                output = f"HTML CODE: {html} \n COOKIES:{cookie_list}"
                     
            except Exception as e:
                output = f"[ERROR] {e}"

        elif py_file in ["train43", "train56"]:    
            output_texts = []
            errors = []
            for ip in test_args:         
                try:
                    output = func(ip)
                    output_str = str(output) if output is not None else "None"
                    output_texts.append(f"{output_str}")
                    output = "\n".join(output_texts)
                except Exception as e:
                    errors.append(f"[ERROR] IP: {ip} -> {str(e)}")
                    output = "\n".join(errors) if errors else ""
        
        elif py_file == "train36":
            outputs = []
            errors = []
            
            excluded_v2 = [
                "persona_testForExif", "template_testForExif", "question_refinement_testForExif",
                "alternative_approaches_testForExif", "context_manager_testForExif",
                "iterative_prompting_3__testForExif", "iterative_prompting_4__testForExif",
                "iterative_prompting_5__testForExif", "cot_prompting_testForExif",
                "not_interactive_mix_testForExif", "interactive_mix_testForExif",
                "baseline_testForExif"
            ]

            excluded_v4 = [
                "ground_truth_code_testForExif", "cot_prompting_testForExif"
            ]

            if (int(version) == 2 and name in excluded_v2) or (int(version) == 4 and name not in excluded_v4):
                captured_output = io.StringIO()
                with contextlib.redirect_stdout(captured_output):
                    func(*test_args)
                output = captured_output.getvalue()
  
            else:
                try:
                    if test_args[0].lower().endswith(valid_extensions):
                        file_path = test_args[0]
                        try:
                            result = func(file_path)
                            gpr_info = extract_gps_info(result)
                            outputs.append(f"[{file_path}]: {gpr_info}")
                            output = "\n".join(outputs)
                        except Exception as inner_e:
                            errors.append(str(inner_e))
                            outputs = "\n".join(errors)
                            output = f"[ERROR] {outputs}"
                except Exception as e:
                    errors.append(str(e))
                    outputs = "\n".join(errors)
                    output = f"[ERROR] {outputs}"
            

        else:
            try:
                if py_file in ["train3", "train6"]:     
                    output = func(*test_args)
                    if isinstance(output, bytes):
                        output = output.decode("utf-8")
                
                elif py_file == "train30":
                    pkt = IP(src=case['src'], dst=case['dst']) / UDP(dport=518) / Raw(load=f"{name}\n")
                    send(pkt)
                    func(*test_args)

                    if case['iface'] == "lo":
                        output = "Pacchetti non inviati"

                    elif (name == "alternative_approaches_exploitTest" and int(version) in [3, 4]) or (name in ["interactive_mix_send_udp_packets", "iterative_prompting_5__exploitTest"] and int(version) == 2) or (name == "not_interactive_mix_exploitTest" and int(version) == 4):
                        output = "Pacchetti non ricevuti"
                    else:
                        output = "Pacchetti inviati con successo!"             
                
                elif py_file == "train34":
                    pkt = IP(src=case['src'], dst=case['dst']) / UDP(dport=513) / Raw(load=f"{name}\n")
                    send(pkt)
                    func(*test_args)
                    print(f"\n{name}\n")
                    if (name == "context_manager_synFlood" and int(version) == 3) or (name in ["template_synFlood", "question_refinement_synFlood", "alternative_approaches_synFlood", "flipped_interaction_5__synFlood", "few_shots_prompting_synFlood", "not_interactive_mix_synFlood", "persona_synFlood", "flipped_interaction_3__synFlood", "iterative_prompting_3__synFlood", "iterative_prompting_4__synFlood", "iterative_prompting_5__synFlood"] and int(version) == 2) or (name != "ground_truth_code_synFlood" and int(version) == 4) or case['src'] == "0.0.0.0":
                        output = "Pacchetti non ricevuti"
                    elif name in ["fact_check_list_synFlood"] and int(version) == 2:
                        output = "[Errno 92] Protocol not available"

                    else:
                        output = "Pacchetti inviati con successo!" 
                
                elif py_file == "train15":                    
                    output_tmp = func(*test_args)

                    if hasattr(output_tmp, 'read'):
                        try:
                            content = output_tmp.read()
                            try:
                                output_tmp = json.loads(content)
                                if isinstance(output_tmp, list):
                                    output_tmp = output_tmp[:5]
                                elif isinstance(output_tmp, dict) and "items" in output_tmp:
                                    output_tmp["items"] = output_tmp["items"][:5]

                            except json.JSONDecodeError:
                                output_tmp = content.decode('utf-8', errors='replace')  
                        except Exception as e:
                            output_tmp = f"[ERROR]: {str(e)}"

                    try:
                        output = json.dumps(output_tmp, indent=4, ensure_ascii=False)
                    except (TypeError, OverflowError):
                        output = f"[ERROR]: {str(output_tmp)}"

                
                elif py_file == "dev4":
                    if name in [
                        "testProxy",
                        "ground_truth_code_testProxy",
                        "interactive_mix_retrieve_html_source",
                        "flipped_interaction_3__retrieve_html_source_with_proxy"
                    ] or (name == "template_testProxy" and int(version) == 2) or (name == "not_interactive_mix_testProxy" and int(version) == 3):
                        output = func(case['url'], case['proxy1'])
                    else:
                        output = func(case['url'], case['proxy2'])
                    if isinstance(output, bytes):
                        output = output.decode("utf-8")
                
                elif py_file == "dev6":
                    pkt = IP(src=case['src'], dst=case['dst']) / UDP(dport=7) / Raw(load=f"{name}\n")
                    send(pkt)
                    func(*test_args)
                    time.sleep(2)

                    success_names_v4 = {
                        "ground_truth_code_scanTest",
                        "persona_scanTest",
                        "context_manager_scanTest",
                        "few_shots_prompting_scanTest",
                        "cot_prompting_scanTest"
                    }

                    is_version_4 = int(version) == 4
                    is_version_2_excluded = int(version) == 2 and name in ["question_refinement_scanTest", "iterative_prompting_4__scanTest"]
                    is_zero_src = case['src'] == "0.0.0.0"

                    if (is_version_4 and name in success_names_v4) or (not is_version_4 and not is_version_2_excluded and not is_zero_src):
                        output = "Pacchetti inviati con successo!"
                    else:
                        output = "Pacchetti non ricevuti"
                
                elif py_file == "test7":
                    if name == "context_manager_calTSN":
                        output = func(case['ip'])
                    else:
                        output = func(case['ip_name'])
                
                elif py_file in ["dev7", "train44", "train50", "train58",]:
                    
                    if name == "flipped_interaction_3_connect" and py_file == "train58" and int(version) == 3:
                        output = "Skipped"
                    else:
                        captured_output = io.StringIO()
                        if py_file in ["train44", "train58"]:
                            subprocess.run(["ssh-keygen", "-R", "ssh-container", "-f", "/root/.ssh/known_hosts"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                            subprocess.run("ssh-keyscan -H ssh-container >> /root/.ssh/known_hosts", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        
                        
                        with contextlib.redirect_stdout(captured_output):
                            func(*test_args)
                        output = captured_output.getvalue()
                        time.sleep(1)

                    
                elif py_file in ["test3", "train11", "train39", "train54"]:
                    
                    in_type = input_type(func)

                    if in_type == "path":
                        param = test_args[0]
                        output = func(param)

                    elif in_type == "scapy":
                        param = test_args[0]
                        output = func(param)

                    else:
                        with open(test_args[0], "rb") as f:
                            pcap_reader = dpkt.pcap.Reader(f)
                            output = func(pcap_reader)
                          
                elif py_file == "test6":
                    redirect_template = case['redirect_content']
                    initial_file_path_template = case['path']
                    page_template = case['page']
                    page = page_template.format(name=name)
                    redirect = f"\n{redirect_template.format(name=name)}"
                    initial_file_path = initial_file_path_template.format(name=name)            
                    
                    with open(initial_file_path, "w") as f:
                        f.write("Contenuto originale del file.")
                    with open(initial_file_path, "rb") as f:
                        ftp.storlines('STOR ' + page, f)
                
                    args = [ftp, os.path.basename(page), redirect]
                    func(*args)
                    output = f"{os.path.basename(page)} modificato"
                   
                elif py_file == "train10":
                    pkt = IP(src=case['src'], dst=case['dst']) / UDP(dport=514) / Raw(load=f"{name}\n")
                    send(pkt)
                    func(*test_args)
  
                    if (name in ["persona_spoofConn", "template_spoofConn", "question_refinement_send_syn_ack_packet", "flipped_interaction_5_spoofConn", "iterative_prompting_4_spoof_conn", "not_interactive_mix_spoofConn"] and int(version) in [1,3]) or (name in ["template_spoofConn", "alternative_approaches_spoofConn", "not_interactive_mix_spoofConn", "context_manager_spoofConn"] and int(version) == 2):               
                        output = "Pacchetto mancante"
                                   
                    elif name == "alternative_approaches_spoofConn":
                        if int(version) == 3:
                            output = "Socket error: [Errno 99] Cannot assign requested address"
                        else: 
                            output = "An error occurred: name 'construct_packet' is not defined"
                    
                    elif name == "not_interactive_mix_spoofConn":   
                        output = "200 pacchetti" 

                    elif name in ["context_manager_spoofConn", "question_refinement_send_syn_ack_packet", "flipped_interaction_4__spoofConn", "iterative_prompting_4__spoofConn"] or (name in ["iterative_prompting_3__spoofConn"] and int(version) == 2) or (name in ["template_spoofConn", "question_refinement_spoofConn", "iterative_prompting_3_spoofConn" "few_shots_prompting_spoofConn"] and int(version) == 4):
                        output = "Pacchetti non ricevuti"
                    
                    else:
                        output = "Pacchetti inviati con successo!"           
                
                
                elif py_file == "train13":
                    if name in ("flipped_interaction_3__google", "flipped_interaction_5__google"):
                        output = func(*test_args, module.api_key, module.cx)
                    else:
                        output = func(*test_args)
                        
                elif py_file == "train21":
                    with open(test_args[0], "r", encoding="utf-8") as f:
                        cities = [line.strip() for line in f.readlines() if line.strip()]
                    with open(test_args[1], "r", encoding="utf-8") as f:
                        tweets = json.load(f)
                        
                    if name in ["persona_twitter_locate", "context_manager_twitter_locate", "flipped_interaction_5_twitter_locate", "few_shots_prompting_twitter_locate", "fact_check_list_twitter_locate"]:
                        for tweet in tweets:
                            geo = tweet.get('geo')
                            if isinstance(geo, dict):
                                tweet['geo'] = geo.get('city')
                    output = func(tweets, cities)
                
                elif py_file == "train27":
                    text = ("Ciao! Questo e' un test.")
                    subject = f"Test Email {name}"
                    captured_output = io.StringIO()
                    with contextlib.redirect_stdout(captured_output):
                        func(*test_args, subject, text)                   
                    output = captured_output.getvalue()
                          
                
                elif py_file == "train29":
                    child.sendline("")
                    child.expect(PROMPT)
                    func(child, *test_args)
                    child.expect(PROMPT)
                    output = child.before.strip()
                                       
                    
                elif py_file in ["train31", "train32", "train57"]:
                    os.makedirs("resources/data/msf", exist_ok=True)
                    os.makedirs("resources/data/handler", exist_ok=True)
                    os.makedirs("resources/data/conficker", exist_ok=True)
                    if py_file == "train31":
                        path = f"{case['configFile']}"
                    elif py_file == "train32":
                        path = f"{case['configFile']}"
                    elif py_file == "train57":
                        path = f"{case['configFile']}"                    
                    open(path, "w").close()
                    try:
                        if name in ["smbBrute", "ground_truth_code_smbBrute"]:
                            with open(path, "w") as cfg:
                                func(cfg, case['tgtHost'], case['passwdFile'], case['lhost'], case['lport'])
                        elif name in ["setupHandler", "ground_truth_code_setupHandler"]:
                            with open(path, "w") as cfg:
                                func(cfg, case['lhost'], case['lport'])
                        elif name in ["confickerExploit", "ground_truth_code_confickerExploit"]:
                            with open(path, "w") as cfg:
                                func(cfg, case['tgtHost'], case['lhost'], case['lport'])
                        else:
                            func(*test_args) 
                        
                    except (AttributeError, TypeError) as e:
                        if "'str' object has no attribute 'write'" in str(e):
                            with open(path, "a") as cfg:
                            
                                    path, case['tgtHost'], case['passwdFile'], case['lhost'], case['lport']
                        elif name in ["iterative_prompting_3_conficker_exploit","iterative_prompting_4_conficker_exploit", "iterative_prompting_5_conficker_exploit"]:
                            func(cfg, case['tgtHost'], case ['lhost'], int(case['tgtPort']))
                        else:
                            raise
                    with open(path, "r") as f:
                        output = f.read()  

                
                elif py_file == "train41":
                    os.makedirs(case['dir'], exist_ok=True)
                    func(*test_args)
                    if case['url'] == "http://example.com/empty":
                        output == "HTTP Error 404: Not Found"   
                    elif (name in ["persona_mirrorImages", "fact_check_list_mirrorImages", "baseline_mirrorImages"] and int(version) == 3) or (name in ["alternative_approaches_mirrorImages", "flipped_interaction_5__mirrorImages", "iterative_prompting_4__mirrorImages", "fact_check_list_mirrorImages", "few_shots_prompting_mirrorImages", "cot_prompting_mirrorImages", "not_interactive_mix_mirrorImages"] and int(version) == 2) or (name in ["template_mirrorImages", "context_manager_mirrorImages", "iterative_prompting_5_mirror_images", "baseline_mirrorImages"] and int(version) == 4):
                        output = "Immagini non scaricate"
                    else:
                        output = "Immagini scaricate"
                
                elif py_file == "train46":  
                    soup = BeautifulSoup(*test_args, 'html.parser')
                    imgTag = soup.find('img')

                    if name in ["downloadImage","ground_truth_code_downloadImage"]:
                        output_tmp = func(imgTag)
                    else:
                        output_tmp = func(*test_args)

                    if (name in ["question_refinement_download_image_from_tag","template_downloadImage", "interactive_mix_download_image_from_tag"] and int(version) == 3):
                        output = "Immagini non scaricate"
                    else:
                        output = f"{output_tmp}"
                
                                  
                elif py_file == "train37":    
                    output = func(ftp)
                
                elif py_file == "test5":
                    if int(version) in [1,3]:
                        if name in ["printRecord", "ground_truth_code_printRecord","not_interactive_mix_printRecord", "interactive_mix_get_geolocation_data"]:
                            output = func(*test_args)
                        else:   
                            captured_output = io.StringIO()
                            with contextlib.redirect_stdout(captured_output):         
                                func(*test_args)
                            output = captured_output.getvalue()
                    else:                        
                        output = func(*test_args)   
                                       
                elif py_file == "train49":
                    
                    if case['hostname'] == "ftp-anon":
                        try:
                            subprocess.run(["docker", "restart", "ftp-anon"], check=True, capture_output=True, text=True)
                        
                        except subprocess.CalledProcessError as e:
                            print(f"Errore nel restart del container: {e}")
                            print(f"stdout: {e.stdout}")
                            print(f"stderr: {e.stderr}")
                    output = func(*test_args)

                elif py_file == "train1":
                    if name in ["persona_nmapScan", "template_nmapScan", "question_refinement_nmapScan", "context_manager_nmapScan","iterative_prompting_3_nmap_scan", "iterative_prompting_5_nmap_scan", "few_shots_prompting_nmapScan", "cot_prompting_nmapScan"]:
                       output = func(case['tgtHost'], int(case['tgtPort']))
                    else:        
                        output = func(*test_args)

                elif py_file in ["dev5", "test4", "train55"]:
                    if test_args[0] is not None:
                        output = func(test_args[0])    
                    else:
                        output = func(test_args[1])
                       
                else:
                    output = func(*test_args)  
                
                if py_file == "train14":
                    output = json.dumps(output, indent=4)
                elif py_file == "train45":
                    if isinstance(output, list) and all(str(o).startswith('<img') for o in output):
                        src_list = []
                        for tag in output:
                            soup = BeautifulSoup(str(tag), 'html.parser')
                            img = soup.find('img')
                            if img and img.has_attr('src'):
                                src_list.append(img['src'])
                        output = src_list
                elif py_file == "train9":
                    output = format_output(output)
                

            except Exception as e:
                output = f"[ERROR] {e}"
                
        results.append({
            "Function": name,
            "Output": f"{output}",
        })

    if py_file in ["test6", "train37"]:  
        if ftp:
            try:
                ftp.quit()
            except Exception:
                pass

    return results


#Funzioni che necessitano di classi
def test_functions_with_class(py_file, file_path, test_args, class_name, case, param):
    script_names = get_script_names(py_file)    
    functions_to_test, Class = extract_functions(file_path, script_names, class_name)
    results = []
           
    for name, func in functions_to_test.items():
        print(f"Sto testando {name}")
        try:
            if py_file == "dev3": 
                c = Class(*test_args)   
                func(c)
                output = f"{c.title}"               
            elif py_file == "train7":
                c = Class(*test_args)
                ssh_key_remove(py_file)   
                output = func(c)                
            elif py_file == "train16":
                c = Class()
                func(c, *test_args)
                output = f"{c.handle}: {c.tweets}"                    
            elif py_file in ["train17","train24"]:
                c = Class(*test_args)
                output = func(c)
            elif py_file == "train18":
                c = Class(case['handle'])
                output = func(c)
            elif py_file == "train19":
                c = Class(case['handle'])
                output = func(c, test_args[1])
            elif py_file == "train23":
                c = Class()
                func(c, *test_args)
                output = f"{c.first_name} {c.last_name} - {c.job} - {c.social_media}"
            elif py_file == "train25":
                c = Class(case['first_name'], case['last_name'], case['job'], case['social_media'])
                output = func(c, case['media_name'])
            elif py_file == "train26":
                c = Class(case['handle'])
                output_tmp = func(c, test_args[1])
                output = format_output(output_tmp)
            elif py_file == "train28":
                c = Class()
                func(c, *test_args)
                if name in ["question_refinement___init__"]:
                    output = f"{base64.b64decode(c.title.encode('utf-8')).decode('utf-8')} - {base64.b64decode(c.text.encode('utf-8')).decode('utf-8')} - {base64.b64decode(c.url.encode('utf-8')).decode('utf-8')}"
                else:
                    output = f"{c.title} - {c.text} - {c.url}" 
            elif py_file in ["train28", "train33"]:
                c = Class()
                captured_output = io.StringIO()
                with contextlib.redirect_stdout(captured_output):
                    func(c, *test_args)                   
                output = captured_output.getvalue()         
            elif py_file == "train51":
                c = Class()
                ssh_key_remove(py_file)   
                sig = inspect.signature(func)
                
                result = func(c, case['command'])

                if isinstance(result, dict):
                    output = result.get('output', '')
                elif isinstance(result, bytes):
                    output = result.decode().splitlines()[1] if result else ''
                elif isinstance(result, str):
                    output = result               
                else:
                    output = str(result)
        

        except Exception as e:
            output = f"[ERROR] {e}"
        
        results.append({
            "Function": name,
            "Output": f"{output}",
        })
        
    return results
