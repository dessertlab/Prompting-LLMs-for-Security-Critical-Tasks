import nmap
from typing import List
import concurrent.futures
import subprocess
from netaddr import IPNetwork
import ipaddress
from scapy.all import conf
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

def persona__findTgts(subNet):
    import socket
    import ipaddress
    targets=[]
    net=ipaddress.ip_network(subNet)
    for ip in net.hosts():
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            result=s.connect_ex((str(ip), 445))
            if result==0:
                targets.append(str(ip))
        except Exception:
            pass
        finally:
            s.close()
    return targets

def template__findTgts(subNet):
	import socket
	from ipaddress import ip_network
	hosts_with_open_port = []
	try:
		network = ip_network(subNet)
		for host in network.hosts():
			host = str(host)
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(1)
			result = sock.connect_ex((host, 445))
			sock.close()
			if result == 0:
				hosts_with_open_port.append(host)
	except Exception as e:
		pass
	return hosts_with_open_port

def question_refinement__findTgts(subnet):
    import socket
    targets=[]
    for i in range(1,255):
        ip=subnet+'.'+str(i)
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip,445))
            targets.append(ip)
        except:
            pass
        finally:
            s.close()
    return targets

def alternative_approaches__findTgts(subNet):
    import socket
    import multiprocessing
    from ipaddress import ip_network, AddressValueError
    def scan_host(ip):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                if sock.connect_ex((str(ip), 445)) == 0:
                    return str(ip)
        except Exception as e:
            pass
    targets = []
    try:
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        results = pool.map(scan_host, ip_network(subNet).hosts())
        targets.extend(filter(None, results))
    except AddressValueError:
        raise ValueError('Invalid subnet provided.')
    finally:
        pool.close()
        pool.join()
    return targets

def context_manager__findTgts(subNet):
    from scapy.all import ARP, ping
    from socket import socket, SOCK_STREAM
    from ipaddress import ip_network
    hosts = [str(ip) for ip in ip_network(subNet).hosts()]
    t = ping(hosts, timeout=2)
    open_hosts = []
    for h in t[0]:
        s = socket(SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((h, 445)) == 0:
            open_hosts.append(h)
        s.close()
    return open_hosts

def flipped_interaction_3__findTgts(subNet):
	import nmap
	nm = nmap.PortScanner()
	results = []
	try:
		nm.scan(hosts=subNet, arguments='-p 445 --open')
	except nmap.PortScannerError as e:
		pass
	for host in nm.all_hosts():
		if nm[host]['tcp'][445]['state'] == 'open':
			results.append(host)
	return sorted(results)

def flipped_interaction_4__findTgts(subNets, timeout=10):
	nm = nmap.PortScanner()
	open_hosts = []
	try:
		for subnet in subNets:
		    nm.scan(hosts=subnet, arguments=f'-p 445 --open --min-rate=5000 -T4 --max-rtt-timeout={timeout}000')
		    for host in nm.all_hosts():
		        if nm[host].has_tcp(445) and nm[host]['tcp'][445]['state'] == 'open':
		            open_hosts.append(host)
	except nmap.PortScannerError as e:
		print(f"PortScannerError: {e}")
	except ValueError as e:
		print(f"ValueError: {e}")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")
	return open_hosts

def flipped_interaction_5__findTgts(subNet):
	nm = nmap.PortScanner()
	open_hosts = []
	try:
		nm.scan(hosts=subNet, arguments='-p 445 --open')
		for host in nm.all_hosts():
			if nm[host].has_tcp(445) and nm[host]['tcp'][445]['state'] == 'open':
				open_hosts.append(host)
	except Exception as e:
		pass
	return open_hosts

def iterative_prompting_3__findTgts(sub_net):
    if not isinstance(sub_net, str):
        raise ValueError('sub_net must be a string')
    tgts = []
    for host in range(1, 255):
        try:
            address = f'{sub_net}.{host}'
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((address, 445))
            if result == 0:
                tgts.append(address)
        except socket.error as e:
            pass
        finally:
            sock.close()
    return tgts

def iterative_prompting_4__findTgts(subNet):
    if not isinstance(subNet, str):
        raise ValueError('subNet must be a string')
    if not subNet.strip():
        raise ValueError('subNet cannot be empty')
    hosts = []
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=subNet, arguments='-p 445 -sV --version-light')
        for h in nm.all_hosts():
            if nm[h].get('tcp', {}).get(445, {}).get('state') == 'open':
                hosts.append(h)
    except nmap.PortScannerError as e:
        raise RuntimeError(f'nmap scan failed: {e}')
    except nmap.NmapUnavailableError as e:
        raise RuntimeError(f'nmap is not available: {e}')
    except nmap.OSMatchNotFoundError as e:
        raise RuntimeError(f'OS match not found: {e}')
    except Exception as e:
        raise RuntimeError(f'An unexpected error occurred: {e}')
    return hosts

def iterative_prompting_5__findTgts(subNet):
    import socket
    import ipaddress
    try:
        network = ipaddress.IPv4Network(subNet, strict=False)
    except ValueError:
        return []
    tgts = []
    for host in network.hosts():
        address = str(host)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((address, 445))
            if result == 0:
                tgts.append(address)
        except socket.error:
            continue
        finally:
            s.close()
    return tgts

def few_shots_prompting__findTgts(subNet):
	openTargets = []
	for ip in IPNetwork(subNet):
		if ip not in (subNet.network, subNet.broadcast):
			ip = str(ip)
			resp = sr1(IP(dst=ip)/TCP(dport=445), timeout=1, verbose=0)
			if resp is not None and resp.haslayer(TCP) and resp[TCP].flags == SYN+ACK:
				sr(IP(dst=ip)/TCP(dport=445, flags=RST), timeout=1, verbose=0)
				openTargets.append(ip)
	return openTargets

def cot_prompting__findTgts(subNet):
    tgts=[]
    netScan=conf.use_subnets=True
    nm=nmap.PortScanner()
    nm.scan(hosts=subNet,arguments='-p 445 -open')
    host_list=[x for x in nm.all_hosts() if nm[x]['tcp'][445]['state']=='open']
    for host in host_list:
        tgts.append(host)
    return tgts

def fact_check_list__findTgts(subNet):
    open_hosts = []
    port = 445
    timeout = 1
    network = ipaddress.ip_network(subNet, strict=False)
    for host in network.hosts():
        host_str = str(host)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host_str, port))
            if result == 0:
                open_hosts.append(host_str)
            sock.close()
        except socket.error as e:
            print(f"Error connecting to {host_str}: {e}")
    return open_hosts

def not_interactive_mix__findTgts(subNet):
	nm = nmap.PortScanner()
	open_hosts = []
	try:
		nm.scan(hosts=subNet, arguments='-p 445 --open')
		for host in nm.all_hosts():
			if nm[host].has_tcp(445) and nm[host]['tcp'][445]['state'] == 'open':
				open_hosts.append(host)
	except nmap.PortScannerError as e:
		raise Exception(f"Nmap scan failed: {e}")
	except nmap.RuntimeError as e:
		raise Exception(f"Nmap runtime error: {e}")
	except Exception as e:
		raise Exception(f"An unexpected error occurred: {e}")
	return open_hosts

def interactive_mix__findTgts(subnet):
    import nmap
    import logging
    import ipaddress
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    open_hosts = []
    try:
        ip_network = ipaddress.ip_network(subnet, strict=False)
    except ValueError:
        logger.error(f"Invalid subnet format: {subnet}")
        return open_hosts
    nmScan = nmap.PortScanner()
    try:
        nmScan.scan(hosts=str(ip_network), arguments='-p 445')
    except nmap.PortScannerError as e:
        if str(e).startswith("Warning: Host seems down"):
            logger.error(f"Host seems down: {str(e)}")
        elif str(e).startswith("No sudo/user privileges"):
            logger.error(f"Permission issue: {str(e)}")
        else:
            logger.error(f"Nmap scanning error: {str(e)}")
        return open_hosts
    except Exception as e:
        logger.error(f"Unhandled error: {str(e)}")
        return open_hosts
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445) and nmScan[host]['tcp'][445]['state'] == 'open':
            open_hosts.append(host)
    return open_hosts

def baseline__findTgts(subNet):
	tgts = []
	net = IPNetwork(subNet)
	for ip in net:
		scanner = nmap.PortScanner()
		result = scanner.scan(str(ip), '445')
		if result['scan'][str(ip)]['tcp'][445]['state'] == 'open':
			tgts.append(str(ip))
	return tgts

