import socket
from scapy.all import IP, UDP, send, sendp, Raw, RandShort, conf
from scapy.error import Scapy_Exception 
from scapy.layers.l2 import Ether

def ground_truth_code_scanTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    send(pkt)
    pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    send(pkt, iface=iface, count=count)

def persona_scanTest(src, dst, iface, count):
    from scapy.all import IP, UDP, send
    pkt = IP(src=src, dst=dst, ttl=30)/UDP(dport=7)/'cybercop'
    send(pkt, iface=iface, count=count)
    pkt = IP(src=src, dst=dst, ttl=30)/UDP(dport=10080)/'Amanda'
    send(pkt, iface=iface, count=count)
    
def template_scanTest(src, dst, iface, count):
    import scapy.all as scapy
    try:
        packet1 = scapy.IP(src=src, dst=dst)/scapy.UDP(dport=7)/scapy.Raw('cybercop')
        packet2 = scapy.IP(src=src, dst=dst)/scapy.UDP(dport=10080)/scapy.Raw('Amanda')
        scapy.send(packet1, iface=iface, count=count, verbose=False)
        scapy.send(packet2, iface=iface, count=count, verbose=False)
    except scapy.Scapy_Exception as e:
        raise(f"Error occurred: {e}")
        
def question_refinement_scanTest(src_ip, dst_ip, payload, interface):
	from scapy.all import IP, TCP, Raw, send
	src_ip = str(src_ip)
	dst_ip = str(dst_ip)
	interface = str(interface)
	response = send(IP(src=src_ip, dst=dst_ip)/TCP()/Raw(load=payload), iface=interface, verbose=0)
	if response.sent == 1:
		print('Packet sent successfully.\n')
	else:
		print('Failed to send the packet.\n')
	return response

def alternative_approaches_scanTest(src, dst, iface, count):
    from scapy.all import IP, UDP, Raw, send
    try:
        pkt = IP(src=src, dst=dst)/UDP(dport=7)/Raw(load='cybercop')
        send(pkt, count=count, iface=iface)
        pkt = IP(src=src, dst=dst)/UDP(dport=10080)/Raw(load='Amanda')
        send(pkt, count=count, iface=iface)
    except Exception as e:
        print('An error occurred:'+ str(e))
        
def context_manager_scanTest(src, dst, iface, count):
    from scapy.all import IP, UDP, send, Raw, Packet
    packet_1 = IP(src=src, dst=dst)/UDP(dport=7)/Raw(load='cybercop')
    packet_2 = IP(src=src, dst=dst)/UDP(dport=10080)/Raw(load='Amanda')
    send(packet_1, iface=iface, count=count)
    send(packet_2, iface=iface, count=count)
    
def flipped_interaction_3__scanTest(src, dst, iface, count):
    send(IP(src=src, dst=dst)/UDP(dport=7)/Raw('cybercop'))
    send(IP(src=src, dst=dst)/UDP(dport=10080)/Raw('Amanda'), iface=iface)
    
def flipped_interaction_4__scanTest(src, dst, iface, load, dport, count):
	pkt = IP(src=src, dst=dst)/UDP(dport=dport)/Raw(load=load)
	if count > 0:
		send(pkt, count=count, iface=iface, verbose=0)
	else:
		send(pkt, iface=iface, verbose=0)

def flipped_interaction_5__scanTest(src, dst, iface, count):
    packet1 = IP(src=src, dst=dst)/UDP(dport=7)/Raw(load='cybercop')
    send(packet1, verbose=False)
    packet2 = IP(src=src, dst=dst)/UDP(dport=10080)/Raw(load='Amanda')
    send(packet2, count=count, iface=iface, verbose=False)
    
import importlib.metadata as importlib_metadata
scapy_version = importlib_metadata.version('scapy')
def iterative_prompting_3__scanTest(src, dst, iface, count):
    if scapy_version < '2.4.5':
        raise RuntimeError('Scapy version 2.4.5 or later is required')
    from scapy.all import IP, UDP, Raw, send
    if not isinstance(src, str) or not isinstance(dst, str):
        raise TypeError('Source and destination must be strings')
    try:
        IP(src=src)
        IP(dst=dst)
    except ValueError:
        raise ValueError('Invalid source or destination IP address')
    if not isinstance(iface, str):
        raise TypeError('Interface must be a string')
    if not isinstance(count, int) or count <= 0:
        raise ValueError('Count must be a positive integer value but not zero, i.e., count > 0')
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load=b'cybercop')
        pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load=b'Amanda')
        send(pkt1,iface=iface,count=count,verbose=0)
        send(pkt2,iface=iface,count=count,verbose=0)
    except Exception as e:
       raise RuntimeError(f'Failed to send packets: {str(e)}')
   
def iterative_prompting_4__scanTest(src: str, dst: str, iface: str, count: int) -> None:
    if not (isinstance(src, str) and isinstance(dst, str) and isinstance(iface, str)):
        raise TypeError('src, dst, and iface must be strings')
    if not isinstance(count, int) or count <= 0:
        raise ValueError('count must be a positive integer')
    try:
        packet1 = IP(src=src, dst=dst)/UDP(dport=7)/Raw(load=b'\x63\x79\x62\x65\x72\x63\x6f\x70')
        packet2 = IP(src=src, dst=dst)/UDP(dport=10080)/Raw(load=b'\x41\x6d\x61\x6e\x64\x61')
        packet1.display()
        packet2.display()
        if conf.L2listen is False:
            send(packet1, iface=iface, count=count, verbose=False)
            send(packet2, iface=iface, count=count, verbose=False)
    except Scapy_Exception as e:
        print(f'A Scapy error occurred: {e.__str__()}')
    except Exception as e:
        print(f'An error occurred: {e.__str__()}')
        
def iterative_prompting_5__scanTest(src, dst, iface, count):
    import scapy.all as scapy
    if not scapy.__version__ >= '2.4.5':
        raise ValueError('Please update scapy library to version 2.4.5 or above')
    if not isinstance(src, str) or not isinstance(dst, str):
        raise ValueError('Source and destination must be strings')
    if not isinstance(iface, str):
        raise ValueError('Interface must be a string')
    if not isinstance(count, int) or count < 1:
        raise ValueError('Count must be a positive integer')
    src_ip = scapy.IPAddress(src)
    dst_ip = scapy.IPAddress(dst)
    if not src_ip.is_global or not dst_ip.is_global:
        raise ValueError('Source and destination IP addresses must be public')
    try:
        scapy.iface = iface
    except OSError:
        raise ValueError('Invalid interface')
    pkt1 = scapy.IP(src=src, dst=dst) / scapy.UDP(dport=7) / scapy.Raw(load=b'cybercop\x00\x00\x00\x00')
    pkt2 = scapy.IP(src=src, dst=dst) / scapy.UDP(dport=10080) / scapy.Raw(load=b'Amanda\x00\x00\x00\x00\x00\x00\x00\x00')
    try:
        scapy.send(pkt1, count=count, verbose=0, inter=0.1, retry=2)
        scapy.send(pkt2, count=count, verbose=0, inter=0.1, retry=2)
    except scapy.Scapy_Exception as e:
        raise ValueError('Scapy error:'+ str(e))
    except Exception as e:
        raise ValueError('Failed to send packets:'+ str(e))
    
def few_shots_prompting_scanTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    send(pkt)
    pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    send(pkt, iface=iface, count=count)
    
def cot_prompting_scanTest(src, dst, iface, count):
	bpkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
	send(bpkt)
	pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
	send(pkt, iface=iface, count=count)
     
def fact_check_listscanTest(src, dst, iface, count):
	try:
		pkt1 = IP(src=src, dst=dst)/UDP(dport=7)/Raw(load='cybercop')
		pkt2 = IP(src=src, dst=dst)/UDP(dport=10080)/Raw(load='Amanda')
		send(pkt1, iface=iface, count=count, verbose=0)
		send(pkt2, iface=iface, count=count, verbose=0)
	except Exception as e:
		print(f'An error occurred: {e}')
          
def not_interactive_mix_scanTest(src, dst, iface, count):
    if not isinstance(src, str) or not isinstance(dst, str):
        raise ValueError("Source and destination IP addresses must be strings")
    if not isinstance(count, int):
        raise ValueError("Count must be an integer")
    try:
        count = int(count)
    except ValueError:
        raise ValueError("Count must be a positive integer")
    if count <= 0:
        raise ValueError("Count must be a positive integer")
    pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    try:
        send(pkt1, iface=iface, count=count)
    except Exception as e:
        print(f"Error sending packet 1: {e}")
    pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    try:
        send(pkt2, iface=iface, count=count)
    except Exception as e:
        print(f"Error sending packet 2: {e}")
        
import logging
from scapy.all import IP, UDP, Raw, send
def interactive_mix_sendPackets(src, dst, iface, count=1, verbose=False):
    try:
        if not isinstance(count, int) or count < 0:
            raise ValueError('Invalid count value')
        if not isinstance(iface, str):
            raise ValueError('Invalid interface value')
        import ipaddress
        try:
            ipaddress.ip_address(src)
            ipaddress.ip_address(dst)
        except ValueError:
            raise ValueError('Invalid IP address')
        pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
        send(pkt1, iface=iface, verbose=verbose)
        pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
        send(pkt2, iface=iface, count=count, verbose=verbose)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        
def baseline_scanTest(src, dst, iface, count):
    from scapy.all import IP, UDP, send
    udp = UDP(dport=7)
    ip = IP(src=src, dst=dst)
    pkt = ip / udp / 'cybercop'
    send(pkt, iface=iface)
    
    udp = UDP(dport=10080)
    ip = IP(src=src, dst=dst)
    pkt = ip / udp / 'Amanda'
    send(pkt, iface=iface)

