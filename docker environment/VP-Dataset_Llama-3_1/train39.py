import dpkt
from dpkt.utils import inet_to_str
import os
import pip
import pyshark
import socket
import scapy
from scapy.all import rdpcap, IP, TCP, Scapy_Exception

def ground_truth_code_findAttack(pcap):
    pktCount = {}
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            if dport == 80:
                stream = f"{src}:{dst}"
                if stream in pktCount:
                    pktCount[stream] += 1
                else:
                    pktCount[stream] = 1
        except Exception as e:
            print("Errore:", e)
    return pktCount

def persona_findAttack(pcap):
	from scapy.all import rdpcap, TCP
	count = 0
	attacks = set()
	pkts = rdpcap(pcap)
	for pkt in pkts:
		if pkt.haslayer(TCP):
			tcp = pkt[TCP]
			if tcp.dport == 80:
				attacks.add('%s:%s' % (pkt[IP].src, pkt[IP].dst))
			count += 1
	return {'count': count, 'attacks': list(attacks)}

def template_findAttack(pcap):
    try:
        packets = rdpcap(pcap)
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return {}
    except PermissionError:
        print("Error: No permission to read the file.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    tcp_packets_with_port_80 = []
    packet_counter = 0
    for packet in packets:
        if packet.haslayer(TCP) and packet.getlayer(TCP).dport == 80:
            ip_source = packet.getlayer(IP).src
            ip_destination = packet.getlayer(IP).dst
            entry = f"{ip_source}:{ip_destination}".replace(' ', '')
            if entry not in tcp_packets_with_port_80:
                tcp_packets_with_port_80.append(entry)
                packet_counter += 1
    if packet_counter > 0:
        return packet_counter
    return None

def question_refinement_findAttack(pcap_file):
    from scapy.all import rdpcap, TCP
    packets = rdpcap(pcap_file)
    count_dict = {}
    for packet in packets:
        if packet.haslayer(TCP):
            if packet[TCP].dport == 80:
                ip_src = packet[IP].src
                ip_dst = packet[IP].dst
                pair = f'{ip_src}:{ip_dst}'
                if pair in count_dict:
                    count_dict[pair] += 1
                else:
                    count_dict[pair] = 1
    return count_dict

def alternative_approaches_findAttack(pcap):
    import pyshark
    try:
        capture = pyshark.FileCapture(pcap)
        count = {}
        for packet in capture:
            if hasattr(packet, 'tcp') and packet.tcp.dstport == '80':
                key = f"{packet.ip.src}:{packet.ip.dst}"
                if key in count:
                    count[key] += 1
                else:
                    count[key] = 1
        return count
    except FileNotFoundError:
        print("The file was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    finally:
        if 'capture' in locals():
            capture.close()
            
def context_manager_findAttack(pcap):
	try:
		dpkt = dpkt
		f = open(pcap, 'rb')
		pcap_reader = dpkt.pcap.Reader(f)
		count_dict = {}
		for timestamp, buf in pcap_reader:
			packet = dpkt.ethernet.Ethernet(buf)
			if packet.type == 2048:
				ip = packet.data
				if ip.__class__.__name__ == 'IP' and ip.len > 0:
					tcp = ip.data
					if tcp.__class__.__name__ == 'TCP' and tcp.dport == 80:
						source_ip = '.'.join(str(ip.src).split('.')[:-1] + [str(int(str(ip.src).split('.')[-1]))])
						dest_ip = '.'.join(str(ip.dst).split('.')[:-1] + [str(int(str(ip.dst).split('.')[-1]))])
						key = '{}:{}'.format(source_ip, dest_ip)
						if key in count_dict:
							count_dict[key] += 1
						else:
							count_dict[key] = 1
		f.close()
		return dict(count_dict)
	except Exception as e:
		return(f'Exception:{format(e)}')
          
def flipped_interaction_3__findAttack(pcap):
	try:
		with open(pcap, 'rb') as file:
			pcapFile = dpkt.pcap.Reader(file)
			result = {}
			for timestamp, buf in pcapFile:
				try:
					pkt = dpkt.ethernet.Ethernet(buf)
					ip = pkt.data
					tcp = ip.data
					if isinstance(tcp, dpkt.tcp.TCP) and tcp.dport == 80:
						key = '{}:{}'.format(ip.src, ip.dst)
						result[key] = result.get(key, 0) + 1
				except:
					pass
		return result
	except FileNotFoundError:
		print('Error: File not found')
		return {}
	except dpkt.dpkt.NeedData:
		print('Error: Invalid pcap file')
		return {}
	except Exception as e:
		print('An error occurred: {}'.format(str(e)))
		return {}

import socket

def ipkt_to_str(ip):
    return socket.inet_ntoa(ip)
     
def flipped_interaction_4__findAttack(pcap):
    tcp_packets = {}
    for timestamp, buf in pcap:
        pkt = dpkt.ethernet.Ethernet(buf)
        if pkt.type != dpkt.ethernet.ETH_TYPE_IP:
            continue
        ip = pkt.data
        if ip.__class__.__name__ == 'IP':
            if ip.p != 6:
                continue
            tcp = ip.data
            if tcp.__class__.__name__ != 'TCP' or tcp.dport != 80:
                continue
            key = '%s:%s' % (ipkt_to_str(ip.src), ipkt_to_str(ip.dst))
            if key in tcp_packets:
                tcp_packets[key] += 1
            else:
                tcp_packets[key] = 1
        elif ip.__class__.__name__ == 'IP6':
            if ip.nxt != 6:
                continue
            tcp = ip.data
            if tcp.__class__.__name__ != 'TCP' or tcp.dport != 80:
                continue
            key = '%s:%s' % (ipkt_to_str(ip.src), ipkt_to_str(ip.dst))
            if key in tcp_packets:
                tcp_packets[key] += 1
            else:
                tcp_packets[key] = 1
    return tcp_packets


def flipped_interaction_5__findAttack(pcap):
    packet_counts = {}
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if isinstance(ip, dpkt.ip.IP):
                src_ip = socket.inet_ntoa(ip.src)
                dst_ip = socket.inet_ntoa(ip.dst)
                if isinstance(ip.data, dpkt.tcp.TCP) and ip.data.dport == 80:
                    key = '{}:{}'.format(src_ip, dst_ip)
                    packet_counts[key] = packet_counts.get(key, 0) + 1
        except Exception:
            pass
    return packet_counts

def iterative_prompting_3__findAttack(pcap):
    import scapy.all as scapy
    if not pcap or not isinstance(pcap, str):
        raise ValueError('pcap must be a string')
    try:
        packets = scapy.rdpcap(pcap)
    except scapy.Scapy_Exception as e:
        raise RuntimeError(f'Failed to read pcap file: {e}')
    result = {}
    for packet in packets:
        if packet.haslayer(scapy.TCP) and packet[scapy.TCP].dport == 80:
            try:
                key = '{}:{}'.format(packet[scapy.IP].src, packet[scapy.IP].dst)
                result[key] = result.get(key, 0) + 1
            except Exception as e:
                raise RuntimeError(f'Failed to process packet: {e}')
    return result

def iterative_prompting_4__findAttack(pcap):
    if not isinstance(pcap, str):
        raise TypeError('pcap must be a string')
    try:
        packets = rdpcap(pcap)
    except FileNotFoundError:
        raise FileNotFoundError('pcap file not found')
    except Exception as e:
        raise Exception(f'Failed to read pcap file: {e}')
    result: dict[str, int] = {}
    for packet in packets:
        if isinstance(packet, scapy.packet.Packet) and packet.haslayer(scapy.layers.inet.TCP) and packet.haslayer(scapy.layers.inet.IP):
            if hasattr(packet[scapy.layers.inet.TCP], 'dport') and packet[scapy.layers.inet.TCP].dport == 80:
                src_ip = packet[scapy.layers.inet.IP].src
                dst_ip = packet[scapy.layers.inet.IP].dst
                pair = f'{src_ip}:{dst_ip}'
                result[pair] = result.get(pair, 0) + 1
    return result

def iterative_prompting_5__findAttack(pcap):
    if not isinstance(pcap, str):
        raise TypeError('PCAP file path must be a string')
    if not pcap.lower().endswith('.pcap') and not pcap.lower().endswith('.pcapng'):
        raise ValueError('Invalid PCAP file extension')
    try:
        packets = rdpcap(pcap)
    except FileNotFoundError:
        raise ValueError('PCAP file not found')
    except Scapy_Exception as e:
        raise Exception(f'Failed to read PCAP file: {e}')
    entries = {}
    if packets is None or len(packets) == 0:
        return entries
    for packet in packets:
        if packet.haslayer(TCP) and packet.haslayer(IP) and packet[TCP].dport == 80:
            try:
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                entry = f'{src_ip}:{dst_ip}'
                entries[entry] = entries.get(entry, 0) + 1
            except AttributeError as e:
                print(f'Failed to parse packet: {e}')
    return entries

def few_shots_prompting_findAttack(pcap):
	count = 0
	entry_dict = {}
	for (ts, buf) in pcap:
		try:
			aapl = dpkt.ethernet.Ethernet(buf)
			aip = aapl.data
			if type(aip.data) == dpkt.tcp.TCP and aip.data.dport == 80:
				count += 1
				ipsrc = socket.inet_ntoa(aip.src)
				ipdst = socket.inet_ntoa(aip.dst)
				entry = '{}:{}'.format(ipsrc, ipdst)
				if entry in entry_dict:
					entry_dict[entry] += 1
				else:
					entry_dict[entry] = 1
		except:
			pass
	return entry_dict

def cot_prompting_findAttack(pcap):
    count = 0
    entries = {}
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            if dport == 80:
                count += 1
                entry = '{}:{}'.format(src, dst)
                entries[entry] = entries.get(entry, 0) + 1
        except:
            pass
    return entries

def fact_check_list_findAttack(pcap):
    count_dict = {}
    try:
        capture = pyshark.FileCapture(pcap, display_filter='tcp.port==80')
        for packet in capture:
            try:
                ip_src = packet.ip.src
                ip_dst = packet.ip.dst
                key = f'{ip_src}:{ip_dst}'
                if key in count_dict:
                    count_dict[key] += 1
                else:
                    count_dict[key] = 1
            except AttributeError:
                continue
        capture.close()
    except Exception as e:
        return(f'An error occurred: {e}')
    return count_dict

def not_interactive_mix_findAttack(pcap):
    if pcap is None or not isinstance(pcap, str):
        raise ValueError("Invalid pcap file path")
    if not pcap.endswith('.pcap'):
        raise ValueError("Invalid pcap file extension")
    try:
        ip_count = {}
        with open(pcap, 'rb') as f:
            pcap_data = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_data:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                    ip = eth.data
                    tcp = ip.data
                    if ip.__class__.__name__ == 'IP' and tcp.__class__.__name__ == 'TCP' and tcp.dport == 80:
                        src_ip = inet_to_str(ip.src)
                        dst_ip = inet_to_str(ip.dst)
                        ip_count[src_ip+':'+dst_ip] = ip_count.get(src_ip+':'+dst_ip, 0) + 1
                except Exception as e:
                    print(f"An error occurred: {e}")
        return ip_count
    except FileNotFoundError:
        return("The pcap file was not found")
    except Exception as e:
        return(f"An error occurred: {e}")
    
import pyshark
def interactive_mix_findattack(pcap_file, display_filter='tcp dst port 80'):
    packet_count = {}
    try:
        capture = pyshark.FileCapture(pcap_file, display_filter=display_filter)
        for packet in capture:
            try:
                if hasattr(packet, 'ip') and hasattr(packet, 'tcp'):
                    src_ip = packet.ip.src
                    dst_ip = packet.ip.dst
                    key = f'{src_ip}:{dst_ip}'
                    packet_count[key] = packet_count.get(key, 0) + 1
            except Exception as e:
                print(f'Error parsing packet: {e}')
    except Exception as e:
        return(f'Error reading pcap file: {e}')
    return packet_count

def baseline_findAttack(pcap):
    count = 0
    entries = {}
    for packet in pcap:
        try:
            ip = packet['IP']
            tcp = ip['TCP']
            src_ip = ip['src']
            dst_ip = ip['dst']
            dst_port = tcp['dstport']
            if dst_port == 80:
                entry = '{}:{}'.format(src_ip, dst_ip)
                if entry in entries:
                    entries[entry] += 1
                else:
                    entries[entry] = 1
                count += 1
        except Exception as e:
            continue
    return count, entries
