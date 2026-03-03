import socket
import dpkt
from typing import Tuple

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
    packets = rdpcap(pcap)
    entry_set = set()
    for packet in packets:
        if TCP in packet and packet[TCP].dport == 80:
            ip_src = packet[1].src
            ip_dst = packet[1].dst
            entry = f'{ip_src}:{ip_dst}'
            entry_set.add(entry)
    return len(entry_set)

def template_findAttack(pcap):
    try:
        packets = rdpcap(pcap)
        tcp_port_80_count = 0
        entries = set()
        for packet in packets:
            if packet.haslayer(TCP) and packet[TCP].dport == 80:
                entry = f"{packet[1].src}:{packet[1].dst}"
                entries.add(entry)
        return len(entries)
    except FileNotFoundError:
        print('File not found. Please check the file path.')
        return 0
    except Exception as e:
        print(f'An error occurred: {e}')
        return 0

def question_refinement_analyze_pcap_tcp_port_80(pcap_file_path: str) -> Tuple[int, int]:
    tcp_port_80_count = 0
    unique_ip_pairs = set()
    try:
        with open(pcap_file_path, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_reader:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                if not isinstance(ip.data, dpkt.tcp.TCP):
                    continue
                tcp = ip.data
                if tcp.dport == 80:
                    tcp_port_80_count += 1
                src_ip = socket.inet_ntoa(ip.src)
                dst_ip = socket.inet_ntoa(ip.dst)
                unique_ip_pairs.add(f"{src_ip}:{dst_ip}")
    except (FileNotFoundError, ValueError, dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError) as e:
        print(f"An error occurred while processing the pcap file: {e}")
        return 0, 0
    return tcp_port_80_count, len(unique_ip_pairs)

def alternative_approaches_findAttack(pcap):
    import dpkt
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            connections = set()
            for timestamp, buf in pcap_reader:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                if isinstance(ip.data, dpkt.tcp.TCP):
                    tcp = ip.data
                    if tcp.dport == 80:
                        connections.add(f"{ip.src}:{ip.dst}")
            return len(connections)
    except (IOError, dpkt.UnpackError) as e:
        return f"An error occurred: {e}"

def context_manager_findAttack(pcap):
    from scapy.all import rdpcap, TCP
    connections = set()
    packets = rdpcap(pcap)
    for pkt in packets:
        if TCP in pkt and pkt[TCP].dport == 80:
            ip_src = pkt[0].src
            ip_dst = pkt[0].dst
            connections.add(f"{ip_src}:{ip_dst}")
    return len(connections)

import pyshark
def flipped_interaction_3_findAttack(pcap):
    cap = pyshark.FileCapture(pcap, display_filter="tcp.dstport == 80")
    unique_pairs = set()
    for packet in cap:
        try:
            ip_src = packet.ip.src
            ip_dst = packet.ip.dst
            pair = f"{ip_src}:{ip_dst}"
            unique_pairs.add(pair)
        except AttributeError:
            continue
    return len(unique_pairs)

from scapy.all import rdpcap, TCP
def flipped_interaction_4_findAttack(pcap):
    try:
        packets = rdpcap(pcap)
    except Exception as e:
        print(f"Failed to read pcap file: {e}")
        return []
    ip_entries = []
    error_count = 0
    for packet in packets:
        try:
            if packet.haslayer(TCP) and packet[TCP].dport == 80:
                ip_src = packet[0][1].src
                ip_dst = packet[0][1].dst
                ip_entries.append(f"{ip_src}:{ip_dst}")
        except Exception as error:
            error_count += 1
            print(f"Error processing packet: {error}")
    if error_count > 0:
        print(f"Total errors encountered: {error_count}")
    return ip_entries

from scapy.all import rdpcap, TCP
def flipped_interaction_5_findAttack(pcap):
    packets = rdpcap(pcap)
    ip_pairs = set()
    for pkt in packets:
        if TCP in pkt and pkt[TCP].dport == 80:
            ip_source = pkt[1].src
            ip_destination = pkt[1].dst
            ip_pairs.add(f"{ip_source}:{ip_destination}")
    return len(ip_pairs)

def iterative_prompting_3_find_attack(pcap):
    import os
    import dpkt
    try:
        import pip
        from subprocess import call
        call([pip.main, 'install', '--upgrade', 'dpkt'])
    except Exception as e:
        print(f"Could not check for updates to dpkt library: {e}")
    if not os.path.isfile(pcap):
        raise ValueError("The specified pcap file does not exist or is not a valid file.")
    ip_pairs = set()
    try:
        with open(pcap, 'rb') as f:
            pcap_data = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_data:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                except dpkt.UnpackError:
                    continue
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                if not isinstance(ip.data, dpkt.tcp.TCP):
                    continue
                tcp = ip.data
                if tcp.dport == 80:
                    ip_src = ".".join(map(str, ip.src))
                    ip_dst = ".".join(map(str, ip.dst))
                    ip_pair = f'{ip_src}:{ip_dst}'
                    ip_pairs.add(ip_pair)
    except (OSError, dpkt.dpkt.Error) as e:
        raise RuntimeError(f"An error occurred while processing the pcap file: {e}")
    return len(ip_pairs)

def iterative_prompting_4_find_attack(pcap):
    import os
    from scapy.all import rdpcap, Scapy_Exception
    if not isinstance(pcap, str):
        raise TypeError('The pcap argument must be a string representing the file path.')
    if not os.path.isfile(pcap):
        raise FileNotFoundError(f'File not found: {pcap}')
    try:
        packets = rdpcap(pcap)
    except Scapy_Exception as e:
        raise ValueError(f'Failed to read pcap file: {e}')
    except Exception as e:
        raise RuntimeError(f'An unexpected error occurred: {e}')
    ip_pairs = set()
    for pkt in packets:
        try:
            if pkt.haslayer('TCP'):
                tcp_layer = pkt.getlayer('TCP')
                if tcp_layer.dport == 80:
                    if pkt.haslayer('IP'):
                        ip_layer = pkt.getlayer('IP')
                        ip_pairs.add((ip_layer.src, ip_layer.dst))
        except AttributeError:
            continue
    return len(ip_pairs)

def iterative_prompting_5_find_attack(pcap):
    import os
    from scapy.all import rdpcap, IP, TCP
    if not os.path.isfile(pcap):
        raise FileNotFoundError(f"The file {pcap} does not exist.")
    if not pcap.endswith('.pcap'):
        raise ValueError("Invalid file format. Expected a .pcap file.")
    ip_pairs = set()
    try:
        packets = rdpcap(pcap)
    except Exception as e:
        raise Exception(f"An error occurred while reading the pcap file: {str(e)}")
    for packet in packets:
        if IP in packet and TCP in packet:
            if packet[TCP].dport == 80:
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                ip_pairs.add(f'{src_ip}:{dst_ip}')
    return len(ip_pairs)

def few_shots_prompting_findAttack(pcap):
    import dpkt
    import socket
    seen_pairs = set()
    count = 0
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data
            if isinstance(ip, dpkt.ip.IP) and isinstance(tcp, dpkt.tcp.TCP):
                if tcp.dport == 80:
                    ipsrc = socket.inet_ntoa(ip.src)
                    ipdst = socket.inet_ntoa(ip.dst)
                    pair = f'{ipsrc}:{ipdst}'
                    if pair not in seen_pairs:
                        seen_pairs.add(pair)
                        count += 1
        except Exception as e:
            continue
    return count

def cot_prompting_findAttack(pcap):
    unique_pairs = set()
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            ip = eth.data
            if not isinstance(ip.data, dpkt.tcp.TCP):
                continue
            tcp = ip.data
            if tcp.dport == 80:
                src = socket.inet_ntoa(ip.src)
                dst = socket.inet_ntoa(ip.dst)
                unique_pairs.add(f'{src}:{dst}')
        except Exception as e:
            pass
    return len(unique_pairs)

from scapy.all import rdpcap
def fact_check_list_findAttack(pcap):
    try:
        packets = rdpcap(pcap)
    except FileNotFoundError:
        print('PCAP file not found.')
        return 0
    except Exception as e:
        print(f'An error occurred: {e}')
        return 0
    tcp_port_80_entries = set()
    for pkt in packets:
        if pkt.haslayer('IP') and pkt.haslayer('TCP'):
            ip_layer = pkt.getlayer('IP')
            tcp_layer = pkt.getlayer('TCP')
            if tcp_layer.dport == 80:
                ip_src = ip_layer.src
                ip_dst = ip_layer.dst
                tcp_port_80_entries.add(f"{ip_src}:{ip_dst}")
    return len(tcp_port_80_entries)

def not_interactive_mix_findAttack(pcap):
    from scapy.all import rdpcap, TCP, IP
    from collections import defaultdict
    try:
        packets = rdpcap(pcap)
    except Exception as e:
        raise ValueError('Error reading pcap file: {}'.format(e))
    ip_pairs = defaultdict(int)
    for pkt in packets:
        if TCP in pkt and pkt[IP].dport == 80:
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst
            ip_pairs[f'{src_ip}:{dst_ip}'] += 1
    return len(ip_pairs)

def interactive_mix_count_tcp_packets_with_dst_port_80(pcap_file_path):
    import pyshark
    from collections import defaultdict
    ip_pair_count = defaultdict(int)
    try:
        capture = pyshark.FileCapture(pcap_file_path, display_filter='tcp.dstport == 80')
        for packet in capture:
            try:
                if hasattr(packet, 'ip'):
                    ip_src = packet.ip.src
                    ip_dst = packet.ip.dst
                    pair = f"{ip_src}:{ip_dst}"
                    ip_pair_count[pair] += 1
            except AttributeError:
                continue
        capture.close()
        result = {pair: count for pair, count in ip_pair_count.items()}
        return result
    except pyshark.capture.capture.TSharkCrashException as e:
        print(f"An error due to TShark occurred: {e}")
    except pyshark.capture.capture.TSharkNotFoundException as e:
        print(f"TShark executable not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def baseline_findAttack(pcap):
    packets = rdpcap(pcap)
    connections = set()
    for pkt in packets:
        if pkt.haslayer(TCP) and pkt[TCP].dport == 80:
            ip_src = pkt[0][1].src
            ip_dst = pkt[0][1].dst
            connections.add(f'{ip_src}:{ip_dst}')
    return len(connections)

