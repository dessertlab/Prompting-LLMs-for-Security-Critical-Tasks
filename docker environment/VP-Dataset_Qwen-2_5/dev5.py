from scapy.all import *

def ground_truth_code_dnsQRTest(pkt):
    if pkt.haslayer(DNSRR) and pkt.getlayer(UDP).sport == 53:
        rcode = pkt.getlayer(DNS).rcode
        qname = pkt.getlayer(DNSQR).qname
        if rcode == 3:
            return True
        else:
            return False

def persona__dnsQRTest(pkt):
	try:
		if pkt.haslayer('DNS') and pkt['DNS'].rcode == 3:
			return True
		else:
			return False
	except AttributeError:
		return False

def template__dnsQRTest(pkt):
	try:
		rcode = pkt.qry.rcode
		return rcode == 3
	except AttributeError:
		return False

def question_refinement__dnsQRTest(packet):
    try:
        from scapy.all import IP, UDP, DNS
        r = IP(packet) / UDP / DNS
        if r.haslayer(DNS) and r.getlayer(DNS).qr == 0 and r.getlayer(DNS).rcode == 3:
            return True
        else:
            return False
    except Exception:
        return False

def alternative_approaches__dnsQRTest(pkt):
    try:
        return pkt.dns.rcode == 3
    except (KeyError, AttributeError):
        return False

def context_manager__dnsQRTest(pkt):
	rcode = pkt.getlayer('DNS').rcode
	return rcode == 3

def flipped_interaction_3__dnsQRTest(pkt):
    if UDP in pkt and pkt[UDP].sport == 53:
        if DNS in pkt:
            if pkt[DNS].rcode == 3:
                return True
    return False

def flipped_interaction_4__dnsQRTest(pkt):
    if pkt.haslayer(DNS) and pkt.haslayer(DNSQR) and pkt.getlayer(UDP).sport == 53:
        rcode = pkt.getlayer(DNS).rcode
        qname = pkt.getlayer(DNSQR).qname.decode('utf-8')
        logging.debug(f"DNS Query Name: {qname}, Response Code: {rcode}")
        if rcode == 3:
            return True
        else:
            logging.debug(f"Response code is not 3 (rcode={rcode})")
            return False
    else:
        logging.debug("Packet does not contain DNSQR or is not UDP from port 53")
        return False

def flipped_interaction_5__dnsQRTest(pkt):
	if pkt.haslayer(DNS):
		return pkt[DNS].rcode == 3
	return False

def iterative_prompting_3__dnsQRTest(pkt):
    try:
        if not pkt:
            return False
        if pkt.haslayer(DNS) and pkt[DNS].rcode == 3:
            return True
        return False
    except AttributeError:
        return False

def iterative_prompting_4__dnsQRTest(pkt):
	if not pkt or not callable(getattr(pkt, 'haslayer', None)):
		return False
	if pkt.haslayer(DNS):
		try:
			return pkt[DNS].rcode == 3
		except (AttributeError, IndexError):
			return False
	return False

def iterative_prompting_5__dnsQRTest(pkt):
    if pkt is None:
        return False
    try:
        dns_layer = pkt.getlayer(DNS)
        return dns_layer is not None and dns_layer.rcode == 3
    except AttributeError:
        return False

def few_shots_prompting__dnsQRTest(pkt):
	dns = IP(pkt)[UDP].payload
	if dns.rcode == 3:
		return True
	return False

def cot_prompting__dnsQRTest(pkt):
	dport = pkt.haslayer(DNS) and pkt.getlayer(DNS).dport
	if dport == 53:
		rcode = pkt.getlayer(DNSRR).rcode
		if rcode == 3:
			return True
	return False

def fact_check_list__dnsQRTest(pkt):
	if pkt.haslayer(DNS):
		dns_layer = pkt.getlayer(DNS)
		if dns_layer.qr == 1:
			rcode = dns_layer.rcode
			return rcode == 3
	return False

def not_interactive_mix__dnsQRTest(pkt):
	try:
		if not pkt.haslayer(IP) or not pkt.haslayer(DNS):
			return False
		dns_layer = pkt.getlayer(DNS)
		if dns_layer.qr != 1:
			return False
		return dns_layer.rcode == 3
	except AttributeError:
		return False

def interactive_mix__check_dns_rcode_3(pkt):
    try:
        if pkt.haslayer(UDP) and pkt.haslayer(DNS):
            udp_layer = pkt.getlayer(UDP)
            dns_layer = pkt.getlayer(DNS)
            if udp_layer.sport == 53:
                rcode = dns_layer.rcode
                if rcode == 3:
                    return True
        return False
    except Exception as e:
        with open('error_log.txt', 'a') as log_file:
            log_file.write(f'An error occurred: {str(e)}\n')
        return False

def baseline__dnsQRTest(pkt):
	rcode = pkt.getlayer('DNS').rcode
	return rcode == 3
