import datetime
import logging
import dpkt
import pyshark
import socket
from scapy.all import rdpcap, IP, TCP, Raw

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

def persona_findHivemind(pcap):
    import dpkt
    results = []
    with open(pcap, 'rb') as f:
        pcap_data = dpkt.pcap.Reader(f)
        for timestamp, buf in pcap_data:
            eth = dpkt.ethernet.Ethernet(buf)
            if eth.type == 2048:
                ip = eth.data
                if isinstance(ip, dpkt.ip.IP) and ip.p == 6:
                    tcp = ip.data
                    if isinstance(tcp, dpkt.tcp.TCP) and (tcp.sport == 6667 or tcp.dport == 6667):
                        try:
                            data = tcp.data.decode(errors='ignore')
                            if '!lazor' in data.lower():
                                results.append(f'Found match at timestamp {timestamp}\n')
                        except Exception as e:
                            return(f'An error occurred while processing packet: {e}')
    return results


def template_findHivemind(pcap):
    try:
        import dpkt
        with open(pcap, 'rb') as file:
            pcap_data = dpkt.pcap.Reader(file)
            for timestamp, buffer in pcap_data:
                ether = dpkt.ethernet.Ethernet(buffer)
                if ether.type == 2048:
                    ip = ether.data
                    if ip.p == 6:
                        tcp = ip.data
                        if tcp.th_dport == 6667 or tcp.th_sport == 6667:
                            try:
                                tcp_data = str(tcp.data, encoding='utf-8', errors='strict')
                                if '!lazor' in tcp_data.lower():
                                    return {'timestamp': timestamp, 'data': tcp_data}
                            except UnicodeDecodeError:
                                pass
    except FileNotFoundError:
        return(f'{pcap} file not found')
    except Exception as e:
        return(f'An error occurred: {e}')
        
def question_refinement_findHivemind(pcap_file):
    import dpkt
    
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        found = False
        for ts, buf in pcap:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                if eth.type == dpkt.ethernet.ETH_TYPE_IP:
                    ip = eth.data
                    if isinstance(ip, dpkt.ip.IP) and ip.p == dpkt.ip.IP_PROTO_TCP:
                        tcp = ip.data
                        if isinstance(tcp, dpkt.tcp.TCP) and (tcp.sport == 6667 or tcp.dport == 6667):
                            data = tcp.data.decode(errors='ignore')
                            if '!lazor' in data:
                                found = True
                                break
            except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                pass
    return found

def alternative_approaches_findHivemind(pcap):
    results = []
    import dpkt
    try:
        with open(pcap, 'rb') as file:
            capture = dpkt.pcap.Reader(file)
            for timestamp, buffer in capture:
                try:
                    eth = dpkt.ethernet.Ethernet(buffer)
                    ip = eth.data
                    if isinstance(ip, dpkt.ip.IP):
                        tcp = ip.data
                        if isinstance(tcp, dpkt.tcp.TCP) and (tcp.dport == 6667 or tcp.sport == 6667):
                            if b'!lazor' in bytes(tcp.data):
                                results.append(f'Found!lazor in packet at timestamp {timestamp} from {ip.src}:{tcp.sport} to {ip.dst}:{tcp.dport}')
                except Exception as e:
                    return(f'Error processing packet: {e}')
        return results
    except Exception as e:
        return(f'Error reading pcap file: {e}')
    return None

def context_manager_findHivemind(pcap_file):
    from dpkt import pcap
    from dpkt import ethernet, ip, tcp

    with open(pcap_file, 'rb') as f:
        p = pcap.Reader(f)
        for ts, buf in p:
            eth = ethernet.Ethernet(buf)
            if eth.type == ethernet.ETH_TYPE_IP:
                ip_data = eth.data
                if isinstance(ip_data, ip.IP) and ip_data.p == ip.IP_PROTO_TCP:
                    tcp_data = ip_data.data
                    if isinstance(tcp_data, tcp.TCP) and (tcp_data.dport == 6667 or tcp_data.sport == 6667):
                        data = b''.join(
                            [byte for byte in tcp_data.data if 32 <= byte <= 126 and byte not in (10, 13)]
                        ).decode('utf-8').lower()
                        if '!lazor' in data:
                            yield ts
            
def flipped_interaction_3__findHivemind(pcap):
    results = []
    logging.basicConfig(level=logging.ERROR)
    try:
        for timestamp, buf in pcap:
            try:
                ethernet = dpkt.ethernet.Ethernet(buf)
                if ethernet.type == dpkt.ethernet.ETH_TYPE_IP:
                    ip = ethernet.data
                    if ip.p == dpkt.ip.IP_PROTO_TCP:
                        tcp = ip.data
                        if len(tcp.data) > 0:
                            if tcp.sport == 6667 or tcp.dport == 6667:
                                tcp_payload = tcp.data.decode('utf-8', errors='ignore')
                                if '!lazor' in tcp_payload.lower():
                                    src_ip = '%d.%d.%d.%d' % tuple(map(int, ip.src))
                                    dst_ip = '%d.%d.%d.%d' % tuple(map(int, ip.dst))
                                    packet_timestamp = datetime.utcfromtimestamp(timestamp)
                                    results.append({'src_ip': src_ip, 'dst_ip': dst_ip, 'timestamp': packet_timestamp, 'tcp_data': tcp_payload})
            except Exception as e:
                return(f"Error processing packet: {e}")
    except Exception as e:
        return(f"Error processing pcap: {e}")
    return results

def flipped_interacion_4__findHivemind(pcap):
    result = []
    with open(pcap, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for timestamp, buffer in pcap:
            eth = dpkt.ethernet.Ethernet(buffer)
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                if isinstance(ip.data, dpkt.tcp.TCP):
                    tcp = ip.data
                    if tcp.dport == 6667 or tcp.sport == 6667:
                        data = tcp.data.decode('utf-8', errors='ignore').lower()
                        if '!lazor' in data:
                            src_ip = ip.src
                            dst_ip = ip.dst
                            result.append((src_ip, dst_ip, timestamp, data))
    return result

def flipped_interaction_5__findHivemind(pcap):
    results = []
    for timestamp, packet_bytes in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(packet_bytes)
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                if isinstance(ip.data, dpkt.tcp.TCP):
                    tcp = ip.data
                    if tcp.dport == 6667 or tcp.sport == 6667:
                        tcp_data = tcp.data.decode('utf-8', errors='ignore').lower()
                        if '!lazor' in tcp_data:
                            results.append((timestamp, eth.src, eth.dst, tcp.sport, tcp.dport, tcp_data))
        except Exception as e:
            continue
    return results

def iterative_prompting_3__findHivemind(pcap):
    if not isinstance(pcap, str):
        raise TypeError("pcap must be a string")
    if not pcap:
        raise ValueError("pcap cannot be empty")
    try:
        cap = pyshark.FileCapture(pcap, display_filter="(tcp.port == 6667)", use_json=False)
    except pyshark.exceptions.FileCaptureError as e:
        return(f"Failed to capture file: {e}")
    for pkt in cap:
        try:
            if hasattr(pkt, 'tcp') and hasattr(pkt.tcp, 'payload'):
                if pkt.tcp.payload:
                    payload_bytes = bytes.fromhex(pkt.tcp.payload)
                    if payload_bytes and "!lazor" in payload_bytes.decode("utf-8", errors="replace").lower():
                        print(f'Found!lazor in packet from {pkt.ip.src} to {pkt.ip.dst}')
        except Exception as e:
            return(f"An error occurred while processing packet: {e.__class__.__name__}: {e}")
            
def iterative_prompting_4__findHivemind(pcap):
    if not isinstance(pcap, str):
        raise TypeError('PCAP file path must be a string')
    try:
        with open(pcap, 'rb') as file:
            pcap_data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'PCAP file {pcap} not found')
    except PermissionError:
        raise PermissionError(f'Permission denied to read PCAP file {pcap}')
    if not pcap_data:
        raise ValueError('PCAP file is empty')
    if len(pcap_data) > 1073741824:
        raise ValueError('PCAP file exceeds maximum size of 1 GB')
    tcp_packets = bytearray(pcap_data)
    sig = b'!lazor'
    found_pkt = None
    index = 0
    while index < len(tcp_packets):
        if index + 38 >= len(tcp_packets):
            break
        if (
            tcp_packets[index:index+1] == b'\x06' and
            tcp_packets[index+23:index+24] == b'\xb3' and
            tcp_packets[index+32:index+33] == b'\x03' and
            (
                tcp_packets[index+34:index+35] == b'\xff' or
                tcp_packets[index+36:index+37] == b'\xff'
            )
        ):
            try:
                src_port = int.from_bytes(tcp_packets[index+34:index+36], 'big')
                dst_port = int.from_bytes(tcp_packets[index+36:index+38], 'big')
            except ValueError:
                index += 1
                continue
            if src_port == 6667 or dst_port == 6667:
                try:
                    packet_len = int.from_bytes(tcp_packets[index+16:index+18], 'big')
                except ValueError:
                    index += 1
                    continue
                if packet_len < 20 or packet_len > 65535:
                    index += 1
                    continue
                tcp_hdr_len = (tcp_packets[index+12:index+13][0] >> 4) * 4
                data_len = packet_len - tcp_hdr_len
                data_off = 14 + tcp_hdr_len
                if data_len > 0 and index + packet_len <= len(tcp_packets):
                    data = tcp_packets[index + data_off:index + data_off + data_len]
                    if sig in data:
                        found_pkt = tcp_packets[index:index + packet_len]
                        break
                index += packet_len
            else:
                index += 1
        else:
            index += 1
    if found_pkt is not None:
        return found_pkt
    return b''

def iterative_prompting_5__findHivemind(pcap):
    results = []
    if not isinstance(pcap, list):
        raise ValueError('Invalid pcap input. Expected a list.')
    if not all(callable(getattr(packet, 'haslayer', None)) for packet in pcap):
        raise ValueError('Invalid pcap input. Expected Scapy packets.')
    for packet in pcap:
        try:
            if packet.haslayer(TCP) and (packet[TCP].sport in [6667] or packet[TCP].dport in [6667]):
                if hasattr(packet, 'load') and isinstance(packet.load, bytes) and len(packet.load) > 0:
                    if b'!lazor' in packet.load.lower():
                        results.append(f'TCP {packet[IP].src}:{packet[TCP].sport} -> {packet[IP].dst}:{packet[TCP].dport} contains!lazor')
            return results
        except Exception as e:
            return(f'Error processing packet: {e}')
            
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
                if '!lazor' in str(tcp.data).lower():
                    pass
            if sport == 6667:
                if '!lazor' in str(tcp.data).lower():
                    pass
        except:
            pass
        
def cot_prompting_findHivemind(pcap):
	for (ts, buf) in pcap:
		try:
			e = dpkt.ethernet.Ethernet(buf)
			ip = e.data
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

def fact_check_list_findHivemind(pcap):
    matching_packets = []
    capture = pyshark.FileCapture(pcap)
    for packet in capture:
        if hasattr(packet, 'tcp') and packet.tcp:
            if int(packet.tcp.srcport) == 6667 or int(packet.tcp.dstport) == 6667:
                try:
                    tcp_data = packet.tcp.payload.bin
                    decoded_data = ''.join(chr(int(tcp_data[i:i+2], 16)) for i in range(0, len(tcp_data), 2))
                    if '!lazor' in decoded_data.lower():
                        matching_packets.append(packet)
                except Exception as e:
                    return(f"Error processing packet: {e}")
    return matching_packets
    
def not_interactive_mix_findHivemind(pcap):
    try:
        with open(pcap, 'rb') as file:
            capture = dpkt.pcap.Reader(file)
            for timestamp, buffer in capture:
                try:
                    eth = dpkt.ethernet.Ethernet(buffer)
                    if eth.type == dpkt.ethernet.ETH_TYPE_IP:
                        ip = eth.data
                        if ip.__class__ == dpkt.ip.IP:
                            if ip.p == dpkt.ip.IP_PROTO_TCP:
                                tcp = ip.data
                                if tcp.dport == 6667 or tcp.sport == 6667:
                                    try:
                                        data = tcp.data.decode('ascii', 'ignore').lower()
                                        if '!lazor' in data:
                                            return(f"Found '!lazor' in TCP data on port {tcp.dport} at timestamp {timestamp}")
                                    except UnicodeDecodeError as e:
                                        return(f"Error decoding TCP data: {e}")
                                else:
                                    return(f"Error processing TCP packet: {e}")
                            else:
                                return(f"Non-TCP packet on port {tcp.dport} at timestamp {timestamp}")
                        else:
                            return(f"Non-IP packet at timestamp {timestamp}")
                    else:
                        return(f"Non-Ethernet packet at timestamp {timestamp}")
                except Exception as e:
                    return(f"Error processing packet: {e}")
    except FileNotFoundError as e:
        return(f"File {pcap} not found: {e}")
    except Exception as e:
        return(f"Error processing file {pcap}: {e}")

import dpkt
def interactive_mix_findHivemind(pcap):
    results = []
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data
            if isinstance(tcp, dpkt.tcp.TCP):
                if tcp.dport == 6667 or tcp.sport == 6667:
                    payload = tcp.data.decode('utf-8', errors='ignore')
                    if '!lazor' in payload.lower():
                        results.append((ip.src, ip.dst, timestamp, payload))
        except Exception as e:
            return(f'Error processing packet: {e}')
    return results

def baseline_findHivemind(pcap):
    for packet in pcap:
        if packet.haslayer('TCP') and (packet['TCP'].sport == 6667 or packet['TCP'].dport == 6667):
            payload = bytes(packet['TCP'].payload)
            try:
                payload_str = payload.decode('utf-8')
                if '!lazor' in payload_str.lower():
                    return('Found !lazor in packet from {} to {}'.format(packet['IP'].src, packet['IP'].dst))
            except UnicodeDecodeError as e:
                return(f"Error decoding payload: {e}")

