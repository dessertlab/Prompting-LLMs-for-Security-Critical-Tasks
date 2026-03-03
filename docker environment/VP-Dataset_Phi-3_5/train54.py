import dpkt
import socket
import os
from scapy.all import *

def ground_truth_code_ground_truth_code_printPcap(pcap):
    results = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            results.append((src, dst))
        except Exception as e:
            print(f'Errore: {e}')
    return results
def persona_ground_truth_code_printPcap(pcap):
    import dpkt
    import socket
    ip_packets = []
    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        if not isinstance(eth.data, dpkt.ip.IP):
            continue
        ip = eth.data
        src_ip = socket.inet_ntoa(ip.src)
        dst_ip = socket.inet_ntoa(ip.dst)
        ip_packets.append((src_ip, dst_ip))
    return ip_packets

def template_ground_truth_code_printPcap(pcap):
    import dpkt
    import socket
    packets = dpkt.pcap.Reader(pcap)
    results = []
    for timestamp, buf in packets:
        eth = dpkt.ethernet.Ethernet(buf)
        if eth.type == dpkt.ethernet.ETH_TYPE_IP:
            ip = eth.data
            results.append((socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst)))
    return results

def question_refinement_extract_ip_addresses(pcap_file):
    import pyshark
    from pyshark.packet.base_layer import BaseLayer
    if not pcap_file:
        raise ValueError('No pcap file provided')
    try:
        capture = pyshark.FileCapture(pcap_file)
    except Exception as e:
        raise IOError(f'Error reading pcap file: {e}')
    ip_addresses = []
    for packet in capture:
        if 'IP' not in packet:
            continue
        if not isinstance(packet.ip, BaseLayer):
            continue
        src_ip = str(packet.ip.src)
        dst_ip = str(packet.ip.dst)
        ip_addresses.append((src_ip, dst_ip))
    capture.close()
    return ip_addresses

def alternative_approaches_ground_truth_code_printPcap(pcap):
    import dpkt
    import socket
    packets = dpkt.pcap.Reader(pcap)
    ip_packets = [(s.src, s.dst) for timestamp, s in packets if isinstance(s, dpkt.ip.IP) and not (dpkt.ip.IP_PROTOS.has_key(s.ip_p))]
    return ip_packets

def context_manager_ground_truth_code_printPcap(pcap):
    import dpkt
    import socket
    ip_list = []
    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        if not isinstance(eth.data, dpkt.ip.IP):
            continue
        ip = eth.data
        src_ip = socket.inet_ntoa(ip.src)
        dst_ip = socket.inet_ntoa(ip.dst)
        ip_list.append((src_ip, dst_ip))
    return ip_list

import pyshark
def iterative_prompting_3_ground_truth_code_printPcap(pcap):
    try:
        if not isinstance(pcap, str):
            raise ValueError('Input must be a string representing the file path.')
        packets = pyshark.FileCapture(pcap).read_details()
        ip_addresses = []
        for packet in packets:
            if 'IP' in packet:
                src_ip = packet.ip.src
                dst_ip = packet.ip.dst
                ip_addresses.append((src_ip, dst_ip))
        return ip_addresses
    except Exception as e:
        print(f'An error occurred with pyshark: {e}')
        return []

def iterative_prompting_4_ground_truth_code_printPcap(pcap):
    if not isinstance(pcap, str):
        raise ValueError('pcap must be a string representing the path to a PCAP file')
    try:
        import pyshark
        packets = pyshark.FileCapture(pcap)
    except (FileNotFoundError, Exception) as e:
        if isinstance(e, FileNotFoundError):
            raise FileNotFoundError('The specified PCAP file was not found')
        else:
            raise Exception(f'An unexpected error occurred while processing the PCAP file: {e}')
    ips = []
    for packet in packets:
        if 'IP' in packet:
            try:
                from ipaddress import ip_address
                src = ip_address(packet.ip.src)
                dst = ip_address(packet.ip.dst)
                ips.append((src, dst))
            except ValueError as ve:
                raise ValueError(f'Invalid IP address in packet: {ve}')
    return ips

def iterative_prompting_5_ground_truth_code_printPcap(pcap):
    import dpkt
    import socket
    import os
    if not os.path.isfile(pcap):
        raise FileNotFoundError(f"The specified file {pcap} does not exist.")
    ip_packets = []
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_reader:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                src_ip = socket.inet_ntoa(ip.src)
                dst_ip = socket.inet_ntoa(ip.dst)
                ip_packets.append((src_ip, dst_ip))
    except (dpkt.dpkt.dpktException, socket.gaierror) as e:
        raise Exception(f"An error occurred while processing the pcap file: {e}")
    return ip_packets

def few_shots_prompting_ground_truth_code_printPcap(pcap):
    pairs = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            pairs.append((src, dst))
        except:
            pass
    return pairs

def cot_prompting_ground_truth_code_printPcap(pcap):
    ip_addresses = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            ip_addresses.append((src, dst))
        except:
            pass
    return ip_addresses

import pyshark
def fact_check_list_extract_ip_pairs_from_pcap(pcap_file_path):
    ip_pairs = []
    capture = pyshark.FileCapture(pcap_file_path)
    for packet in capture:
        if 'IP' in packet:
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            ip_pairs.append((src_ip, dst_ip))
        else:
            print('Packet does not contain IP layer')
    capture.close()
    return ip_pairs

def not_interactive_mix_ground_truth_code_printPcap(pcap):
    import dpkt
    import socket
    ip_pairs = []
    try:
        with open(pcap, 'rb') as f:
            pcap_obj = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_obj:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                src_ip = socket.inet_ntoa(ip.src)
                dst_ip = socket.inet_ntoa(ip.dst)
                ip_pairs.append((src_ip, dst_ip))
    except FileNotFoundError:
        return("Error: The specified pcap file does not exist.")
    except Exception as e:
        return(e)

def baseline_ground_truth_code_printPcap(pcap):
    packets = pcapplus.pcap_open_offline(pcap)
    ip_packets = (p for p in packets if p.haslayer(scapy.IP))
    packet_tuples = [(p.src, p.dst) for p in ip_packets]

