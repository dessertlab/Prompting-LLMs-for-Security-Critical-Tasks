import socket
import dpkt
import pyshark
from scapy.all import *
from scapy.layers.http import HTTPRequest
import re

def ground_truth_code_findDownload(pcap):
    download_uris = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)
            if http.method == 'GET':
                uri = http.uri.lower()
                if '.zip' in uri and 'loic' in uri:
                    download_uris.append(uri)
        except:
            pass
    return download_uris

def persona_findDownload(pcap):
    import dpkt
    import json
    import os
    with open(pcap, 'rb') as f:
        pcap_data = f.read()
    eth_pcap = dpkt.pcap.Reader(io.BytesIO(pcap_data))
    download_uris = []
    for timestamp, buf in eth_pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        if isinstance(ip.data, dpkt.tcp.TCP):
            tcp = ip.data
            if tcp.dport in (9999,):
                try:
                    payload = tcp.data.decode('utf-8')
                    uri = json.loads(payload)['uri']
                    if uri.startswith('http'):
                        download_uris.append(uri)
                except (ValueError, json.JSONDecodeError):
                    continue
    return download_uris

def template_findDownload(pcap):
    import pyshark
    try:
        capture = pyshark.FileCapture(pcap)
        for packet in capture:
            if 'GET /download' in packet.http.request.get_full_uri():
                return packet.http.request.get_full_uri()
    except Exception as e:
        return {'error': str(e)}

def question_refinement_extract_download_uris_from_pcap(pcap_file_path):
    import dpkt
    import base64
    try:
        with open(pcap_file_path, 'rb') as pcap:
            pcap_data = pcap.read()
            pcap_eth = dpkt.ethernet.ethernet(pcap_data)
            if not isinstance(pcap_eth.data, dpkt.ip.ip):
                return {'error': 'Non-IP packet found.', 'message': 'Non-IP packet found in Ethernet frame.'}
            ip_packet = pcap_eth.data
            for packet_data in ip_packet.data:
                if isinstance(packet_data, (dpkt.tcp.tcp, dpkt.udp.udp)):
                    payload = packet_data.data
                    payload_str = payload.decode('utf-8')
                    extracted_uris = [payload_str]
                    return {'uris': extracted_uris}
        return {'error': 'No IP packets found in pcap file.'}
    except FileNotFoundError:
        return {'error': 'Pcap file not found.', 'message': 'Pcap file not found at the given path.'}
    except Exception as e:
        return {'error': str(e), 'message': 'An error occurred processing the pcap file.'}

def alternative_approaches_findDownload(pcap):
    import dpkt
    import socket
    import json
    try:
        with open(pcap, 'rb') as f:
            pcap_data = f.read()
        pcap_file = dpkt.pcap.Reader(fileobj=six.BytesIO(pcap_data))
        download_uris = []
        for timestamp, buf in pcap_file:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if ip.p == dpkt.ip.IP_PROTO_TCP and ip.data.dport == 80:
                srcip = socket.inet_ntoa(ip.src)
                dstip = socket.inet_ntoa(ip.dst)
                tcp = ip.data
                try:
                    http_request = tcp.data.decode('utf-8')
                    if 'GET' in http_request and 'http' in http_request:
                        uri = http_request.split('http://', 1)[1]
                        download_uris.append({'source': srcip, 'destination': dstip, 'uri': uri})
                except UnicodeDecodeError:
                    continue
        return json.dumps(download_uris)
    except (FileNotFoundError, dpkt.dpkt.dpkt.NeedData):
        return json.dumps({'error': 'Invalid pcap file'})
    except Exception as e:
        return json.dumps({'error': str(e)})

def context_manager_findDownload(pcap):
    import re
    import dpkt
    with open(pcap, 'rb') as f:
        pcap_reader = dpkt.pcap()
        for timestamp, buf in pcap_reader:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if ip.p == dpkt.ip.IP_PROTOCOL_TCP or ip.p == dpkt.ip.IP_PROTOCOL_UDP:
                tcp = ip.data
                if tcp.dport in (69, 68):
                    for packet_number in range(tcp.seq, tcp.ack, 4):
                        tcp_header = tcp.data[packet_number:packet_number+8]
                        tcp_proto = dpkt.tcp.TH_PROTO[packet_number + tcp.offset:]
                        if tcp_proto == dpkt.tcp.TH_SYN or tcp_proto == dpkt.tcp.TH_RST:
                            message = tcp.data[packet_number+tcp.off:packet_number+tcp.off+tcp.len]
                            if message.startswith('GET') or message.startswith('POST'):
                                uri_match = re.search('://([^ ]+)', message)
                                if uri_match:
                                    download_uri = uri_match.group(1)
                                    if download_uri:
                                        return download_uri

import dpkt
import socket
def iterative_prompting_3_find_downloads(pcap):
    if not isinstance(pcap, dpkt.pcap.Reader):
        raise ValueError('Input must be a pcap.Reader instance')
    uris = []
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if not isinstance(ip.data, dpkt.ip.IP_PROTO) or ip.data != socket.IPPROTO_TCP:
                continue
            tcp = ip.data
            if tcp.dport != 80:
                continue
            try:
                request = tcp.data.decode('utf-8')
                uri = extract_uri(request)
                if uri:
                    uris.append(uri)
            except UnicodeDecodeError as ude:
                print(f'UnicodeDecodeError occurred: {ude}')
                continue
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            continue
    return uris

def iterative_prompting_4_find_download(pcap):
    if not isinstance(pcap, str):
        raise ValueError("Input must be a valid file path to a pcap file.")
    import scapy.all as scapy
    try:
        dns_packets = scapy.rdpcap(pcap)
    except scapy.ScapyError as e:
        raise RuntimeError(e)

def iterative_prompting_5_find_download(pcap):
    if not isinstance(pcap, str):
        raise ValueError("Input must be a string representing a file path to a pcap file.")
    from dpkt import pcap, https
    uris = []
    try:
        cap = pcap.Reader(pcap)
    except Exception as e:
        raise IOError(f"Failed to read pcap file: {e}")
    for timestamp, buf in cap:
        try:
            eth = ethernet.Ethernet(buf)
            ip = ip.IP(eth.data)
        except Exception as e:
            continue
        if ip.p == https.https.IP_PROTOCOL.HTTPS:
            try:
                https_layer = https.https(ip.data)
                if https_layer.method == 'GET':
                    request = https_layer.request.split(' ')[1].strip('\r\n')
                    if 'download' in request.lower():
                        uri = request.split('&')[0]
                        if '?' in uri:
                            uri = uri.split('?')[0]
                        uris.append(uri)
            except Exception as e:
                continue
    if not uris:
        raise ValueError("No download URIs found in the pcap file.")
    return uris

def few_shots_prompting_findDownload(pcap):
    download_uris = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            if dport == 80 and 'GET' in tcp.data:
                uri = tcp.data.split(' ')[1].decode('utf-8')
                if 'http://' in uri or 'https://' in uri:
                    download_uris.append(uri)
        except: pass
    return download_uris

def cot_prompting_findDownload(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data
            dport = tcp.dport
            if dport == 80:
                data = tcp.data
                uri = data.decode('utf-8').split('')
        except: pass
        
from scapy.all import rdpcap
from scapy.layers.http import HTTPRequest
def fact_check_list_find_download(pcap_file):
    packets = rdpcap(pcap_file)
    http_reqs = [pkt for pkt in packets if pkt.haslayer(HTTPRequest)]
    download_uris = []
    for req in http_reqs:
        try:
            uri = req.get_uri()
            if uri:
                download_uris.append(uri)
        except AttributeError:
            continue

from scapy.all import rdpcap, DNS
def not_interactive_mix_findDownload(pcap):
    packets = rdpcap(pcap)
    download_uris = []
    for packet in packets:
        if packet.haslayer(DNS) and packet[DNS].qd.qtype == 15:
            for i in range(packet.sprintf("%len%")):
                next_packet = packets[packet.sprintf("{%len%})" % i)]
                if next_packet.haslayer(DNS) and next_packet[DNS].qd.qtype == 15:
                    dns_resource = next_packet[DNS].qd.qd.qname.decode('utf-8')
                    if dns_resource.startswith(".download"):
                        download_uris.append(dns_resource)
    return download_uris

def baseline_findDownload(pcap):
    import dpkt
    import socket
    import json
    download_uris = []
    try:
        pcap = dpkt.pcap.Reader(open(pcap, 'rb'))
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if ip.p == dpkt.ip.IP_PROTOCOL_TCP:
                tcp = ip.data
                if tcp.dport == 80 or tcp.sport == 80:
                    try:
                        headers = tcp.data.split(b'\n')
                        for header in headers:
                            if header.startswith(b'GET'):
                                uri_start = header.find(b' ') + 1
                                uri_end = header.find(b' HTTP/')
                                uri = header[uri_start:uri_end].decode('utf-8')
                                download_uris.append(uri)
                                break
                    except IndexError:
                        pass
    except: pass
    return download_uris

