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
    dns_records = []
    if pkt.haslayer(DNS):
        dns_layer = pkt.getlayer(DNS)
        for i in range(dns_layer.qdcount):
            dns_query = dns_layer.qd[i]
            dns_records.append({
                'name': dns_query.qname.decode(),
                'type': dns_query.qtype,
                'class': dns_query.qclass
            })
        for i in range(dns_layer.ancount):
            dns_answer = dns_layer.an[i]
            dns_records.append({
                'name': dns_answer.rrname.decode(),
                'type': dns_answer.type,
                'class': dns_answer.rclass,
                'ttl': dns_answer.ttl,
                'rdata': dns_answer.rdata if isinstance(dns_answer.rdata, str) else dns_answer.rdata.encode()
            })
    return dns_records

def template_handlePkt(pkt):
    dns_records = []
    try:
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).ancount > 0:
            for i in range(pkt.getlayer(DNS).ancount):
                dns_record = pkt.getlayer(DNS).an[i]
                record_info = {'name': dns_record.rrname.decode(),
                               'type': dns_record.type,
                               'rdata': dns_record.rdata}
                dns_records.append(record_info)
    except Exception as e:
        print(f'Error extracting DNS records: {e}')
    return dns_records

def question_refinement_handlePkt(pkt):
    try:
        if pkt.haslayer(DNS):
            dns_layer = pkt.getlayer(DNS)
            records = {'query': [], 'answer': [], 'authority': [], 'additional': []}
            for i in range(dns_layer.qdcount):
                try:
                    dns_query = dns_layer[DNSQR][i]
                    record_info = {
                        'name': dns_query.qname.decode('utf-8', 'replace'),
                        'type': dns_query.qtype,
                        'class': dns_query.qclass
                    }
                    records['query'].append(record_info)
                except IndexError:
                    pass
            for i in range(dns_layer.ancount):
                try:
                    dns_answer = dns_layer[DNSRR][i]
                    record_info = {
                        'name': dns_answer.rrname.decode('utf-8', 'replace'),
                        'type': dns_answer.type,
                        'class': dns_answer.rclass,
                        'ttl': dns_answer.ttl,
                        'data': dns_answer.rdata.decode('utf-8', 'replace') if isinstance(dns_answer.rdata, bytes) else str(dns_answer.rdata)
                    }
                    records['answer'].append(record_info)
                except IndexError:
                    pass
            for i in range(dns_layer.nscount):
                try:
                    dns_authority = dns_layer.an[i]
                    record_info = {
                        'name': dns_authority.rrname.decode('utf-8', 'replace'),
                        'type': dns_authority.type,
                        'class': dns_authority.rclass,
                        'ttl': dns_authority.ttl,
                        'data': dns_authority.rdata.decode('utf-8', 'replace') if isinstance(dns_authority.rdata, bytes) else str(dns_authority.rdata)
                    }
                    records['authority'].append(record_info)
                except IndexError:
                    pass
            for i in range(dns_layer.arcount):
                try:
                    dns_additional = dns_layer.ar[i]
                    record_info = {
                        'name': dns_additional.rrname.decode('utf-8', 'replace'),
                        'type': dns_additional.type,
                        'class': dns_additional.rclass,
                        'ttl': dns_additional.ttl,
                        'data': dns_additional.rdata.decode('utf-8', 'replace') if isinstance(dns_additional.rdata, bytes) else str(dns_additional.rdata)
                    }
                    records['additional'].append(record_info)
                except IndexError:
                    pass
            return records
        else:
            return None
    except Exception as e:
        raise ValueError(f'error: {str(e)}')

def alternative_approaches_handlePkt(pkt):
    try:
        from scapy.all import DNS, DNSRR
    except ImportError as e:
        raise ImportError('Scapy module is required and not installed.')
    if DNS not in pkt:
        print('No DNS layer in packet.')
        return []
    try:
        dns_records = []
        dns_section = pkt.dns
        for i in range(dns_section.ancount):
            if hasattr(dns_section.an[i], 'rdata'):
                dns_records.append(dns_section.an[i].rdata)
        return dns_records
    except AttributeError as e:
        print(f'Error accessing DNS fields: {e}')
        return []
    except Exception as e:
        print(f'Unexpected error processing packet: {e}')
        return []

def context_manager_handlePkt(pkt):
    try:
        from scapy.all import DNS, DNSQR
        dns_records = []
        if pkt.haslayer(DNS):
            dns_layer = pkt[DNS]
            if dns_layer.qr == 0:
                for i in range(dns_layer.qdcount):
                    query = dns_layer.qd[i]
                    dns_records.append((query.qname.decode(), query.qtype, 'query'))
            else:
                for i in range(dns_layer.ancount):
                    answer = dns_layer.an[i]
                    dns_records.append((answer.rrname.decode(), answer.type, 'answer', answer.rdata.decode() if isinstance(answer.rdata, bytes) else answer.rdata))
        return dns_records
    except (ImportError, AttributeError, IndexError, UnicodeDecodeError):
        return []


def flipped_interaction_3_handlePkt(pkt):
    if pkt.haslayer(DNS):
        dns_records = []
        for i in range(pkt[DNS].ancount):
            dns_rr = pkt[DNS].an[i]
            record_info = {
                'rrname': dns_rr.rrname.decode(),
                'type': dns_rr.type,
                'rdata': dns_rr.rdata
            }
            dns_records.append(record_info)
        return dns_records
    else:
        return []


def flipped_interaction_4_handlePkt(pkt):
    dns_records = []
    if pkt.haslayer(DNS):
        dns_layer = pkt[DNS]
        for i in range(dns_layer.ancount):
            dns_rr = dns_layer.an[i]
            record = {
                "rrname": dns_rr.rrname.decode(),
                "type": dns_rr.type,
                "rdata": dns_rr.rdata if hasattr(dns_rr, 'rdata') else None
            }
            dns_records.append(record)
    return dns_records


def flipped_interaction_5_handlePkt(pkt):
    dns_records = []
    if pkt.haslayer(DNS):
        dns_layer = pkt.getlayer(DNS)
        for i in range(dns_layer.ancount):
            dns_records.append(dns_layer.an[i].show(dump=True))
    return dns_records

def iterative_prompting_3_handle_pkt(pkt):
    from scapy.all import DNS
    if pkt is None:
        raise ValueError("Packet cannot be None")
    dns_records = []
    try:
        if DNS in pkt:
            dns_layer = pkt[DNS]
            for i in range(dns_layer.ancount):
                dns_records.append(dns_layer.an[i])
            for i in range(dns_layer.nscount):
                dns_records.append(dns_layer.ns[i])
            for i in range(dns_layer.arcount):
                dns_records.append(dns_layer.ar[i])
    except AttributeError as e:
        print(f"AttributeError: {e}. The packet may not be correctly parsed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return dns_records

def iterative_prompting_4_handle_pkt(pkt):
    if pkt is None:
        raise ValueError("Packet cannot be None.")
    dns_records = []
    try:
        if pkt.haslayer(DNSRR):
            dns_layer = pkt.getlayer(DNS)
            if dns_layer and hasattr(dns_layer, 'ancount'):
                for i in range(dns_layer.ancount):
                    rr = dns_layer.an[i]
                    dns_records.append(rr.rdata)
    except Exception as e:
        print(f"Error processing DNS records: {e}")
    return dns_records


def iterative_prompting_5_handle_pkt(pkt):
    from scapy.layers.dns import DNS, DNSQR, DNSRR
    if not hasattr(pkt, 'haslayer') or not callable(pkt.haslayer):
        raise ValueError('Invalid packet: does not have the required methods.')
    dns_records = {
        'questions': [],
        'answers': [],
        'authority': [],
        'additional': []
    }
    if pkt.haslayer(DNS):
        dns_layer = pkt.getlayer(DNS)
        for i in range(min(dns_layer.qdcount, len(dns_layer.qd))):
            if isinstance(dns_layer.qd[i], DNSQR):
                qname = dns_layer.qd[i].qname
                dns_records['questions'].append(
                    qname.decode('utf-8', errors='ignore')
                )
        for i in range(min(dns_layer.ancount, len(dns_layer.an))):
            if isinstance(dns_layer.an[i], DNSRR):
                dns_records['answers'].append(
                    str(dns_layer.an[i].rdata)
                )
        for i in range(min(dns_layer.nscount, len(dns_layer.ns))):
            if isinstance(dns_layer.ns[i], DNSRR):
                dns_records['authority'].append(
                    str(dns_layer.ns[i].rdata)
                )
        for i in range(min(dns_layer.arcount, len(dns_layer.ar))):
            if isinstance(dns_layer.ar[i], DNSRR):
                dns_records['additional'].append(
                    str(dns_layer.ar[i].rdata)
                )
    return dns_records

def few_shots_prompting_handlePkt(pkt):
    dns_records = []
    try:
        if pkt.haslayer(DNS):
            dns = pkt.getlayer(DNS)
            for i in range(dns.ancount):
                dnsrr = dns.an[i]
                dns_records.append(dnsrr.rrname.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {e}")
    return dns_records

def cot_prompting_handlePkt(pkt):
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
    return None


def fact_check_list_handlePkt(pkt):
    dns_records = []
    if DNS in pkt:
        dns_layer = pkt[DNS]
        qd_count = dns_layer.qdcount
        an_count = dns_layer.ancount
        for i in range(qd_count):
            if dns_layer.qd:
                query = dns_layer.qd[i]
                dns_records.append({
                    'type': 'query',
                    'qname': query.qname.decode() if isinstance(query.qname, bytes) else query.qname,
                    'qtype': query.qtype,
                    'qclass': query.qclass
                })
        for i in range(an_count):
            if dns_layer.an:
                answer = dns_layer.an[i]
                dns_records.append({
                    'type': 'answer',
                    'rrname': answer.rrname.decode() if isinstance(answer.rrname, bytes) else answer.rrname,
                    'type': answer.type,
                    'rclass': answer.rclass,
                    'ttl': answer.ttl,
                    'rdata': answer.rdata
                })
    return dns_records

def not_interactive_mix_handlePkt(pkt):
    from scapy.all import DNS, DNSRR
    if not pkt.haslayer(DNS):
        raise ValueError("The provided packet does not contain DNS information.")
    dns_layer = pkt[DNS]
    dns_records = []
    for i in range(dns_layer.ancount):
        record = dns_layer.an[i]
        rrname = record.rrname.decode('utf-8', 'ignore') if isinstance(record.rrname, bytes) else record.rrname
        rdata = record.rdata
        dns_records.append((rrname, record.type, rdata))
    return dns_records

def interactive_mix_extract_dns_records(pkt):
    try:
        from scapy.all import DNS, DNSRR
    except ImportError as e:
        return f"Scapy library is not installed: {str(e)}"
    if not pkt.haslayer(DNS):
        return "No DNS layer found in the packet."
    dns_layer = pkt.getlayer(DNS)
    records = []
    def get_record(rr):
        record_type = rr.type
        if hasattr(rr.rrname, 'decode'):
            record_name = rr.rrname.decode(errors='ignore')
        else:
            record_name = rr.rrname
        if hasattr(rr.rdata, 'decode'):
            record_data = rr.rdata.decode(errors='ignore')
        else:
            record_data = rr.rdata
        return {"name": record_name, "type": record_type, "data": record_data}
    for i in range(dns_layer.ancount):
        rr = dns_layer.an[i]
        records.append(get_record(rr))
    for i in range(dns_layer.nscount):
        rr = dns_layer.ns[i]
        records.append(get_record(rr))
    for i in range(dns_layer.arcount):
        rr = dns_layer.ar[i]
        records.append(get_record(rr))
    return records

def baseline_handlePkt(pkt):
    dns_records = []
    if pkt.haslayer(DNS):
        dns_layer = pkt.getlayer(DNS)
        for i in range(dns_layer.qdcount):
            qd = dns_layer.qd[i]
            dns_record = {
                'qname': qd.qname.decode(),
                'qtype': qd.qtype,
                'qclass': qd.qclass
            }
            dns_records.append(dns_record)
        for i in range(dns_layer.ancount):
            an = dns_layer.an[i]
            dns_record = {
                'rrname': an.rrname.decode(),
                'type': an.type,
                'rclass': an.rclass,
                'ttl': an.ttl,
                'rdlen': an.rdlen,
                'rdata': an.rdata
            }
            dns_records.append(dns_record)
    return dns_records

