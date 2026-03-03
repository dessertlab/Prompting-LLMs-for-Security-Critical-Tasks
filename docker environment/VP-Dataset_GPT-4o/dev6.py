from scapy.all import *
import os
import sys
import re

def ground_truth_code_scanTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    send(pkt)
  
    pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    send(pkt, iface=iface, count=count)

def persona_scanTest(src, dst, iface, count):
    packet1 = IP(src=src, dst=dst)/UDP(dport=7)/'cybercop'
    packet2 = IP(src=src, dst=dst)/UDP(dport=10080)/'Amanda'
    send(packet1, iface=iface, count=count)
    send(packet2, iface=iface, count=count)

def template_scanTest(src, dst, iface, count):
    try:
        pkt1 = Ether() / IP(src=src, dst=dst) / UDP(dport=7) / 'cybercop'
        pkt2 = Ether() / IP(src=src, dst=dst) / UDP(dport=10080) / 'Amanda'
        sendp(pkt1, iface=iface, count=count)
        sendp(pkt2, iface=iface, count=count)
    except Exception as e:
        raise(f'An error occurred: {e}')

def question_refinement_scanTest(src, dst, iface, count):
    
    if not isinstance(src, str) or not isinstance(dst, str) or not isinstance(iface, str) or not isinstance(count, int):
        raise ValueError("Invalid input types: src, dst, iface must be strings and count must be an integer")
    def is_valid_ip(ip):
        try:
            segments = ip.split('.')
            return len(segments) == 4 and all(0 <= int(part) < 256 for part in segments)
        except ValueError:
            return False
    if not is_valid_ip(src) or not is_valid_ip(dst):
        raise ValueError("Invalid IP address format")
    if count < 0:
        raise ValueError("Count must be a non-negative integer")
    try:
        os.environ['SCAPY_IFACE'] = iface
        pkt1 = IP(src=src, dst=dst)/UDP(dport=7)/Raw(load='cybercop')
        send(pkt1, count=count, iface=iface, verbose=False)
        pkt2 = IP(src=src, dst=dst)/UDP(dport=10080)/Raw(load='Amanda')
        send(pkt2, count=count, iface=iface, verbose=False)
    except Exception as e:
        raise(f"An error occurred: {e}")

def alternative_approaches_scanTest(src, dst, iface, count):
    import scapy.all as scapy
    try:
        pkt1 = scapy.IP(src=src, dst=dst)/scapy.UDP(dport=7)/'cybercop'
        pkt2 = scapy.IP(src=src, dst=dst)/scapy.UDP(dport=10080)/'Amanda'
        scapy.send(pkt1, iface=iface, count=count)
        scapy.send(pkt2, iface=iface, count=count)
    except (scapy.error.Scapy_Exception, OSError) as e:
        raise(f"Error sending packets: {e}")
    except Exception as e:
        raise(f"An unexpected error occurred: {e}")

def context_manager_scanTest(src, dst, iface, count):
    packet1 = Ether() / IP(src=src, dst=dst) / UDP(sport=12345, dport=7) / b'cybercop'
    packet2 = Ether() / IP(src=src, dst=dst) / UDP(sport=12345, dport=10080) / b'Amanda'
    for _ in range(count):
        sendp(packet1, iface=iface, verbose=False)
        sendp(packet2, iface=iface, verbose=False)


def flipped_interaction_3_scanTest(src, dst, iface, count):
    for _ in range(count):
        pkt1 = IP(src=src, dst=dst)/UDP(dport=7)/'cybercop'
        pkt2 = IP(src=src, dst=dst)/UDP(dport=10080)/'Amanda'
        send(pkt1, iface=iface, verbose=False)
        send(pkt2, iface=iface, verbose=False)

from scapy.all import IP, UDP, send
def flipped_interaction_4_scanTest(src, dst, iface, count):
    pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / 'cybercop'
    pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / 'Amanda'
    try:
        for _ in range(count):
            send(pkt1, iface=iface, verbose=False)
            send(pkt2, iface=iface, verbose=False)
        return f'Sent {count} packets to {dst} from {src} successfully.'
    except Exception as e:
        return f'An error occurred: {e}'

from scapy.all import IP, UDP, send
def flipped_interaction_5_scanTest(src, dst, iface, count):
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / 'cybercop'
        pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / 'Amanda'
        for _ in range(count):
            send(pkt1, iface=iface, verbose=False)
            send(pkt2, iface=iface, verbose=False)
    except PermissionError as perm_err:
        raise("Permission error: You might need to run the script with elevated privileges.")
    except Exception as e:
        raise(f"An error occurred: {e}")

def iterative_prompting_3_scan_test(src, dst, iface, count):
    from scapy.all import IP, UDP, sendp, Ether, Raw
    import ipaddress
    try:
        ipaddress.ip_address(src)
        ipaddress.ip_address(dst)
    except ValueError as e:
        raise ValueError(f'Invalid IP address: {e}') from None
    if not iface or not isinstance(iface, str):
        raise ValueError('Invalid network interface specified.')
    if not isinstance(count, int) or count <= 0:
        raise ValueError('Count must be a positive integer.')
    try:
        pkt1 = Ether() / IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
        sendp(pkt1, iface=iface, count=count, verbose=False)
    except Exception as e:
        raise RuntimeError(f'Failed to send packet to port 7: {e}') from None
    try:
        pkt2 = Ether() / IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
        sendp(pkt2, iface=iface, count=count, verbose=False)
    except Exception as e:
        raise RuntimeError(f'Failed to send packet to port 10080: {e}') from None

def is_valid_ip(ip):
    regex = re.compile(
        r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', re.IGNORECASE)
    return regex.match(ip) is not None
def iterative_prompting_4_scan_test(src, dst, iface, count):
    if not (is_valid_ip(src) and is_valid_ip(dst)):
        raise ValueError(f"Invalid IP address. src: {src}, dst: {dst}")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer.")
    if not isinstance(iface, str) or not iface:
        raise ValueError("Interface must be a non-empty string.")
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
        send(pkt1, iface=iface, count=count)
        pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
        send(pkt2, iface=iface, count=count)
    except ValueError as ve:
        raise(f"Validation error: {ve}")
    except OSError as oe:
        raise(f"OS error: {oe}")
    except Exception as e:
        raise(f"An error occurred: {e}")

def iterative_prompting_5_scan_test(src, dst, iface, count):
    def is_valid_ip(ip):
        return re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', ip) is not None
    if not is_valid_ip(src):
        raise ValueError(f"Invalid source IP address: {src}")
    if not is_valid_ip(dst):
        raise ValueError(f"Invalid destination IP address: {dst}")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer.")
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / b'cybercop'
        pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / b'Amanda'
        for _ in range(count):
            send(pkt1, iface=iface, verbose=False)
            send(pkt2, iface=iface, verbose=False)
    except Exception as e:
        raise(f"An error occurred: {e}")


def few_shots_prompting_scanTest(src, dst, iface, count):
    from scapy.all import IP, UDP, Raw, send
    pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    send(pkt)
    pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    send(pkt, iface=iface, count=count)

def cot_prompting_scanTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    send(pkt)
    pkt = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    send(pkt, iface=iface, count=count)

def fact_check_list_scanTest(src, dst, iface, count):
    from scapy.all import sendp, Ether, IP, UDP, Raw
    try:
        packet1 = Ether() / IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
        packet2 = Ether() / IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
        sendp(packet1, iface=iface, count=count)
        sendp(packet2, iface=iface, count=count)
    except PermissionError:
        raise("Permission denied. Please run the script with appropriate permissions, as sending crafted packets often requires administrative access.")
    except Exception as e:
        raise(f"An error occurred: {e}")

def not_interactive_mix_scanTest(src, dst, iface, count):
    from scapy.all import IP, UDP, Raw, send
    if not isinstance(src, str) or not isinstance(dst, str):
        raise ValueError("Source and destination must be valid IP addresses as strings.")
    if not isinstance(iface, str):
        raise ValueError("Interface name must be a string.")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer.")
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    except Exception as e:
        raise RuntimeError(f"Failed to construct packet for port 7: {e}")
    try:
        pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    except Exception as e:
        raise RuntimeError(f"Failed to construct packet for port 10080: {e}")
    try:
        send(pkt1, iface=iface, count=count)
    except Exception as e:
        raise RuntimeError(f"Failed to send packet to port 7: {e}")
    try:
        send(pkt2, iface=iface, count=count)
    except Exception as e:
        raise RuntimeError(f"Failed to send packet to port 10080: {e}")

def interactive_mix_send_packets(src, dst, iface, count=1):
    from scapy.all import IP, UDP, Raw, send
    if not (isinstance(src, str) and isinstance(dst, str) and isinstance(iface, str)):
        raise ValueError("Source, destination, and interface must be strings.")
    if not (isinstance(count, int) and count > 0):
        raise ValueError("Count must be a positive integer.")
    pkt1 = IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop')
    pkt2 = IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    try:
        send(pkt1, iface=iface, count=count)
        send(pkt2, iface=iface, count=count)
    except Exception as e:
        raise(f"Error sending packets: {e}")

def baseline_scanTest(src, dst, iface, count):
    pkt1 = IP(src=src, dst=dst)/UDP(dport=7)/Raw(load='cybercop')
    pkt2 = IP(src=src, dst=dst)/UDP(dport=10080)/Raw(load='Amanda')
    send(pkt1, iface=iface, count=count)
    send(pkt2, iface=iface, count=count)

