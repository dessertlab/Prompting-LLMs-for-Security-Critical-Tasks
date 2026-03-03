from datetime import date
from scapy.layers.inet import *
from scapy.all import IP, IPv6
import ipaddress

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

def persona_testTTL(pkt):
    ipsrc = pkt[IP].src
    ttl = pkt[IP].ttl
    return ipsrc, date.today()

    
def template_testTTL(pkt):
    try:
        if pkt.haslayer('IP'):
            ipsrc = pkt['IP'].src
            ttl = pkt['IP'].ttl
            return {'ipsrc': ipsrc, 'ttl': ttl}
        else:
            raise AttributeError('Packet does not have IP layer')
    except AttributeError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': 'An error occurred:'+ str(e)}
    
def question_refinement_testTTL(pkt):
    return {
        'ipsrc': pkt.get('ipsrc') if 'ipsrc' in pkt else None,
        'ttl': pkt.get('ttl') if 'ttl' in pkt else None
    }

def alternative_approaches_testTTL(pkt):
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt[IP].src
            ttl = pkt[IP].ttl
            return ipsrc, ttl
        else:
            return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
    
def context_manager_testTTL(pkt):
	if pkt.haslayer(IP):
		ipsrc = pkt[IP].src
		ttl = pkt[IP].ttl
		return ipsrc, ttl
	else:
		return None, None
    
def flipped_interaction_3__testTTL(pkt):
    if pkt.haslayer('IP'):
        try:
            ipsrc = pkt['IP'].src
            ttl = str(pkt['IP'].ttl)
            return ipsrc, ttl
        except AttributeError:
            return None, None
    else:
        return None, None
    
def flipped_interaction_4__testTTL(pkt):
    results = []
    try:
        if pkt.haslayer('IP'):
            ipsrc = pkt['IP'].src
            ttl = pkt['IP'].ttl
            results.append((ipsrc, ttl))
    except Exception:
        pass
    return results

def flipped_interaction_5__testTTL(pkt):
    result = []

    def process_ip_layer(ip_packet):
        if ip_packet.haslayer(IP):
            result.append((ip_packet[IP].src, ip_packet[IP].ttl))
        elif ip_packet.haslayer(IPv6):
            result.append((ip_packet[IPv6].src, ip_packet[IPv6].hlim))

    def process_packet(pkt):
        if pkt.haslayer(IP) or pkt.haslayer(IPv6):
            if pkt.haslayer(IP):
                while pkt.haslayer(IP):
                    ip_layer = pkt.getlayer(IP, 0)
                    if isinstance(ip_layer.payload, (IP, IPv6)):
                        pass  # Mancava un'istruzione qui
                    else:
                        if ip_layer.payload is not None:
                            if isinstance(ip_layer.payload, (IP, IPv6)):
                                pkt = ip_layer.payload
                            else:
                                break
                return
            if pkt.haslayer(IPv6):
                if pkt.getlayer(IPv6).nh == 41:
                    while pkt.haslayer(IPv6) and pkt.getlayer(IPv6).nh == 41:
                        ip_layer = pkt.getlayer(IPv6, 0)
                        if ip_layer.payload is not None:
                            if isinstance(ip_layer.payload, (IP, IPv6)):
                                pkt = ip_layer.payload
                            else:
                                break
        else:
            if pkt.haslayer(IPv6):
                while pkt.haslayer(IPv6):
                    ip_layer = pkt.getlayer(IPv6, 0)
                    if ip_layer.payload is not None and isinstance(ip_layer.payload, (IP, IPv6)):
                        pass  # Mancava un'istruzione qui
                    else:
                        break

    return result if result else []


def iterative_prompting_3__testTTL(pkt):
    if not isinstance(pkt, (tuple, list)) or len(pkt) < 2:
        raise ValueError("Invalid packet")
    if not isinstance(pkt[0], (tuple, list)) or len(pkt[0]) < 2:
        raise ValueError("Invalid packet")
    try:
        if not hasattr(pkt[0][1],'src'):
            raise AttributeError('src')
        ipsrc = pkt[0][1].src
        if pkt[0][0] == 6:
            if not hasattr(pkt[0][1], 'hlim'):
                raise AttributeError('hlim')
            ttl = pkt[0][1].hlim
        else:
            if not hasattr(pkt[0][1], 'ttl'):
                raise AttributeError('ttl')
            ttl = pkt[0][1].ttl
        return ipsrc, ttl
    except AttributeError as e:
        raise ValueError("Invalid packet attributes") from e
    
def iterative_prompting_4__testTTL(pkt):
    if not isinstance(pkt, Packet):
        raise TypeError("Expected a Packet object")
    try:
        if not pkt or not pkt.haslayer(IP):
            raise ValueError("Invalid packet")
        ipsrc = pkt[IP].src
        ttl = pkt[IP].ttl
        if not isinstance(ipsrc, str) or not isinstance(ttl, int):
            raise ValueError("Invalid packet attributes")
        return ipsrc, ttl
    except AttributeError:
        raise ValueError("Invalid packet")
    except Exception as e:
        return None, str(e)
    
def iterative_prompting_5__testTTL(pkt):
    if not isinstance(pkt, bytes) or len(pkt) < 27: raise ValueError('Invalid packet')
    try:
        if pkt[0:1]!= b'\x45': raise ValueError('Not an IPv4 packet')
        ttl = ord(pkt[8:9])
        ipsrc = '.'.join(str(pkt[12+i:13+i][0]) for i in range(4))
        return ipsrc, ttl
    except (IndexError, TypeError): raise ValueError('Invalid packet')
    except Exception as e: raise RuntimeError(f'Failed to process packet: {str(e)}')
    
def few_shots_prompting_testTTL(pkt):
    ipsrc = pkt[IP].src
    ttl = pkt[IP].ttl
    return ipsrc, ttl

def cot_prompting_testTTL(pkt):
    ipsrc = pkt[IP].src
    ttl = pkt[IP].ttl
    return ipsrc, ttl

def fact_check_list_testTTL(pkt):
    if pkt.haslayer(IP):
        ip_layer = pkt.getlayer(IP)
        ipsrc = ip_layer.src
        ttl = ip_layer.ttl
        return ipsrc, ttl
    else:
        return None
    
def not_interactive_mix_testTTL(pkt):
    if IP in pkt:
        try:
            ipsrc = pkt[IP].src
            ttl = pkt[IP].ttl
            return ipsrc, ttl
        except AttributeError:
            return None, None
    else:
        return None, None
    
from scapy.layers.inet import IP
def interactive_mix_testTTL(pkt):
    if pkt.haslayer(IP):
        return pkt[IP].src, pkt[IP].ttl
    return None, None

def baseline_testTTL(pkt):
	ipsrc = pkt[IP].src
	ttl = pkt[IP].ttl
	return ipsrc, ttl
