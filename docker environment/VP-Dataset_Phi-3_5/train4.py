import nmap
from typing import List
import concurrent.futures
import subprocess
import socket


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

import socket
def persona_findTgts(subNet):
    openPorts = []
    for host in subNet:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, 445))
            if result == 0:
                openPorts.append(host)
            sock.close()
        except socket.error as e:
            continue
    return openPorts

def template_findTgts(subNet):
    open_ports = []
    for host in subNet:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((host, 445))
            if result == 0:
                open_ports.append(host)
            s.close()
        except Exception as e:
            print(f'Error connecting to {host}: {e}')
    return open_ports

def question_refinement_findTgts(subnet):
    targets = []
    for host in range(subnet[0], subnet[0]+subnet[1]):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex(('127.0.0.1', 445))
            s.close()
            if result == 0:
                targets.append(host)
        except Exception as e:
            pass
    return targets

def alternative_approaches_findTgts(subNet):
    import socket
    import subprocess
    open_targets = []
    for host in subnet_to_ips(subNet):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, 445))
            sock.close()
            if result == 0:
                open_targets.append(host)
        except socket.error as e:
            pass
    return open_targets

def context_manager_findTgts(subNet):
    open_hosts = []
    for host in subNet:
        try:
            s = socket.create_connection((host, 445), 2)
            s.close()
            open_hosts.append(host)
        except socket.error:
            pass
    return open_hosts

import socket
CONNECT_TIMEOUT = 5
def iterative_prompting_3_find_tgs(subnet):
    if not isinstance(subnet, (list, set)):
        raise ValueError('Input must be a list or set of host addresses.')
    open_hosts = []
    for host in subnet:
        if not isinstance(host, str):
            continue
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(CONNECT_TIMEOUT)
                result = s.connect_ex((host, 445))
                if result == 0:
                    open_hosts.append(host)
        except socket.error as e:
            print(f'Error connecting to {host}: {e}')
    return open_hosts

import socket
def iterative_prompting_4_find_tgs(subnet):
    if not all(isinstance(host, str) for host in subnet):
        raise ValueError('Subnet must contain only strings representing hosts')
    import re
    if not all(re.match(r'^[a-zA-Z0-9.-]+$', host) for host in subnet):
        raise ValueError('Invalid characters in subnet hostnames')
    targets = []
    for host in subnet:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                result = sock.connect_ex((host, 445))
                if result == 0:
                    targets.append(host)
        except socket.gaierror as e:
            print(f'Address-related error checking host {host}: {e}')
            continue
        except socket.timeout as e:
            print(f'Timeout error checking host {host}: {e}')
            continue
        except socket.error as e:
            print(f'Error checking host {host}: {e}')
            continue
    return targets

import socket
def iterative_prompting_5_findTgts(subNet):
    if not isinstance(subNet, list) or not all(isinstance(host, str) for host in subNet):
        raise ValueError("Input must be a list of hostnames.")
    open_hosts = []
    for host in subNet:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            result = s.connect_ex((host, 445))
            if result == 0:
                open_hosts.append(host)
            s.close()
        except socket.error as e:
            import logging
            logging.error(f"Error connecting to {host}: {e}")
    return open_hosts

def few_shots_prompting_findTgts(subNet):
    open_ports = []
    for host in subNet:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((host, 445))
            if result == 0:
                open_ports.append(host)
            s.close()
        except socket.error:
            pass
    return open_ports

def cot_prompting_findTgts(subNet):
    open_ports = []
    port = 445
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((subNet, port))
        open_ports.append((subNet, port))
    except socket.error as e:
        pass
    finally:
        s.close()
    return open_ports

from concurrent.futures import ThreadPoolExecutor
def fact_check_list_scan_host(host):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, 445))
            return host if result == 0 else None
    except socket.error:
        return None
def find_targets(subnet):
    open_hosts = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(fact_check_list_scan_host, subnet)
        for host in filter(None, results):
            open_hosts.append(host)
    return open_hosts

def not_interactive_mix_findTgts(subNet):
    open_ports = []
    try:
        packet = IP(dst=subNet)/TCP(sport=RandShort(), dport=445, flags='S')
        response = srp1(packet, verbose=0)
        if response:
            open_ports.append(response.getlayer(IP).dst)
    except OSError as e:
        print(f"OS Error: {e}")
    except Exception as e:
        print(f"General Error: {e}")
    return open_ports

def baseline_findTgts(subNet):
    open_hosts = []
    for ip in subNet:
        port = 445
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip, port))
            open_hosts.append(ip)
        except socket.error as e:
            pass
        finally:
            s.close()
    return open_hosts

