from scapy.all import *
import binascii
import dpkt

def ground_truth_code_testTTL(pkt):
    results = []
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            results.append((ipsrc, ttl))
    except:
        pass
    return results

def persona__testTTL(pkt):
	import scapy.all as scapy
	if pkt.haslayer(scapy.IP):
		ipsrc = pkt[scapy.IP].src
		ttl = pkt[scapy.IP].ttl
		return {'ipsrc': ipsrc, 'ttl': ttl}
	else:
		return None

def template__testTTL(pkt):
    try:
        ipsrc = pkt.payload.src
        ttl = pkt.payload.ttl
        return {'source_ip': ipsrc, 'ttl': ttl}
    except AttributeError as e:
        return None

def question_refinement__testTTL(pkt):
    try:
        if not isinstance(pkt, bytes):
            return {'error': 'Invalid input type'}
        if len(pkt) < 20:
            return {'error': 'Packet size too small'}
        ip_version = (pkt[0] & 0xf0) >> 4
        if ip_version != 4:
            return {'error': 'Unsupported IP version'}
        ihl = (pkt[0] & 0x0f) * 4
        if len(pkt) < ihl:
            return {'error': 'Invalid IHL'}
        ipsrc = '.'.join(str(pkt[i + 12]) for i in range(4))
        ttl = pkt[8]
        return {'ipsrc': ipsrc, 'ttl': ttl}
    except Exception as e:
        return {'error': 'General parsing error'}

def alternative_approaches__testTTL(pkt):
    import struct
    if not isinstance(pkt, bytes) or len(pkt) < 20:
        raise ValueError('Invalid packet data')
    ip_header = pkt[:20]
    unpacked_data = struct.unpack('!BBHHHBBH4s4s', ip_header)
    ttl = unpacked_data[5]
    ipsrc_bytes = unpacked_data[8]
    ipsrc = '.'.join(str(byte) for byte in ipsrc_bytes)
    return (ipsrc, ttl)

def context_manager__testTTL(pkt):
	import socket
	import struct
	if pkt[0] != 69:
		return None,None
	iph = pkt[1:21]
	ttl, ipsrc = struct.unpack('!BBHHHBBH4s4s', iph)[5:7]
	ipsrc = socket.inet_ntoa(ipsrc)
	return ipsrc, ttl

def flipped_interaction_3__testTTL(pkt):
    try:
        ip_layer = pkt.getlayer(IP)
        if ip_layer:
            ipsrc = ip_layer.src
            ttl = ip_layer.ttl
            return [(ipsrc, ttl)]
    except Exception:
        pass
    return []

def flipped_interaction_4__testTTL(pkt):
	if pkt.haslayer('IP'):
		return (pkt['IP'].src, pkt['IP'].ttl)
	elif pkt.haslayer('IPv6'):
		return (pkt['IPv6'].src, pkt['IPv6'].hlim)
	else:
		return (None, None)

def flipped_interaction_5__testTTL(pkt, fields=None):
	if fields is None:
		fields = ['src', 'ttl']
	result = {}
	if pkt.haslayer(IP):
		ip_layer = pkt.getlayer(IP)
		for field in fields:
			try:
				result[field] = getattr(ip_layer, field)
			except AttributeError:
				result[field] = None
	else:
		result = {field: None for field in fields}
	return result

def iterative_prompting_3__testTTL(pkt):
    try:
        if pkt and pkt.haslayer("IP"):
            ipsrc = pkt["IP"].src
            ttl = pkt["IP"].ttl
            return ipsrc, ttl
        else:
            return None, None
    except Exception as e:
        return None, None

def iterative_prompting_4__testTTL(pkt):
    if not pkt or not isinstance(pkt, Packet):
        return None, None
    try:
        ip_layer = pkt.getlayer(IP)
        if ip_layer:
            src_ip = getattr(ip_layer, 'src', None)
            ttl = getattr(ip_layer, 'ttl', None)
            return src_ip, ttl
    except AttributeError:
        return None, None
    except Exception as e:
        return None, None

def iterative_prompting_5__testTTL(pkt):
    try:
        if not pkt or not hasattr(pkt, "haslayer") or not pkt.haslayer("IP"):
            return None, None
        ip_layer = pkt["IP"]
        ipsrc = ip_layer.getfieldval("src") if ip_layer.hasfield("src") else None
        ttl = ip_layer.getfieldval("ttl") if ip_layer.hasfield("ttl") else None
        return ipsrc, ttl
    except (AttributeError, KeyError):
        return None, None

def few_shots_prompting__testTTL(pkt):
	ipsrc = pkt.getlayer('IP').src
	ttl = pkt.getlayer('IP').ttl

def cot_prompting__testTTL(pkt):
	ipsrc = pkt[dpkt.ip.IP].src
	ttl = pkt[dpkt.ip.IP].ttl

def fact_check_list__testTTL(pkt):
    if IP in pkt:
        ipsrc = pkt[IP].src
        ttl = pkt[IP].ttl
        return ipsrc, ttl
    else:
        raise ValueError("Packet does not contain an IP layer")

def not_interactive_mix__testTTL(pkt):
    if not isinstance(pkt, scapy.packet.Packet):
        return None, None
    ip_layer = pkt.getlayer(scapy.IP)
    if ip_layer is None:
        return None, None
    ipsrc = ip_layer.src
    ttl = ip_layer.ttl
    return ipsrc, ttl

def interactive_mix__testTTL(pkt):
    results = []
    try:
        if pkt.haslayer('IP'):
            ipsrc = pkt['IP'].src
            ttl = str(pkt['IP'].ttl)
            results.append((ipsrc, ttl))
    except Exception:
        pass
    return results

def baseline__testTTL(pkt):
	ipsrc = pkt['IP'].src
	ttl = pkt['IP'].ttl
	return ipsrc, ttl
