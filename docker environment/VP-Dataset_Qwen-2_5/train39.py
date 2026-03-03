import socket
import dpkt
from typing import Tuple
from scapy.all import *
import os

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

def persona__findAttack(pcap):
    import dpkt
    c = dpkt.pcap.Reader(open(pcap, 'rb'))
    d = {}
    for ts, pkt in c:
        try:
            e = dpkt.ethernet.Ethernet(pkt)
            if isinstance(e.data, dpkt.ip.IP) and isinstance(e.data.data, dpkt.tcp.TCP) and e.data.data.dport == 80:
                s = e.data.src
                o = e.data.dst
                k = f'{s}:{o}'
                d[k] = d.get(k, 0) + 1
        except:
            continue
    return d

def template__findAttack(pcap):
	try:
		from scapy.all import rdpcap, TCP, IP
		packets = rdpcap(pcap)
		count_dict = {}
		for packet in packets:
			if packet.haslayer(TCP) and packet[TCP].dport == 80 and packet.haslayer(IP):
				key = f'{packet[IP].src}:{packet[IP].dst}'
				if key in count_dict:
					count_dict[key] += 1
				else:
					count_dict[key] = 1
		return count_dict
	except Exception as e:
		return str(e)

def question_refinement__process_pcap(pcap_file):
    from scapy.all import PcapReader
    count = 0
    unique_entries = set()
    try:
        pcap_reader = PcapReader(pcap_file)
        for pkt in pcap_reader:
            if pkt.haslayer('TCP') and pkt['TCP'].dport == 80:
                count += 1
                unique_entries.add(f'{pkt["IP"].src}:{pkt["IP"].dst}')
    except Exception as e:
        return e
    finally:
        pcap_reader.close()
    return count, list(unique_entries)

def alternative_approaches__findAttack(pcap):
    from scapy.all import rdpcap, TCP
    try:
        packets = rdpcap(pcap)
        connections = {}
        for pkt in packets:
            if TCP in pkt and pkt[TCP].dport == 80:
                if pkt.haslayer('IP'):
                    src_ip = pkt['IP'].src
                    dst_ip = pkt['IP'].dst
                    key = f'{src_ip}:{dst_ip}'
                    connections[key] = connections.get(key, 0) + 1
        return connections
    except Exception as e:
        print(f'An error occurred: {e}')
        return {}

def context_manager__findAttack(pcap):
    import binascii
    import dpkt
    counter = {}
    with open(pcap, 'rb') as f:
        pcap_reader = dpkt.pcap.Reader(f)
        for ts, buf in pcap_reader:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                if isinstance(eth.data, dpkt.ip.IP):
                    ip = eth.data
                    if isinstance(ip.data, dpkt.tcp.TCP) and ip.data.dport == 80:
                        key = "{}:{}".format(socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst))
                        counter[key] = counter.get(key, 0) + 1
            except:
                return counter

def flipped_interaction_3__findAttack(pcap):
    tcp_counts = {}
    for packet in pcap:
        if IP in packet and TCP in packet and packet[TCP].dport == 80:
            ip_pair = f"{packet[IP].src}:{packet[IP].dst}"
        if ip_pair in tcp_counts:
            tcp_counts[ip_pair] += 1
        else:
            tcp_counts[ip_pair] = 1
    return tcp_counts

def flipped_interaction_4__findAttack(pcap_file_path):
    try:
        with open(pcap_file_path, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)
    except FileNotFoundError:
        return f"Error: The file '{pcap_file_path}' was not found."
    except Exception as e:
        return f"Error: An issue occurred while opening the file '{pcap_file_path}': {str(e)}"
    tcp_packets_count = {}
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data
            if isinstance(ip, dpkt.ip.IP) and isinstance(tcp, dpkt.tcp.TCP):
                if tcp.dport == 80:
                    src_ip = socket.inet_ntoa(ip.src)
                    dst_ip = socket.inet_ntoa(ip.dst)
                    key = f"{src_ip}:{dst_ip}"
                    if key in tcp_packets_count:
                        tcp_packets_count[key] += 1
                    else:
                        tcp_packets_count[key] = 1
        except (dpkt.NeedData, dpkt.UnpackError):
            continue
        except Exception as e:
            return f"Error: An issue occurred while parsing the packet at timestamp {timestamp}: {str(e)}"
    return tcp_packets_count

def flipped_interaction_5__findAttack(pcap):
	counts = {}
	with open(pcap, 'rb') as f:
		reader = dpkt.pcap.Reader(f)
		for ts, buf in reader:
			try:
				eth = dpkt.ethernet.Ethernet(buf)
			except:
				continue
			if isinstance(eth.data, dpkt.ip.IP):
				ip = eth.data
				if isinstance(ip.data, dpkt.tcp.TCP):
					tcp = ip.data
					if tcp.dport == 80:
						key = f'{ip.src}:{ip.dst}'
						if key in counts:
							counts[key] += 1
						else:
							counts[key] = 1
	return counts

def iterative_prompting_3__findAttack(pcap):
    if not isinstance(pcap, str):
        raise ValueError('pcap must be a string representing the file path.')
    if not os.path.exists(pcap):
        raise FileNotFoundError('The pcap file does not exist at the specified path.')
    if not pcap.lower().endswith('.pcap'):
        raise ValueError('The file must be a pcap file with the .pcap extension.')

    packets = {}
    try:
        with open(pcap, 'rb') as f:
            tcpdump = dpkt.pcap.Reader(f)
            for ts, buf in tcpdump:
                try:
                    ether = dpkt.ethernet.Ethernet(buf)
                except Exception:
                    continue
                if not isinstance(ether.data, dpkt.ip.IP):
                    continue
                ip = ether.data
                if not isinstance(ip.data, dpkt.tcp.TCP):
                    continue
                tcp = ip.data
                if tcp.dport == 80:
                    ip_src = socket.inet_ntoa(ip.src)
                    ip_dst = socket.inet_ntoa(ip.dst)
                    key = (ip_src, ip_dst)
                    packets[key] = packets.get(key, 0) + 1
    except Exception as e:
        raise RuntimeError('An error occurred while processing the pcap file.') from e

    result = {'{0}:{1}'.format(src, dst): count for (src, dst), count in packets.items()}
    return result


def iterative_prompting_4__findAttack(pcap):
    try:
        if not isinstance(pcap, str):
            return 0
        packets = rdpcap(pcap)
        connections = set()
        for packet in packets:
            if packet.haslayer('TCP') and packet['TCP'].dport == 80:
                ip_source = packet['IP'].src
                ip_destination = packet['IP'].dst
                connections.add(f'{ip_source}:{ip_destination}')
        return len(connections)
    except FileNotFoundError:
        return 0
    except Exception as e:
        return 0

def iterative_prompting_5__findAttack(pcap):
    if not isinstance(pcap, str):
        raise TypeError('pcap must be a string representing a file path')
    if not pcap.endswith('.pcap'):
        raise ValueError('Invalid pcap file extension')
    packets = {}
    try:
        with open(pcap, 'rb') as f:
            reader = dpkt.pcap.Reader(f)
            for ts, buf in reader:
                try:
                    e = dpkt.ethernet.Ethernet(buf)
                    if isinstance(e.data, dpkt.ip.IP):
                        ip = e.data
                        if isinstance(ip.data, dpkt.tcp.TCP):
                            tcp = ip.data
                            if tcp.dport == 80:
                                key = f'{socket.inet_ntoa(ip.src)}:{socket.inet_ntoa(ip.dst)}'
                                packets[key] = packets.get(key, 0) + 1
                except (dpkt.UnpackError, AttributeError):
                    continue
    except FileNotFoundError:
        raise FileNotFoundError('The specified pcap file does not exist')
    except PermissionError:
        raise PermissionError('Permission denied to read the pcap file')
    except Exception as e:
        raise RuntimeError(f'An unexpected error occurred: {str(e)}')
    return packets

def few_shots_prompting__findAttack(pcap):
	import dpkt
	import socket
	from collections import defaultdict
	count_dict = defaultdict(int)
	for ts, buf in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			tcp = ip.data
			if tcp.dport == 80:
				src = socket.inet_ntoa(ip.src)
				dst = socket.inet_ntoa(ip.dst)
				key = f'{src}:{dst}'
				count_dict[key] += 1
		except:
			pass
	return count_dict

def cot_prompting__findAttack(pcap):
	conn_dict = {}
	for (ts, buf) in pcap:
		try:
			hdr = dpkt.ethernet.Ethernet(buf)
			ip = hdr.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			tcp = ip.data
			dport = tcp.dport
			if dport == 80:
				key = f'{src}:{dst}'
				if key in conn_dict:
					conn_dict[key] += 1
				else:
					conn_dict[key] = 1
		except:
			pass
	return conn_dict

def fact_check_list__findAttack(pcap_filename):
    tcp_counts = {}
    try:
        packets = rdpcap(pcap_filename)
    except IOError as e:
        print(f'Error reading file {pcap_filename}: {e}')
        return {}
    for packet in packets:
        if packet.haslayer(IP) and packet.haslayer(TCP):
            ip_source = packet[IP].src
            ip_destination = packet[IP].dst
            tcp_destination_port = packet[TCP].dport
        if tcp_destination_port == 80:
            entry_key = f'{ip_source}:{ip_destination}'
            tcp_counts[entry_key] = tcp_counts.get(entry_key, 0) + 1
    return tcp_counts

def not_interactive_mix__findAttack(pcap):
    if not isinstance(pcap, str) or not pcap:
        raise ValueError("Invalid input type or empty pcap filename.")
    if not os.path.isfile(pcap):
        raise FileNotFoundError("The specified pcap file does not exist.")
    result_dict = {}
    try:
        cap = pyshark.FileCapture(pcap, display_filter='tcp.dstport == 80')
        for pkt in cap:
            if 'IP' in pkt:
                ip_src = pkt.ip.src
                ip_dst = pkt.ip.dst
                key = f"{ip_src}:{ip_dst}"
                if key in result_dict:
                    result_dict[key] += 1
                else:
                    result_dict[key] = 1
        cap.close()
    except Exception as e:
        raise RuntimeError(f"An error occurred while processing the pcap file: {str(e)}")
    return result_dict

def interactive_mix__count_tcp_packets_to_port_80(pcap):
    if not isinstance(pcap, str) or not pcap.endswith('.pcap'):
        raise ValueError('Invalid file name or format.')
    try:
        with open(pcap, 'rb') as f:
            pcap_content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'The file {pcap} does not exist.')
    except IOError:
        raise IOError(f'Cannot read the file {pcap}.')
    try:
        pc = dpkt.pcap.Reader(pcap_content)
    except dpkt.NeedData as e:
        raise IOError(f'Failed to read pcap content: {e}')
    tcp_packet_counts = {}
    for timestamp, buf in pc:
        eth = dpkt.ethernet.Ethernet(buf)
        if not isinstance(eth.data, dpkt.ip.IP):
            continue
        ip = eth.data
        if ip.p != dpkt.ip.IP_PROTO_TCP:
            continue
        tcp = ip.data
        if tcp.dport == 80:
            src_ip = socket.inet_ntoa(ip.src)
            dst_ip = socket.inet_ntoa(ip.dst)
            key = f'{src_ip}:{dst_ip}'
            tcp_packet_counts[key] = tcp_packet_counts.get(key, 0) + 1
    return tcp_packet_counts

def baseline__findAttack(pcap):
	from scapy.all import rdpcap
	packets = rdpcap(pcap)
	connections = set()
	for packet in packets:
		if packet.haslayer('TCP') and packet['TCP'].dport == 80:
			source_ip = packet['IP'].src
			destination_ip = packet['IP'].dst
			connections.add(f'{source_ip}:{destination_ip}')
	return len(connections)
