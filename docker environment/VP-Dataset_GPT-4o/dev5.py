from scapy.all import *

def ground_truth_code_dnsQRTest(pkt):
    if pkt.haslayer(DNSRR) and pkt.getlayer(UDP).sport == 53:
        rcode = pkt.getlayer(DNS).rcode
        qname = pkt.getlayer(DNSQR).qname
        if rcode == 3:
            return True
        else:
            return False

def persona_dnsQRTest(pkt):
    if not pkt.haslayer(DNS):
        return False
    dns_layer = pkt.getlayer(DNS)
    if dns_layer.rcode == 3:
        return True
    return False

def template_dnsQRTest(pkt):
    try:
        if pkt.haslayer('DNS') and pkt['DNS'].ancount == 0 and pkt['DNS'].rcode == 3:
            return True
        return False
    except Exception as e:
        return False

def question_refinement_dnsQRTest(pkt):
    try:
        if pkt.haslayer(DNS):
            dns_layer = pkt[DNS]
            if dns_layer.qr == 1 and dns_layer.rcode == 3:
                return True
    except Exception as e:
        print(f"An error occurred: {e}")
    return False

def alternative_approaches_dnsQRTest(pkt):
    try:
        if pkt.haslayer('DNS') and pkt[DNS].qr == 1:
            return pkt[DNS].rcode == 3
    except AttributeError:
        return False
    return False

def context_manager_dnsQRTest(pkt):
    try:
        if hasattr(pkt, 'haslayer') and pkt.haslayer('DNS'):
            dns_layer = pkt.getlayer('DNS')
            if dns_layer.rcode == 3:
                return True
        return False
    except Exception:
        return False


def flipped_interaction_3_dnsQRTest(pkt):
    if DNS in pkt and pkt[DNS].opcode == 0 and pkt[DNS].ancount == 0:
        return pkt[DNS].rcode == 3
    return False


def flipped_interaction_4_dnsQRTest(pkt):
    if pkt.haslayer(DNS):
        dns_layer = pkt.getlayer(DNS)
        if dns_layer.rcode == 3:
            return True
    return False


def flipped_interaction_5_dnsQRTest(pkt):
    try:
        if pkt.haslayer(DNS) and pkt[DNS].qr == 1 and pkt[DNS].rcode == 3:
            return True
    except Exception:
        pass
    return False

def iterative_prompting_3_dns_qr_test(pkt):
    if pkt is None:
        raise ValueError("Packet cannot be None.")
    try:
        if pkt.haslayer(DNS):
            dns_layer = pkt.getlayer(DNS)
            if dns_layer.qr == 1 and dns_layer.rcode == 3:
                return True
    except Exception as e:
        print(f"Error processing packet: {e}")
    return False

    
def iterative_prompting_4_dns_qr_test(pkt):
    if not hasattr(pkt, 'haslayer'):
        raise TypeError("Expected a Scapy packet with method 'haslayer'")
    try:
        if pkt.haslayer(DNS):
            dns_layer = pkt.getlayer(DNS)
            return dns_layer.rcode == 3
    except AttributeError:
        print("DNS layer not found in packet")
    except Exception as e:
        print(f"An error occurred while processing the packet: {e}")
    return False

def iterative_prompting_5_dns_qr_test(pkt):
    if pkt is None:
        raise ValueError("The packet cannot be None.")
    if not hasattr(pkt, 'haslayer'):
        raise TypeError("The input object must be a packet with layers.")
    try:
        if pkt.haslayer(DNS):
            if pkt[DNS].qr == 1:
                if pkt[DNS].rcode == 3:
                    return True
        return False
    except Exception as e:
        raise RuntimeError("An error occurred while processing the packet.") from e

def few_shots_prompting_dnsQRTest(pkt):
    if pkt.haslayer(DNS):
        dns_layer = pkt.getlayer(DNS)
        if dns_layer.qr == 1 and dns_layer.rcode == 3:
            return True
    return False

def cot_prompting_dnsQRTest(pkt):
    if pkt.haslayer(DNS):
        dns = pkt.getlayer(DNS)
        if dns.qr == 1 and dns.rcode == 3:
            return True
    return False

def fact_check_list_dnsQRTest(pkt):
    if pkt.haslayer(DNS):
        if pkt[DNS].qr == 1:
            if pkt[DNS].rcode == 3:
                return True
    return False

def not_interactive_mix_dnsQRTest(pkt):
    if not pkt.haslayer(DNS) or not pkt.haslayer(DNSQR):
        return False
    dns_layer = pkt.getlayer(DNS)
    return dns_layer.rcode == 3

def interactive_mix_check_dns_rcode_3(pkt):
    try:
        if pkt.haslayer(DNS):
            dns_layer = pkt.getlayer(DNS)
            if isinstance(dns_layer.rcode, int):
                if dns_layer.rcode == 3:
                    return True
                else:
                    return False
            else:
                return None
        else:
            return None
    except Exception as e:
        return None

def baseline_dnsQRTest(pkt):
    if pkt.haslayer(DNS):
        dns_layer = pkt.getlayer(DNS)
        return dns_layer.rcode == 3
    return False

