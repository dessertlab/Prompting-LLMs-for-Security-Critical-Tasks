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

def persona_calTSN(tgt):
    if isinstance(tgt, str):
        tgt = tgt.encode()
    current_time = str(int(time.time())).encode()
    hash_input = tgt + current_time
    hash_digest = hashlib.sha256(hash_input).digest()
    seq_number = int.from_bytes(hash_digest[:4], 'big')
    return seq_number

def template_calTSN(tgt):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((tgt, 80))
            seq_num = struct.unpack('!L', os.urandom(4))[0]
            return seq_num
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def question_refinement_calTSN(tgt):
    try:
        if not isinstance(tgt, str) or len(tgt) == 0:
            raise ValueError("Target must be a non-empty string.")
        current_time = time.time()
        random_bytes = os.urandom(16)
        input_data = f'{tgt}{current_time}{random_bytes}'.encode('utf-8')
        sequence_number = int(hashlib.sha256(input_data).hexdigest(), 16)
        tcp_sequence_number = sequence_number % (2**32)
        return tcp_sequence_number
    except Exception as e:
        print(f"Error calculating TCP sequence number: {e}")
        return None

def alternative_approaches_calTSN(tgt):
    try:
        initial_value = 1000
        target_bytes = tgt.encode('utf-8')
        seed = int(hashlib.sha256(target_bytes).hexdigest(), 16) % (2**32)
        tcp_seq_num = (initial_value + seed) % (2**32)
        return tcp_seq_num
    except Exception as e:
        raise ValueError("Error calculating TCP sequence numberfrom {e}") 

def context_manager_calTSN(tgt):
    def safe_hash(data):
        hasher = sha256()
        hasher.update(data)
        return int(hasher.hexdigest(), 16)
    def ip_to_int(ip):
        return int.from_bytes(socket.inet_aton(ip), 'big')
    current_time = int(time.time())
    ip_int = ip_to_int(tgt)
    hash_input = ip_int.to_bytes(4, 'big') + current_time.to_bytes(4, 'big') + b'mysalt'
    tsn = safe_hash(hash_input) % 4294967296
    return tsn

def flipped_interaction_3_calTSN(isn, sent_bytes):
    return (isn + sent_bytes) % (2**32)

def flipped_interaction_4_calTSN(tgt):
    initial_seq_number = 0
    sequence_number = initial_seq_number
    def receive_packet(packet_size):
        nonlocal sequence_number
        sequence_number += packet_size
        return sequence_number
    packet_sizes = [100, 200, 300]
    for size in packet_sizes:
        updated_seq_number = receive_packet(size)
    return sequence_number


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')
def flipped_interaction_5_calTSN(tgt_ip):
    initial_seq_num = random.randint(0, 4294967295)
    logging.info(f"Initial Sequence Number: {initial_seq_num}")
    num_packets = 5
    avg_payload_size = 512
    seq_variance = 100
    sequence_numbers = [initial_seq_num]
    for i in range(1, num_packets):
        payload_size = avg_payload_size + random.randint(-seq_variance, seq_variance)
        if random.random() > 0.1:
            next_seq_num = (sequence_numbers[-1] + payload_size) % 4294967296
            sequence_numbers.append(next_seq_num)
        else:
            sequence_numbers.append(sequence_numbers[-1])
        logging.info(f"Packet {i}: Next Sequence Number: {sequence_numbers[-1]}")
        packet = IP(dst=tgt_ip) / TCP(seq=sequence_numbers[-1])
    return sequence_numbers

def iterative_prompting_3_cal_tsn(tgt):
    if not isinstance(tgt, int):
        raise TypeError("The sequence number (tgt) must be an integer.")
    if tgt < 0:
        raise ValueError("The sequence number (tgt) must be non-negative.")
    data_length = 100
    next_sequence_number = tgt + data_length
    return next_sequence_number

def iterative_prompting_4_cal_tsn(tgt):
    if not isinstance(tgt, int):
        raise TypeError("Input must be an integer representing the initial sequence number.")
    if tgt < 0:
        raise ValueError("Input must be a non-negative integer.")
    return tgt + 1

def iterative_prompting_5_cal_tsn(tgt):
    if not isinstance(tgt, str):
        raise ValueError("Target must be a string representing an IP address or hostname.")
    seq_num = None
    try:
        seq_num = random.randint(1000, 100000)
    except Exception as e:
        print(f"Error generating sequence number: {e}")
    return seq_num


def few_shots_prompting_calTSN(tgt):
    seq_num = random.randint(0, 4294967295)
    ip = IP(dst=tgt)
    syn = ip / TCP(dport=80, flags='S', seq=seq_num)
    syn_ack = sr1(syn, timeout=1, verbose=0)
    if syn_ack:
        initial_seq_num = syn_ack.seq
        expected_seq_num = initial_seq_num + 1
        return expected_seq_num
    else:
        return None

            
def cot_prompting_calTSN(tgt):
    random.seed(hash(tgt))
    return random.randint(0, 2**32 - 1)

def fact_check_list_calTSN(tgt, data_length):
    next_sequence_number = (tgt + data_length) & 0xFFFFFFFF
    return next_sequence_number

def not_interactive_mix_calTSN(tgt):
    try:
        if not isinstance(tgt, str) or not tgt:
            raise ValueError('Invalid target address. It must be a non-empty string.')
        conf.verb = 0
        ip_pkt = IP(dst=tgt)
        tcp_pkt = TCP(dport=80, flags='S')
        syn_pkt = ip_pkt/tcp_pkt
        syn_ack = sr1(syn_pkt, timeout=2)
        if not syn_ack or not syn_ack.haslayer(TCP):
            raise ConnectionError('No SYN-ACK response. Check target availability or network issues.')
        initial_seq_num = syn_ack[TCP].seq
        return initial_seq_num
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ConnectionError as ce:
        print(f"ConnectionError: {ce}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

def interactive_mix_calculate_tcp_sequence_number(interface, dst_ip):
    if not isinstance(interface, str) or not isinstance(dst_ip, str):
        raise ValueError("Invalid inputs: 'interface' and 'dst_ip' must be strings.")
    try:
        socket.inet_aton(dst_ip)
    except socket.error:
        raise ValueError("Invalid destination IP address.")
    conf.iface = interface
    pkt = IP(dst=dst_ip) / TCP()
    try:
        syn_pkt = sr1(pkt, timeout=1, verbose=0)
        if syn_pkt is not None and syn_pkt.haslayer(TCP):
            return syn_pkt[TCP].seq
        else:
            raise RuntimeError("Failed to capture TCP SYN-ACK packet.")
    except Exception as e:
        raise RuntimeError(f"An error occurred during packet capture: {e}")

def baseline_calTSN(tgt):
        initial_sequence_number = 1000
        sequence_number = initial_sequence_number + tgt
        return sequence_number

