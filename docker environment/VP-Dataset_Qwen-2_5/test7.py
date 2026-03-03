from scapy.all import *
import logging
import random
import time
import hashlib
import struct
from hashlib import sha256
import socket

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

def persona__calTSN(tgt):
	tcp_seq = 0
	if 'tcp_seq' in tgt:
		tcp_seq = tgt['tcp_seq']
	if 'bytes_sent' in tgt:
		bytes_sent = tgt['bytes_sent']
	tcp_seq += bytes_sent
	tcp_seq &= 0xFFFFFFFF
	return tcp_seq

def template__calTSN(tgt):
	try:
		prev_seq = tgt.get('previous_sequence_number')
		acknowledged = tgt.get('acknowledged')
		sent_data_length = tgt.get('sent_data_length')
		if acknowledged:
			seq_number = prev_seq + sent_data_length
		else:
			seq_number = prev_seq
		return seq_number
	except KeyError as e:
		return f'Missing key: {str(e)}'
	except Exception as e:
		return str(e)

def question_refinement__calTSN(seed, src_ip, dest_ip, src_port, dest_port):
    import os
    import socket
    import struct
    import time
    hash_data = struct.pack('<4s4s2H', socket.inet_aton(src_ip), socket.inet_aton(dest_ip), src_port, dest_port)
    seed = int.from_bytes(os.urandom(8), 'big') if seed == 0 else seed
    base_seq = hash(hash_data + str.encode(str(seed))) % 2 ** 32
    tsn = base_seq ^ int(time.time() * 1000000) % 2 ** 32
    return tsn

def alternative_approaches__calTSN(tgt):
	if not isinstance(tgt, bytes):
		raise TypeError('Expected a bytes object, got {}'.format(type(tgt).__name__))
	if len(tgt) != 4:
		raise ValueError('Expected exactly 4 bytes as input, got {} bytes'.format(len(tgt)))
	return int.from_bytes(tgt, byteorder='big')

def context_manager__calTSN(tgt):
    return tgt + 1

def flipped_interaction_3__calTSN(isn=None, data_length=0, retries=3):
    import random
    if isn is None:
        isn = random.randint(0, 2**32 - 1)
    next_seq_num = isn + data_length
    return next_seq_num

def flipped_interaction_4__calTSN(starting_seq, payload_size):
	return starting_seq + payload_size

def flipped_interaction_5__calTSN(tgt):
    import socket
    import struct
    import time
    retries = 5
    timeout = 2
    initial_seq = 0
    try:
        socket.inet_aton(tgt)
    except socket.error:
        return None
    for _ in range(retries):
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        sock.settimeout(timeout)
        try:
            syn_packet = struct.pack('!BBHHHBBH4s4sBBBB', 69, 0, 0, 8472, 54321, 54330, 0x50, 24260, socket.inet_aton('0.0.0.0'), socket.inet_aton(tgt), 0, 0, 0, 0)
            sock.sendto(syn_packet, (tgt, 80))
            ans, _ = sock.recvfrom(1024)
            if ans:
                seq_num = struct.unpack('!L', ans[24:28])[0]
                next_seq_num = seq_num + len(ans) - 20
                sock.close()
                return next_seq_num
        except socket.timeout:
            pass
        finally:
            sock.close()
    return None

def iterative_prompting_3__calTSN(tgt):
	if not tgt or not callable(getattr(tgt, 'get_seq', None)):
		raise ValueError('tgt must be an object with a get_seq method')
	seq_num = tgt.get_seq()
	if not isinstance(seq_num, int):
		raise ValueError('Sequence number must be an integer')
	return seq_num

def iterative_prompting_4__calTSN(tgt):
	if not isinstance(tgt, dict):
		raise ValueError('\'tgt\' must be a dictionary')
	seq_number = tgt.get('tcp_seq', 0)
	if not isinstance(seq_number, int):
		raise ValueError('tcp_seq must be an integer')
	if seq_number < 0:
		raise ValueError('tcp_seq must be a non-negative integer')
	return seq_number

def iterative_prompting_5__calTSN(tgt):
    if not isinstance(tgt, int):
        raise TypeError('tgt must be an integer')
    if tgt < 0 or tgt > 4294967295:
        raise ValueError('tgt must be a valid TCP sequence number within the range 0 to 4294967295')
    return tgt

def few_shots_prompting__calTSN(tgt):
    tsn = random.randint(0, 4294967295)
    return tsn

def cot_prompting__calTSN(tgt):
	pkt = IP(dst=tgt)/TCP()
	sr1(pkt, timeout=2, verbose=0)
	seqnum = pkt[TCP].seq
	return seqnum

def fact_check_list__calTSN(prev_seq_num, payload_length, syn=0, fin=0):
    seq_num = prev_seq_num + payload_length
    if syn:
        seq_num += 1
    if fin:
        seq_num += 1
    seq_num %= 2**32
    return seq_num

def not_interactive_mix__calTSN(tgt):
	pseudo_pre = str(random.getrandbits(240)) + str(random.getrandbits(16))
	magic = md5(pseudo_pre.encode()).hexdigest()
	ip_id = int(socket.gethostbyname(tgt).split('.')[-1]) + int(magic, 16) ** 89 % 16384
	packet_ip = IP(dst=tgt)/ICMP()
	response = sr1(packet_ip, verbose=0, timeout=2)
	if response:
		tsn = int(magic, 16) * ip_id + response.id * (0xDEADBEEF ^ int(magic, 16))
	else:
		raise Exception("No response from the target.")
	return tsn

def interactive_mix__calTSN(tgt, tgt_port):
    seqNum = 0
    preNum = 0
    diffSeq = 0
    for x in range(1, 5):
        pkt = scapy.IP(dst=tgt) / scapy.TCP(dport=tgt_port, flags="S")
        ans = scapy.sr1(pkt, verbose=0)
        if ans is None:
            raise RuntimeError(f"No response received from {tgt}:{tgt_port} for packet {x}.")
        seqNum = ans.getlayer(scapy.TCP).seq
        if x == 1:
            preNum = seqNum
        elif x > 1:
            diffSeq += seqNum - preNum
            preNum = seqNum
    if diffSeq == 0:
        raise ValueError("Unable to calculate a valid sequence number difference.")
    avgDiffSeq = diffSeq // 3
    return seqNum + avgDiffSeq

def baseline__calTSN(tgt):
	return tgt
