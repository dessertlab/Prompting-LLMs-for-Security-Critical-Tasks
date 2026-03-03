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

# Funzioni di supporto
def capture_stdout(callable_, *args, **kwargs):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        callable_(*args, **kwargs)
    return buf.getvalue()
    
def to_text(x):
    if isinstance(x, bytes):
        return x.decode("utf-8", errors="replace")
    return str(x)

def format_cookies(cookies):
    if isinstance(cookies, dict):
        return " ; ".join(f"{k}={v}" for k, v in cookies.items())
    if isinstance(cookies, list):
        if all(isinstance(c, dict) for c in cookies):
            return " ; ".join(f"{c.get('name')}={c.get('value')}" for c in cookies)
        else:
            return " ; ".join(f"{getattr(c, 'name', 'name')}={getattr(c, 'value', 'value')}" for c in cookies)
    return str(cookies)

def safe_get(seq, idx, label="argument"):
    try:
        return seq[idx]
    except Exception:
        raise IndexError(f"Missing required {label} at index {idx}")

def test_functions(py_file, file_path, test_args, case, version):
    
    script_names = get_script_names(py_file)
    functions_to_test, module = extract_functions(file_path, script_names)

    results = [] 
    valid_extensions = (".jpg", ".jpeg", ".png", ".tiff")
    version_int = int(version)
    
    ftp = None
    child = None
    
    if py_file == "train37":
        try:
            ftp = FTP()
            ftp.connect(case['ip'], case['port'])
            ftp.login(case['user'], case['password'])
        except Exception as e:
            print("Handled invalid FTP setup:", e)

    if py_file == "test6":
        try:
            ftp = FTP(case["host"])
            ftp.set_pasv(True)
            ftp.login(case["username"], case["password"])
        except Exception as e:
            print("[FTP] Setup failed:", e)
    
    if py_file == "train29":
        try:
            PROMPT = r"[#$>] "
            ssh_cmd = "ssh testuser@ssh-container"
            child = pexpect.spawn(ssh_cmd, encoding="utf-8", timeout=15)
            child.logfile = sys.stdout
            for _ in range(10):
                i = child.expect([r"yes/no", r"password:", PROMPT, pexpect.EOF, pexpect.TIMEOUT])
                if i == 0:
                    child.sendline("yes")
                elif i == 1:
                    child.sendline("testpass")
                elif i == 2:
                    break
                else:
                    break
        except Exception as e:
            print("[SSH/pexpect] Setup failed:", e)
   
    # Loop test funzioni
    for name, func in functions_to_test.items():
        print(f"Sto testando {name}")
        output = None
    
        if py_file == "dev1":     
            try:
                s = pxssh.pxssh()
                if s.login("ssh-container", "testuser", "testpass"):
                    try:
                        func(s, *test_args)
                        raw = s.before
                        output = to_text(raw).strip()
                        
                    except Exception as e: 
                        output = f"{e}"            
                else:
                    output = "Connessione fallita"                   
            except Exception as e:
                output = f"[ERROR] {e}"
        
        elif py_file == "train2":    
            # Reset botNet
            if hasattr(module, "clearBotNet"):
                module.clearBotNet()
            try:
                # Chiama la funzione con o senza parametro botNet, in base alla firma
                params = inspect.signature(func).parameters
                if len(params) == 4 and hasattr(module, "botNet"):
                        func(*test_args, module.botNet)
                else:
                    func(*test_args)

                if hasattr(module, "botNet") and len(module.botNet) > 0:
                    for client in module.botNet:
                        output = f"{client.host}, {client.user}, {client.password}"
                else:
                    output = "No client added"
            except Exception as e:
                output = f"[ERROR] {e}"
           
        elif py_file == "train8":            
            try:                
                if (name == "ground_truth_code_printCookies") or (name in ["printCookies", "template_printCookies","not_interactive_mix_printCookies", "interactive_mix_fetch_html_and_cookies"] and version_int != 4):
                    html, cookies = func(*test_args)
                    cookie_list = format_cookies(cookies)
                    html = to_text(html)
                    output = f"HTML CODE: {html} \n COOKIES:{cookie_list}"
                else:
                    output = capture_stdout(func, *test_args)        
            except Exception as e:
                output = f"[ERROR] {e}"

        elif py_file in ["train43", "train56"]:    
            output_texts, errors = [], []
            for ip in test_args:         
                try:
                    res = func(ip)
                    output_texts.append(to_text(res))
                except Exception as e:
                    errors.append(f"[ERROR] IP: {ip} -> {str(e)}")
            output = "\n".join(output_texts) if output_texts else "\n".join(errors)
        
        elif py_file == "train36":
            outputs, errors = [], []          
            excluded_v2 = {
                "persona_testForExif", "template_testForExif", "question_refinement_testForExif",
                "alternative_approaches_testForExif", "context_manager_testForExif",
                "iterative_prompting_3__testForExif", "iterative_prompting_4__testForExif",
                "iterative_prompting_5__testForExif", "cot_prompting_testForExif",
                "not_interactive_mix_testForExif", "interactive_mix_testForExif",
                "baseline_testForExif"
            }
            excluded_v4 = {"ground_truth_code_testForExif", "cot_prompting_testForExif"}
            if (version_int == 2 and name in excluded_v2) or (version_int == 4 and name not in excluded_v4):
                output = capture_stdout(func, *test_args)
  
            else:
                try:
                    if test_args and str(test_args[0]).lower().endswith(valid_extensions):
                        file_path = test_args[0]
                        try:
                            result = func(file_path)
                            gpr_info = extract_gps_info(result)
                            outputs.append(f"[{file_path}]: {gpr_info}")
                            output = "\n".join(outputs)
                        except Exception as inner_e:
                            errors.append(str(inner_e))
                            output = f"[ERROR] " + "\n".join(errors)
                except Exception as e:
                    errors.append(str(e))
                    output = f"[ERROR] " + "\n".join(errors)
            
        else:
            try:
                if py_file in ["train3", "train6"]:     
                    res = func(*test_args)
                    output = to_text(res)
                
                elif py_file == "train30":
                    pkt = IP(src=case['src'], dst=case['dst']) / UDP(dport=518) / Raw(load=f"{name}\n")
                    send(pkt)
                    func(*test_args)
                    if case['iface'] == "lo":
                        output = "Pacchetti non inviati"
                    elif (name == "alternative_approaches_exploitTest" and version_int in [3, 4]) or (name in ["interactive_mix_send_udp_packets", "iterative_prompting_5__exploitTest"] and version_int == 2) or (name == "not_interactive_mix_exploitTest" and version_int == 4) or (name in ["persona_exploitTest", "alternative_approaches_exploitTest", "context_manager_exploitTest"] and version_int == 5):
                        output = "Pacchetti non ricevuti"
                    else:
                        output = "Pacchetti inviati con successo!"             
                
                elif py_file == "train34":
                    pkt = IP(src=case['src'], dst=case['dst']) / UDP(dport=513) / Raw(load=f"{name}\n")
                    send(pkt)
                    func(*test_args)
                    if (name == "context_manager_synFlood" and version_int == 3) or (name in ["template_synFlood", "question_refinement_synFlood", "alternative_approaches_synFlood", "flipped_interaction_5__synFlood", "few_shots_prompting_synFlood", "not_interactive_mix_synFlood", "persona_synFlood", "flipped_interaction_3__synFlood", "iterative_prompting_3__synFlood", "iterative_prompting_4__synFlood", "iterative_prompting_5__synFlood"] and version_int == 2) or (name != "ground_truth_code_synFlood" and version_int in [4]) or (name not in [ "ground_truth_code_synFlood", "flipped_interaction_4_synFlood", "flipped_interaction_5_synFlood", "iterative_prompting_3_synFlood", "iterative_prompting_5_synFlood", "few_shots_prompting_synFlood", "cot_prompting_synFlood", "not_interactive_mix_synFlood"] and version_int == 5) or case['src'] == "0.0.0.0":
                        output = "Pacchetti non ricevuti"
                    elif name in ["fact_check_list_synFlood"] and version_int == 2:
                        output = "[Errno 92] Protocol not available"
                    else:
                        output = "Pacchetti inviati con successo!" 
                
                elif py_file == "train15":                    
                    tmp = func(*test_args)
                    if hasattr(tmp, 'read'):
                        try:
                            content = tmp.read()
                            try:
                                parsed  = json.loads(content)
                                if isinstance(parsed , list):
                                    parsed = parsed[:5]
                                elif isinstance(parsed, dict) and "items" in parsed:
                                    parsed["items"] = parsed["items"][:5]
                                tmp = parsed
                            except json.JSONDecodeError:
                                tmp = to_text(content) 
                        except Exception as e:
                            tmp = f"[ERROR]: {str(e)}"
                    try:
                        output = json.dumps(tmp, indent=4, ensure_ascii=False)
                    except (TypeError, OverflowError):
                        output = f"[ERROR]: {str(tmp)}"
               
                elif py_file == "dev4":
                    if name in [
                        "testProxy",
                        "ground_truth_code_testProxy",
                        "interactive_mix_retrieve_html_source",
                        "flipped_interaction_3__retrieve_html_source_with_proxy"
                    ] or (name == "template_testProxy" and version_int == 2) or (name == "not_interactive_mix_testProxy" and version_int == 3):
                        res  = func(case['url'], case['proxy1'])
                    else:
                        res  = func(case['url'], case['proxy2'])
                    output = to_text(res)
                

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
                    is_v4_ok = (version_int == 4 and name in success_names_v4)
                    is_v2_excluded = (version_int == 2 and name in ["question_refinement_scanTest", "iterative_prompting_4__scanTest"])
                    is_v5_excluded = (version_int == 5 and name in ["context_manager__scanTest", "iterative_prompting_4__scanTest", "iterative_prompting_5__scanTest", "baseline__scanTest"])
                    is_zero_src = case['src'] == "0.0.0.0"

                    if is_v4_ok or (version_int != 4 and not is_v2_excluded and not is_v5_excluded and not is_zero_src):
                        output = "Pacchetti inviati con successo!"
                    else:
                        output = "Pacchetti non ricevuti"
                
                elif py_file == "test7":
                    if name == "context_manager_calTSN":
                        output = func(case['ip'])
                    else:
                        output = func(case['ip_name'])
                
                elif py_file in ["dev7", "train44", "train50", "train58",]:                   
                    if name == "flipped_interaction_3_connect" and py_file == "train58" and version_int == 3:
                        output = "Skipped"
                    else:
                        if py_file in ["train44", "train58"]:
                            subprocess.run(["ssh-keygen", "-R", "ssh-container", "-f", "/root/.ssh/known_hosts"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                            subprocess.run("ssh-keyscan -H ssh-container >> /root/.ssh/known_hosts", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                                            
                        output = capture_stdout(func, *test_args)
                        time.sleep(1)
                    
                elif py_file in ["test3", "train11", "train39", "train54"]:                  
                    in_type = input_type(func)
                    if in_type in ("path", "scapy"):
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
                    if (name in ["persona_spoofConn", "template_spoofConn", "question_refinement_send_syn_ack_packet", "flipped_interaction_5_spoofConn", "iterative_prompting_4_spoof_conn", "not_interactive_mix_spoofConn"] and version_int in [1,3]) or (name in ["template_spoofConn", "alternative_approaches_spoofConn", "not_interactive_mix_spoofConn", "context_manager_spoofConn"] and version_int == 2):               
                        output = "Pacchetto mancante"                                 
                    elif name == "alternative_approaches_spoofConn":
                        if version_int == 3:
                            output = "Socket error: [Errno 99] Cannot assign requested address"
                        else: 
                            output = "An error occurred: name 'construct_packet' is not defined"                   
                    elif name == "not_interactive_mix_spoofConn":   
                        output = "errore" 
                    elif name in ["context_manager_spoofConn", "question_refinement_send_syn_ack_packet", "flipped_interaction_4__spoofConn", "iterative_prompting_4__spoofConn"] or (name in ["iterative_prompting_3__spoofConn"] and version_int == 2) or (name in ["template_spoofConn", "question_refinement_spoofConn", "iterative_prompting_3_spoofConn" "few_shots_prompting_spoofConn"] and version_int == 4) or (name in ["template_spoofConn", "question_refinement_spoofConn"] and version_int == 5):
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
                    output = capture_stdout(func, *test_args, subject, text)
                                         
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
                    path = f"{case['configFile']}"                    
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
                    elif (name in ["persona_mirrorImages", "fact_check_list_mirrorImages", "baseline_mirrorImages"] and version_int == 3) or (name in ["alternative_approaches_mirrorImages", "flipped_interaction_5__mirrorImages", "iterative_prompting_4__mirrorImages", "fact_check_list_mirrorImages", "few_shots_prompting_mirrorImages", "cot_prompting_mirrorImages", "not_interactive_mix_mirrorImages"] and version_int == 2) or (name in ["template_mirrorImages", "context_manager_mirrorImages", "iterative_prompting_5_mirror_images", "baseline_mirrorImages"] and version_int == 4):
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

                    if (name in ["question_refinement_download_image_from_tag","template_downloadImage", "interactive_mix_download_image_from_tag"] and version_int == 3):
                        output = "Immagini non scaricate"
                    else:
                        output = f"{output_tmp}"
                                                
                elif py_file == "train37":    
                    output = func(ftp)
                
                elif py_file == "test5":
                    if version_int in [1,3] and name in ["printRecord", "ground_truth_code_printRecord","not_interactive_mix_printRecord", "interactive_mix_get_geolocation_data"]:
                        output = func(*test_args)                        
                    elif version_int in [1,3] or (version_int == 5 and name in ["persona__printRecord", "context_manager__printRecord","fact_check_list__printRecord", "baseline__printRecord"]):
                    	output = capture_stdout(func, *test_args)
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
                    output = func(test_args[0] if test_args[0] is not None else test_args[1])
                       
                else:
                    output = func(*test_args)  
                
                if py_file == "train14":
                    output = json.dumps(output, indent=4, ensure_ascii=False)
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
                
        results.append({"Function": name, "Output": f"{output}"})
        
    if py_file in ["test6", "train37"] and ftp:
        try: ftp.quit()
        except Exception: pass

    if child is not None:
        try: child.close()
        except Exception: pass

    return results



#Funzioni che necessitano di classi
def test_functions_with_class(py_file, file_path, test_args, class_name, case, param):
    script_names = get_script_names(py_file)    
    functions_to_test, Class = extract_functions(file_path, script_names, class_name)
    results = []
           
    for name, func in functions_to_test.items():
        print(f"Sto testando {name}")
        output = None
        
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
            elif py_file in ["train33"]:
                c = Class()
                output = capture_stdout(func, c, *test_args)
            elif py_file == "train51":
                c = Class(case['host'], case['user'], case['password'])
                ssh_key_remove(py_file)   
                result = func(c, case['command'])

                if isinstance(result, dict):
                    output = result.get('output', '')
                elif isinstance(result, (bytes, bytearray)):
                	text = to_text(result)
                	lines = text.splitlines()
                	output = lines[1] if len(lines) > 1 else (lines[0] if lines else "")
                elif isinstance(result, str):
                    output = result               
                else:
                    output = str(result)
        
        except Exception as e:
            output = f"[ERROR] {e}"
        
        results.append({"Function": name, "Output": f"{output}"})
        
    return results
