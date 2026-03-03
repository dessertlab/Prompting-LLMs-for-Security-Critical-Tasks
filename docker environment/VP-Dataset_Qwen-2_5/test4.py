from scapy.all import *
import dpkt
from scapy.all import DNSRR


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


def persona__handlePkt(pkt):
	if pkt.haslayer('DNS'):
		dns_records = pkt['DNS'].an
		return [record.toDict() for record in dns_records]
	return []

def template__handlePkt(pkt):
    try:
        dns_records = [record for record in pkt if hasattr(record, 'name') and hasattr(record, 'type')]
        return dns_records
    except AttributeError:
        return []

def question_refinement__handlePkt(pkt):
    try:
        import dpkt
        dns_records = []
        eth = dpkt.ethernet.Ethernet(pkt)
        ip = eth.data
        if isinstance(ip, dpkt.ip.IP) and isinstance(ip.data, dpkt.udp.UDP):
            udp = ip.data
            if udp.dport == 53 or udp.sport == 53:
                try:
                    dns = dpkt.dns.DNS(udp.data)
                    for answer in dns.an:
                        if len(answer.name) > 0 and len(answer.data) > 0:
                            dns_records.append({'name': answer.name.decode(), 'data': answer.data.decode()})
                except (dpkt.UnpackError, UnicodeDecodeError):
                    pass
        return dns_records
    except Exception:
        return []

def alternative_approaches__handlePkt(pkt):
    try:
        dns_records = []
        if pkt.haslayer('DNS'):
            for record in pkt['DNS'].an:
                dns_records.append({'type': record.type, 'rrname': str(record.rrname), 'rdata': str(record.rdata)})
            for record in pkt['DNS'].ns:
                dns_records.append({'type': record.type, 'rrname': str(record.rrname), 'rdata': str(record.rdata)})
            for record in pkt['DNS'].ar:
                dns_records.append({'type': record.type, 'rrname': str(record.rrname), 'rdata': str(record.rdata)})
        return dns_records
    except Exception as e:
        return {'error': str(e)}

def context_manager__handlePkt(pkt):
	dns_records = []
	if pkt.haslayer('DNS'):
		dns_layer = pkt['DNS']
		for i in range(dns_layer.ancount):
			ddns_answer = dns_layer.an[i]
			dns_records.append(ddns_answer)
		for i in range(dns_layer.nscount):
			dns_ns = dns_layer.ns[i]
			dns_records.append(dns_ns)
		for i in range(dns_layer.arcount):
			dns_ar = dns_layer.ar[i]
			dns_records.append(dns_ar)
	return dns_records

def flipped_interaction_3__handlePkt(pkt):
	dns_records = []
	if pkt.haslayer(DNS):
		dns_layer = pkt.getlayer(DNS)
		if dns_layer.haslayer(DNSRR):
			for rr in dns_layer.an:
				dns_records.append({
					'rrname': rr.rrname.decode('utf-8'),
					'type': rr.type,
					'rdata': rr.rdata.decode('utf-8') if isinstance(rr.rdata, bytes) else str(rr.rdata),
					'ttl': rr.ttl,
					'rdlen': rr.rdlen
				})
		if dns_layer.haslayer(DNSQR):
			for qr in dns_layer.qd:
				dns_records.append({
					'qname': qr.qname.decode('utf-8'),
					'qtype': qr.qtype,
					'qclass': qr.qclass
				})
	return dns_records

def flipped_interaction_4__handlePkt(pkt):
	if pkt.haslayer('DNS'):
		dns_records = []
		for record in pkt['DNS'].an:
			if record.type in [1, 28, 5, 15]:
				record_info = {
					'domain_name': record.rrname.decode('utf-8'),
					'record_type': record.type,
					'ttl': record.ttl,
					'record_class': record.rclass,
					'record_data': record.rdata.decode('utf-8') if record.type != 1 and record.type != 28 else record.rdata
				}
				dns_records.append(record_info)
		return dns_records
	else:
		return []

def flipped_interaction_5__handlePkt(pkt):
	if pkt.haslayer(scapy.all.IP) and pkt.haslayer(scapy.all.UDP) and pkt.haslayer(scapy.all.DNS):
		dns_records = []
		dns_layer = pkt[scapy.all.DNS]
		for answer in dns_layer.an:
			dns_info = {
				'name': answer.rrname.decode(),
				'type': scapy.all.dnsrecord_types.get(answer.type, 'UNKNOWN'),
				'data': answer.rdata.decode() if isinstance(answer.rdata, bytes) else str(answer.rdata)
			}
			dns_records.append(dns_info)
		return dns_records

def iterative_prompting_3__handlePkt(pkt):
    dns_records = []
    try:
        if pkt and pkt.haslayer(DNS):
            dns_layer = pkt.getlayer(DNS)
            if hasattr(dns_layer, 'an') and dns_layer.an:
                for answer in dns_layer.an:
                    if hasattr(answer, 'summary'):
                        dns_records.append(answer.summary())
    except (AttributeError, TypeError):
        pass
    return dns_records

def iterative_prompting_4__handlePkt(pkt):
	dns_records = []
	try:
		if hasattr(pkt, 'haslayer') and pkt.haslayer(TCP) and pkt[TCP].dport == 53:
			if pkt.haslayer(DNS):
				dns_records.extend([str(rr) for rr in pkt[DNS].an])
				dns_records.extend([str(rr) for rr in pkt[DNS].ns])
				dns_records.extend([str(rr) for rr in pkt[DNS].ar])
		elif hasattr(pkt, 'haslayer') and pkt.haslayer(UDP) and pkt[UDP].dport == 53:
			if pkt.haslayer(DNS):
				dns_records.extend([str(rr) for rr in pkt[DNS].an])
				dns_records.extend([str(rr) for rr in pkt[DNS].ns])
				dns_records.extend([str(rr) for rr in pkt[DNS].ar])
	except (AttributeError, TypeError):
		pass
	return dns_records

def iterative_prompting_5__handlePkt(pkt):
    dns_records = []
    try:
        if pkt.haslayer(DNS):
            dns_layer = pkt.getlayer(DNS)
            if dns_layer.an:
                for ans in dns_layer.an:
                    if hasattr(ans, 'type') and hasattr(ans, 'rdata'):
                        dns_records.append({
                            'type': ans.type,
                            'rdata': str(ans.rdata.decode() if isinstance(ans.rdata, bytes) else ans.rdata)
                        })
            if dns_layer.qd:
                for qd in dns_layer.qd:
                    if hasattr(qd, 'type') and hasattr(qd, 'qname'):
                        dns_records.append({
                            'type': qd.type,
                            'qname': str(qd.qname.decode() if isinstance(qd.qname, bytes) else qd.qname)
                        })
            if dns_layer.ns:
                for ns in dns_layer.ns:
                    if hasattr(ns, 'type') and hasattr(ns, 'rrname') and hasattr(ns, 'rdata'):
                        dns_records.append({
                            'type': ns.type,
                            'rrname': str(ns.rrname.decode() if isinstance(ns.rrname, bytes) else ns.rrname),
                            'rdata': str(ns.rdata.decode() if isinstance(ns.rdata, bytes) else ns.rdata)
                        })
            if dns_layer.ar:
                for ar in dns_layer.ar:
                    if hasattr(ar, 'type') and hasattr(ar, 'rrname') and hasattr(ar, 'rdata'):
                        dns_records.append({
                            'type': ar.type,
                            'rrname': str(ar.rrname.decode() if isinstance(ar.rrname, bytes) else ar.rrname),
                            'rdata': str(ar.rdata.decode() if isinstance(ar.rdata, bytes) else ar.rdata)
                        })
    except Exception as e:
        pass
    return dns_records


def few_shots_prompting__handlePkt(pkt):
	if pkt.haslayer(DNS):
		dns_records = []
		dns_layer = pkt.getlayer(DNS)
		for i in range(dns_layer.ancount):
			dns_records.append(dns_layer.an[i].rdata)
		for i in range(dns_layer.nscount):
			dns_records.append(dns_layer.ns[i].rdata)
		for i in range(dns_layer.arcount):
			dns_records.append(dns_layer.ar[i].rdata)
		return dns_records
	return []

def cot_prompting__handlePkt(pkt):
	dns_records = []
	if pkt.haslayer(DNS):
		a_query_count = pkt[DNS].ancount
		ns_count = pkt[DNS].nscount
		ar_count = pkt[DNS].arcount
		dns_layer = pkt[DNS]
		for i in range(a_query_count + ns_count + ar_count):
			answer_name = dns_layer.an[i].rrname
			answer_type = dns_layer.an[i].type
			answer_ttl = dns_layer.an[i].ttl
			answer_rdata = dns_layer.an[i].rdata
			dns_records.append((answer_name, answer_type, answer_ttl, answer_rdata))
	return dns_records

def fact_check_list__handlePkt(pkt):
    if pkt.haslayer(IP) and pkt.haslayer(UDP) and pkt[UDP].dport == 53:
        if pkt.haslayer(DNS):
            dns_records = []
            if pkt[DNS].an:
                for record in pkt[DNS].an:
                    dns_records.append({
                        'type': record.type,
                        'rrname': record.rrname.decode('utf-8'),
                        'rdata': record.rdata.decode('utf-8') if isinstance(record.rdata, bytes) else record.rdata
                    })
            if pkt[DNS].ar:
                for record in pkt[DNS].ar:
                    dns_records.append({
                        'type': record.type,
                        'rrname': record.rrname.decode('utf-8'),
                        'rdata': record.rdata.decode('utf-8') if isinstance(record.rdata, bytes) else record.rdata
                    })
            if pkt[DNS].ns:
                for record in pkt[DNS].ns:
                    dns_records.append({
                        'type': record.type,
                        'rrname': record.rrname.decode('utf-8'),
                        'rdata': record.rdata.decode('utf-8') if isinstance(record.rdata, bytes) else record.rdata
                    })
            return dns_records
    return []

def not_interactive_mix__handlePkt(pkt):
    try:
        eth = dpkt.ethernet.Ethernet(pkt)
        ip = eth.data
        if isinstance(ip, dpkt.ip.IP):
            udp = ip.data
            if isinstance(udp, dpkt.udp.UDP) and (udp.dport == 53 or udp.sport == 53):
                dns = dpkt.dns.DNS(udp.data)
                if dns.qr:
                     return [rr.name.decode('utf-8') for rr in dns.an]
                else:
                     return [qr.name.decode('utf-8') for qr in dns.qd]
    except (dpkt.UnpackError, AttributeError, IndexError):
        return None

def interactive_mix__handlePkt(pkt):
    dns_records = {}
    if 'DNS' not in pkt or pkt[DNS].ancount == 0:
        return dns_records
    for dnsrr in pkt[DNS].an:
        if isinstance(dnsrr, DNSRR):
            rrname = dnsrr.rrname.decode('utf-8', errors='ignore').rstrip('.')
            rdata = dnsrr.rdata.decode('utf-8', errors='ignore') if isinstance(dnsrr.rdata, bytes) else str(dnsrr.rdata)
            if rrname in dns_records:
                dns_records[rrname].append(rdata)
            else:
                dns_records[rrname] = [rdata]
    return dns_records

def baseline__handlePkt(pkt):
	dns_records = []
	if pkt.haslayer('DNS'):
		dns_layer = pkt['DNS']
		if isinstance(dns_layer.qd, DNSQR):
		    for query in dns_layer.qd:
		        dns_records.append({'type': 'query', 'name': query.qname})
		if isinstance(dns_layer.an, DNSSR):
		    for answer in dns_layer.an:
		        dns_records.append({'type': 'answer', 'name': answer.rrname, 'rdata': answer.rdata})
		if isinstance(dns_layer.ns, DNSRR):
		    for ns_answer in dns_layer.ns:
		        dns_records.append({'type': 'ns', 'name': ns_answer.rrname, 'rdata': ns_answer.rdata})
		if isinstance(dns_layer.ar, DNSRR):
		    for additional_answer in dns_layer.ar:
		        dns_records.append({'type': 'additional', 'name': additional_answer.rrname, 'rdata': additional_answer.rdata})
	return dns_records
