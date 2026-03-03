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

def persona_findHivemind(pcap):
    results = []
    try:
        with open(pcap, 'rb') as f:
            pcap_content = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_content:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                if not isinstance(ip.data, dpkt.tcp.TCP):
                    continue
                tcp = ip.data
                if tcp.sport == 6667 or tcp.dport == 6667:
                    if b'!lazor' in tcp.data.lower():
                        print(f"Timestamp: {timestamp}", "src:dst", ip.src, ip.dst)
                        results.append({
                            'timestamp': timestamp,
                            'src': socket.inet_ntoa(ip.src),
                            'dst': socket.inet_ntoa(ip.dst)
                        })
    except (IOError, dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
        raise ValueError("Error processing the pcap file.")
    return results

def template_findHivemind(pcap):
    import pyshark
    results = []
    try:
        capture = pyshark.FileCapture(pcap, display_filter='tcp.port == 6667')
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {pcap} does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while opening the pcap file: {e}")
    for packet in capture:
        try:
            if 'tcp' in packet:
                if hasattr(packet.tcp, 'payload'):
                    payload = str(packet.tcp.payload).lower()
                    if '!lazor' in payload:
                        results.append({
                            'timestamp': packet.sniff_time.isoformat(),
                            'src': packet.ip.src,
                            'dst': packet.ip.dst,
                            'sport': packet.tcp.srcport,
                            'dport': packet.tcp.dstport
                        })
                        
        except AttributeError:
            continue
    return results

def question_refinement_process_pcap(pcap_file_path):
    target_port = 6667
    target_string = '!lazor'
    results = []
    try:
        logging.info('Starting to process the pcap file.')
        capture = pyshark.FileCapture(pcap_file_path, display_filter='tcp')
        for packet in capture:
            try:
                if 'TCP' in packet:
                    tcp_layer = packet['TCP']
                    if int(tcp_layer.srcport) == target_port or int(tcp_layer.dstport) == target_port:
                        if hasattr(tcp_layer, 'payload'):
                            payload_data = tcp_layer.payload.binary_value.decode('utf-8', errors='ignore')
                            if target_string in payload_data:
                                packet_info = {
                                    'timestamp': packet.sniff_time.isoformat(),
                                    'src_ip': packet.ip.src,
                                    'dst_ip': packet.ip.dst,
                                    'sport': tcp_layer.srcport,
                                    'dport': tcp_layer.dstport,
                                    'payload': payload_data
                                }
                                logging.info('Found target string in packet: %s', packet_info)
                                print(f'Found: {packet_info}')
                                results.append(packet_info)
            except AttributeError as e:
                logging.warning('Attribute error while processing a packet: %s', e)
            except Exception as e:
                logging.error('Unexpected error during packet processing: %s', e)
    except FileNotFoundError:
        logging.error('File not found: %s', pcap_file_path)
    except pyshark.SharkIOException as e:
        logging.error('Error reading pcap file: %s', e)
    except Exception as e:
        logging.critical('Critical error encountered: %s', e)
    finally:
        logging.info('Finished processing pcap file.')
    return results

def alternative_approaches_findHivemind(pcap):
    import pyshark
    results = []
    try:
        cap = pyshark.FileCapture(pcap, display_filter='tcp.port == 6667')
        for packet in cap:
            try:
                if '!lazor' in packet.tcp.payload.lower():
                    packet_info = {
                        'timestamp': packet.sniff_time.isoformat(),
                        'src_ip': packet.ip.src,
                        'dst_ip': packet.ip.dst,
                        'sport': packet.tcp.srcport,
                        'dport': packet.tcp.dstport,
                        'payload': packet.tcp.payload
                    }
                    print(f'Found: {packet_info}')
                    results.append(packet_info)
            except AttributeError:
                continue
        return results
    except Exception as e:
        raise RuntimeError(f'Failed to process pcap file: {e}')


def context_manager_findHivemind(pcap):
    import dpkt
    results = []
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap_reader:
                eth = dpkt.ethernet.Ethernet(buf)
                if isinstance(eth.data, dpkt.ip.IP):
                    ip = eth.data
                    if isinstance(ip.data, dpkt.tcp.TCP):
                        tcp = ip.data
                        if tcp.dport == 6667 or tcp.sport == 6667:
                            if b'!lazor' in tcp.data:
                                result_entry = {
                                    'timestamp': timestamp,
                                    'src': socket.inet_ntoa(ip.src),
                                    'dst': socket.inet_ntoa(ip.dst),
                                    'sport': tcp.sport,
                                    'dport': tcp.dport
                                }
                                results.append(result_entry)
    except (IOError, dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
        return False
    return results


def flipped_interaction_3_findHivemind(pcap):
    matches = []
    for timestamp, buf in dpkt.pcap.Reader(pcap):
        eth = dpkt.ethernet.Ethernet(buf)
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            if isinstance(ip.data, dpkt.tcp.TCP):
                tcp = ip.data
                if tcp.sport == 6667 or tcp.dport == 6667:
                    try:
                        data = tcp.data.decode('utf-8')
                        if '!lazor' in data:
                            match_info = {
                                'timestamp': timestamp,
                                'src_ip': socket.inet_ntoa(ip.src),
                                'dst_ip': socket.inet_ntoa(ip.dst),
                                'data': data
                            }
                            matches.append(match_info)
                    except UnicodeDecodeError:
                        continue
    return matches


def flipped_interaction_4_findHivemind(pcap):
    matches = []
    with open(pcap, 'rb') as f:
        pcap_reader = dpkt.pcap.Reader(f)
        for timestamp, buf in pcap_reader:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if isinstance(ip, dpkt.ip.IP):
                tcp = ip.data
                if isinstance(tcp, dpkt.tcp.TCP):
                    if tcp.sport == 6667 or tcp.dport == 6667:
                        try:
                            data = tcp.data.decode('utf-8')
                            if '!lazor' in data:
                                src_ip = dpkt.utils.inet_to_str(ip.src)
                                dst_ip = dpkt.utils.inet_to_str(ip.dst)
                                matches.append((src_ip, dst_ip, data))
                        except UnicodeDecodeError:
                            continue
    return matches


def flipped_interaction_5_findHivemind(pcap):
    results = []
    packets = rdpcap(pcap)
    for packet in packets:
        if TCP in packet:
            if packet[TCP].sport == 6667 or packet[TCP].dport == 6667:
                if b'!lazor' in bytes(packet[TCP].payload).lower():
                    entry = {
                        'timestamp': packet.time,
                        'src_ip': packet[0][1].src,
                        'dst_ip': packet[0][1].dst,
                        'sport': packet[TCP].sport,
                        'dport': packet[TCP].dport,
                        'payload': bytes(packet[TCP].payload)
                    }
                    print(f'Found: {entry}')
                    results.append(entry)
    return results

def iterative_prompting_3_find_hivemind(pcap):
    results = []
    try:
        with open(pcap, 'rb') as f:
            pcap_reader = dpkt.pcap.Reader(f)
            for timestamp, raw_buf in pcap_reader:
                try:
                    eth = dpkt.ethernet.Ethernet(raw_buf)
                    if isinstance(eth.data, dpkt.ip.IP):
                        ip = eth.data
                        if isinstance(ip.data, dpkt.tcp.TCP):
                            tcp = ip.data
                            if tcp.sport == 6667 or tcp.dport == 6667:
                                if b'!lazor' in tcp.data.lower():
                                    entry = {
                                        'timestamp': timestamp,
                                        'src': dpkt.utils.inet_to_str(ip.src),
                                        'dst': dpkt.utils.inet_to_str(ip.dst),
                                        'sport': tcp.sport,
                                        'dport': tcp.dport,
                                        'payload': tcp.data
                                    }
                                    print(f'Found: {entry}')
                                    results.append(entry)
                except Exception:
                    continue
    except (OSError, dpkt.dpkt.UnpackError):
        raise RuntimeError(f"Error reading pcap file.")
    return results

def iterative_prompting_4_find_hivemind(pcap):
    results = []
    packets = rdpcap(pcap)
    target_string = b'!lazor'
    for packet in packets:
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            if tcp_layer.sport == 6667 or tcp_layer.dport == 6667:
                payload = bytes(tcp_layer.payload)
                if target_string in payload:
                    entry = {
                        'timestamp': packet.time,
                        'src_ip': packet[0][1].src,
                        'dst_ip': packet[0][1].dst,
                        'sport': tcp_layer.sport,
                        'dport': tcp_layer.dport,
                        'payload': payload
                    }
                    print(f'Found: {entry}')
                    results.append(entry)
    return result


def iterative_prompting_5_find_hivemind(pcap):
    results = []
    packets = rdpcap(pcap)
    for packet in packets:
        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            if tcp_layer.sport == 6667 or tcp_layer.dport == 6667:
                if tcp_layer.payload:
                    payload = bytes(tcp_layer.payload)
                    if b'!lazor' in payload:
                        entry = {
                            'timestamp': packet.time,
                            'src_ip': packet[0][1].src,
                            'dst_ip': packet[0][1].dst,
                            'sport': tcp_layer.sport,
                            'dport': tcp_layer.dport,
                            'payload': payload
                        }
                        print(f'Found: {entry}')
                        results.append(entry)
    return results

def few_shots_prompting_findHivemind(pcap):
    import dpkt, socket
    results = []
    for ts, buf in dpkt.pcap.Reader(pcap):
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if isinstance(ip, dpkt.ip.IP):
                tcp = ip.data
                if isinstance(tcp, dpkt.tcp.TCP):
                    if tcp.dport == 6667 or tcp.sport == 6667:
                        if b'!lazor' in tcp.data.lower():
                            packet_info = {
                                'timestamp': ts,
                                'src': socket.inet_ntoa(ip.src),
                                'dst': socket.inet_ntoa(ip.dst),
                                'sport': tcp.sport,
                                'dport': tcp.dport,
                                'payload': tcp.data
                            }
                            print(f'Found: {packet_info}')
                            results.append(packet_info)
        except Exception as e:
            print(f'Error processing packet: {e}')
    return results


def cot_prompting_findHivemind(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data
            dport = tcp.dport
            sport = tcp.sport
            if (dport == 6667 or sport == 6667) and b'!lazor' in tcp.data.lower():
                pass
        except Exception as e:
            pass

def fact_check_list_findHivemind(pcap):
    from scapy.all import rdpcap, TCP
    results = []
    packets = rdpcap(pcap)
    for packet in packets:
        if TCP in packet:
            tcp_layer = packet[TCP]
            if tcp_layer.sport == 6667 or tcp_layer.dport == 6667:
                if b'!lazor' in bytes(tcp_layer.payload).lower():
                    packet_info = {
                        'timestamp': packet.time,
                        'src_ip': packet[0][1].src,
                        'dst_ip': packet[0][1].dst,
                        'sport': tcp_layer.sport,
                        'dport': tcp_layer.dport,
                        'payload': bytes(tcp_layer.payload)
                    }
                    print(f'Found: {packet_info}')
                    results.append(packet_info)
    return results


def not_interactive_mix_findHivemind(pcap_file_path):
    import dpkt
    import socket
    results = []
    try:
        with open(pcap_file_path, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)
            for timestamp, buf in pcap:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                    if isinstance(eth.data, dpkt.ip.IP):
                        ip = eth.data
                        if isinstance(ip.data, dpkt.tcp.TCP):
                            tcp = ip.data
                            if tcp.sport == 6667 or tcp.dport == 6667:
                                if b'!lazor' in tcp.data.lower():
                                    packet_info = {
                                        'timestamp': timestamp,
                                        'src': socket.inet_ntoa(ip.src),
                                        'dst': socket.inet_ntoa(ip.dst),
                                        'sport': tcp.sport,
                                        'dport': tcp.dport,
                                        'payload': tcp.data
                                    }
                                    print(f'Found packet: {packet_info}')
                                    results.append(packet_info)
                except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                    continue
    except (FileNotFoundError, IOError) as e:
        print(f'Error opening file {pcap_file_path}: {e}')
    return results


def interactive_mix_search_string_in_pcap(pcap_file):
    from scapy.all import rdpcap, TCP
    results = []
    try:
        packets = rdpcap(pcap_file)
    except Exception as e:
        print(f'Could not read pcap file: {e}')
        return []

    for packet in packets:
        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            if tcp_layer.sport == 6667 or tcp_layer.dport == 6667:
                try:
                    payload_data = bytes(tcp_layer.payload)
                    if b'!lazor' in payload_data:
                        packet_info = {
                            'timestamp': packet.time,
                            'src_ip': packet[0][1].src,
                            'dst_ip': packet[0][1].dst,
                            'sport': tcp_layer.sport,
                            'dport': tcp_layer.dport,
                            'payload': payload_data
                        }
                        print(f'Found: {packet_info}')
                        results.append(packet_info)
                except Exception:
                    continue
    return results


def baseline_findHivemind(pcap):
    import dpkt, socket
    results = []
    for timestamp, buf in dpkt.pcap.Reader(pcap):
        eth = dpkt.ethernet.Ethernet(buf)
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            if isinstance(ip.data, dpkt.tcp.TCP):
                tcp = ip.data
                if tcp.sport == 6667 or tcp.dport == 6667:
                    if b'!lazor' in tcp.data.lower():
                        packet_info = {
                            'timestamp': timestamp,
                            'src': socket.inet_ntoa(ip.src),
                            'dst': socket.inet_ntoa(ip.dst),
                            'sport': tcp.sport,
                            'dport': tcp.dport,
                            'payload': tcp.data
                        }
                        print(f'Found packet: {packet_info}')
                        results.append(packet_info)
    return results


