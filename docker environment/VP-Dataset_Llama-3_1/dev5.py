import scapy
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
    from scapy.all import DNSRR, DNS
    if pkt.haslayer(DNSRR):
        for rr in pkt[DNSRR]:
            if rr.rclass == 3:
                return True
    elif pkt.haslayer(DNS):
        if pkt[DNS].rcode == 3:
            return True
    return False


def template_dnsQRTest(pkt):
    try:
        if hasattr(pkt, 'qr'):
            return True
        else:
            return False
    except Exception as e:
        print(f'An error occurred: {e}')
        return False


def question_refinement_dnsQRTest(packet):
    try:
        dns_pkt = DNS(packet)
        rcode = dns_pkt[DNS].ancount
        for rr in dns_pkt[DNSRR]:
            if rr.rrname.decode('utf-8') == dns_pkt[DNS].qd.qname.decode('utf-8') and rr.type == 5:
                if rr.rdata.decode('utf-8') == '':
                    dns_pkt.show()
                    return True
                else:
                    return {'rcode': 0, 'message': 'Success', 'status': 'ok'}
        if dns_pkt[DNS].rcode == 3:
            return {'rcode': 3, 'message': 'No such name', 'status': 'ko'}
        else:
            return {'rcode': 0, 'message': 'Success', 'status': 'ok'}
    except Exception as e:
        return {'rcode': -1, 'message': str(e), 'status': 'ko'}


def alternative_approaches_dnsQRTest(pkt):
    try:
        if pkt.haslayer('DNS'):
            if pkt['DNS'].ancount > 0:
                if pkt['DNS'].an.rcode == 3:
                    return True
                return False
            return False
        return False
    except Exception as e:
        print(f'An error occurred: {e}')
        return False


def context_manager_dnsQRTest(pkt):
    if pkt.haslayer('DNS') and pkt.getlayer('DNS').ancount > 0:
        for answer in pkt.getlayer('DNS').an:
            if answer.type == 5 or answer.type == 12 or answer.type == 2:
                return 'Unicast Response faraway'
            if answer.type == 1:
                return 'rcode faraway'
        if pkt.getlayer('DNS').rcode == 3:
            return True
    return False


def flipped_interaction_3__dnsQRTest(pkt):
    if pkt.qr == 1 and pkt.ancount > 0 and pkt.an[0].type == 5 and pkt.an[0].rcode == 3:
        return True
    return False


def flipped_interaction_4__dnsQRTest(pkt):
    return pkt.haslayer(DNSRR) and pkt.getlayer(DNS).ancount == 0 and pkt.getlayer(DNS).rcode == 3


def flipped_interaction_5__dnsQRTest(pkt):
    if pkt.haslayer(scapy.DNSRR) and pkt.getlayer(scapy.UDP).sport == 53:
        if pkt.haslayer(scapy.DNSQR):
            if pkt.getlayer(scapy.DNSRR).ancount >= 1 and pkt.getlayer(scapy.DNSRR).rcode == 3:
                return True
    return False


def iterative_prompting_3__dnsQRTest(pkt):
    if not pkt:
        return False
    try:
        if pkt.haslayer(DNS):
            dns_ans = pkt.getlayer(DNS)
            if hasattr(dns_ans, 'ancount') and dns_ans.ancount > 0 and hasattr(dns_ans.an, 'rcode') and hasattr(dns_ans.an, 'rdata'):
                if dns_ans.an.rdata == "\x00\x00\x00\x00" and dns_ans.an.rcode == 3:
                    return True
    except Exception as e:
        import logging
        logging.error(f"An error occurred: {e}")
    return False


def iterative_prompting_4__dnsQRTest(pkt):
    if not isinstance(pkt, scapy.packet.Packet):
        return False
    try:
        if pkt.haslayer(scapy.layers.dns.DNS) and pkt[scapy.layers.dns.DNS].ancount > 0:
            if pkt[scapy.layers.dns.DNS].ancount > 0 and len(pkt[scapy.layers.dns.DNSRR]) > 0 and pkt[scapy.layers.dns.DNSRR][0].haslayer(scapy.layers.dns.DNSRR):
                dns_rr = pkt[scapy.layers.dns.DNSRR][0]
                if dns_rr.type == 5 and dns_rr.rcode == 3 and all(isinstance(x, int) for x in [dns_rr.type, dns_rr.rcode]):
                    return True
        return False
    except (IndexError, AttributeError, TypeError):
        return False


def iterative_prompting_5__dnsQRTest(pkt):
    if not isinstance(pkt, object):
        raise TypeError('Input must be a valid packet object')
    try:
        dns_layer = pkt.getlayer('DNS')
    except:
        return False
    if dns_layer and getattr(dns_layer, 'ancount', None) == 1:
        try:
            dnsrr_layer = pkt.getlayer('DNSRR')
        except:
            return False
        if dnsrr_layer and getattr(dnsrr_layer, 'type', None) == 5 and getattr(dnsrr_layer, 'rcode', None) == 3:
            return True
    return False


def few_shots_prompting_dnsQRTest(pkt):
    if pkt.haslayer(scapy.dns.DNS):
        rcode = pkt.getlayer(scapy.dns.DNS).rcode
        if rcode == 3:
            return True
    return False


def cot_prompting_dnsQRTest(pkt):
    if pkt.haslayer(DNS):
        if pkt.getlayer(DNS).ancount > 0:
            for answer in pkt.getlayer(DNS).an:
                if answer.type == 5:
                    if answer.ttl == 0 and answer.rdlen == 0:
                        return True
                if answer.type == 2:
                    if answer.ttl == 0 and answer.rdlen == 0 and answer.rdata.startswith(" Mail server answer: 0 IP address RR for MX is Unknown Type "):
                        return True
    return False


def fact_check_list_dnsQRTest(pkt):
    if pkt.haslayer(DNS):
        dns_layer = pkt.getlayer(DNS)
        if dns_layer.ancount > 0 and hasattr(dns_layer, 'qd') and hasattr(dns_layer, 'an') and dns_layer.an.rdata == dns_layer.qd.qname:
            return True
    return False


def not_interactve_mix_dnsQRTest(pkt):
    try:
        if pkt.__class__.__name__ == 'DNS':
            rcode = getattr(pkt, 'rcode', None)
            if rcode == 3:
                return True
            else:
                return False
        else:
            raise TypeError("The packet is not a DNS packet.")
    except AttributeError:
        print("The packet does not have a 'rcode' attribute.")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


from scapy.layers.dns import DNS
from scapy.layers.inet import UDP
from scapy.packet import Packet

def interactive_mix_dnsQRTest(pkt):
    if not isinstance(pkt, Packet):
        raise TypeError('Invalid packet type')
    if pkt.haslayer(UDP) and pkt.getlayer(UDP).sport == 53:
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).rcode == 3:
            return True
    return False


def baseline_dnsQRTest(pkt):
    if pkt.haslayer(DNS):
        if pkt.getlayer(DNS).ancount > 0:
            pkt.getlayer(DNSRR)[0].type
            pkt.getlayer(DNSRR)[0].rdata
        return True
    return False

