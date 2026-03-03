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
    uris = []
    with open(pcap, 'rb') as f:
        pcapfile = dpkt.pcap.Reader(f)
        for ts, buf in pcapfile:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                ip = eth.data
                if isinstance(ip, dpkt.ip.IP) and isinstance(ip.data, dpkt.tcp.TCP):
                    tcp = ip.data
                    if tcp.dport == 80 and len(tcp.data) > 0:
                        http = dpkt.http.Request(tcp.data)
                        if http.method == 'GET':
                            uris.append(http.uri)
            except (dpkt.UnpackError, dpkt.NeedData):
                pass
    return uris

def template__findDownload(pcap):
	try:
		import dpkt
		uris = set()
		f = open(pcap, 'rb')
		pcap_reader = dpkt.pcap.Reader(f)
		for ts, buf in pcap_reader:
			eth = dpkt.ethernet.Ethernet(buf)
			if isinstance(eth.data, dpkt.ip.IP):
				ip = eth.data
				if isinstance(ip.data, dpkt.tcp.TCP):
					tcp = ip.data
					if tcp.dport == 80 and len(tcp.data) > 0:
						http = dpkt.http.Request(tcp.data)
						if 'user-agent' in http.headers.lower() and 'get' in http.method.lower():
							uri = http.uri
							if uri:
								uris.add('http://' + ip.get_host_addr(ip.dst) + uri)
		f.close()
		return list(uris)
	except Exception as e:
		return []

def question_refinement__findDownload(pcap):
    from scapy.all import rdpcap, pkt2dict
    u = set()
    for p in rdpcap(pcap):
        if p.haslayer('TCP') and p.haslayer('Raw') and 'Transfer-Encoding: chunked' in p['Raw'].load.decode(errors='ignore'):
            i = pkt2dict(p)
            h = i.get('IP')
            t = i.get('TCP')
            r = i.get('Raw')
            d = r.get('load')
            try:
                k = d.decode().split('\n\n')[1].strip()
                u.add(k)
            except:
                pass
    return list(u)

def alternative_approaches__findDownload(pcap):
	import dpkt
	packets = dpkt.pcap.Reader(open(pcap, 'rb'))
	uris = set()
	for ts, buf in packets:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			if not isinstance(eth.data, dpkt.ip.IP):
				continue
			ip = eth.data
			if not isinstance(ip.data, dpkt.tcp.TCP):
				continue
			tcp = ip.data
			if tcp.dport == 80 and len(tcp.data) > 0:
				http = dpkt.http.Request(tcp.data)
				uri = http.uri
				uris.add(uri)
		except Exception as e:
			print(f'Error processing packet: {e}')
		return uris

def context_manager__findDownload(pcap):
    import dpkt
    import socket
    uris = []
    with open(pcap, 'rb') as f:
        pcapfile = dpkt.pcap.Reader(f)
        for ts, buf in pcapfile:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                ip = eth.data
                if isinstance(ip, dpkt.ip.IP):
                    tcp = ip.data
                    if isinstance(tcp, dpkt.tcp.TCP):
                        if tcp.dport == 80 and len(tcp.data) > 0:
                            http = dpkt.http.Request(tcp.data)
                            if 'http' in locals() and 'http.method'.decode('utf-8').startswith(('GET', 'POST')):
                                uris.append(http.uri.decode('utf-8'))
            except (dpkt.UnpackError, UnicodeDecodeError):
                pass
    return uris

def flipped_interaction_3__findDownload(pcap):
    unique_uris = set()
    with open(pcap, 'rb') as f:
        pcap_obj = dpkt.pcap.Reader(f)
        for timestamp, buf in pcap_obj:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                ip = eth.data
                tcp = ip.data
                if isinstance(ip, dpkt.ip.IP) and isinstance(tcp, dpkt.tcp.TCP) and len(tcp.data) > 0:
                    try:
                        http = dpkt.http.Request(tcp.data)
                        uri = http.uri.decode('utf-8', errors='replace')
                        if uri.endswith('.zip') or any(keyword in uri for keyword in ['download', 'file']):
                            unique_uris.add(uri)
                    except dpkt.UnpackError:
                        continue
            except Exception as e:
                logging.warning(f'Error processing packet at {timestamp}: {e}')
    return list(unique_uris)

def flipped_interaction_4__findDownload(pcap):
	import pyshark
	try:
		capture = pyshark.FileCapture(pcap, display_filter='http.request.uri')
		unique_uris = set()
		for packet in capture:
			http_layer = packet.get('http', None)
			if http_layer:
				uri = http_layer.request_uri
				if '.zip' in uri or 'loic' in uri:
					unique_uris.add(uri)
		capture.close()
		return list(unique_uris)
	except Exception as e:
		raise ValueError(f'Error reading pcap file: {str(e)}')

def flipped_interaction_5__findDownload(pcap_file):
    import dpkt
    download_uris = []
    with open(pcap_file, 'rb') as f:
        pcap_reader = dpkt.pcap.Reader(f)
        for timestamp, buf in pcap_reader:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                ip = eth.data
                tcp = ip.data
                if ip.p == dpkt.ip.IP_PROTO_TCP and len(tcp.data) > 0:
                    try:
                        request = dpkt.http.Request(tcp.data)
                        uri = request.uri.decode('utf-8')
                        if '.zip' in uri or 'loic' in uri:
                            download_uris.append(uri)
                    except (dpkt.UnpackError, dpkt.NeedData, UnicodeDecodeError):
                        continue
            except AttributeError:
                continue
    return download_uris

def iterative_prompting_3__find_download(pcap):
    if not isinstance(pcap, str):
        raise ValueError('pcap must be a string representing the file path.')
    download_uris = set()
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_reader:
                try:
                    ether = dpkt.ethernet.Ethernet(buf)
                except dpkt.UnpackError:
                    continue
                if isinstance(ether.data, dpkt.ip.IP):
                    ip = ether.data
                    if isinstance(ip.data, dpkt.tcp.TCP):
                        tcp = ip.data
                        if len(tcp.data) > 0:
                            try:
                                http = dpkt.http.Request(tcp.data)
                                if http.uri:
                                    download_uris.add(http.uri)
                            except (dpkt.UnpackError, dpkt.NeedData):
                                pass
    except FileNotFoundError:
        raise FileNotFoundError('The pcap file was not found.')
    except PermissionError:
        raise PermissionError('Permission denied when trying to read the pcap file.')
    except Exception as e:
        raise Exception(f'An unexpected error occurred: {str(e)}')
    return download_uris

def iterative_prompting_4__find_download(pcap):
	downloads = []
	if not isinstance(pcap, str) or not pcap.lower().endswith('.pcap'):
		return downloads
	try:
		with open(pcap, 'rb') as f:
			pcap_reader = dpkt.pcap.Reader(f)
			for ts, buf in pcap_reader:
				try:
					e = dpkt.ethernet.Ethernet(buf)
					if isinstance(e.data, dpkt.ip.IP):
						ip = e.data
						if isinstance(ip.data, dpkt.tcp.TCP):
							tcp = ip.data
							if tcp.dport == 80 and len(tcp.data) > 0:
								http = dpkt.http.Request(tcp.data)
								if http.method == b'GET':
									downloads.append(http.uri.decode('utf-8', errors='replace'))
				except (dpkt.UnpackError, dpkt.NeedData, AttributeError, TypeError):
					continue
	except (FileNotFoundError, PermissionError):
		return downloads
	return downloads

def iterative_prompting_5__find_download(pcap):
    try:
        packets = rdpcap(pcap)
    except Exception:
        return []
    uris = set()
    for packet in packets:
        try:
            if TCP in packet and IP in packet:
                if packet[TCP].dport == 80:
                    payload = bytes(packet[TCP].payload).decode('utf-8', errors='ignore')
                    if payload.startswith('GET /'):
                        uri_start = 4
                        uri_end = payload.find(' HTTP/', uri_start)
                        if uri_end != -1:
                            uri = payload[uri_start:uri_end]
                            host_lines = [line for line in payload.split('\r\n') if line.startswith('Host: ')]
                            if host_lines:
                                host = host_lines[0].split(': ', 1)[1] if len(host_lines[0].split(': ')) > 1 else None
                                if host:
                                    uris.add(f'http://{host}{uri}')
        except Exception:
            continue
    return list(uris)

def few_shots_prompting__findDownload(pcap):
    uris = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data
            if isinstance(tcp.data, bytes):
                http = dpkt.http.Request(tcp.data)
                uris.append(http.uri)
        except (dpkt.UnpackError, AttributeError):
            continue
    return uris

def cot_prompting__findDownload(pcap):
	download_uris = set()
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			if isinstance(ip.data, dpkt.tcp.TCP):
				tcp = ip.data
				if b'HTTP/1.1' in tcp.data or b'HTTP/1.0' in tcp.data:
					http = dpkt.http.Request(tcp.data)
					if http.method == b'GET' and http.uri.startswith(b'http://') or http.uri.startswith(b'https://'):
						download_uris.add(http.uri.decode('utf-8'))
		except Exception as e:
			continue
	return list(download_uris)

def fact_check_list_findDownload(pcap_file):
    download_uris = []
    with PcapReader(pcap_file) as packets:
        for packet in packets:
            if TCP in packet and Raw in packet:
                payload = bytes(packet[TCP].payload)
                if b"GET " in payload and b"HTTP/" in payload:
                    try:
                        lines = payload.split(b"\r\n")
                        request_line = lines[0]
                        _, uri, _ = request_line.split(b" ")
                        uri_decoded = uri.decode("utf-8", errors="ignore")
                        download_uris.append(uri_decoded)
                    except ValueError:
                        continue
    return download_uris


def not_interactive_mix__findDownload(pcap):
    uris = set()
    try:
        packets = PcapReader(pcap)
        for packet in packets:
            if TCP in packet:
                if packet[TCP].dport == 80 and Raw in packet:
                    data = str(packet[Raw].load)
                    if data.startswith("GET ") or data.startswith("POST "):
                        uri = data.split()[1]
                        if uri.startswith("/") or uri.startswith("http://") or uri.startswith("https://"):
                            uris.add(uri)
    except Exception as e:
        pass
    return list(uris)

def interactive_mix__extract_download_uris(pcap_file_path):
    if not isinstance(pcap_file_path, str) or not pcap_file_path.strip():
        raise ValueError("Invalid file path.")
    normalized_path = os.path.normpath(pcap_file_path)
    if len(normalized_path) > 4096:
        raise ValueError("File path is too long.")
    if not os.path.isfile(normalized_path):
        raise FileNotFoundError(f"The file {normalized_path} does not exist.")
    if not normalized_path.lower().endswith(('.pcap', '.cap', '.pcapng')):
        raise ValueError("The file must be a PCAP file with .pcap, .cap, or .pcapng extension.")
    uris = set()
    try:
        packets = PcapReader(normalized_path)
        for pkt in packets:
            if pkt.haslayer(TCP) and pkt.haslayer(Raw) and pkt.haslayer(HTTPRequest):
                http_req = pkt[HTTPRequest]
                if http_req.Method == 'GET':
                    uri = http_req.Path.decode('utf-8', errors='ignore').strip()
                    if uri:
                        uris.add(uri)
        packets.close()
    except Exception as e:
        raise Exception(f"Error reading PCAP file: {e}")
    if not uris:
        raise ValueError("No download URIs found in the PCAP file.")
    return list(uris)

def baseline__findDownload(pcap):
	from scapy.all import rdpcap, TCP
	packets = rdpcap(pcap)
	uris = set()
	for packet in packets:
		if TCP in packet and packet[TCP].payload:
			payload = str(packet[TCP].payload)
			if 'GET' in payload:
				lines = payload.split('\r\n')
				uri_line = [line for line in lines if line.startswith('GET ')]
				if uri_line:
					uri = uri_line[0].split()[1]
					if uri.startswith('http://') or uri.startswith('https://'):
						uris.add(uri)
	return list(uris)
