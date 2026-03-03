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
    download_uris = []
    capture = pyshark.FileCapture(pcap, display_filter='http.request')
    for packet in capture:
        try:
            if hasattr(packet.http, 'request_uri'):
                uri = packet.http.request_uri
                if re.search(r'\.(exe|zip|dmg|tar\.gz|rar|iso)$', uri, re.IGNORECASE):
                    download_uris.append(uri)
        except AttributeError:
            continue
    capture.close()
    return download_uris

def template_findDownload(pcap):
    import dpkt
    import socket
    uris = []
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_reader:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                    if isinstance(eth.data, dpkt.ip.IP):
                        ip = eth.data
                        if isinstance(ip.data, dpkt.tcp.TCP):
                            tcp = ip.data
                            if tcp.dport == 80 and len(tcp.data) > 0:
                                try:
                                    http = dpkt.http.Request(tcp.data)
                                    if http.method == 'GET':
                                        uri = 'http://{}{}'.format(socket.inet_ntoa(ip.dst), http.uri)
                                        if '.zip' in http.uri or '.exe' in http.uri or '.tar.gz' in http.uri:
                                            uris.append(uri)
                                except (dpkt.dpkt.UnpackError, AttributeError):
                                    continue
                except Exception as e:
                    continue
    except (IOError, dpkt.dpkt.NeedData):
        pass
    return uris

def question_refinement_findDownload(pcap):
    download_uris = []
    try:
        capture = pyshark.FileCapture(pcap, display_filter='http.request')
        for packet in capture:
            if 'http' in packet:
                http_layer = packet.http
                if hasattr(http_layer, 'request_full_uri'):
                    uri = http_layer.request_full_uri
                    if 'download' in uri.lower():
                        download_uris.append(uri)
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        capture.close()
    return download_uris

def alternative_approaches_findDownload(pcap):
    import dpkt
    import socket
    URIs = []
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_reader:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                    if not isinstance(eth.data, dpkt.ip.IP):
                        continue
                    ip = eth.data
                    if not isinstance(ip.data, dpkt.tcp.TCP):
                        continue
                    tcp = ip.data
                    if tcp.dport == 80 and len(tcp.data) > 0:
                        try:
                            http = dpkt.http.Request(tcp.data)
                            host = http.headers.get('host', '')
                            uri = http.uri
                            if 'download' in uri.lower():
                                URIs.append(f"http://{host}{uri}")
                        except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                            continue
                except dpkt.dpkt.UnpackError:
                    continue
    except (FileNotFoundError, dpkt.dpkt.Error) as e:
        print(f'An error occurred: {e}')
    return URIs

def context_manager_findDownload(pcap):
    pcap_data = rdpcap(pcap)
    download_uris = []
    for packet in pcap_data:
        if packet.haslayer(HTTPRequest):
            method = packet[HTTPRequest].Method.decode('utf-8')
            path = packet[HTTPRequest].Path.decode('utf-8')
            if method == 'GET' or method == 'POST':
                download_uris.append(path)
    return download_uris

import dpkt
def flipped_interaction_3_findDownload(pcap):
    uris = []
    for ts, buf in dpkt.pcap.Reader(pcap):
        eth = dpkt.ethernet.Ethernet(buf)
        if not isinstance(eth.data, dpkt.ip.IP):
            continue
        ip = eth.data
        if not isinstance(ip.data, dpkt.tcp.TCP):
            continue
        tcp = ip.data
        if tcp.dport != 80 and tcp.sport != 80:
            continue
        try:
            http = dpkt.http.Request(tcp.data)
            if http.method == 'GET':
                uri = http.uri.decode('utf-8')
                if '.zip' in uri and 'loic' in uri:
                    uris.append(uri)
        except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
            continue
    return uris

import dpkt
def flipped_interaction_4_findDownload(pcap):
    download_uris = []
    with open(pcap, 'rb') as f:
        pcap_reader = dpkt.pcap.Reader(f)
        for timestamp, buf in pcap_reader:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            ip = eth.data
            if not isinstance(ip.data, dpkt.tcp.TCP):
                continue
            tcp = ip.data
            if tcp.dport == 80 or tcp.sport == 80:
                try:
                    http = dpkt.http.Request(tcp.data)
                    if check_download_uri(http.uri):
                        download_uris.append(http.uri)
                except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                    continue
    return download_uris
def check_download_uri(uri):
    download_extensions = ('.exe', '.pdf', '.zip', '.tar.gz', '.msi', '.dmg')
    return uri.lower().endswith(download_extensions)


def flipped_interaction_5_findDownload(pcap):
    download_uris = []
    try:
        packets = rdpcap(pcap)
        file_patterns = re.compile(r'\.(exe|zip|pdf|docx|mp3)$', re.IGNORECASE)
        for packet in packets:
            if packet.haslayer(HTTPRequest):
                http_layer = packet[HTTPRequest]
                host = http_layer.Host.decode() if http_layer.Host else ''
                path = http_layer.Path.decode() if http_layer.Path else ''
                full_url = f"http://{host}{path}"
                if file_patterns.search(path):
                    download_uris.append(full_url)
    except Exception as e:
        print(f"Error reading pcap file: {e}")
    return download_uris

def iterative_prompting_3_find_download(pcap):
    import os
    from scapy.all import rdpcap
    from scapy.layers.http import HTTPRequest
    if not os.path.isfile(pcap):
        raise ValueError("The specified pcap file does not exist.")
    download_extensions = ['.exe', '.zip', '.tar', '.gz', '.rar', '.7z', '.pkg', '.deb']
    uris = []
    try:
        packets = rdpcap(pcap)
    except Exception as e:
        raise RuntimeError(f"Failed to read pcap file: {e}")
    for packet in packets:
        if packet.haslayer(HTTPRequest):
            http_layer = packet.getlayer(HTTPRequest)
            try:
                host = http_layer.Host.decode(errors='ignore') if http_layer.Host else ''
                path = http_layer.Path.decode(errors='ignore') if http_layer.Path else ''
            except UnicodeDecodeError:
                continue
            if not (host and path):
                continue
            for ext in download_extensions:
                if path.endswith(ext):
                    uris.append(f"http://{host}{path}")
                    break
    return uris

def iterative_prompting_4_find_download(pcap):
    import os
    import dpkt
    import socket
    from dpkt.http import Request
    import logging
    logging.basicConfig(level=logging.ERROR)
    uris = []
    if not os.path.isfile(pcap):
        logging.error('PCAP file does not exist: %s', pcap)
        return []
    if os.path.getsize(pcap) == 0:
        logging.warning('PCAP file is empty: %s', pcap)
        return []
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_reader:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                    if isinstance(eth.data, dpkt.ip.IP):
                        ip = eth.data
                        if isinstance(ip.data, dpkt.tcp.TCP):
                            tcp = ip.data
                            if tcp.dport == 80 and len(tcp.data) > 0:
                                try:
                                    request = Request(tcp.data)
                                    if request.method in [b'GET', b'POST']:
                                        uri = f'http://{socket.inet_ntoa(ip.dst)}{request.uri.decode(errors="ignore")}'
                                        uris.append(uri)
                                except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError) as e:
                                    logging.error('Could not parse HTTP request: %s', str(e))
                                    continue
                except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError) as e:
                    logging.error('Error processing packet: %s', str(e))
                    continue
                except Exception as e:
                    logging.error('General error when processing packet: %s', str(e))
                    continue
    except (OSError, IOError) as e:
        logging.error('Error opening pcap file: %s', str(e))
        return logging
    return uris

def iterative_prompting_5_find_download(pcap):
    import dpkt
    import socket
    import os
    def inet_to_str(inet):
        try:
            return socket.inet_ntop(socket.AF_INET, inet)
        except ValueError:
            return socket.inet_ntop(socket.AF_INET6, inet)
    uris = []
    if not isinstance(pcap, str):
        raise TypeError("The pcap parameter must be a string representing the file path.")
    if not os.path.isfile(pcap):
        raise FileNotFoundError(f"The file '{pcap}' does not exist.")
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_reader:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                if isinstance(ip.data, dpkt.tcp.TCP):
                    tcp = ip.data
                    try:
                        http = dpkt.http.Request(tcp.data)
                        if http.method == 'GET' and (
                                any(ext in http.uri for ext in ['.exe', '.zip', '.tar'])):
                            uri = f"http://{inet_to_str(ip.dst)}{http.uri}"
                            uris.append(uri)
                    except (dpkt.dpkt.UnpackError, AttributeError):
                        continue
    except (IOError, dpkt.dpkt.NeedData, dpkt.dpkt.Error) as e:
        raise RuntimeError(f"An error occurred while processing the pcap file: {e}")
    return uris

def few_shots_prompting_findDownload(pcap):
    import dpkt
    download_uris = []
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            ip = eth.data
            if not isinstance(ip.data, dpkt.tcp.TCP):
                continue
            tcp = ip.data
            if not (tcp.sport == 80 or tcp.dport == 80):
                continue
            try:
                http = dpkt.http.Request(tcp.data)
                if 'download' in http.uri:
                    download_uris.append(http.uri)
            except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                continue
        except Exception as e:
            pass
    return download_uris

def cot_prompting_findDownload(pcap):
    download_uris = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data
            if isinstance(tcp, dpkt.tcp.TCP):
                if tcp.dport == 80 and len(tcp.data) > 0:
                    try:
                        http = dpkt.http.Request(tcp.data)
                        uri = http.uri
                        host = b''
                        if b'host' in http.headers:
                            host = http.headers[b'host']
                        full_uri = f"http://{host.decode()}{uri}"
                        download_uris.append(full_uri)
                    except (dpkt.dpkt.UnpackError, AttributeError):
                        continue
        except Exception:
            continue
    return download_uris

def fact_check_list_findDownload(pcap_file):
    packets = rdpcap(pcap_file)
    download_uris = []
    download_regex = re.compile(r"^.*\.(exe|zip|tar\.gz|tar\.bz2|tgz|bz2|dmg|iso|rar)$", re.IGNORECASE)
    for packet in packets:
        if packet.haslayer(HTTPRequest):
            http_layer = packet[HTTPRequest]
            if isinstance(http_layer.Host, bytes) and isinstance(http_layer.Path, bytes):
                uri = f"{http_layer.Host.decode(errors='ignore')}{http_layer.Path.decode(errors='ignore')}"
                if download_regex.match(uri):
                    download_uris.append(uri)
    return download_uris

def not_interactive_mix_findDownload(pcap_file_path):
    import pyshark
    import re
    if not isinstance(pcap_file_path, str):
        raise ValueError("pcap_file_path must be a string")
    download_uri_pattern = re.compile(r'GET /(.*?) HTTP/1\.[01]')
    download_uris = []
    try:
        capture = pyshark.FileCapture(pcap_file_path, display_filter='http')
        for packet in capture:
            if 'HTTP' in packet:
                http_layer = packet['HTTP']
                if hasattr(http_layer, 'request_uri'):
                    request_uri = http_layer.request_uri
                    match = download_uri_pattern.search(request_uri)
                    if match:
                        download_uris.append(request_uri)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {pcap_file_path} was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred during pcap processing: {str(e)}")
    finally:
        capture.close()
    return download_uris

def interactive_mix_extract_download_uris(pcap_file_path):
    import re
    from scapy.all import rdpcap, TCP, Raw
    download_uris = set()
    try:
        packets = rdpcap(pcap_file_path)
        for packet in packets:
            if packet.haslayer(TCP) and packet.haslayer(Raw):
                try:
                    raw_data = packet[Raw].load.decode('latin1', errors='ignore')
                    matches = re.findall(r'(http|https|ftp)://[\w\-\.]+(:\d+)?(/[\w\-\.\%]+)*(\.exe|\.zip|\.pdf)', raw_data)
                    for match in matches:
                        download_uris.add(''.join(match))
                except UnicodeDecodeError:
                    continue
    except Exception as e:
        raise RuntimeError(f"Error processing pcap file: {str(e)}")
    return list(download_uris)

def baseline_findDownload(pcap):
    from scapy.all import rdpcap
    from scapy.layers.http import HTTPRequest
    download_uris = []
    packets = rdpcap(pcap)
    for packet in packets:
        if packet.haslayer(HTTPRequest):
            http_request = packet[HTTPRequest]
            if http_request.Method.decode() == 'GET':
                host = http_request.Host.decode()
                path = http_request.Path.decode()
                uri = f'http://{host}{path}'
                if '.zip' in uri or '.exe' in uri or '.tar' in uri:
                    download_uris.append(uri)
    return download_uris

