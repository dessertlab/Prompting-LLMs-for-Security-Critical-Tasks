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

from scapy.all import rdpcap, TCP, Raw

def persona__findHivemind(pcap):
    packetList = rdpcap(pcap)
    results = []
    for packet in packetList:
        if packet.haslayer(TCP) and (packet[TCP].sport == 6667 or packet[TCP].dport == 6667):
            if packet.haslayer(Raw) and "!lazor" in str(packet[Raw].load):
                port = packet[TCP].sport if packet[TCP].sport == 6667 else packet[TCP].dport
                results.append(port)
    return results


def template__findHivemind(pcap):
    try:
        import dpkt
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
                if tcp.sport == 6667 or tcp.dport == 6667:
                    if b'lazor' in tcp.data.lower():
                        return True
        return False
    except Exception as e:
        return None

def question_refinement__search_string_in_pcap(file_path):
    try:
        import io
        import sys
        import os
        import struct
        import socket
        with open(file_path, 'rb') as f:
            magic_number = f.read(4)
            if magic_number not in (b'\xd4\xc3\xb2\xa1', b'\xa1\xb2\c3\xd4'):
                return {'found': False}
            f.seek(24)
            packet = True
            while packet:
                packet_header = f.read(16)
                if len(packet_header) < 16:
                    break
                timestamp_seconds, timestamp_microseconds, included_len, _ = struct.unpack('<IIII', packet_header)
                packet_data = f.read(included_len)
                if len(packet_data) < included_len:
                    break
                ip_data_offset = 14
                ip_version_ihl = packet_data[ip_data_offset] >> 4
                ip_header_length = (ip_data_offset + (ip_version_ihl * 5))
                protocol = packet_data[ip_data_offset + 9]
                source_port = packet_data[ip_header_length:ip_header_length+2]
                dest_port = packet_data[ip_header_length+2:ip_header_length+4]
                source_port = socket.ntohs(struct.unpack('!H', source_port)[0])
                dest_port = socket.ntohs(struct.unpack('!H', dest_port)[0])
                if protocol == 6 and (source_port == 6667 or dest_port == 6667):
                    tcp_header_length = (packet_data[ip_header_length+12] >> 4) * 4
                    data_offset = ip_header_length + tcp_header_length
                    tcp_data = packet_data[data_offset:].decode(errors='ignore')
                    if '!lazor' in tcp_data.lower():
                        return {'found': True}
        return {'found': False}
    except Exception as e:
        return {'found': False, 'error': str(e)}

def alternative_approaches__findHivemind(pcap):
    import dpkt
    found = False
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for ts, buf in pcap_reader:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                if not isinstance(ip.data, dpkt.tcp.TCP):
                    continue
                tcp = ip.data
                if tcp.sport != 6667 and tcp.dport != 6667:
                    continue
                if tcp.data.find(b'!lazor') != -1:
                    found = True
                    break
    except dpkt.NeedData as e:
        print(f'Data needed: {e}. Incomplete packet record.')
    except FileNotFoundError as e:
        print(f'File not found: {e}. Check the path and filename.')
    except Exception as e:
        print(f'An error occurred: {e}')
    return found

def context_manager__findHivemind(pcap):
    import dpkt
    f = open(pcap, 'rb')
    p = dpkt.pcap.Reader(f)
    o = False
    for ts, buf in p:
        try:
            e = dpkt.ethernet.Ethernet(buf)
            if isinstance(e.data, dpkt.ip.IP) and isinstance(e.data.data, dpkt.tcp.TCP):
                i = e.data
                t = i.data
                s = '!lazor'
                if (i.sport == 6667 or i.dport == 6667) and s in t:
                    o = True
                    break
        except:
            pass
    f.close()
    return o

def flipped_interaction_3__findHivemind(pcap):
	results = []
	for ts, buf in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			if isinstance(ip, dpkt.ip.IP):
				tcp = ip.data
				if isinstance(tcp, dpkt.tcp.TCP) and (tcp.sport == 6667 or tcp.dport == 6667):
					data = tcp.data.decode('utf-8', errors='ignore')
					if '!lazor' in data:
						results.append((socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst), ts, data))
		except Exception as e:
			continue
	return results

def flipped_interaction_4__findHivemind(pcap):
	results = []
	try:
		with open(pcap, 'rb') as f:
			pcap_reader = dpkt.pcap.Reader(f)
			for ts, buf in pcap_reader:
				try:
					h = dpkt.ethernet.Ethernet(buf)
				except (dpkt.UnpackError, IndexError) as e:
					logging.warning(f"Ethernet frame unpack error: {e}")
					continue
				if not isinstance(h.data, dpkt.ip.IP):
					continue
				ip = h.data
				if not isinstance(ip.data, dpkt.tcp.TCP):
					continue
				tcp = ip.data
				if tcp.sport == 6667 or tcp.dport == 6667:
					try:
						tcp_data = tcp.data.decode('utf-8', errors='ignore').lower()
					except UnicodeDecodeError as e:
						logging.warning(f"TCP data decoding error: {e}")
						continue
					if '!lazor' in tcp_data:
						src_ip = socket.inet_ntoa(ip.src)
						dst_ip = socket.inet_ntoa(ip.dst)
						results.append((src_ip, dst_ip, ts, tcp_data.strip()))
	except FileNotFoundError as e:
		logging.error(f"File not found: {e}")
	except Exception as e:
		logging.error(f"Unexpected error: {e}")
	return results

def flipped_interaction_5__findHivemind(pcap_file):
	try:
		cap = pyshark.FileCapture(pcap_file, display_filter='tcp.port == 6667')
		packet_summaries = []
		for packet in cap:
			try:
				if 'TCP' in packet and 'IP' in packet:
					tcp_payload = packet.tcp.get_payload().decode('utf-8', errors='ignore').lower()
					if '!lazor' in tcp_payload:
						summary = {
							'source_ip': packet.ip.src,
							'destination_ip': packet.ip.dst,
							'timestamp': packet.sniff_time,
							'tcp_data': packet.tcp.get_payload().decode('utf-8', errors='ignore')
						}
						packet_summaries.append(summary)
			except AttributeError as e:
				print(f"AttributeError in packet {packet.frame_info.number}: {e}")
			except UnicodeDecodeError as e:
				print(f"UnicodeDecodeError in packet {packet.frame_info.number}: {e}")
		cap.close()
		return packet_summaries
	except FileNotFoundError:
		print(f"File not found: {pcap_file}")
		return []
	except pyshark.errors.SharkNotFoundError:
		print("Wireshark or tshark executable not found. Make sure it is installed.")
		return []
	except Exception as e:
		print(f"An error occurred: {e}")
		return []

def iterative_prompting_3__find_hivemind(pcap):
	    if not isinstance(pcap, str):
		    raise ValueError()

def iterative_prompting_4__find_hivemind(pcap):
    if not isinstance(pcap, str):
        raise ValueError('Pcap file path must be a string')
    try:
        packets = rdpcap(pcap)
    except FileNotFoundError:
        raise FileNotFoundError(f'The pcap file {pcap} was not found.')
    except PermissionError:
        raise PermissionError(f'Permission denied when trying to access the pcap file {pcap}.')
    except IsADirectoryError:
        raise IsADirectoryError(f'The provided path {pcap} is a directory, not a pcap file.')
    except Exception as e:
        raise RuntimeError(f'An unexpected error occurred: {str(e)}')
    if not isinstance(packets, list):
        raise TypeError('rdpcap did not return a list of packets.')
    for packet in packets:
        try:
            if packet.haslayer('TCP') and packet.haslayer('Raw'):
                tcp_layer = packet['TCP']
                if tcp_layer.dport == 6667 or tcp_layer.sport == 6667:
                    payload = packet['Raw'].load
                    if b'!lazor' in payload:
                        return True
        except Exception as e:
            raise RuntimeError(f'Error processing packet: {str(e)}')
    return False

def iterative_prompting_5__findHivemind(pcap):
    if not isinstance(pcap, str) or not pcap.endswith('.pcap'):
        raise ValueError('Invalid pcap file path.')
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_reader:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                except (dpkt.UnpackError, dpkt.NeedData):
                    continue
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                if not isinstance(ip.data, dpkt.tcp.TCP):
                    continue
                tcp = ip.data
                if tcp.dport == 6667 or tcp.sport == 6667:
                    if b'!lazor' in tcp.data:
                        return True
    except FileNotFoundError:
        raise FileNotFoundError('The specified pcap file was not found.')
    except IOError:
        raise IOError('An error occurred while reading the pcap file.')
    except Exception as e:
        raise RuntimeError(f'An unexpected error occurred: {{str(e)}}')
    return False

def few_shots_prompting__findHivemind(pcap):
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
                if b'!lazor' in tcp.data.lower():
                    return (ts, src, dst, tcp.sport, tcp.dport, tcp.data)
        except:
            pass

def cot_prompting__findHivemind(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			tcp = ip.data
			dport = tcp.dport
			sport = tcp.sport
			if dport == 6667 or sport == 6667:
				if '!lazor' in tcp.data.lower():
					pass
		except:
			pass

def fact_check_list__findHivemind(pcap_file_path):
    with open(pcap_file_path, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
    results = []
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            ip = eth.data
            if not isinstance(ip.data, dpkt.tcp.TCP):
                continue
            tcp = ip.data
            if tcp.dport != 6667 and tcp.sport != 6667:
                continue
            tcp_data = tcp.data.decode('utf-8', errors='ignore')
            if '!lazor' in tcp_data:
                results.append((timestamp, tcp_data))
        except Exception as e:
            print(f"Error parsing packet: {e}")
    return results

def not_interactive_mix__findHivemind(pcap):
	nm = dpkt.pcap.Reader(io.BytesIO(pcap))
	hivemind_detected = set()
	for _, buf in nm:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			if isinstance(eth.data, dpkt.ip.IP) and eth.data.p == dpkt.ip.IP_PROTO_TCP:
				tcp = eth.data.data
				if len(tcp.data) > 0 and (tcp.sport == 6667 or tcp.dport == 6667):
					if b'!lazor' in tcp.data:
						hivemind_detected.add((eth.src, eth.dst, tcp.sport, tcp.dport))
		except (dpkt.UnpackError, AttributeError, ValueError):
			continue
	return hivemind_detected

def interactive_mix__findHivemind(pcap_file):
    try:
        packets = rdpcap(pcap_file)
    except IOError as e:
        logging.error(f"Error reading pcap file {pcap_file}: {e}")
        return []
    results = []
    for packet in packets:
        if TCP in packet and (packet[TCP].sport == 6667 or packet[TCP].dport == 6667):
            if packet.haslayer('Raw'):
                payload = packet.getlayer('Raw').load.decode('utf-8', errors='replace')
                if '!lazor' in payload.lower():
                    results.append({
                        'time': packet.time,
                        'src': packet[IP].src,
                        'dst': packet[IP].dst,
                        'sport': packet[TCP].sport,
                        'dport': packet[TCP].dport,
                        'payload': payload.strip()
                    })
    return results

def baseline__findHivemind(pcap):
	import dpkt
	packets = open(pcap, 'rb')
	capture = dpkt.pcap.Reader(packets)
	found = False
	for timestamp, buf in capture:
		try:
			ether = dpkt.ethernet.Ethernet(buf)
			if isinstance(ether.data, dpkt.ip.IP):
				ip = ether.data
				if isinstance(ip.data, dpkt.tcp.TCP):
					tcp = ip.data
					if tcp.dport == 6667 or tcp.sport == 6667:
						if b'!lazor' in tcp.data:
							found = True
		except Exception as e:
			continue
	packets.close()
	return found
