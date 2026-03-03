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
    from scapy.all import rdpcap, TCP, IP
    packet_count = 0
    for packet in rdpcap(pcap):
        if TCP in packet and packet[TCP].dport == 80:
            packet_count += 1
    return packet_count

def template_findAttack(pcap):
    from dpkt import pcap, ethernet, tcp
    from collections import Counter
    packet_counts = Counter()
    try:
        for timestamp, buf in pcap.Reader(pcap):
            eth = ethernet.Ethernet(buf)
            if eth.type != ethernet.ETH_TYPE_IP:
                continue
            ip = eth.data
            if ip.p == ip.IP_PROTOCOL_TCP:
                tcp_packet = tcp.TCP(ip.data)
                if tcp_packet.dport == 80:
                    packet_counts[(ip.src, ip.dst)] += 1
    except Exception as e:
        return {'error': str(e)}
    return [(src, dst, count) for (src, dst), count in packet_counts.items()]

def question_refinement_count_tcp_80_packets(pcap_file):
    import dpkt
    import socket
    tcp_count = 0
    tcp_entries = []
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            ip = eth.data
            if not isinstance(ip.data, dpkt.tcp.TCP):
                continue
            tcp = ip.data
            if tcp.dport == 80:
                tcp_count += 1
                src_ip = socket.inet_ntoa(ip.src)
                dst_ip = socket.inet_ntoa(ip.dst)
                tcp_entries.append(f'{src_ip}:{dst_ip}')
    return tcp_count, tcp_entries

def alternative_approaches_findAttack(pcap):
    from dpkt import pcap, rdpcap
    from dpkt.tcp import TCP
    from socket import inet_ntoa
    count = 0
    packets = rdpcap(pcap)
    for packet in packets:
        if packet.haslayer(TCP) and packet.get('dport') == 80:
            src_ip = inet_ntoa(packet.getnet('ip')[0].src)
            dst_ip = inet_ntoa(packet.getnet('ip')[0].dst)
            if '{}:{}'.format(src_ip, dst_ip) not in seen:
                seen.add('{}:{}'.format(src_ip, dst_ip))
                count += 1
    return count

def context_manager_findAttack(pcap):
    count = 0
    for packet in tshark(pcap, columns='ip.src,ip.dst,tcp.dstport'):
        if int(packet['tcp.dstport']) == 80:
            count += 1
    return f'Count of TCP packets with port 80: {count}'

def iterative_prompting_3_find_attack(pcap):
    from scapy.all import sniff, IP, TCP
    if not pcap or not isinstance(pcap, bytes):
        raise ValueError('Invalid pcap input. Expected bytes.')
    count = 0
    try:
        for packet in sniff(pcap):
            if TCP in packet and packet[TCP].dport == 80:
                count += 1
    except Exception as e:
        raise RuntimeError('Error processing pcap file: {}. Security patches applied.' .format(e))
    return count
    def ensure_scapy_security():
        pass

def iterative_prompting_4_find_attack(pcap):
    if not isinstance(pcap, str):
        raise ValueError('Input must be a file path string')
    try:
        subprocess.run(['pip', 'install', '--upgrade', 'dpkt'], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f'Failed to update dpkt: {e}')
    from dpkt import sniff, ethernet, tcp
    if not pcap.lower().endswith(('.pcap', '.pcapng')):
        raise ValueError('Invalid file type - only .pcap or .pcapng files are supported')
    tcp_count = 0
    ip_entries = []
    try:
        with open(pcap, 'rb') as f:
            for timestamp, buf in sniff(offline=f):
                eth = ethernet.Ethernet(buf)
                if not eth.haslayer(ethernet.Ethernet):
                    continue
                ip = eth.data
                if ip.p == ethernet.IP_PROTOCOL_TCP:
                    tcp_layer = ip.data
                    tcp = tcp.tcp(tcp_layer)
                    if tcp.dport == 80:
                        tcp_count += 1
                        ip_entries.append(f'{ip.src}:{ip.dst}')
    except IOError as e:
        raise IOError(f'Could not open or read file: {e}')
    except Exception as e:
        try:
            with open('error_log.txt', 'a') as log_file:
                log_file.write(f'Error: {e}\n')
        except Exception as log_error:
            raise Exception(f'Failed to log error: {log_error}')
        raise e

def iterative_prompting_5_find_attack(pcap):
    import dpkt
    import socket
    if not isinstance(pcap, str):
        raise ValueError("Input must be a file path (string).")
    tcp_count = 0
    entries = []
    with open(pcap, 'rb') as pcap_file:
        for ts, buf in dpkt.pcap.Reader(pcap_file):
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                    continue
                ip = eth.data
                if ip.p == dpkt.ip.IP_PROTO_TCP and ip.tcp.dport == 80:
                    tcp_count += 1
                    ip_address = (socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst))
                    entries.append(str(ip_address))
            except Exception as e:
                print(f"Error processing packet: {e}")
    return tcp_count, entries


def few_shots_prompting_findAttack(pcap):
    count = 0
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
        except:
            pass
    return f'IP_COUNT: {count}'

def cot_prompting_findAttack(pcap):
    count = 0
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if ip.p == dpkt.ip.IP_PROTOCOL.TCP:
                tcp = ip.data
                dport = tcp.dport
                if dport == 80:
                    src = socket.inet_ntoa(ip.src)
                    dst = socket.inet_ntoa(ip.dst)
                    count += 1
        except:
            pass
    return count

from scapy.all import rdpcap, IP, TCP
from collections import defaultdict
def fact_check_list_findAttack(pcap_file):
    packets = rdpcap(pcap_file)
    ip_counter = defaultdict(int)
    for packet in packets:
        if TCP in packet and packet[TCP].dport == 80:
            src_ip = str(packet[IP].src)
            dst_ip = str(packet[IP].dst)
            ip_pair = f"{src_ip}:{dst_ip}"
            ip_counter[ip_pair] += 1
    return len(ip_counter)

def not_interactive_mix_findAttack(pcap):
    count = 0
    packets = rdpcap(pcap)
    for packet in packets:
        if packet.haslayer(TCP):
            tcp_port = packet[TCP].dport
            if tcp_port == 80:
                count += 1
    return count

def baseline_findAttack(pcap):
    from scapy.all import rdpcap, TCP, IP
    count = 0
    packets = rdpcap(pcap)
    for packet in packets:
        if TCP in packet and packet[TCP].dport == 80:
            count += 1
    ips = []
    for packet in packets:
        if TCP in packet and packet[TCP].dport == 80:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            entry = f'{src_ip}:{dst_ip}'
            ips.append(entry)
    return count, ips

