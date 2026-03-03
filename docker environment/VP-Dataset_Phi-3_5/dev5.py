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
    try:
        response = dns.query.udp(pkt.get_header(), pkt.get_payload())
        return response.rcode() == 3
    except:
        return False
def template_dnsQRTest(pkt):
    try:
        if 'DNS QR' in pkt and pkt['DNS QR'] == (3, 0):
            return True
        else:
            return False
    except KeyError:
        raise ValueError('Packet is missing DNS QR field')

def question_refinement_dnsQRTest(packet):
    qr = packet.get('DNS_QUERY', {}).get('QR', 0)
    return qr == 3

def alternative_approaches_dnsQRTest(pkt):
    try:
        dns_response = pkt[DNS].qr
        rcode = dns_response.rcode
        return rcode == 3
    except Exception as e:
        print(f'Error occurred: {e}')
        return False

def context_manager_dnsQRTest(pkt):
    import dpkt
    try:
        tcp = pkt[dpkt.tcp.TH_SYN]
        if tcp:
            dns = tcp.data
            tcp_header = dpkt.ip.IP(dns)
            return tcp_header.tos & 0xC0 == 0xC0 and tcp_header.doff == 5
    except:
        return False
        
def iterative_prompting_3_dnsQRTest(pkt):
    try:
        dns_queries = pkt.get('DNS Queries')
        if dns_queries is None:
            raise ValueError('Missing DNS Queries key in packet')
        return isinstance(dns_queries, str) and dns_queries == 'rcode 3'
    except (TypeError, ValueError) as e:
        print(f'Error: {e}')
        return False

def iterative_prompting_4_dnsQRTest(pkt):
    try:
        if not hasattr(pkt, 'rcode'):
            raise ValueError('The provided object does not have an rcode attribute.')
        return pkt.rcode == 3
    except ValueError as ve:
        raise ValueError(f'Specific error: {ve}')
    except TypeError as te:
        raise TypeError(f'Specific error: {te}')
    except AttributeError:
        raise AttributeError('The provided object does not have an rcode attribute')
    except Exception as e:
        raise Exception(f'An unexpected error occurred: {e}')

import dns.rcode
from dns import resolver, exception
def iterative_prompting_5_dnsQRTest(pkt):
    try:
        if not pkt:
            raise ValueError("The packet (pkt) is not provided/valid.")
        if not hasattr(resolver, 'Resolver') or resolver.get_default_resolver() is None:
            raise RuntimeError("The dns resolver dependencies are not properly set up or updated.")
        rrset = pkt.get_rrset('a', 0, resolver.rdatatype.QR, resolver.rcode.NOERROR)
        if rrset is None:
            raise ValueError("No RRset found for the given parameters.")
        return rrset.rcode == dns.rcode.NOERROR
    except exception.DNSException as e:
        print(f"DNS query error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")

def few_shots_prompting_dnsQRTest(pkt):
    try:
        eth = dpkt.ethernet.Ethernet(pkt)
        ip = eth.data
        udp = ip.data
        dport = udp.dport
        if dport == 53:
            qr = udp.qr
            opcode = udp.opcode
            return 3 == qr and opcode == dpkt.dns.DNS_QUERY
    except:
        return False
        
def cot_prompting_dnsQRTest(pkt):
    dns = pkt[DNS]
    if dns:
        for question in dns.questions:
            rcode = question.rcode
            if rcode == 3:
                pass

def fact_check_list_dnsQRTest(pkt):
    if IP in pkt and DNS in pkt[IP]:
        query_rcode = pkt[IP][DNS].rcode()
        return query_rcode == 3
    return False

def not_interactive_mix_dnsQRTest(pkt):
    if IP in pkt and UDP in pkt and DNSQR in pkt:
        if pkt[DNSQR].rcode() == 3:
            return True
    return False

def baseline_dnsQRTest(pkt):
    return pkt.get('DNSQR').rcode == 3

