import socket
import dpkt
from scapy.all import *
import os
import pyshark

def ground_truth_code_findHivemind(pcap):
    results = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            sport = tcp.sport
            if dport == 6667 or sport == 6667:
                if isinstance(tcp.data, bytes):
                    tcp_data = tcp.data.decode('utf-8', errors='ignore')
                else:
                    tcp_data = tcp.data
                if '!lazor' in tcp_data.lower():
                    results.append((src, dst, ts, tcp_data.strip()))
        except Exception as e:
            pass
    return results

import pyshark
def persona_findHivemind(pcap):
    reader = pyshark.FileCapture(pcap)
    for packet in reader:
        for upperfield in ['ip', 'tcp']:
            for upperfield_element in packet.get_field_by_name(upperfield):
                for lower_field in ['data']:
                    if lower_field in packet[upperfield].fields:
                        data = packet[upperfield][lower_field]
                        if '!' + 'lazor' in data:
                            return True
    return False

def template_findHivemind(pcap):
    try:
        import dpkt
        import socket
        packet_list = dpkt.pcap.Reader(open(pcap, 'rb'))
        for timestamp, buf in packet_list:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            ip = eth.data
            if ip.p != dpkt.ip.IP_PROTOCOL_TCP:
                continue
            tcp = ip.data
            src_port = tcp.sport
            dst_port = tcp.dport
            if (src_port == 6667 or dst_port == 6667):
                tcp_data = tcp.data
                if isinstance(tcp_data, dpkt.tcp.TCP):
                    tcp_packet = tcp_data.data
                    if '!lazor' in tcp_packet:
                        return True
        return False
    except Exception as e:
        print(f'Error: {e}')
        return False

import json, scapy
from scapy.utils import PcapReader
def question_refinement_find_packets_with_string(pcap_file, string, src_port=6667, dst_port=6667):
    result_packets = []
    with PcapReader(pcap_file) as packets:
        for packet in packets:
            if packet.haslayer(TCP):
                src = packet[TCP].src
                dst = packet[TCP].dst
                if (src == src_port or dst == dst_port) and string in packet[TCP].payload.decode():
                    result_packets.append({
                        'packet': ''.join(str(packet)[:-2]),
                        'src_port': src,
                        'dst_port': dst
                    })
    return json.dumps(result_packets, indent=4)

def alternative_approaches_findHivemind(pcap):
    from scapy.all import rdpcap, TCP, Raw
    packets = rdpcap(pcap)
    host_peers = {6667}
    for packet in packets:
        if TCP in packet and packet[TCP].sport in host_peers or TCP in packet and packet[TCP].dport in host_peers:
            try:
                data = Raw(load=packet[TCP].load).payload.decode()
                if '!lazor' in data.lower():
                    return True
            except UnicodeDecodeError:
                continue
    return False

def context_manager_findHivemind(pcap):
    import dpkt
    import binascii
    for ts, pack in pcap.iterpackets():
        try:
            eth = dpkt.ethernet.Ethernet(pack)
            ip = eth.data
            tcp = ip.data
            data = binascii.hexlify(tcp.data)
            if '6667' in data and '!lazor' in data.lower():
                return True
        except Exception as e:
            pass

def iterative_prompting_3_find_hivemind(pcap):
    if not hasattr(pcap, 'iter_packets') or not callable(getattr(pcap, 'iter_packets')):
        raise ValueError('Invalid input: pcap must have an iter_packets method.')
    import dpkt
    import socket
    from dpkt.tcp import TCP
    try:
        for timestamp, buf in pcap.iter_packets():
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            ip = eth.data
            if ip.p != socket.IPPROTO_TCP:
                continue
            tcp = tcp = ip.data
            if isinstance(tcp, TCP) and (tcp.dport == 6667 or tcp.sport == 6667):
                data = str(tcp.data)
                if '!lazor' in data.lower():
                    return True
        return False
    except ImportError as e:
        print(f'ImportError: {e}')
        raise
    except Exception as e:
        print(f'An error occurred: {e}')
        raise

import pyshark
def iterative_prompting_4_find_hivemind(pcap):
    if not isinstance(pcap, str) or not pcap:
        raise ValueError('Invalid pcap file path provided. It must be a non-empty string.')
    try:
        capture = pyshark.FileCapture(pcap)
    except Exception as e:
        raise IOError(f'Error opening pcap file: {str(e)}')
    if not hasattr(capture, '__iter__'):
        raise TypeError('Invalid capture object. Expected an iterable object.')
    for packet in capture:
        if 'tcp' in packet:
            try:
                src_port = packet['tcp'].srcport
                dst_port = packet['tcp'].dstport
                src_port_int = int(src_port)
                dst_port_int = int(dst_port)
                if src_port_int == 6667 or dst_port_int == 6667:
                    tcp_payload = packet['tcp'].load
                    if '!lazor' in tcp_payload.lower():
                        return True
            except ValueError as ve:
                raise ValueError(f'Invalid port data encountered: {str(ve)}')
    return False

def iterative_prompting_5_find_hivemind(pcap):
    import pyshark
    import datetime
    results = []
    if not isinstance(pcap, str):
        raise ValueError('Invalid input: pcap must be a file path string.')
    try:
        cap = pyshark.FileCapture(pcap)
    except Exception as e:
        raise RuntimeError(f'Failed to load pcap file: {e}')
    for packet in cap:
        if packet.high_level_protocol_type == 'tcp':
            try:
                src_port = int(packet.src)
                dst_port = int(packet.dst)
            except ValueError:
                continue
            if src_port == 6667 or dst_port == 6667:
                data = packet.tcp.data.decode()
                if '!lazor' in data.lower():
                    timestamp = datetime.datetime.now()
                    print(f'Found at {timestamp}')
                    results.append((src, dst, ts, tcp_data.strip()))
    return results

def few_shots_prompting_findHivemind(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            sport = tcp.sport
            if dport == 6667:
                if '!lazor' in tcp.data.lower():
                    pass
            if sport == 6667:
                if '!lazor' in tcp.data.lower():
                    pass
        except:
            pass

def cot_prompting_findHivemind(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            sport = tcp.sport
            if dport == 6667 or sport == 6667:
                if '!lazor' in tcp.data.lower():
                    pass
        except:
            pass

import pyshark
def fact_check_list_findHivemind(pcap_file):
    cap = pyshark.FileCapture(pcap_file)
    hivemind_occurrences = []
    for packet in cap:
        try:
            ip_layer = packet.ip
            tcp_layer = ip_layer.tcp
            if (tcp_layer.srcport == 6667 or tcp_layer.dstport == 6667):
                tcp_data = tcp_layer.tcp_payload.lower()
                if '!lazor' in tcp_data:
                    hivemind_occurrences.append((packet, tcp_layer))
        except AttributeError:
            pass
    cap.free()
    return hivemind_occurrences


def not_interactive_mix_findHivemind(pcap_file):
    packets = rdpcap(pcap_file)
    found_lazor = False
    for packet in packets:
        try:
            if TCP in packet and (packet[TCP].dport == 6667 or packet[TCP].sport == 6667):
                payload_str = str(packet[TCP].payload)
                if '!lazor' in payload_str:
                    found_lazor = True
                    print(f"'!lazor' found in packet with payload: {payload_str}")
        except Exception as e:
            print(f"Error processing packet: {e}")
    return found_lazor

def baseline_findHivemind(pcap):
    for packet in pyshark.FileCapture(pcap):
        if 'tcp.srcport' in packet.fields or 'tcp.dstport' in packet.fields:
            src_port = packet.fields['tcp.srcport'].split('/')[0] if 'tcp.srcport' in packet.fields else '0'
            dst_port = packet.fields['tcp.dstport'].split('/')[0] if 'tcp.dstport' in packet.fields else '0'
            if src_port == '6667' or dst_port == '6667':
                if 'DATA' in packet and '!lazor' in packet.data:
                    return True
    return False

