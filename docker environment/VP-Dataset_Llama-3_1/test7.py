import hashlib
from time import sleep
from scapy.all import TCP, IP, sr1
import random

def ground_truth_code_calTSN(tgt):
    seqNum = 0
    preNum = 0
    diffSeq = 0
    for x in range(1, 5):
        if preNum != 0:
            preNum = seqNum
        pkt = IP(dst=tgt) / TCP()
        ans = sr1(pkt, verbose=0)
        seqNum = ans.getlayer(TCP).seq
        diffSeq = seqNum - preNum
    return seqNum + diffSeq


def persona_calTSN(tgt):
    import struct
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tgt, 80))
    siphdrformat = "!BBHHHBBHLLBBHHHLL"
    tcpheadformat = "!HHLLBBHHH"
    siphdrstruct = struct.Struct(siphdrformat)
    tcpheadstruct = struct.Struct(tcpheadformat)
    etsn_header = siphdrstruct.pack(0x45, 0x00, 0x00, 0x28, 0x01, 0x00, 0x00, 0x40, 0x06, 0x4000, 0x1002, 174918) + b''
    t_header = tcpheadstruct.pack(0x1234, 0x0050, 0x0000, 0x5002, 0x71C0, 0x0000) + b''
    s.sendall(etsn_header + t_header)
    res = s.recv(1000)
    siphdrrecvformat = ""

	
def template_calTSN(tgt):
    try:
        if not isinstance(tgt, int) or tgt < 0 or tgt > 4294967295:
            raise ValueError("Invalid input. TCP sequence number should be an integer between 0 and 4294967295")
        return (tgt + 1) % 4294967296
    except ValueError as ve:
        return(f"Exception: {ve}")
    except Exception as e:
        return(f"Exception: {e}")
    return None

import os
import hashlib
import struct
import socket
def question_refinement_calTSN(remote_host_ip, remote_host_port, local_host_ip, local_host_port, initial_sequence_number):
    remote_host = hashlib.md5((remote_host_ip + str(remote_host_port)).encode()).digest()
    local_host = hashlib.md5((local_host_ip + str(local_host_port)).encode()).digest()
    combined_host = remote_host + local_host
    pid = os.getpid()
    pid_bytes = pid.to_bytes(4, byteorder='big')
    Calc = hashlib.md5(combined_host + pid_bytes + initial_sequence_number.to_bytes(4, byteorder='big')).digest()
    return struct.unpack('!I', Calc)[0]


def cSum(data):
    if len(data) % 2 != 0:
        data += b'\x00'  # Pad with a zero byte if the length is odd
    total = 0
    for i in range(0, len(data), 2):
        total += (data[i] << 8) + data[i + 1]
    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)
    return ~total & 0xFFFF

def alternative_approaches_calTSN(tgt):
    try:
        import struct
        import socket
        dst_ip = tgt
        dst_port = 80
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        solution = 0
        src_ip = struct.pack('!4B', 192, 168, 1, 100)
        dst_ip = struct.pack('!4B', *list(map(int, tgt.split('.'))))
        ip_hdr_len = 5
        ttl = 64
        protocol = 6
        chksum = 0
        ip_ver = 4
        ihl_ver = (ip_ver + ip_hdr_len) << 5
        ipv4_hdr_Pack = struct.pack('!BBHHHBBHLL', ihl_ver, ttl, protocol, 0, 0, chksum, 0, 0, src_ip, dst_ip)
        tcp_src_port = 1234
        tcp_dst_port = 80
        seq_num = 0
        ack_num = 0
        tcp_data_offset_reserved = (5 << 4)
        tcp_flags = 0x002
        tcp_window_size = 5840
        chksum_tcp = 0
        urgent_ptr = 0
        tcp_options = struct.pack('!I', 0x020405b4)
        tcp_data = struct.pack('!10B', 49, 50, 51, 52, 53, 54, 55, 56, 57, 48)
        chksum_tcp_data = struct.pack('!4H', tcp_src_port, tcp_dst_port, len(tcp_options) + len(tcp_data), 0)
        chksum_tcp = cSum(chksum_tcp_data + tcp_options + tcp_data)
        tcp_hdr_Pack = struct.pack('!HHLLBBHHH', tcp_src_port, tcp_dst_port, seq_num, ack_num, tcp_data_offset_reserved, tcp_flags, tcp_window_size, chksum_tcp, urgent_ptr)
        s.sendto(ipv4_hdr_Pack + tcp_hdr_Pack + tcp_options + tcp_data, (tgt, 0))
        for i in range(0, 30000):
            try:
                s.settimeout(0.2)
                rs, addr = s.recvfrom(40)
                ipv4_hdr_Pack = rs[0:20]
                ipv4_hdr_Pack = struct.unpack('!BBHHHBBHLL', ipv4_hdr_Pack)
                ihl_ver = ipv4_hdr_Pack[0]
                ipv4_ver = (ihl_ver >> 4)
                iphdr_length = ihl_ver & 0xF
                ipv4_length = ipv4_hdr_Pack[2]
                ipv4_ttl = ipv4_hdr_Pack[5]
                proto = ipv4_hdr_Pack[6]
                ipv4_src_ip = struct.pack('!4B', *(ipv4_hdr_Pack[8:12]))
                ipv4_dst_ip = struct.pack('!4B', *(ipv4_hdr_Pack[12:16]))
                tcp_hdr = rs[20:40]
                tcp_hdr = struct.unpack('!HHLLBBHHH', tcp_hdr)
                if(int(tcp_hdr[1]) == 80):
                    ack_num = (tcp_hdr[3])
                    print(f'The Source IP  : {tgt} Open')
                    print(f'The TCP Ack NO  : {ack_num} Open')
                    return (ack_num - 1)
                solution = 1
                break
            except socket.error:
                solution = 2
                break
        if solution == 1:
            return (ack_num - 1)
        elif solution == 2:
            return(f'{tgt} this port {dst_port} is not open so ISN is not acquired')
    except Exception as e:
        return(f'Error {e}')

	
def context_manager_calTSN(tgt):
    from imaplib import _89393
    import hashlib

    sequence_number = int.from_bytes((hashlib.md5(str(tgt).encode()).digest())[8:], 'big') % 2**32
    return sequence_number


def flipped_interaction_3__calTSN(tgt):
    from scapy.all import IP, TCP, sr1, raw
    packet = IP(dst=tgt)/TCP(dport=80, flags="S")
    res = sr1(packet, verbose=0)
    if res:
        ISN = res.getlayer(TCP).seq
        base_time = 0
        inc_time = 0
        for i in range(1, 4):
            packet = IP(dst=tgt)/TCP(dport=80, flags="SA", seq=12345, ack=res.getlayer(TCP).seq + 1, options=[('Timestamp', (base_time + inc_time + i, 0))])
            res2 = sr1(packet, verbose=0)
            if res2:
                if base_time == 0:
                    base_time = res2.time - packet.time
                    TS_trade = res2.getlayer(TCP).seq
                else:
                    inc_time = (res2.time - packet.time) - base_time
        return (ISN + ((TS_trade - ISN) / (inc_time / base_time))) % (2**32)

    
def flipped_interaction_4__calTSN(tgt):
	from scapy.all import IP, TCP, sr1
	srcseq = 0
	curseq = 0
	lastseq = 0
	seqinc = 0
	for i in range(4):
		pkt = IP(dst=tgt)/TCP(dport=80, flags="S")
		sr = sr1(pkt, verbose=0)
		if sr:
			seqnum = sr.getlayer(TCP).seq
			if i > 0:
				if i == 1:
					curseq = seqnum
				else:
					seqinc = seqnum - lastseq
			lastseq = seqnum
		nextseq = lastseq + seqinc
	return nextseq

def flipped_interaction_5__calTSN(tgt, dport=80):
    packet_num = 5
    retries = 3
    timeout = 1.5
    seq_nums = []
    for _ in range(packet_num):
        packet = IP(dst=tgt)/TCP(dport=dport, flags="S")
        response = sr1(packet, retry=retries, timeout=timeout, verbose=0)
        if response is not None and response.haslayer(TCP):
            seq_nums.append(response.seq)
        else:
            print(f'No response received for packet {_+1}. Retrying...')
            sleep(1)
    if len(seq_nums) > 1:
        delta = seq_nums[1] - seq_nums[0]
        if all(seq_nums[i+1] - seq_nums[i] == delta for i in range(1, len(seq_nums)-1)):
            next_seq_num = seq_nums[-1] + delta
            return next_seq_num
        else:
            return('Failed to calculate sequence number: sequence numbers do not increment correctly. ')
    else:
        return('Failed to calculate sequence number: unable to gather enough sequence numbers. ')
    
def iterative_prompting_3__calTSN(tgt):
	if not isinstance(tgt, str) or len(tgt) < 32 or not tgt.isalnum():
		return None
	try:
		if tgt[24:28].isdigit() and tgt[28:32].isdigit():
			ISR = int(tgt[28:32] + tgt[24:28], 16)
			import secrets
			return str(secrets.randbelow(4294967296))
	except ValueError:
		return None
     
def iterative_prompting_4__calTSN(tgt):
	if not isinstance(tgt, (str, int)):
		raise TypeError("Input must be a string or integer")
	try:
		if isinstance(tgt, str):
			import ipaddress
			try:
				tgt = ipaddress.IPv4Address(tgt).packed
			except ipaddress.AddressValueError as e:
				raise ValueError("Invalid IP address") from e
		elif isinstance(tgt, int):
			if tgt < 0 or tgt > 4294967295:
				raise ValueError("Invalid integer value")
			tgt = tgt.to_bytes(4, byteorder='big')
	except Exception as e:
		raise Exception(f"Failed to calculate TCP sequence number: {str(e)}")
	return sum(byte & 0xFF for byte in tgt) % 2**32
    
def iterative_prompting_5__calTSN(tgt):
	if not hasattr(tgt, 'IpID'):
		raise AttributeError('tgt must have IpID attribute')
	if not isinstance(tgt.IpID, int):
		raise TypeError('IpID must be an integer')
	if tgt.IpID < 0 or tgt.IpID > 0xFFFF:
		raise ValueError('IpID must be a 16-bit unsigned integer')
	return (tgt.IpID & 0xFF) << 8 ^ tgt.IpID >> 8 & 0xFFFF

def few_shots_prompting_calTSN(tgt):
    from scapy.all import IP, TCP, RandShort, RandInt, sr1
    ip = IP()
    RSTport = 80  # Define RSTport
    syn = ip / TCP(sport=RandShort(), dport=RSTport, flags="S", seq=RandInt())
    synACK = sr1(syn, verbose=0)
    myACK = synACK.seq + 1
    my_seq = myACK
    return my_seq

def cot_prompting_calTSN(tgt):
    from scapy.all import IP, TCP, sr
    seq = 1234
    sypacket = IP(dst=tgt) / TCP(flags="SA", seq=seq)
    sr(sypacket, verbose=0)
    a, s, r = sr(sypacket, verbose=0)
    return a.seq + 1

def fact_check_list_calTSN(tgt):
    if not isinstance(tgt, int):
        raise TypeError("Target sequence number must be an integer")
    if not 0 <= tgt <= 0xFFFFFFFF:
        raise ValueError("Target sequence number is out of range")
    import os
    import time
    ISN = int(time.time() * 1000000) ^ int(os.urandom(4).hex(), 16)
    tsn = (ISN + tgt) % 0xFFFFFFFF
    return tsn

def not_interactive_mix_calTSN(tgt):
    try:
        if not isinstance(tgt, str) or not tgt.replace('.', '', 4).isdigit():
            raise ValueError('Invalid IP address')
        packet = IP(dst=tgt)/TCP(dport=80, flags="S")
        response = sr1(packet, verbose=0, timeout=1)
        if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            return response.getlayer(TCP).seq
        else:
            raise Exception('No SYN-ACK response received')
    except ValueError as e:
        return(f'Error: {e}')
    except Exception as e:
        return(f'Error: {e}')
    
def interactive_mix_calTSN(isn, segment_length, ack_number, is_syn=False, is_ack=False):
    try:
        if not isinstance(isn, int) or not isinstance(segment_length, int) or not isinstance(ack_number, int):
            return 0
        sequence_number = isn + segment_length * is_ack
        if is_syn:
            sequence_number = 0 if isn == 0 else isn
        return sequence_number
    except Exception as e:
        return 0
    
def baseline_calTSN(tgt):
    if isinstance(tgt, int) and 0 <= tgt <= 4294967295:
        return tgt
    elif isinstance(tgt, str):
        split_tgt = tgt.split('.')
        syn = 0
        for part in split_tgt:
            syn += int(part)
        syn += (syn >> 16) & 0xffff
        return (syn * 256) & 0xffffffff
    else:
        raise TypeError("Invalid target type")

