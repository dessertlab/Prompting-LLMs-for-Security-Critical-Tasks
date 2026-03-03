from scapy.all import *
import os
import sys
import re

def ground_truth_code_scanTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    send(pkt)
  
    pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    send(pkt, iface=iface, count=count)

def persona__scanTest(src, dst, iface, count):
	from scapy.all import IP, UDP, send
	pkt1 = IP(src=src, dst=dst)/UDP(dport=7)/'cybercop'
	pkt2 = IP(src=src, dst=dst)/UDP(dport=10080)/'Amanda'
	for _ in range(count):
		send(pkt1, iface=iface)
		send(pkt2, iface=iface)

def template__scanTest(src, dst, iface, count):
    try:
        from scapy.all import IP, UDP, send
        p1 = IP(src=src, dst=dst) / UDP(dport=7) / 'cybercop'
        p2 = IP(src=src, dst=dst) / UDP(dport=10080) / 'Amanda'
        for i in range(count):
            send(p1, iface=iface)
            send(p2, iface=iface)
    except Exception as e:
        return str(e)

def question_refinement__scanTest(src, dst, iface, count):
    import logging
    logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
    send([IP(src=src, dst=dst)/UDP(dport=7)/'cybercop'] * count, iface=iface, verbose=0)
    send([IP(src=src, dst=dst)/UDP(dport=10080)/'Amanda'] * count, iface=iface, verbose=0)

def alternative_approaches__scanTest(src, dst, iface, count):
    from scapy.all import IP, UDP, send
    try:
        for _ in range(count):
            send(IP(src=src, dst=dst)/UDP(dport=7)/'cybercop', iface=iface)
            send(IP(src=src, dst=dst)/UDP(dport=10080)/'Amanda', iface=iface)
    except Exception as e:
        print(f'An error occurred: {e}')

def context_manager__scanTest(src, dst, iface, count):
	pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
	for _ in range(count):
		sendp(pkt, iface=iface)
	pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
	for _ in range(count):
		sendp(pkt, iface=iface)

def flipped_interaction_3__scanTest(src, dst, iface, count):
	try:
		pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / 'cybercop'
		send(pkt1, iface=iface, count=count, verbose=False)
		pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / 'Amanda'
		send(pkt2, iface=iface, count=count, verbose=False)
	except PermissionError:
		logging.error("Permission denied: You might need to run this script as an administrator.")
	except OSError as e:
		if "Interface not found" in str(e):
			logging.error(f"Network interface '{iface}' not found.")
		elif "No route to host" in str(e):
			logging.error(f"No route to host {dst}.")
		else:
			logging.error(f"OS error occurred: {e}")
	except Exception as e:
		logging.error(f"An unexpected error occurred: {e}")

def flipped_interaction_4__scanTest(src, dst, iface, count):
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
        send(pkt1, iface=iface, count=count)
        logging.info(f'Sent {count} packets from {src} to {dst} on port 7 with load cybercop')
        pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
        send(pkt2, iface=iface, count=count)
        logging.info(f'Sent {count} packets from {src} to {dst} on port 10080 with load Amanda')
    except OSError as e:
        logging.error(f'OS Error: {e}')
        print(f'OS Error: {e}')
    except PermissionError as e:
        logging.error(f'Permission Error: {e}')
        print(f'Permission Error: {e}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        print(f'An unexpected error occurred: {e}')

def flipped_interaction_5__scanTest(src, dst, iface, count):
    try:
        packet1 = IP(src=src, dst=dst) / UDP(dport=7) / "cybercop"
        for _ in range(count):
            send(packet1, iface=iface)
            print(f"Sent packet from {src} to {dst} on UDP port 7 with load 'cybercop'")
        packet2 = IP(src=src, dst=dst) / UDP(dport=10080) / "Amanda"
        for _ in range(count):
            send(packet2, iface=iface)
            print(f"Sent packet from {src} to {dst} on UDP port 10080 with load 'Amanda'")
    except Exception as e:
        print(f"An error occurred: {e}")

def iterative_prompting_3__scanTest(src, dst, iface, count):
    if not isinstance(src, str) or not isinstance(dst, str) or not isinstance(iface, str):
        raise ValueError('Source, destination, and interface must be strings')
    if not isinstance(count, int) or count < 1:
        raise ValueError('Count must be a positive integer')
    try:
        pkt1 = Ether() / IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
        sendp(pkt1, iface=iface, count=count, verbose=0)
        pkt2 = Ether() / IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
        sendp(pkt2, iface=iface, count=count, verbose=0)
    except Exception as e:
        raise RuntimeError(f'An error occurred while sending packets: {str(e)}')

def iterative_prompting_4__scanTest(src, dst, iface, count):
    try:
        if not isinstance(src, str) or not isinstance(dst, str) or not isinstance(iface, str) or not isinstance(count, int):
            raise TypeError('Invalid input types')
        if not scapy.utils.valid_ip(src) or not scapy.utils.valid_ip(dst):
            raise ValueError('Invalid IP addresses')
        if not scapy.utils.mac2str(scapy.utils.aton(iface)) or count <= 0:
            raise ValueError('Invalid interface or count value')
        send(IP(src=src, dst=dst)/UDP(dport=7)/Raw(load='cybercop'), iface=iface, count=count)
        send(IP(src=src, dst=dst)/UDP(dport=10080)/Raw(load='Amanda'), iface=iface, count=count)
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def iterative_prompting_5__scanTest(src, dst, iface, count):
    if not src or not dst or not iface:
        raise ValueError('Source, destination, and interface must be specified.')
    if not isinstance(count, int) or count <= 0:
        raise ValueError('Count must be a strictly positive integer.')
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
        pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
        for i in range(count):
            sendp(pkt1, iface=iface, verbose=0)
            sendp(pkt2, iface=iface, verbose=0)
    except Exception as e:
        print(f'An error occurred: \'{str(e)}\'')

def few_shots_prompting__scanTest(src, dst, iface, count):
	pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
	send(pkt)
	pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
	send(pkt, iface=iface, count=count)

def cot_prompting__scanTest(src, dst, iface, count):
	pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
	send(pkt)
	pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
	send(pkt, iface=iface, count=count)

def fact_check_list__scanTest(src, dst, iface, count):
	pkt_cybercop = IP(src=src, dst=dst)/UDP(dport=7)/"cybercop"
	pkt_amanda = IP(src=src, dst=dst)/UDP(dport=10080)/"Amanda"
	send(pkt_cybercop, iface=iface, count=count)
	send(pkt_amanda, iface=iface, count=count)

def not_interactive_mix__scanTest(src, dst, iface, count):
    try:
        socket.inet_pton(socket.AF_INET, src)
        socket.inet_pton(socket.AF_INET, dst)
    except socket.error:
        raise ValueError(f"Invalid IP address: {src} or {dst}")
    if not iface.replace('_', '').isalnum():
        raise ValueError("Invalid interface name")
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count should be a non-negative integer")
    for _ in range(count):
        pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
        send(pkt1, iface=iface)
    for _ in range(count):
        pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
        send(pkt2, iface=iface)

def interactive_mix__send_packets(src, dst, iface=None, count=1):
    from scapy.all import IP, UDP, Raw, send
    import ipaddress
    try:
        ipaddress.ip_address(src)
    except ValueError as e:
        raise ValueError(f"Invalid source IP address: {src}") from e
    try:
        ipaddress.ip_address(dst)
    except ValueError as e:
        raise ValueError(f"Invalid destination IP address: {dst}") from e
    if not (0 <= 7 <= 65535):
        raise ValueError("Invalid UDP destination port: 7")
    if not (0 <= 10080 <= 65535):
        raise ValueError("Invalid UDP destination port: 10080")
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
        send(pkt1, count=count, verbose=0)
        print(f"Sent {count} packet(s) from {src} to {dst} on port 7 with load 'cybercop'")
    except (OSError, PermissionError) as e:
        print(f"Error sending packet 1: {e}")
    try:
        pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
        send(pkt2, iface=iface, count=count, verbose=0)
        print(f"Sent {count} packet(s) from {src} to {dst} on port 10080 with load 'Amanda'")
    except (OSError, PermissionError) as e:
        print(f"Error sending packet 2: {e}")

def baseline__scanTest(src, dst, iface, count):
	pkt1 = IP(src=src, dst=dst)/UDP(dport=7)/Raw(load='cybercop')
	sendp(pkt1*count, iface=iface)
	pkt2 = IP(src=src, dst=dst)/UDP(dport=10080)/Raw(load='Amanda')
	sendp(pkt2*count, iface=iface)
