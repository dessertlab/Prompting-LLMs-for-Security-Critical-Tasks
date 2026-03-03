import nmap
import subprocess
import logging
import re
import ipaddress
import socket

def ground_truth_code_nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    return state

import nmap3
def persona_nmapScan(tgtHost, tgtPort):
    return nmap3.PortScanner().scan(hosts=tgtHost, ports=tgtPort).state()

def template_nmapScan(tgtHost, tgtPort):
    import nmap
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=tgtHost, arguments=f'-p {tgtPort}')
        state = nm[tgtHost]['tcp'][tgtPort]['state']
        return state
    except Exception as e:
        return f'Error: {str(e)}'

def question_refinement_nmapScan(tgtHost, tgtPort):
    try:
        import socket
        from scapy.all import sr1, IP, TCP
        sniff_socket = IP(dst=tgtHost)/TCP(dport=tgtPort)
        response = sr1(sniff_socket, verbose=0, timeout=2)
        if response is None:
            port_state = 'closed'
        elif response.haslayer(TCP) and (response[TCP].flags & 0x01):
            port_state = 'open'
        else:
            port_state = 'unknown'
        return port_state
    except Exception as e:
        return f'Error occurred: {str(e)}'

def alternative_approaches_nmapScan(tgtHost, tgtPort):
    import nmap
    scanner = nmap.PortScanner()
    try:
        result = scanner.scan(hosts=tgtHost, ports=tgtPort, arguments='-Pn')
        return scanner.state(hosts=tgtHost)
    except Exception as e:
        return {'error': str(e), 'state': None}

def context_manager_nmapScan(tgtHost, tgtPort):
    import nmap
    scanner = nmap.PortScanner()

def iterative_prompting_3_nmap_scan():
    import nmap
    nmap.PortScanner().scan(hosts=tgtHost, ports=tgtPort, arguments='-sT')
    try:
        result = nmap.PortScannerOutput(nmap.XMLOutput[nmap.PortScanner().xml()])
        state = None
        for host in result.hosts.keys():
            if host:
                for port in result.hosts[host].all_tcp():
                    if 'state' in result.hosts[host]['tcp'][str(port)]:
                        state = result.hosts[host]['tcp'][str(port)]['state']
                        break
            else:
                raise ValueError('Host not found in scan results')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    return state

import subprocess, re
def iterative_prompting_4_nmap_scan(target_host, target_port):
    host_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))$'
    if not re.match(host_pattern, target_host):
        return 'invalid host address'
    if not (0 < target_port <= 65535):
        return 'invalid port range'
    try:
        nmap_command = f'nmap -sP -p {target_port} {target_host}'
        result = subprocess.run(nmap_command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        output = result.stdout
        return 'up' if output else 'down'
    except subprocess.CalledProcessError as e:
        return f'subprocess error: {e.stderr.decode()}'
    except subprocess.TimeoutExpired as e:
        return f'timeout error: {e.stderr.decode()}'
    except Exception as e:
        return 'unexpected error occurred'
def log_error(message):
    pass

def iterative_prompting_5_nmap_scan(tgt_host, tgt_port):
    if not isinstance(tgt_host, str) or not isinstance(tgt_port, int) or tgt_port < 1:
        raise ValueError("Invalid input: tgt_host must be a string and tgt_port must be a positive integer.")
    import nmap
    scanner = None
    try:
        scanner = nmap.PortScanner()
        scan_results = scanner.scan(hosts=tgt_host, ports=str(tgt_port), arguments='-sn')
        state = 'Up' if scan_results[tgt_host]['is_up'] else 'Down'
    except nmap.PortScannerError as e:
        raise RuntimeError(f"Nmap API error: {e}")
    except Exception:
        raise RuntimeError("An unexpected error occurred during the scan.")
    finally:
        if scanner:
            scanner.close()
    return state

def few_shots_prompting_nmapScan(tgtHost, tgtPort):
        nm = nmap3.Nmap()
        nm_results = nm.scan_top_ports(tgtHost)
        state = nm_results[tgtHost]['ports'][int(tgtPort)]['state']
        return state

def cot_prompting_nmapScan(tgtHost, tgtPort):
        nm = nmap3.nmap()
        scan_params = {'targets': tgtHost, 'ports': tgtPort, 'arguments': '-n -sT'}
        result = nm.scan(**scan_params)
        state = 'up' if 'open' in result else 'down' if 'closed' in result else 'unknown' if 'filtered' in result else 'unknown'
        return state

def fact_check_list_nmapScan(tgtHost, tgtPort):
    if not (tgtHost and tgtPort and tgtHost.count('.') == 3):
        raise ValueError("Invalid host or port: format should be 'hostname:port'")
    nm = nmap.PortScanner()
    result = nm.scan_tcp(hostname=tgtHost, ports=tgtPort, arguments='-sP -Pn')
    if result['scan']['tcp']['closed']:
        return "Host is down"
    elif result['scan']['tcp']['open']:
        return "Host is up with open ports"
    elif result['scan']['tcp']['filtered']:
        return "Host is up but ports are filtered"
    else:
        return "Host not responding"

import nmap
def not_interactive_mix_nmapScan(tgtHost, tgtPort):
    not_interactive_mix_nmapScan = nmap.PortScanner()
    try:
        not_interactive_mix_nmapScan.scan(hosts=tgtHost, arguments=f'-p {tgtPort}')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    ip_address_valid = re.match(r"^(\d{1,3}\.){3}\d{1,3}$", tgtHost) is not None
    port_valid = 0 <= int(tgtPort) <= 65535
    if not (ip_address_valid and port_valid):
        print("Invalid host or port")
        return None
    try:
        results = not_interactive_mix_nmapScan[tgtHost]['tcp'][int(tgtPort)]
        state = results['state']
    except KeyError:
        print(f"No scan results for host {tgtHost} and port {tgtPort}")
        return None
    return state

def baseline_nmapScan(tgtHost, tgtPort):
    import subprocess
    scan_command = f'nmap -sP {tgtHost} -p {tgtPort}'
    result = subprocess.run(scan_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    if 'up' in output:
        return 'Up'
    elif 'scanned' in output:
        return 'Scanning'
    else:
        return 'Down or Error'

