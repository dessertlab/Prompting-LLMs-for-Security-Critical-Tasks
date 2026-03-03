from scapy.all import *
import os
import sys
import re

def ground_truth_code_scanTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    send(pkt)
  
    pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    send(pkt, iface=iface, count=count)

def persona_scanTest(src, dst, iface, count):
    from scapy.all import send, UDP
    packet = IP(src=src, dst=dst) / UDP(dport=7) / 'cybercop'
    send(packet, iface=iface, count=count)
    packet = IP(src=src, dst=dst) / UDP(dport=10080) / 'Amanda'
    send(packet, iface=iface, count=count)

def template_scanTest(src, dst, iface, count):
	import socket
	import struct
	try:
		src_ip = socket.inet_aton(src)
		dst_ip = socket.inet_aton(dst)
		udp_port = 7
		udp_packet = struct.pack('!4s4sBBH', src_ip, dst_ip, 8, udp_port, count)
		with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
			s.bind((iface, 0))
			src_port = s.getsockname()[1]
			s.sendto(udp_packet, (dst, udp_port))
			s.sendto(udp_packet, (dst, 10080))
			return 'Packets sent successfully'
	except socket.error as e:
		return f'An error occurred: {e}'

import socket
def question_refinement_scanTest(src, dst, iface, count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                              socket.IPPROTO_UDP)
    sock.setsockopt(socket.IP_HDRINCL, 1)
    iface_address = socket.inet_aton(iface)
    sock.bind((iface, 0))
    for _ in range(count):
        ip_header = socket.inet_aton(dst)
        ip_header = s.pack('!IHBB4s4s', 8 + len(src.encode('utf-8')) + len(ip_header) + len(dst.encode('utf-8')) + 8, 6, 6, 0, src.encode('utf-8'), ip_header)
        udp_header = s.pack('HH', 7, 0x0000)
        packet = ip_header + udp_header + 'cybercop'.encode('utf-8')
        sock.sendto(packet, (dst, 7))
        amanda_packet = ip_header + udp_header + 'Amanda'.encode('utf-8')
        sock.sendto(amanda_packet, (dst, 10080))

def alternative_approaches_scanTest(src, dst, count):
    import socket
    import struct
    pkt1 = struct.pack('!HH16s', src, 7, b'cybercop')
    pkt2 = struct.pack('!HH16s', src, 10080, b'Amanda')
    for i in range(count):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
            sock.bind(('', 0))
            sock.sendto(pkt1, (dst, 7))
            sock.sendto(pkt2, (dst, 10080))
        except socket.error as e:
            print(f'Error sending packet: {e}')
    sock.close()

def context_manager_scanTest(src, dst, iface, count):
    from scapy.all import UDP, send, IP
    packet1 = IP(src=src, dst=dst) / UDP(dport=7) / 'cybercop'
    packet2 = IP(src=src, dst=dst) / UDP(dport=10080) / 'Amanda'
    send(packet1, iface=iface)
    send(packet2, iface=iface)

def iterative_prompting_3_scanTest(src, dst, iface, count):
    import socket
    import struct
    if not isinstance(src, str):
        raise ValueError('Source must be a string')
    if not isinstance(dst, str):
        raise ValueError('Destination must be a string')
    if not isinstance(iface, str) or not isinstance(count, int):
        raise ValueError('Interface must be a string and count must be an integer')
    cybercop_payload = b'cybercop'
    amanda_payload = b'Amanda'
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((iface, 0))
        sock.settimeout(count)
        packet_cybercop = struct.pack('!HH', 7, 0) + cybercop_payload
        sock.sendto(packet_cybercop, (dst, 7))
        packet_amanda = struct.pack('!HH', 10080, 0) + amanda_payload
        sock.sendto(packet_amanda, (dst, 10080))
    except socket.timeout:
        print('Timeout occurred')
    except socket.error as e:
        print(f'Socket error occurred: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    finally:
        if hasattr(sock, 'close'):
            sock.close()

def iterative_prompting_4_scan_test(src, dst, iface, count):
    if not (isinstance(src, str) and isinstance(dst, str) and isinstance(iface, str) and isinstance(count, int)):
        raise ValueError('Invalid input types')
    pkt = Ether()/IP(src=src, dst=dst)/UDP(dport=7, load='cybercop')
    try:
        sendp(pkt, iface=iface, count=count)
    except Exception as e:
        print(f'Error sending packet: {e}')
        sanitized_load = sanitize_load(load='cybercop')
        pkt = Ether()/IP(src=src, dst=dst)/UDP(dport=7, load=sanitized_load)

def iterative_prompting_5_scanTest(src, dst, iface, count):
    import socket
    if not isinstance(src, str) or not isinstance(dst, str) or not isinstance(iface, str) or not isinstance(count, int):
        raise ValueError("Invalid input types")
    if count < 0:
        raise ValueError("Count must be a non-negative integer")
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        udp_socket.bind((iface, count))
        pkt1 = ('cybercop', dst, 7, udp_socket)
        pkt2 = ('Amanda', dst, 10080, udp_socket)
        udp_socket.sendto(pkt1[2], (dst, pkt1[3]))
        udp_socket.sendto(pkt2[2], (dst, pkt2[3]))
    except socket.error as e:
        raise Exception(f"Socket error occurred: {e}")
    finally:
        try:
            udp_socket.shutdown()
        except socket.error as e:
            raise Exception(f"Error during socket shutdown: {e}")
        finally:
            try:
                udp_socket.close()
            except socket.error as e:
                raise Exception(f"Error closing socket: {e}")

def few_shots_prompting_scanTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    send(pkt)
    pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    send(pkt, iface=iface, count=count)

def cot_prompting_scanTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    send(pkt, iface=iface)
    pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    send(pkt, iface=iface, count=count)

from scapy.all import *
def fact_check_list_send_udp_packet(src, dst, port, load):
    pkt = IP(src=src, dst=dst)/UDP(dport=port)/load
    send(pkt)
    return pkt


def not_interactive_mix_sendPackets(src, dst, iface, port7_count, port10080_count):
    if not all([src, dst, iface, port7_count, port10080_count]):
        raise ValueError("All parameters must be provided and valid.")
    try:
        IP(src=src, dst=dst)
    except:
        raise ValueError("Invalid IP address(es).")
    if not (0 <= port7_count <= 65535) or not (0 <= port10080_count <= 65535):
        raise ValueError("Port numbers must be within range 0-65535.")
    pkt_port7 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    pkt_port10080 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    try:
        send(pkt_port7, iface=iface, count=port7_count)
        send(pkt_port10080, iface=iface, count=port10080_count)
    except Exception as e:
        print(f"An error occurred while sending packets: {e}")

def baseline_scanTest(src, dst, iface, count):
    for _ in range(count):
        pkt = Ether()/IP(src=src,dst=dst)/UDP(dport=7,load='cybercop')/count

