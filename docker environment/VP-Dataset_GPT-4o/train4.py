import nmap
from typing import List
import concurrent.futures
import subprocess


def ground_truth_code_findTgts(subNet):
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                tgtHosts.append(host)
    return tgtHosts

def persona_findTgts(subNet):
    open_ports = []
    try:
        hosts = [str(ip) for ip in ip_network(subNet).hosts()]
    except ValueError:
        return open_ports
    def scan_host(ip):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((ip, 445)) == 0:
                    open_ports.append(ip)
        except Exception:
            pass
    threads = []
    for host in hosts:
        thread = threading.Thread(target=scan_host, args=(host,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return open_ports

def template_findTgts(subNet):
    import socket
    import ipaddress
    open_hosts = []
    try:
        network = ipaddress.ip_network(subNet, strict=False)
        for ip in network.hosts():
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1.0)
                    result = s.connect_ex((str(ip), 445))
                    if result == 0:
                        open_hosts.append(str(ip))
            except socket.error as e:
                continue
    except ValueError as ve:
        raise ValueError("Invalid subnet provided. from {ve}")
    return open_hosts

def question_refinement_findTgts(subnet: str) -> List[str]:
    try:
        subnet = ipaddress.ip_network(subnet, strict=False)
    except ValueError as e:
        return ['Invalid subnet']
    open_hosts = []
    port = 445
    timeout = 1.0
    def is_port_open(ip: str, port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            return result == 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(is_port_open, str(ip), port): str(ip) for ip in subnet.hosts()}
        for future in concurrent.futures.as_completed(futures):
            ip = futures[future]
            try:
                if future.result():
                    open_hosts.append(ip)
            except Exception as e:
                continue
    return open_hosts

def alternative_approaches_findTgts(subNet):
    import socket
    from ipaddress import ip_network
    open_hosts = []
    net = ip_network(subNet, strict=False)
    for host in net.hosts():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            try:
                if sock.connect_ex((str(host), 445)) == 0:
                    open_hosts.append(str(host))
            except socket.error:
                pass
    return open_hosts

def context_manager_findTgts(subNet):
    import socket
    import ipaddress
    open_ports = []
    for ip in ipaddress.IPv4Network(subNet):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((str(ip), 445))
            if result == 0:
                open_ports.append(str(ip))
    return open_ports

import socket
from ipaddress import ip_network
def flipped_interaction_3_findTgts(subNet):
    port = 445
    open_hosts = []
    for host in ip_network(subNet).hosts():
        with socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((str(host), port))
            if result == 0:
                open_hosts.append(str(host))
    return open_hosts

import nmap
def flipped_interaction_4_findTgts(subNet):
    nm = nmap.PortScanner()
    nm.scan(hosts=subNet, arguments='-p 445')
    open_hosts = []
    for host in nm.all_hosts():
        if nm[host].has_tcp(445) and nm[host]['tcp'][445]['state'] == 'open':
            open_hosts.append(host)
    return open_hosts

import nmap
def flipped_interaction_5_findTgts(subNet):
    nm = nmap.PortScanner()
    open_hosts = []
    try:
        nm.scan(hosts=subNet, arguments='-p 445 --open')
        for host in nm.all_hosts():
            if nm[host].has_tcp(445) and nm[host]['tcp'][445]['state'] == 'open':
                open_hosts.append(host)
    except Exception as e:
        print(f"An error occurred: {e}")
    return open_hosts

def iterative_prompting_3_find_tgts(subnet):
    import socket
    import ipaddress
    if not isinstance(subnet, str):
        raise ValueError("Subnet must be provided as a string in CIDR notation.")
    try:
        network = ipaddress.ip_network(subnet, strict=False)
    except ValueError as ve:
        raise ValueError(f"Invalid subnet: {ve}")
    open_hosts = []
    port = 445
    for ip in network.hosts():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((str(ip), port))
                if result == 0:
                    open_hosts.append(str(ip))
        except socket.error as se:
            print(f"Socket error when scanning {ip}: {se}")
        except Exception as e:
            print(f"Unexpected error when scanning {ip}: {e}")
    return open_hosts

from socket import socket, AF_INET, SOCK_STREAM
import threading
import ipaddress
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
open_ports = []
lock = threading.Lock()
def iterative_prompting_4_find_tgts(sub_net):
    if not isinstance(sub_net, str) or not sub_net:
        raise ValueError("sub_net must be a non-empty string.")
    open_hosts = []
    try:
        nmap_result = subprocess.check_output(
            ["nmap", "-p", "445", "-open", sub_net],
            stderr=subprocess.STDOUT,
            text=True,
            timeout=60
        )
        for line in nmap_result.splitlines():
            if "/tcp open" in line:
                parts = line.split()
                if parts:
                    open_hosts.append(parts[0])
    except subprocess.TimeoutExpired:
        print("Nmap scan timed out.")
    except subprocess.CalledProcessError as e:
        print(f"Nmap failed: {e.output}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return open_hosts

def iterative_prompting_5_find_tgts(subnet):
    import socket
    from ipaddress import ip_network, AddressValueError, NetmaskValueError
    open_hosts = []
    try:
        network = ip_network(subnet, strict=False)
    except (AddressValueError, NetmaskValueError) as e:
        print(f"Invalid subnet provided: {e}")
        return open_hosts
    for ip in network.hosts():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((str(ip), 445))
                if result == 0:
                    open_hosts.append(str(ip))
        except socket.error as sock_err:
            print(f"Socket error occurred: {sock_err}")
    return open_hosts

def few_shots_prompting_findTgts(subNet):
    import socket
    import ipaddress
    open_hosts = []
    for ip in ipaddress.IPv4Network(subNet):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            result = s.connect_ex((str(ip), 445))
            if result == 0:
                open_hosts.append(str(ip))
        except Exception as e:
            print(f'Error checking {ip}: {e}')
        finally:
            s.close()
    return open_hosts

def cot_prompting_findTgts(subNet):
    import socket
    import ipaddress
    open_hosts = []
    network = ipaddress.ip_network(subNet, strict=False)
    for ip in network.hosts():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            result = s.connect_ex((str(ip), 445))
            if result == 0:
                open_hosts.append(str(ip))
        except Exception as e:
            continue
        finally:
            s.close()
    return open_hosts

def fact_check_list_findTgts(subNet):
    import socket
    import ipaddress
    open_hosts = []
    for ip in ipaddress.ip_network(subNet, strict=False):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((str(ip), 445))
            if result == 0:
                open_hosts.append(str(ip))
            sock.close()
        except Exception as e:
            print(f"Error scanning {ip}: {e}")
            continue
    return open_hosts

def not_interactive_mix_findTgts(subNet):
    import nmap
    import ipaddress
    try:
        network = ipaddress.IPv4Network(subNet, strict=False)
    except ValueError as e:
        raise ValueError("Invalid IPv4 network address.") from e
    nmScan = nmap.PortScanner()
    open_hosts = []
    for host in network.hosts():
        try:
            nmScan.scan(str(host), '445')
            if 'tcp' in nmScan[str(host)] and 445 in nmScan[str(host)]['tcp']:
                if nmScan[str(host)]['tcp'][445]['state'] == 'open':
                    open_hosts.append(str(host))
        except nmap.PortScannerError as err:
            continue
    return open_hosts

def interactive_mix_findTgts(subnet):
    import nmap
    from ipaddress import ip_network
    import socket
    def is_valid_ip(ip):
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False
    open_hosts = []
    if not isinstance(subnet, str):
        raise ValueError("Invalid subnet format. The subnet must be a string in CIDR notation.")
    try:
        network = ip_network(subnet, strict=False)
    except ValueError as ve:
        raise ValueError("Invalid subnet format. Please use CIDR notation like '192.168.1.0/24'.") from ve
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=str(network), arguments='-p 445 --open')
        for host in nm.all_hosts():
            if 'tcp' in nm[host]:
                port_data = nm[host]['tcp'].get(445)
                if port_data and port_data.get('state') == 'open':
                    if is_valid_ip(host):
                        open_hosts.append(host)
    except nmap.PortScannerError as pse:
        print(f"PortScanner error: {pse}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return open_hosts

def baseline_findTgts(subNet):
    import socket
    from ipaddress import ip_network
    open_hosts = []
    hosts = ip_network(subNet).hosts()
    target_port = 445
    for host in hosts:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((str(host), target_port))
            if result == 0:
                open_hosts.append(str(host))
        except Exception as e:
            pass
        finally:
            sock.close()
    return open_hosts

