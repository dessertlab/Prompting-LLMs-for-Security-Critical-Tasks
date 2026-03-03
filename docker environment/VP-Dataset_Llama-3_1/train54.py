import logging
import dpkt
import pyshark
import socket
from scapy.all import rdpcap, IP

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
    ip_addresses = []
    for timestamp, buf in dpkt.pdt.pcap.Reader(pcap):
        eth = dpkt.ethernet.Ethernet(buf)
        if eth.type == dpkt.ethernet.ETH_TYPE_IP:
            ip = eth.data
            src_ip = '%d.%d.%d.%d' % (ip.src[0], ip.src[1], ip.src[2], ip.src[3])
            dst_ip = '%d.%d.%d.%d' % (ip.dst[0], ip.dst[1], ip.dst[2], ip.dst[3])
            ip_addresses.append((src_ip, dst_ip))
    print(ip_addresses)
    
def template_ground_truth_code_printPcap(pcap):
    try:
        packets = rdpcap(pcap)
        ip_packet_list = []
        for packet in packets:
            if packet.haslayer(IP):
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                ip_packet_list.append((src_ip, dst_ip))
        return ip_packet_list
    except FileNotFoundError:
        print("File not found. Please check the pcap file path.")
        return []
    except Exception as e:
        print("An error occurred: ", str(e))
        return []
    
from scapy.all import rdpcap, IP
def question_refinement_printPcap(pcap_file):
    results = []
    for packet in rdpcap(pcap_file):
        if packet.haslayer(IP) and packet[IP].flags != 2 and packet[IP].proto in [1, 6, 17]:
            results.append((packet[IP].src, packet[IP].dst))
    return results

def alternative_approaches_ground_truth_code_printPcap(pcap):
    try:
        packets = rdpcap(pcap)
        ip_packets = [packet for packet in packets if packet.haslayer(IP)]
        ip_addresses = [(packet[IP].src, packet[IP].dst) for packet in ip_packets]
        return ip_addresses
    except AttributeError:
        print("The pcap file does not contain any IP packets.")
        return []
    except FileNotFoundError:
        print("The specified pcap file does not exist.")
        return []
    except Exception as e:
        print("An error occurred: ", str(e))
        return []
    
def context_manager_ground_truth_code_printPcap(pcap):
	import dpkt
	result = []
	handle = open(pcap, 'rb')
	reader = dpkt.pcap.Reader(handle)
	for timestamp, buf in reader:
		packet = dpkt.ethernet.Ethernet(buf)
		if packet.data.__class__.__name__ == 'IP':
			src = '%d.%d.%d.%d' % tuple(map(ord, list(packet.data.src)))
			dst = '%d.%d.%d.%d' % tuple(map(ord, list(packet.data.dst)))
			result.append((src, dst))
	handle.close()
	return result

def flipped_interaction_3__ground_truth_code_printPcap(pcap):
    ip_addresses = []
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if isinstance(ip, dpkt.ip.IP):
                src_ip = inet_to_str(ip.src)
                dst_ip = inet_to_str(ip.dst)
                ip_addresses.append((src_ip, dst_ip))
        except Exception:
            pass
    return ip_addresses
def inet_to_str(inet):
    try:
        return inet.to_ip()
    except ValueError:
        return str(inet)
    
def flipped_interaction_4__ground_truth_code_printPcap(pcap):
	try:
		f = open(pcap, 'rb')
		packets = dpkt.pcap.Reader(f)
		result = []
		for ts, buf in packets:
			try:
				e = dpkt.ethernet.Ethernet(buf)
				ip = e.data
				if isinstance(ip, dpkt.ip.IP) and ip.v == 4:
					result.append((ip.src, ip.dst))
			except Exception as e:
				pass
		f.close()
		return result
	except Exception:
		return []
     
def flipped_interaction_5__ground_truth_code_printPcap(pcap_file):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    try:
        capture = pyshark.FileCapture(pcap_file, use_json=True)
        ip_addresses = []
        for packet in capture:
            try:
                if hasattr(packet, 'ip'):
                    ip_layer = packet.ip
                elif hasattr(packet, 'ipv6'):
                    ip_layer = packet.ipv6
                else:
                    logger.warning("Packet doesn't have an IP layer. Skipping packet.")
                    continue
                src_ip = ip_layer.src
                dst_ip = ip_layer.dst
                ip_addresses.append((src_ip, dst_ip))
            except Exception as e:
                logger.warning(f"Failed to extract IP addresses from packet: {str(e)}")
        return ip_addresses
    except FileNotFoundError:
        logger.error(f"PCAP file '{pcap_file}' not found.")
        return []
    except Exception as e:
        logger.error(f"Error processing pcap file: {str(e)}")
        return []
    
def iterative_prompting_3__ground_truth_code_printPcap(pcap):
    if not isinstance(pcap, (list, tuple)) or not all(isinstance(packet, bytes) for packet in pcap):
        raise ValueError('Invalid input type')
    result = []
    for packet in pcap:
        if len(packet) < 34:
            continue
        try:
            if not (0 <= packet[14 + 1] <= 15):
                continue
            eth_header = packet[:14]
            iph_length = packet[14 + 1]
            ip_header = packet[14:34]
            iph_length_int = int(iph_length)
            if iph_length_int < 5:
                continue
            if not all(0 <= byte <= 255 for byte in packet[26:30]) or not all(0 <= byte <= 255 for byte in packet[30:34]):
                continue
            src_ip = '.'.join(map(str, packet[26:30]))
            dst_ip = '.'.join(map(str, packet[30:34]))
            result.append((src_ip, dst_ip))
        except Exception as e:
            print(f'Error processing packet: {e}')
    return result

def iterative_prompting_4__ground_truth_code_printPcap(pcap):
    if not isinstance(pcap, (list, tuple)):
        raise TypeError('Expected pcap to be a list or tuple')
    if len(pcap) == 0:
        raise ValueError('Expected pcap to be non-empty')
    ip_packets = [
    ]
    try:
        for packet in pcap:
            if not hasattr(packet, 'haslayer'):
                raise ValueError('Invalid packet object')
            if packet.haslayer(IP):
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                if not (isinstance(src_ip, str) and isinstance(dst_ip, str)):
                    raise ValueError('Invalid IP addresses')
                ip_packets.append((src_ip, dst_ip))
    except Exception as e:
        import logging
        logging.exception(f'An error occurred: {e}')
        raise
    return ip_packets

def iterative_prompting_5__ground_truth_code_printPcap(pcap):
    try:
        import dpkt
        if not (hasattr(pcap,'read') and callable(pcap.read)) or not (hasattr(pcap,'seek') and callable(pcap.seek)):
            raise TypeError('Input pcap must be a file-like object')
        packet_info = []
        with dpkt.pcap.Reader(pcap) as reader:
            for _, buf in reader:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                    if eth.type == dpkt.ethernet.ETH_TYPE_IP:
                        ip = eth.data
                        if isinstance(ip, dpkt.ip.IP):
                            packet_info.append((ip.src, ip.dst))
                except (dpkt.dpkt.Error, AttributeError):
                    continue
        return packet_info
    except (TypeError, dpkt.dpkt.Error) as e:
        raise ValueError('Invalid pcap file: %s' % str(e))
    
def few_shots_prompting_ground_truth_code_printPcap(pcap):
    result = []
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            result.append((src, dst))
        except:
            pass
    return result

def cot_prompting_ground_truth_code_printPcap(pcap):
	ipList = []
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			if isinstance(eth.data, dpkt.ip.IP):
				ip = eth.data
				if isinstance(ip.data, dpkt.tcp.TCP):
					src = socket.inet_ntoa(ip.src)
					dst = socket.inet_ntoa(ip.dst)
					ipList.append((src, dst))
		except:
			pass
	return ipList

def fact_check_list_ground_truth_code_printPcap(pcap_file):
    if not isinstance(pcap_file, str):
        raise TypeError("pcap_file must be a string")
    if not pcap_file.endswith('.pcap'):
        raise ValueError("pcap_file must end with '.pcap'")
    try:
        capture = pyshark.FileCapture(pcap_file, display_filter='ip')
    except pyshark.capture.capture.FileCaptureError as e:
        raise RuntimeError(f"Failed to capture pcap file: {e}")
    ip_addresses = []
    for packet in capture:
        try:
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
        except AttributeError:
            continue
        ip_addresses.append((src_ip, dst_ip))
    return ip_addresses

def not_interactive_mix_ground_truth_code_printPcap(pcap):
    result = []
    if not pcap:
        raise ValueError("PCAP file is empty")
    try:
        try:
            for timestamp, buf in dpkt.pcap.Reader(pcap):
                if buf.getbytes().startswith(b'\x08\x00'):
                    ip_hdr = dpkt.ip.IP(buf)
                    if ip_hdr:
                        src_ip = '%d.%d.%d.%d' % tuple(map(ord, ip_hdr.src))
                        dst_ip = '%d.%d.%d.%d' % tuple(map(ord, ip_hdr.dst))
                        result.append((src_ip, dst_ip))
        except dpkt.dpkt.NeedData as e:
            raise Exception("Not enough data to unpack the packet: {}".format(e))
        except dpkt.dpkt.UnpackError as e:
            raise Exception("Error unpacking the packet: {}".format(e))
    except Exception as e:
        raise Exception("An error occurred: {}".format(e))
    return result

from scapy.all import rdpcap
from ipaddress import ip_address
def intercative_mix_ground_trhuth_code_printPcap(pcap_file):
    ip_addresses = []
    try:
        packets = rdpcap(pcap_file)
        for packet in packets:
            if packet.haslayer(IP):
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                if not (isinstance(src_ip, str) and isinstance(dst_ip, str)):
                    continue
                ip_addresses.append((src_ip, dst_ip))
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    return ip_addresses
    
def baseline_ground_truth_code_printPcap(pcap):
	from scapy.all import rdpcap, IP
	addresses = []
	for packet in pcap:
		if packet.haslayer(IP):
			src_ip = packet[IP].src
			dst_ip = packet[IP].dst
			addresses.append((src_ip, dst_ip))
	return addresses
