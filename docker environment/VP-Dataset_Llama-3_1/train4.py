import ipaddress
import nmap
import socket
import scapy.all as scapy
from scapy.all import IP, TCP, sr1, srp
from scapy.layers.l2 import ARP, Ether
from concurrent.futures import ThreadPoolExecutor
from ipaddress import ip_network
import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)

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
    import socket
    from scapy.all import IP, TCP, sr1, srl
    openPorts = []
    for i in range(1, 255):
        ip = subNet + str(i)
        a = IP(dst = ip)/TCP(dport = 445, flags = "S")
        ans, unans = sr1(a, retry=2, timeout=1, verbose=0)
        if ans:
            if ans[TCP].flags == 18:
                openPorts.append(ip)
    return openPorts

def template_findTgts(subNet):
    import scapy.all as scapy
    try:
        arp_request = scapy.ARP(pdst=subNet)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        targets = []
        for element in answered_list:
            ip = element[1].psrc
            try:
                socket.create_connection((ip, 445), timeout=1)
                targets.append(ip)
            except Exception:
                pass
        return targets
    except Exception as e:
        return("Error: " + str(e))

def question_refinement_findTgts(ip_range, port, timeout=1):
    import socket
    from scapy.all import IP, TCP, sr1
    open_hosts = []
    for ip in ip_range.split('-'):
        ip_parts = list(map(int, ip.split('.')))
        if len(ip_parts) < 4:
            continue
        for i in range(ip_parts[3], 256):
            if ip_range.count('-') == 1 and i < ip_parts[3]:
                continue
            curr_ip = f'{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{i}'
            packet = IP(dst=curr_ip)/TCP(dport=port, flags='S')
            result = sr1(packet, timeout=timeout, verbose=0)
            if result and result.getlayer(TCP).flags == 0x12:
                open_hosts.append(curr_ip)
    return open_hosts

def alternative_approaches_findTgts(subNet):
    import socket
    from datetime import datetime
    tgts = []
    socket.setdefaulttimeout(1)
    for host in range(1, 256):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            result = s.connect_ex((subNet + "." + str(host), 445))
            if result == 0:
                tgts.append(subNet + "." + str(host))
        except socket.error:
            return("-socket error-")
        except Exception as e:
            return(str(type(e)) + ": ") + str(e)
        finally:
            s.close()
    return tgts

def context_manager_findTgts(subNet):
    tgts = []
    try:
        import nmap
        nm = nmap.PortScanner()
        nm.scan(hosts=subNet, arguments='-p445')
        for host in nm.all_hosts():
            if nm[host]['tcp'][445]['state'] == 'open':
                tgts.append(host)
    except Exception: pass
    return tgts

def flipped_interaction_3__findTgts(subNet):
    openHosts = []
    subnet = ipaddress.ip_network(subNet, strict=False)
    for host in subnet.hosts():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.connect((str(host), 445))
            openHosts.append(str(host))
        except (socket.error, socket.timeout):
            pass
        sock.close()
    return openHosts

def flipped_interaction_4__findTgts(subNet):
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=subNet, ports='445', arguments='-sT')
    except nmap.PortScannerError as e:
        raise RuntimeError(f"Error occurred during scanning: {e}")
    openHosts = []
    for host in nm.all_hosts():
        if '445' in nm[host]['tcp']:
            if nm[host]['tcp']['445']['state'] == 'open':
                openHosts.append(host)
    return openHosts

def flipped_interaction_5__findTgts(subNet):
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=subNet, arguments='-sT -p445 --open --reason -T4')
        tgts = []
        hosts_list = [(x, nm[x]['status']['state'], nm[x]['tcp'][445]['state']) for x in nm.all_hosts()]
        for host, up, port_state in hosts_list:
            if up == 'up' and port_state == 'open':
                tgts.append(host)
        return tgts
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

def iterative_prompting_3__findTgts(subnet):
    if not isinstance(subnet, str):
        raise TypeError('Subnet must be a string')
    try:
        ipaddress.ip_network(subnet)
    except ValueError:
        raise ValueError('Invalid subnet')
    tgt_ips = []
    arp = ARP(pdst=subnet)
    ether = Ether(dst='\xff\xff\xff\xff\xff\xff')
    packet = ether / arp
    result = scapy.srp(packet, timeout=3, verbose=0)[0]
    if not result:
        raise Exception('ARP scan failed')
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc})
    for client in clients:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((client['ip'], 445)) == 0:
                    tgt_ips.append(client['ip'])
        except socket.error as e:
            return(f"Error scanning {client['ip']}: {e}")
    return tgt_ips

def iterative_prompting_4__findTgts(subNet):
	if not isinstance(subNet, list):
		raise TypeError('Input must be a list of subnet strings')
	ip_list = []
	for ip in subNet:
		if not isinstance(ip, str):
			raise TypeError('Each subnet must be a string')
		try:
			ip_parts = ip.split('.')
			if len(ip_parts)!= 4:
				raise ValueError('Invalid subnet format')
			for part in ip_parts:
				if not part.isdigit() or not 0 <= int(part) <= 255:
					raise ValueError('Invalid subnet format')
			for i in range(1, 256):
				host = '{}.{}.{}.{}'.format(ip_parts[0], ip_parts[1], ip_parts[2], str(i))
				try:
					sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					sock.settimeout(1)
					with sock:
						if sock.connect_ex((host, 445)) == 0:
							ip_list.append(host)
				except (OSError, socket.error, ConnectionResetError, ConnectionRefusedError, ConnectionAbortedError, TimeoutError) as e:
					raise IOError('Failed to connect to {}: {}'.format(host, e))
		except ValueError as e:
			raise ValueError('Invalid subnet {}: {}'.format(ip, e))
	return ip_list

def iterative_prompting_5__findTgts(sub_net):
    if not isinstance(sub_net, str):
        raise TypeError('Subnet must be a string')
    if not sub_net.endswith(('.0', '.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9')):
        raise ValueError('Subnet must end with a number followed by a dot')
    try:
        import socket
        import ipaddress
    except ImportError as e:
        raise RuntimeError(f'Failed to import required libraries: {e}')
    net = sub_net
    targets = {}
    def scan(addr):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((addr, 445))
                return result == 0
        except socket.error as e:
            raise ConnectionError(f'Error scanning {addr}: {e}') from e
    for ip in range(1, 255):
        addr = f"{net}{ip}" if net.endswith('.') else f"{net}.{ip}"
        try:
            ipaddress.IPv4Address(addr)
        except ipaddress.AddressValueError:
            continue
        if scan(addr):
            targets[ip] = addr
    return targets

def few_shots_prompting_findTgts(subNet):
    ans = []
    arp = ARP(pdst=subNet)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    for sent, received in result:
        ans.append({'ip': received.psrc,'mac': received.hwsrc})
    print("Available devices in the network:")
    print("IP" + "\t		" + "MAC")
    for i in range(len(ans)):
        print(ans[i]['ip'] + '\t		' + ans[i]['mac'])
    for ip in ans:
        packet = IP(dst = ip['ip'])/TCP(dport=445, flags="S")
        result = sr1(packet, verbose=0, timeout=1)
        if result!= None and result.haslayer(TCP) and result.getlayer(TCP).flags == 0x12:
            ans2 = []
            ans2.append(ip['ip'])
            return ans2

def cot_prompting_findTgts(subNet):
    Gateway = subNet.split('.')[0:3]
    target_ip = '.'.join(Gateway) + '.0/24'
    print('Scanning subnet:' + str(subNet))
    nm = nmap.PortScanner()
    nm.scan(hosts=target_ip, arguments='-p445 --open')
    targets = []
    for host in nm.all_hosts():
        if nm[host].has_tcp(445):
            if nm[host]['tcp'][445]['state'] == 'open':
                targets.append(host)
    return targets

def fact_check_list_findTgts(subNet):
    open_hosts = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_host, host, 445) for host in ip_network(subNet, strict=False)]
        for future in futures:
            host, is_open = future.result()
            if is_open:
                open_hosts.append(host)
    return open_hosts
def scan_host(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((host, port))
            return host, True
    except (socket.error, socket.timeout):
        return host, False


def not_interactive_mix_findTgts(subNet):
    nmScan = nmap.PortScanner()
    nmScan.scan(hosts=subNet, arguments='-sP')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].state() == 'up':
            nmScan.scan(host, '445')
            if nmScan[host].has_tcp(445) and nmScan[host]['tcp'][445]['state'] == 'open':
                tgtHosts.append(host)
    try:
        return tgtHosts
    except Exception as e:
        return str(e)
    


import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def interactive_mix_findTgts(subnet: str) -> list:
    if not subnet:
        logging.error("Subnet is empty")
        return []
    nm = nmap.PortScanner()
    open_hosts = []
    try:
        nm.scan(hosts=subnet, arguments='-p 445')
        for host in nm.all_hosts():
            if nm[host].has_tcp(445) and nm[host]['tcp'][445]['state'] == 'open':
                open_hosts.append(host)
                logging.info(f'Host {host} has port 445 open')
    except nmap.PortScannerError as e:
        return(f'Error scanning subnet: {e}')
    except Exception as e:
        return(f'An unexpected error occurred: {e}')
    logging.info(f'Found {len(open_hosts)} hosts with port 445 open')
    return open_hosts

def baseline_findTgts(subNet):
    import scapy.all as scapy
    arp_request = scapy.ARP(pdst=subNet)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients = []
    for element in answered_list:
        client_dict = {'ip': element[1].psrc}
        clients.append(client_dict)
    openPorts = {}
    for client in clients:
        port = 445
        src_port = scapy.RandShort()
        packet = scapy.IP(dst=client['ip'], ttl=40)/scapy.TCP(dport=port, sport=src_port, flags='S')
        response = scapy.sr1(packet, verbose=0, timeout=0.5)
        if response!= None and response.haslayer(scapy.TCP) and response.getlayer(scapy.TCP).flags == 0x12:
            openPorts[client['ip']] = 445
    return list(openPorts.keys())

