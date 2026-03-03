import scapy
from scapy.all import IP, UDP, DNS, DNSQR, DNSRR
import dns.message
from dns import *

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
	if pkt.haslayer(DNS):
		dns_records = []
		for i in range(pkt[DNS].ancount):
			dns_records.append(pkt[DNS].an[i].rdata)
		return dns_records
	else:
		return []
      
def template_handlePkt(pkt):
    try:
        if pkt.haslayer('DNS'):
            dns_records = pkt['DNS'].qd + pkt['DNS'].an + pkt['DNS'].ns + pkt['DNS'].ar
            return dns_records
        else:
            raise ValueError('Packet is not a DNS packet')
    except Exception as e:
        return(f'An error occurred: {e}')

import json
import dpkt
from dns import rdatatype
def question_refinement_handlePkt(pkt):
    try:
        ip = dpkt.ip.IP(pkt)
        udp = ip.data
        data = dpkt.dns.DNS(udp.data)
        records = []
        if data.qd:
            for question in data.qd:
                records.append({'name': str(question.name), 'type': rdatatype.to_text(question.qtype), 'class': question.qclass})
        if data.an:
            for answer in data.an:
                rdata = ''
                if answer.type == dpkt.dns.DNS_A:
                    rdata = str(answer.rddata)
                elif answer.type == dpkt.dns.DNS_AAAA:
                    rdata = str(answer.rddata)
                elif answer.type == dpkt.dns.DNS_CNAME or answer.type == dpkt.dns.DNS_NS:
                    rdata = str(answer.cname)
                records.append({'name': str(answer.name), 'type': rdatatype.to_text(answer.type), 'class': answer.cls, 'ttl': answer.ttl, 'rdata': rdata})
        if data.ns:
            for ns in data.ns:
                rdata = str(ns.cname) if dpkt.dns.DNS_NS == ns.type else ''
                records.append({'name': str(ns.name), 'type': rdatatype.to_text(ns.type), 'class': ns.cls, 'ttl': ns.ttl, 'rdata': rdata})
        if data.ar:
            for additional in data.ar:
                rdata = str(additional.rddata) if dpkt.dns.DNS_A == additional.type or dpkt.dns.DNS_AAAA == additional.type else ''
                records.append({'name': str(additional.name), 'type': rdatatype.to_text(additional.type), 'class': additional.cls, 'ttl': additional.ttl, 'rdata': rdata})
        return json.dumps(records, indent=4)
    except Exception as e:
        return str(e)
    
def alternative_approaches_handlePkt(pkt):
	if not pkt.haslayer('DNS'):
		raise ValueError('Packet does not contain DNS layer')
	dns_records = []
	for rr in pkt['DNS'].an:
		dns_records.append({'name': rr.rrname.decode('utf-8'), 'type': rr.type, 'rdata': rr.rdata, 'ttl': rr.ttl})
	return dns_records

def context_manager_handlePkt(pkt):
    import dpkt
    dns_records = []
    if pkt.haslayer(dpkt.dns.DNS):
        dns_layer = pkt.getlayer(dpkt.dns.DNS)
        if dns_layer.qd:
            for qr in dns_layer.qd:
                if qr.type == 1:
                    dns_records.append({'type': 'A', 'domain': qr.name, 'value': ''})
                elif qr.type == 28:
                    dns_records.append({'type': 'AAAA', 'domain': qr.name, 'value': ''})
        if dns_layer.an:
            for an in dns_layer.an:
                if an.type == 1:
                    dns_records.append({'type': 'A', 'domain': an.name, 'value': an.ip})
                elif an.type == 28:
                    dns_records.append({'type': 'AAAA', 'domain': an.name, 'value': an.ip})
    return dns_records

def flipped_interaction_3__handlePkt(pkt):
	if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 1:
		dns_records = []
		for answer in pkt.getlayer(DNS).an:
			dns_records.append((answer.rrname, answer.type, answer.rdata))
		for ns in pkt.getlayer(DNS).ns:
			dns_records.append((ns.rrname, 2, ns.rdata))
		for additional in pkt.getlayer(DNS).ar:
			dns_records.append((additional.rrname, additional.type, additional.rdata))
	return dns_records

def flipped_interaction_4__handlePkt(pkt):
    dns_records = {}
    for rr in pkt[DNS].an:
        if rr.rrname not in dns_records:
            dns_records[rr.rrname] = {}
        if rr.rdata in dns_records[rr.rrname]:
            continue
        dns_records[rr.rrname][rr.rdata] = rr.type
    return dns_records

def flipped_interaction_5__handlePkt(pkt):
    dns_records = {}
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).ancount > 0:
        for answer in pkt.getlayer(DNS).an:
            if answer.type in [1, 2, 5, 6, 12, 15, 16, 28, 252, 255]:
                if answer.rrname not in dns_records:
                    dns_records[answer.rrname] = []
                dns_records[answer.rrname].append(answer.rdata)
    return dns_records

def iterative_prompting_3__handlePkt(pkt):
	if not isinstance(pkt, scapy.Packet):
		raise TypeError('Packet must be a scapy.Packet instance')
	try:
		if not pkt:
			raise ValueError('Packet cannot be empty')
		if pkt.haslayer(DNS):
			if pkt.getlayer(DNS).qd is None:
				raise AttributeError('Packet has no DNS questions')
			return pkt.getlayer(DNS).qd
		else:
			return []
	except AttributeError as e:
		import logging
		return(f'Attribute error: {e}')
	except ValueError as e:
		import logging
		return(f'Value error: {e}')
	except TypeError as e:
		import logging
		return(f'Type error: {e}')
	except Exception as e:
		import logging
		return(f'An error occurred: {e}')
      
def iterative_prompting_4__handlePkt(pkt):
    if not isinstance(pkt, scapy.Packet) or pkt is None or not pkt.haslayer(scapy.layers.inet.IP):
        raise TypeError('Input packet must be a non-null Scapy packet with IP layer')
    try:
        if pkt.haslayer(DNS):
            dns_records = getattr(pkt[DNS], 'qd', [])
            dns_answers = getattr(pkt[DNS], 'an', [])
            dns_authority = getattr(pkt[DNS], 'ns', [])
            dns_additional = getattr(pkt[DNS], 'ar', [])
            return {
                'question': dns_records.copy(),
                'answers': [
                    {
                        'name': ans.name,
                        'type': ans.type,
                        'class': ans.qclass,
                        'ttl': ans.ttl,
                        'rdata': ans.rdata
                    } for ans in dns_answers
                ],
                'authority': dns_authority.copy(),
                'additional': dns_additional.copy()
            }
        else:
            return {}
    except (MemoryError, SystemExit) as e:
        raise ValueError(f'Failed to process packet due to low memory or system exit: {str(e)}')
    except Exception as e:
        raise ValueError(f'Failed to process packet: {str(e)}')
    
def iterative_prompting_5__handlePkt(pkt):
    if not pkt or not isinstance(pkt, object):
        return None
    try:
        if pkt.haslayer('DNS'):
            dns_records = []
            if (
                isinstance(pkt.getlayer('DNS').qd, tuple) and pkt.getlayer('DNS').qd and
                hasattr(pkt.getlayer('DNS'), 'an') and isinstance(pkt.getlayer('DNS').an, tuple) and pkt.getlayer('DNS').an
            ):
                for answer in pkt.getlayer('DNS').an:
                    if (
                        hasattr(answer, 'type') and answer.type > 0 and answer.type < 256 and
                        hasattr(answer, 'rclass') and answer.rclass >= 0 and
                        hasattr(answer, 'ttl') and answer.ttl >= 0 and
                        hasattr(answer, 'rdata') and answer.rdata
                    ):
                        rdata = str(answer.rdata).encode('ascii', errors='ignore').decode('ascii', errors='ignore')
                        dns_records.append({
                            'name': str(pkt.getlayer('DNS').qd[0].qname).encode('ascii', errors='ignore').decode('ascii', errors='ignore'),
                            'type': answer.type,
                            'class': answer.rclass,
                            'ttl': answer.ttl,
                            'data': rdata
                        })
            return dns_records
        else:
            return []
    except Exception as e:
        return None

      
def few_shots_prompting_handlePkt(pkt):
	if pkt.haslayer(DNS):
		dns_records = pkt.getlayer(DNS).qd
		return dns_records
	else:
		return []
      
def cot_prompting_handlePkt(pkt):
    dns_records = []
    if pkt.haslayer(DNS):
        for answer in pkt[DNS].an:
            dns_records.append((answer.rrname, answer.type, answer.rdata))
    return dns_records

def fact_check_list_handlePkt(pkt):
	if pkt.__class__ == dpkt.ip.IP and pkt.p == dpkt.ip.IP_PROTO_UDP:
		udp_pkt = pkt.data
		if udp_pkt.__class__ == dpkt.udp.UDP and udp_pkt.dport == 53:
			dns_pkt = dpkt.dns.DNS(udp_pkt.data)
			if dns_pkt.qr == dpkt.dns.DNS_Q and dns_pkt.opcode == dpkt.dns.DNS_QUERY:
				answers = []
				for answer in dns_pkt.an:
					answers.append({
						'name': answer.name,
						'type': answer.type,
						'cls': answer.cls,
						'ttl': answer.ttl,
						'data': answer.data
				})
			return answers
	return []

def not_interactive_mix_handlePkt(pkt):
    if pkt.haslayer(DNS):
        dns_question_records = []
        dns_a_records = []
        dns_cname_records = []
        dns_ns_records = []
        dns_mx_records = []
        dns_fields = ['qd', 'an', 'ns', 'ar']
        for field in dns_fields:
            if hasattr(pkt['DNS'], field):
                records = getattr(pkt['DNS'], field)
                if records:
                    if field == 'qd':
                        for record in records:
                            dns_question_records.append(record.qname)
                    else:
                        for record in records:
                            if record.type == 1:
                                dns_a_records.append((record.rdata, record.rrname))
                            elif record.type == 5:
                                dns_cname_records.append((record.rdata, record.rrname))
                            elif record.type == 2:
                                dns_ns_records.append((record.rdata, record.rrname))
                            elif record.type == 15:
                                dns_mx_records.append((record.rdata, record.rrname))
    return {
        'dns_question_records': dns_question_records,
        'dns_a_records': dns_a_records,
        'dns_cname_records': dns_cname_records,
        'dns_ns_records': dns_ns_records,
        'dns_mx_records': dns_mx_records
    }



import scapy.all as scapy
def interactive_mix_handlePkt(pkt):
    dns_records = {}
    if pkt.haslayer(scapy.DNS):
        for rr in pkt[scapy.DNS].an:
            rrname = rr.rrname.decode('utf-8')
            rdata = str(rr.rdata)
            if rrname in dns_records:
                if isinstance(dns_records[rrname], list):
                    dns_records[rrname].append(rdata)
                else:
                    dns_records[rrname] = [dns_records[rrname], rdata]
            else:
                dns_records[rrname] = rdata
    return dns_records

def baseline_handlePkt(pkt):
    dns_records = []
    if pkt.haslayer('DNS'):
        for answer in pkt[DNS].an:
            dns_records.append({'name': answer.rrname, 'type': answer.type, 'rdata': answer.rdata})
    return dns_records
