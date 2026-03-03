import re
from urllib.parse import parse_qs, urlparse
import certifi
import os
import pyshark
import ssl
import urllib3
from scapy.all import rdpcap, TCP, IP, Raw
import dpkt
import socket

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
	from scapy.all import rdpcap
	from urllib.parse import urlparse
	packets = rdpcap(pcap)
	downloads = []
	for packet in packets:
		if packet.haslayer('HTTPRequest'):
			header = packet['HTTPRequest']
			if 'Host' in header.fields and 'Path' in header.fields:
				host = header.fields['Host']
				path = header.fields['Path']
				if urlparse(path).query:
					path += '?' + urlparse(path).query
				downloads.append('http://' + host + path)
	return downloads

def template_findDownload(pcap):
	try:
		from scapy.all import PcapReader, TCP, HTTPRequest
		huris = []
		with PcapReader(pcap) as packets:
			for packet in packets:
				if packet.haslayer(HTTPRequest):
					huris.append(packet[HTTPRequest].Path.decode('utf-8'))
		return set(huris)
	except Exception as e:
		return {'error': str(e)}
      
def question_refinement_findDownload(pcap_file):
    import dpkt
    import json
    import binascii
    from dpkt.http import Request
    try:
        with open(pcap_file, 'rb') as file:
            pcap = dpkt.pcap.Reader(file)
            uris = {}
            for timestamp, buf in pcap:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                    ip = eth.data
                    tcp = ip.data
                    http_request = None
                    if isinstance(eth.data, dpkt.ip.IP) and isinstance(tcp.data, bytes) and b'GET' in tcp.data:
                        http_request = Request(tcp.data)
                        uri = http_request.uri.decode('utf-8')
                        if uri not in uris and (uri.endswith('.exe') or uri.endswith('.msi') or uri.endswith('.zip') or uri.endswith('.rar') or uri.endswith('.7z')):
                            uris[uri] = timestamp
                except Exception as e:
                    print(str(e))
            try:
                sorted_uris = sorted(uris.items(), key=lambda item:item[1])
                download_uris = [x[0] for x in sorted_uris]
                return {"download_uris": download_uris}
            except Exception as e:
                print(str(e))
    except FileNotFoundError as e:
        print(str(e))
    except Exception as e:
        print(str(e))
    return json.dumps({"download_uris": ""})

def alternative_approaches_findDownload(pcap):
    import pyshark
    try:
        capture = pyshark.FileCapture(pcap, display_filter='http.request.method == ""GET""')
        download_uris = []
        for packet in capture:
            try:
                uri = packet.http.request_uri
                download_uris.append(uri)
            except AttributeError:
                continue
        return download_uris
    except Exception as e:
        raise Exception('An error occurred while parsing the pcap file:'+ str(e))
    
def context_manager_findDownload(pcap):
    import dpkt
    uris = {}
    for ts, buf in dpkt.pcap.Reader(open(pcap, 'rb')):
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if eth.type == dpkt.ethernet.ETH_TYPE_IP:
                ip = eth.data
                if ip.p == dpkt.ip.IP_PROTO_TCP:
                    tcp = ip.data
                    if len(tcp.data) > 0:
                        try:
                            http = dpkt.http.Request(tcp.data)
                            uris[http.uri] = True
                        except dpkt.dpkt.NeedData:
                            continue
        except Exception as e:
            continue
    return [uri for uri in uris.keys()]

def flipped_interaction_3__findDownload(pcap):
	from scapy.all import PcapReader, TCP, HTTP
	uris = []
	for packet in PcapReader(pcap):
		if packet.haslayer(TCP):
			payload = packet.getlayer(TCP).payload
			if payload and payload.haslayer(HTTP):
				http = payload.getlayer(HTTP)
				if http.fields and b'GET' in http.fields['Method']:
					path = http.fields['Path'].decode('utf-8').lower()
					if '.zip' in path or 'loic' in path:
						uris.append(http.fields['Path'].decode('utf-8'))
	return uris

def flipped_interaction_4__findDownload(pcap):
    file_types = ['.zip', '.pdf', '.exe', '.docx', '.xlsx', '.pptx']
    download_uris = []
    capture = pyshark.FileCapture(pcap)
    for packet in capture:
        if hasattr(packet, 'http'):
            if packet.http.request_method == 'GET':
                uri = packet.http.request_uri
                parsed_uri = urlparse(uri)
                if any(file_type in parsed_uri.path for file_type in file_types):
                    download_uris.append(uri)
                else:
                    query_params = parse_qs(parsed_uri.query)
                    if 'file' in query_params:
                        if any(file_type in query_params['file'][0] for file_type in file_types):
                            download_uris.append(uri)
                    if 'filename' in query_params:
                        if any(re.search(file_type + '$', query_params['filename'][0]) for file_type in file_types):
                            download_uris.append(uri)
    return download_uris

def flipped_interaction_5__findDownload(pcap):
    uris = []
    for ts, buf in pcap:
        pkt = dpkt.ethernet.Ethernet(buf)
        if pkt.type == dpkt.ethernet.ETH_TYPE_IP:
            ip = pkt.data
            if ip.p == dpkt.ip.IP_PROTO_TCP:
                tcp = ip.data
                if hasattr(tcp, 'data') and hasattr(tcp.data, 'find'):
                    payload = tcp.data
                    start = payload.find(b'GET')
                    if start != -1:
                        end = payload.find(b'HTTP/', start)
                        if end != -1:
                            uris.append(payload[start + 4:end].decode())
    httppattern = '.zip'
    specificpacket = 'specificstring'
    hurilist = [x for x in uris if httppattern in x and specificpacket in x]
    return hurilist


def iterative_prompting_3__findDownload(pcap):
    import pkg_resources
    from scapy.all import rdpcap, HTTPRequest
    try:
        pkg_resources.require('scapy==4.8.1')
    except pkg_resources.DistributionNotFound as e:
        raise ValueError(f'Scapy version mismatch: {e}')
    if not isinstance(pcap, str) or not pcap.endswith('.pcap'):
        raise ValueError('Invalid pcap file path')
    try:
        packets = rdpcap(pcap)
    except Exception as e:
        raise FileNotFoundError(f'Failed to read pcap file: {e}')
    downloads = []
    for packet in packets:
        try:
            if packet.haslayer(HTTPRequest):
                http_layer = packet.getlayer(HTTPRequest)
                if http_layer.Path and 'GET' in http_layer.Method:
                    try:
                        host = http_layer.Host.decode('utf-8', errors='ignore')
                        path = http_layer.Path.decode('utf-8', errors='ignore')
                        downloads.append(f'{host}{path}')
                    except UnicodeDecodeError:
                        pass
        except Exception as e:
            print(f'Error processing packet: {e}')
    return downloads

def iterative_prompting_4__findDownload(pcap):
    import dpkt
    if not isinstance(pcap, str):
        raise TypeError('PCAP file path must be a string')
    try:
        import pkg_resources
        dpkt_version = pkg_resources.get_distribution('dpkt').version
        if dpkt_version < '1.9.6':
            raise ValueError('dpkt library is outdated. Please update to 1.9.6 or later.')
        with open(pcap, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)
            urls = []
            for ts, buf in pcap:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                    if eth.data.__class__ == dpkt.ip.IP:
                        ip = eth.data
                        if ip.data.__class__ == dpkt.tcp.TCP:
                            tcp = ip.data
                            payload = tcp.data
                            if payload:
                                try:
                                    http = dpkt.http.Request(payload)
                                    method = http.method.decode('utf-8', errors='ignore')
                                    uri = http.uri.decode('utf-8', errors='ignore')
                                    version = http.version.decode('utf-8', errors='ignore')
                                    if method in ['GET', 'POST']:
                                        if isinstance(method, str) and isinstance(uri, str) and uri.startswith('http'):
                                            urls.append(uri)
                                except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                                    pass
                except Exception as e:
                    pass
            return urls
    except dpkt.dpkt.NeedData:
        raise ValueError('Not enough data to parse PCAP file')
    except dpkt.dpkt.UnpackError:
        raise ValueError('Invalid PCAP file format')
    except Exception as e:
        raise ValueError(f'Invalid PCAP file: {e}')


def iterative_prompting_5__findDownload(pcap):
    if not isinstance(pcap, str):
        raise TypeError('Input pcap must be a string')
    try:
        from scapy.all import Tcp, HTTP, rdpcap, HTTP_Control_Data, flat_list
    except ImportError as e:
        raise ImportError('Scapy library not found') from e
    try:
        packets = rdpcap(pcap)
    except IOError as e:
        raise IOError('Failed to read pcap file') from e
    uris = set()
    for packet in packets:
        if packet.haslayer(Tcp):
            try:
                header_length = packet.getlayer(Tcp).dataofs * 4
            except AttributeError as e:
                continue
            if (packet[Tcp].payload and
                    packet[Tcp].payload[:header_length].hex().startswith('160301') and
                    '\x0f\x01' in packet[Tcp].payload[header_length:].hex()):
                tls_data = packet[Tcp].payload[header_length:]
                for record in tls_data.split(b'\x17\x03'):
                    if record and record[0:5].hex().startswith('1603') and len(record) > 7:
                        tls_record = record[5:]
                        if '\x0f\x01' in tls_record.hex():
                            if (tls_record.find(b'\x0f\x01') <
                                    tls_record.find(b'\x16\x03')):
                                try:
                                    record_body = tls_record[tls_record.find(b'\x0f\x01') + 3:
                                                     tls_record.find(b'\x00\x00\xff\x01')]
                                except IndexError:
                                    continue
                                for h in HTTP_Control_Data(record_body):
                                    uris.add(h[0])
    uris = [uri for uri in uris if uri and isinstance(uri, str)]
    output = []
    for uri in uris:
        uri_lines = str(uri).replace('HTTP/1.1\r\n', '').split('\r\n')
        for line in uri_lines:
            if line and line.startswith('Host'):
                host = line.split(':')[0]
                output.append({'Host': host})
    return output

def few_shots_prompting_findDownload(pcap):
	for (ts, buf) in pcap:
		try:
			http = dpkt.http.Request(buf)
			if hasattr(http, 'uri'):
				print(http.uri.decode())
			if hasattr(http, 'headers'):
				for (key, val) in http.headers.items():
					if key.lower() == 'location':
						print(val.decode())
			if hasattr(http, 'data'):
				if hasattr(http,'method') and http.method == b'GET':
					print(http.uri.decode())
		except:
			pass

def cot_prompting_findDownload(pcap):
    download_uris = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data
            if isinstance(tcp, dpkt.tcp.TCP):
                http = dpkt.http.HTTPResponse(tcp.data)
                if hasattr(http, 'uri'):
                    download_uris.append(http.uri)
        except:
            pass
    return download_uris

def fact_check_list_findDownload(pcap_file: str) -> list:
    uris = []
    capture = pyshark.FileCapture(pcap_file)
    for packet in capture:
        if hasattr(packet, 'http'):
            uri = packet.http.request_uri
            if uri:
                uris.append(uri)
    return uris

def not_interactive_mix_findDownload(pcap):
    if not isinstance(pcap, str) or not pcap.endswith('.pcap'):
        raise ValueError('Invalid pcap file path')
    try:
        capture = pyshark.FileCapture(pcap, display_filter='http.request')
        uris = []
        for packet in capture:
            try:
                if hasattr(packet, 'http'):
                    uri = packet.http.request_uri
                    uris.append(uri)
            except AttributeError:
                pass
        return uris
    except Exception as e:
        print(f'An error occurred: {e}')
        return []
    
import dpkt
import socket

def inet_to_str(inet):
    return socket.inet_ntoa(inet)

def interactive_mix_findDownload(pcap_file):
    uris = []
    try:
        with open(pcap_file, 'rb') as file:
            packets = dpkt.pcap.Reader(file)
            for timestamp, buffer in packets:
                try:
                    eth = dpkt.ethernet.Ethernet(buffer)
                    ip = eth.data
                    tcp = ip.data
                    if isinstance(ip, dpkt.ip.IP) and isinstance(ip.data, dpkt.tcp.TCP):
                        tcp = ip.data
                        data = tcp.data
                        if data:
                            try:
                                http = dpkt.http.Request(data)
                                if http.method == 'GET':
                                    uri = http.uri.decode('utf-8', errors='ignore')
                                    if uri.endswith('.zip') and 'loic' in uri:
                                        uris.append({
                                            'uri': uri,
                                            'src_ip': inet_to_str(ip.src)
                                        })
                            except (dpkt.Error, AttributeError):
                                continue
                except (dpkt.Error, AttributeError):
                    continue
    except FileNotFoundError:
        print(f"File {pcap_file} not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    return uris

def baseline_findDownload(pcap):
    from scapy.all import rdpcap
    from urllib.parse import urlsplit
    sessions = rdpcap(pcap)
    uris = set()
    for packet in sessions:
        if packet.haslayer('TCP') and packet['TCP'].flags == 'PA':
            try:
                data = bytes(packet['TCP'].payload).decode()
                lines = data.split('\r\n')
                for line in lines:
                    if line.startswith('GET'):
                        uri = urlsplit(line.split(' ')[1]).path
                        uris.add(uri)
            except UnicodeDecodeError:
                pass
    return list(uris)
