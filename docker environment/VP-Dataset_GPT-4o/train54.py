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
    packets = rdpcap(pcap)
    ip_addresses = []
    for packet in packets:
        if packet.haslayer('IP'):
            src = packet['IP'].src
            dst = packet['IP'].dst
            ip_addresses.append((src, dst))
    return ip_addresses

def template_ground_truth_code_printPcap(pcap):
    ip_addresses = []
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for _, buf in pcap_reader:
                eth = dpkt.ethernet.Ethernet(buf)
                if isinstance(eth.data, dpkt.ip.IP):
                    ip_packet = eth.data
                    src_ip = socket.inet_ntoa(ip_packet.src)
                    dst_ip = socket.inet_ntoa(ip_packet.dst)
                    ip_addresses.append((src_ip, dst_ip))
    except (IOError, dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError) as e:
        print(f"Error processing pcap file: {e}")
    return ip_addresses

def question_refinement_ground_truth_code_printPcap(pcap):
    ip_addresses = []
    try:
        if isinstance(pcap, bytes):
            with dpkt.pcap.Reader(io.BytesIO(pcap)) as pcap_reader:
                for timestamp, buf in pcap_reader:
                    try:
                        eth = dpkt.ethernet.Ethernet(buf)
                        if isinstance(eth.data, dpkt.ip.IP):
                            ip = eth.data
                            src_ip = dpkt.socket.inet_ntoa(ip.src)
                            dst_ip = dpkt.socket.inet_ntoa(ip.dst)
                            ip_addresses.append((src_ip, dst_ip))
                    except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError, ValueError):
                        continue
    except Exception as e:
        raise ValueError('Failed to process pcap data securely') from e
    return ip_addresses

def alternative_approaches_ground_truth_code_printPcap(pcap):
    try:
        packets = rdpcap(pcap)
        ip_addresses = [(pkt[IP].src, pkt[IP].dst) for pkt in packets if IP in pkt]
        return ip_addresses
    except FileNotFoundError:
        raise Exception('The provided pcap file was not found.')
    except Exception as e:
        raise Exception(f'An error occurred: {e}')

def context_manager_ground_truth_code_printPcap(pcap):
    results = []
    for timestamp, buf in dpkt.pcap.Reader(pcap):
        eth = dpkt.ethernet.Ethernet(buf)
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            src_ip = socket.inet_ntoa(ip.src)
            dst_ip = socket.inet_ntoa(ip.dst)
            results.append((src_ip, dst_ip))
    return results


def flipped_interaction_3_ground_truth_code_printPcap(pcap):
    ip_list = []
    try:
        packets = rdpcap(pcap)
        for packet in packets:
            if packet.haslayer(IP) or packet.haslayer(IPv6):
                src = packet[IP].src if packet.haslayer(IP) else packet[IPv6].src
                dst = packet[IP].dst if packet.haslayer(IP) else packet[IPv6].dst
                ip_list.append((src, dst))
    except Exception as e:
        print(f"An error occurred while processing the pcap file: {e}")
    return ip_list


def flipped_interaction_4_ground_truth_code_printPcap(pcap):
    ip_addresses = []
    with open(pcap, 'rb') as f:
        pcap_reader = dpkt.pcap.Reader(f)
        for timestamp, buf in pcap_reader:
            eth = dpkt.ethernet.Ethernet(buf)
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                src_ip = inet_to_str(ip.src)
                dst_ip = inet_to_str(ip.dst)
                ip_addresses.append((src_ip, dst_ip))
    return ip_addresses
def inet_to_str(inet):
    return '.'.join(map(str, inet))


def flipped_interaction_5_ground_truth_code_printPcap(pcap_file_path):
    packets = rdpcap(pcap_file_path)
    ip_addresses = []
    for packet in packets:
        if IP in packet:
            ip_layer = packet[IP]
            src_ip = ip_layer.src
            dst_ip = ip_layer.dst
            ip_addresses.append((src_ip, dst_ip))
        elif IPv6 in packet:
            ip_layer = packet[IPv6]
            src_ip = ip_layer.src
            dst_ip = ip_layer.dst
            ip_addresses.append((src_ip, dst_ip))
    return ip_addresses

def iterative_prompting_3_ground_truth_code_print_pcap(pcap):
    if not isinstance(pcap, str):
        raise ValueError('The pcap parameter must be a string representing the file path.')
    if not os.path.isfile(pcap):
        raise FileNotFoundError(f'The file {pcap} does not exist.')
    if not pcap.endswith('.pcap'):
        raise ValueError('The file does not seem to be a pcap file. Ensure the file extension is .pcap.')
    ip_list = []
    try:
        packets = rdpcap(pcap)
        for packet in packets:
            if IP in packet:
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                ip_list.append((src_ip, dst_ip))
    except Exception as e:
        raise RuntimeError(f'An error occurred while processing the pcap file: {str(e)}')
    return ip_list


def iterative_prompting_4_ground_truth_code_printPcap(pcap):
    if not isinstance(pcap, str):
        raise TypeError('pcap must be a string representing a file path')
    if not os.path.exists(pcap):
        raise FileNotFoundError(f'The file {pcap} does not exist')
    if not os.path.isfile(pcap):
        raise ValueError(f'The path {pcap} is not a file')
    try:
        packets = rdpcap(pcap)
    except Scapy_Exception as e:
        raise RuntimeError(f'Failed to read pcap file: {e}')
    ip_addresses = []
    for packet in packets:
        if packet.haslayer('IP'):
            src = packet['IP'].src
            dst = packet['IP'].dst
            ip_addresses.append((src, dst))
    return ip_addresses

def iterative_prompting_5_ground_truth_code_printPcap(pcap):
    if not isinstance(pcap, str):
        raise ValueError("Pcap path must be a string.")
    if not os.path.isfile(pcap):
        raise FileNotFoundError(f"Pcap file {pcap} does not exist.")
    results = []
    try:
        packets = rdpcap(pcap)
        for pkt in packets:
            if IP in pkt:
                results.append((pkt[IP].src, pkt[IP].dst))
    except Exception as e:
        print(f"Error reading pcap file: {e}")
    return results

    
def few_shots_prompting_ground_truth_code_printPcap(pcap):
    addresses = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if isinstance(ip, dpkt.ip.IP):
                src = socket.inet_ntoa(ip.src)
                dst = socket.inet_ntoa(ip.dst)
                addresses.append((src, dst))
        except Exception as e:
            pass
    return addresses

def cot_prompting_ground_truth_code_printPcap(pcap):
    ip_pairs = []
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            ip_pairs.append((src, dst))
        except Exception as e:
            pass
    return ip_pairs


def fact_check_list_ground_truth_code_printPcap(pcap_file):
    packets = rdpcap(pcap_file)
    ip_addresses = []
    for packet in packets:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            ip_addresses.append((src_ip, dst_ip))
    return ip_addresses

def not_interactive_mix_ground_truth_code_printPcap(pcap):
    src_dst_list = []
    try:
        packets = rdpcap(pcap)
        for packet in packets:
            if IP in packet:
                src = packet[IP].src
                dst = packet[IP].dst
                src_dst_list.append((src, dst))
    except (IOError, OSError) as error:
        print(f'Failed to read pcap file: {error}')
    except Exception as ex:
        print(f'An error occurred: {ex}')
    return src_dst_list

def interactive_mix_extract_ip_addresses_from_pcap(pcap_file):
    ip_addresses = []
    try:
        with open(pcap_file, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                    if isinstance(eth.data, dpkt.ip.IP):
                        ip = eth.data
                        src = socket.inet_ntoa(ip.src)
                        dst = socket.inet_ntoa(ip.dst)
                        ip_addresses.append((src, dst))
                except (dpkt.UnpackError, dpkt.NeedData) as e:
                    continue
                except Exception as e:
                    continue
    except IOError as e:
        print(f"Error reading pcap file: {e}")
    return ip_addresses

def baseline_ground_truth_code_printPcap(pcap):
    packets = rdpcap(pcap)
    ip_pairs = []
    for packet in packets:
        if packet.haslayer('IP'):
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            ip_pairs.append((src_ip, dst_ip))
    return ip_pairs

