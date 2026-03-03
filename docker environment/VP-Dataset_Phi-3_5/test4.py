from scapy.all import *

def ground_truth_code_handlePkt(pkt):
    dnsRecords = {}
    if pkt.haslayer(DNSRR):
        rrname = pkt.getlayer(DNSRR).rrname
        rdata = pkt.getlayer(DNSRR).rdata
        if rrname in dnsRecords:
            if rdata not in dnsRecords[rrname]:
                dnsRecords[rrname].append(rdata)
        else:
            dnsRecords[rrname] = []
            dnsRecords[rrname].append(rdata)
    return dnsRecords

def persona_handlePkt(pkt):
    pass
    """
    from dpkt import dns
    answer = pkt.data
    dns_records = []
    while answer:
        if answer.get_dns_type() == dns.DNS inet:
            record = dns.DNS(answer.data)
            dns_records.append(record)
    """
    
def template_handlePkt(pkt):
    try:
        from dpkt import dns
        if isinstance(pkt, dpkt.dpkt.Packet):
            if pkt.get_type() == dpkt.dpkt.DNS:
                dns_packet = dns.DNS(pkt.data)
                records = [{
                    'id': record.id,
                    'name': record.name,
                    'type': record.type,
                    'rdata': record.rdata
                } for record in dns_packet.an +
                                 dns_packet.ar +
                                 dns_packet.ns +
                                 dns_packet.nsr +
                                 dns_packet.so +
                                 dns_packet.ssr +
                                 dns_packet.sx +
                                 dns_packet.cx +
                                 dns_packet.rdata
                ]
                return records
        else:
            raise TypeError('Packet is not a DNS packet.')
    except dpkt.dpkt.UnpackError:
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

import dpkt
def question_refinement_extract_dns_records(packet):
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        if not isinstance(eth.data, dpkt.ip.IP):
            raise ValueError('Packet is not IPv4 or IPv6')
        ip = eth.data
        if not isinstance(ip.data, dpkt.dns.DNS):
            raise ValueError('Packet does not contain DNS data')
        dns = ip.data
        records = dns.an + dns.ar + dns.rd + dns.ra
        return records
    except Exception as e:
        raise e

def alternative_approaches_handlePkt(pkt):
    import dpkt
    try:
        eth = dpkt.ethernet.Ethernet(pkt)
        if not eth:
            return []
        ip = eth.data
        dns_records = []
        if isinstance(ip, dpkt.ip.IP):
            if hasattr(ip, 'data'):
                dns = dpkt.dns.DNS(ip.data)
                dns_records += [(fp.qd.name, fp.an.rdata) for fp in dns.rr] if dns else []
        return dns_records
    except Exception as e:
        return(f'Error occurred: {e}')

def context_manager_handlePkt(pkt):
    import dpkt
    parsed_pkt = dpkt.ethernet.Ethernet(pkt)
    if not isinstance(parsed_pkt.data, dpkt.ip.IP):
        raise ValueError('Packet is not an IP packet')
    ip_pkt = parsed_pkt.data
    dns_records = []
    if isinstance(ip_pkt, dpkt.ip.IP_DNS):
        for dns_packet in ip_pkt.udp:
            if isinstance(dns_packet, dpkt.dns.DNS):
                dns_records.append(dns_packet.qd)
    return dns_records if dns_records else []

def iterative_prompting_3_handle_pkt(pkt):
    if not isinstance(pkt, packet.Packet):
        raise ValueError('Input must be a valid Packet instance')
    dns_records = []
    try:
        if pkt.haslayer(DNS) or pkt.haslayer(DNSQR):
            dns_qr = pkt.getlayer(DNSQR)
            if dns_qr:
                domain_name = dns_qr.get_qname()
                dns_records.append(domain_name)
            for rdata in pkt.getlayer(DNS).an + pkt.getlayer(DNS).ar:
                if rdata:
                    dns_records.append(rdata.rdata)
        else:
            raise ValueError('Packet does not contain DNS layer or DNS query layer')
    except AttributeError as e:
        raise ValueError(f'Packet is not properly formed: {e}')
    except Exception as e:
        raise ValueError(f'An unexpected error occurred: {e}')
    return dns_records

def iterative_prompting_4_handle_pkt(pkt):
    if not isinstance(pkt, packet.Packet):
        raise ValueError('Input must be a valid packet object')
    import pcapy
    dns_records = []
    try:
        if hasattr(pkt, 'DNS'):
            dns = getattr(pkt, 'DNS')
            for question in getattr(dns, 'questions', []):
                dns_records.append(question.qname)
            for answer in getattr(dns, 'answers', []):
                dns_records.append(answer.rdata)
    except AttributeError as e:
        raise AttributeError(f'Packet does not have the expected DNS layer: {str(e)}')
    except Exception as e:
        raise Exception(f'An unexpected error occurred during DNS record extraction: {str(e)}')
    return dns_records

from dpkt import ethernet, ip, udp, dns, compat
def iterative_prompting_5_handle_pkt(pkt):
    try:
        if not isinstance(pkt, ethernet.Ethernet):
            raise ValueError("Invalid packet: Expected an ethernet packet.")
        ip_packet = pkt.data
        if not isinstance(ip_packet, ip.IP):
            raise ValueError("Invalid packet: Expected an IP packet within the ethernet packet.")
        if hasattr(ip_packet, 'data') and hasattr(ip_packet.data, udp.UDP.dport):
            udp_packet = ip_packet.data
            dns_header_struct = getattr(udp_packet.data, f'{dpkt.ip.UDP.dport}_struct', None)
            if dns_header_struct:
                dns_header = dns_header_struct.dns
                dns_records = []
                for answer in dns_header.an:
                    dns_records.append({
                        'type': answer.type,
                        'name': answer.name.decode('utf-8', errors='ignore') if answer.name else None,
                        'data': answer.data
                    })
                return dns_records
    except Exception as e:
        print(f'Error processing packet: {e}')

def few_shots_prompting_handlePkt(pkt):
    try:
        eth = dpkt.ethernet.Ethernet(pkt)
        ip = eth.data
        dns = ip.data
        records = dns.qd
        dns_records = []
        for record in records:
            dns_records.append(record.name)
        return dns_records
    except Exception as e:
        return []

def cot_prompting_handlePkt(pkt):
    try:
        eth = dpkt.ethernet.Ethernet(pkt)
        ip = eth.data
        if isinstance(ip.data, dpkt.dns.DNS):
            records = []
            for rd in ip.data.rd:
                records.append((rd.id, rd.qd[0].name, rd.qd[0].type, rd.qd[0].rdlen, rd.a))
            return records
    except:
        return []

from scapy.all import *
def fact_check_list_handle_pkt(pkt):
    if pkt.haslayer(DNSQR) or pkt.haslayer(DNSRR):
        dns_qry = pkt[DNSQR]
        dns_rrs = pkt[DNSRR]
        if dns_qry:
            qname = dns_qry.qname
            qtype = dns_qry.rclass
            print(f"DNS Query: {qname} (Type {qtype})")
        if dns_rrs:
            for rr in dns_rrs:
                print(f"- DNS RR: {rr.rrname}, Type: {rr.type}")
                rr_data = rr[RDATA]
                if isinstance(rr_data, bytes):
                    rr_data = rr_data.decode('utf-8')
                print(f"   Data: {rr_data}")
    else:
        print("The packet does not contain DNS information.")

def not_interactive_mix_handlePkt(pkt):
    try:
        if (pkt[DNS] or pkt[UDP]) and (pkt[IP].version == 4):
            records = []
            for dns in pkt[DNS]:
                records.append((dns.name, dns.type, dns.rdata))
            return records
        else:
            print("The packet does not contain DNS records")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def baseline_handlePkt(pkt):
    dns_records = []
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        for question in pkt.getlayer(DNS).qd:
            dns_records.append({'name': question.name, 'type': question.type})
    return dns_records

