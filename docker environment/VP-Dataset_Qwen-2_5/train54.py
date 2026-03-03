import dpkt
import socket
import os
from scapy.all import *
import pyshark

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

def persona__ground_truth_code_printPcap(pcap):
    import dpkt
    src_dst_list = []
    with open(pcap, 'rb') as f:
        pcap_reader = dpkt.pcap.Reader(f)
        for timestamp, buf in pcap_reader:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                if isinstance(eth.data, dpkt.ip.IP):
                    ip = eth.data
                    src_dst_list.append((socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst)))
            except dpkt.NeedData or socket.error:
                continue
    return src_dst_list

def template__ground_truth_code_printPcap(pcap):
    import dpkt
    from socket import inet_ntoa
    pkt_list = []
    with open(pcap, 'rb') as f:
        try:
            r = dpkt.pcap.Reader(f)
        except Exception as e:
            return []
        for ts, buf in r:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                ip = eth.data
                if isinstance(ip, dpkt.ip.IP):
                    pkt_list.append((inet_ntoa(ip.src), inet_ntoa(ip.dst)))
            except Exception as e:
                continue
    return pkt_list

def question_refinement__extract_ip_addresses(pcap_data):
    try:
        import struct
        import io
        result, buffer = [], io.BytesIO(pcap_data)
        buffer.seek(24)
        while True:
            packet_header = buffer.read(16)
            if len(packet_header) != 16: break
            ts_sec, ts_usec, incl_len, orig_len = struct.unpack('>IIII', packet_header)
            if incl_len < 40: continue
            ip_header = buffer.read(20)
            ihl, _type, tot_len, identification, flags, ttl, protocol, checksum, src_addr, dst_addr = struct.unpack('!BBHHHBBH4s4s', ip_header)
            if _type != 8:
                buffer.seek(orig_len - 40, 1)
                continue
            result.append((socket.inet_ntoa(src_addr), socket.inet_ntoa(dst_addr)))
    except Exception: pass
    return result

def alternative_approaches__ground_truth_code_printPcap(pcap):
    try:
        import dpkt
        packets = []
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for ts, buf in pcap_reader:
                eth = dpkt.ethernet.Ethernet(buf)
                if isinstance(eth.data, dpkt.ip.IP):
                    ip = eth.data
                    src = socket.inet_ntoa(ip.src)
                    dst = socket.inet_ntoa(ip.dst)
                    packets.append((src, dst))
        return packets
    except Exception as e:
        raise RuntimeError(f"An error occurred while processing the PCAP file: {str(e)}")

def context_manager__ground_truth_code_printPcap(pcap):
	packets = []
	for ts, buf in pcap:
		ethernet_frame = buf[0:14]
		ep_type = ethernet_frame[-2:]
		if ep_type == b'\x08\x00':
			ip_header = buf[14:34]
			src_ip = socket.inet_ntoa(ip_header[12:16])
			dst_ip = socket.inet_ntoa(ip_header[16:20])
			packets.append((src_ip, dst_ip))
	return packets

def flipped_interaction_3__ground_truth_code_printPcap(pcap):
	try:
		with open(pcap, 'rb') as f:
			pcap_reader = dpkt.pcap.Reader(f)
			results = []
			for timestamp, buf in pcap_reader:
				try:
					eth = dpkt.ethernet.Ethernet(buf)
					if isinstance(eth.data, dpkt.ip.IP):
						ip = eth.data
						src_ip = socket.inet_ntoa(ip.src)
						dst_ip = socket.inet_ntoa(ip.dst)
						results.append((src_ip, dst_ip))
				except Exception as e:
					continue
		return results
	except FileNotFoundError:
		return []
	except Exception as e:
		return []

def flipped_interaction_4__ground_truth_code_printPcap(pcap_file_path):
    ip_addresses = []
    try:
        if not os.path.exists(pcap_file_path):
            raise FileNotFoundError()
        packets = rdpcap(pcap_file_path)
        for packet in packets:
            if packet.haslayer(IP):
                src = packet[IP].src
                dst = packet[IP].dst
                ip_addresses.append((src, dst))
            elif packet.haslayer(IPv6):
                src = packet[IPv6].src
                dst = packet[IPv6].dst
                ip_addresses.append((src, dst))
    except FileNotFoundError:
        print(f"Error: The file {pcap_file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred while processing the pcap file: {e}")
        return []
    return ip_addresses

def flipped_interaction_5__ground_truth_code_printPcap(pcap_file):
    ip_addresses = []
    cap = pyshark.FileCapture(pcap_file, display_filter='ip')
    for packet in cap:
        try:
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            ip_addresses.append((src_ip, dst_ip))
        except AttributeError:
            continue
        except Exception:
            continue
        cap.close()
    return ip_addresses

def iterative_prompting_3__ground_truth_code_printPcap(pcap):
    try:
        if not isinstance(pcap, str) or not pcap:
            raise ValueError('Invalid pcap file path provided.')
        packets = rdpcap(pcap)
        ip_addresses = []
        for packet in packets:
            if packet.haslayer(IP):
                src = packet[IP].src
                dst = packet[IP].dst
                ip_addresses.append((src, dst))
        return ip_addresses
    except FileNotFoundError:
        return []
    except ScapyException as e:
        return []

def iterative_prompting_4__ground_truth_code_print_pcap(pcap):
    if not isinstance(pcap, list):
        raise TypeError('Expected a list of packets')
    entries = []
    for packet in pcap:
        if isinstance(packet, dict) and 'IP' in packet:
            ip_layer = packet['IP']
            if isinstance(ip_layer, dict) and 'src' in ip_layer and 'dst' in ip_layer:
                src_ip = str(ip_layer['src'])
                dst_ip = str(ip_layer['dst'])
                entries.append((src_ip, dst_ip))
    return entries

def iterative_prompting_5__ground_truth_code_printPcap(pcap):
    import dpkt
    import socket
    import os
    if not isinstance(pcap, str):
        raise TypeError('The pcap parameter must be a string')
    if not os.path.isfile(pcap):
        raise ValueError('The provided path is not a valid file')
    ip_addresses = []
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_reader:
                try:
                    ether = dpkt.ethernet.Ethernet(buf)
                    if isinstance(ether.data, dpkt.ip.IP):
                        ip = ether.data
                        src_ip = socket.inet_ntoa(ip.src)
                        dst_ip = socket.inet_ntoa(ip.dst)
                        ip_addresses.append((src_ip, dst_ip))
                except (dpkt.UnpackError, dpkt.NeedData, AttributeError):
                    continue
    except IOError as e:
        raise IOError(f'An error occurred while reading the pcap file: {e}')
    return ip_addresses

def few_shots_prompting__ground_truth_code_printPcap(pcap):
	result = []
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			result.append((src, dst))
		except AttributeError:
			pass
	return result

def cot_prompting__ground_truth_code_printPcap(pcap):
	ip_addresses = []
	for (ts, buf) in pcap:
		try:
			e = dpkt.ethernet.Ethernet(buf)
			if isinstance(e.data, dpkt.ip.IP):
				ip = e.data
				src = socket.inet_ntoa(ip.src)
				dst = socket.inet_ntoa(ip.dst)
				ip_addresses.append((src, dst))
		except:
			pass
	return ip_addresses

def fact_check_list__ground_truth_code_printPcap(pcap_filename):
    try:
        packets = rdpcap(pcap_filename)
        ip_addresses = []
        for packet in packets:
            if IP in packet:
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                ip_addresses.append((src_ip, dst_ip))
        return ip_addresses
    except FileNotFoundError:
        print(f"Error: The file {pcap_filename} does not exist.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def not_interactive_mix__ground_truth_code_printPcap(pcap):
    if not isinstance(pcap, str):
        raise ValueError("Input must be a string representing the file path of a pcap file.")
    ip_entries = []
    try:
        with PcapReader(pcap) as packets:
            for packet in packets:
                if IP in packet:
                    ip_layer = packet[IP]
                    ip_entry = (ip_layer.src, ip_layer.dst)
                    ip_entries.append(ip_entry)
    except FileNotFoundError:
        raise FileNotFoundError("The specified pcap file does not exist.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the pcap file: {e}")
    return ip_entries

def interactive_mix__extract_ip_addresses(pcap_file):
    from scapy.all import rdpcap, IP
    packets = rdpcap(pcap_file)
    ip_addresses = []
    for packet in packets:
        if packet.haslayer(IP):
            ip_layer = packet.getlayer(IP)
            src = ip_layer.src
            dst = ip_layer.dst
            ip_addresses.append((src, dst))
    return ip_addresses

def baseline__ground_truth_code_printPcap(pcap):
	import dpkt
	src_dst_list = []
	with open(pcap, 'rb') as f:
		pcap_reader = dpkt.pcap.Reader(f)
		for timestamp, buf in pcap_reader:
			event = dpkt.ethernet.Ethernet(buf)
			if isinstance(event.data, dpkt.ip.IP):
				ip = event.data
				src_ip = socket.inet_ntoa(ip.src)
				dst_ip = socket.inet_ntoa(ip.dst)
				src_dst_list.append((src_ip, dst_ip))
	return src_dst_list
