from scapy.all import *
import binascii

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
    ipsrc = pkt.src
    ttl = pkt[IP].ttl

def template_testTTL(pkt):
    try:
        if not hasattr(pkt, 'src'):
            raise ValueError('Packet does not contain source address information.')
        ipsrc = pkt.src
        ttl = pkt.ttl
        return {'source_ip': ipsrc, 'ttl': ttl if ttl is not None else 'ttl not available'}
    except AttributeError:
        return {'error': 'Invalid input. Expected a packet object.'}
    except ValueError as e:
        return {'error': str(e)}

def question_refinement_testTTL(pkt):
    try:
        ipsrc = pkt['src'].addr
        ttl = pkt['ttl']
        return (ipsrc, ttl)
    except KeyError as e:
        raise ValueError('Missing packet attribute: ' + str(e))

def alternative_approaches_testTTL(pkt):
    ipsrc = pkt[IP].src
    ttl = pkt[IP].ttl

def context_manager_testTTL(pkt):
    ipsrc = pkt['IP'].src
    ttl = pkt['IP'].ttl

import scapy
def iterative_prompting_3_testTTL(pkt):
    if not isinstance(pkt, (scapy.layers.l2.Ether, scapy.layers.inet.IP)):
        raise TypeError('Invalid packet type. Expected a packet of type Ether or IP')
    if not hasattr(pkt, 'IP'):
        raise ValueError('Packet does not contain IP layer')
    if not isinstance(pkt.IP, scapy.IP):
        raise TypeError('IP attribute of the packet does not belong to IP class')
    ipsrc = pkt.IP.src
    ttl = pkt.IP.ttl
    if not isinstance(ipsrc, (str, bytes)) or not isinstance(ttl, int):
        raise ValueError('Invalid IP source address or TTL value')
    scapy_version = scapy.__version__
    known_vulnerabilities = {
        '1.5.1': ['flaws_to_fix'],
    }
    if scapy_version in known_vulnerabilities:
        raise Warning(f'Warning: Potential security vulnerability known for scapy version {scapy_version}')

def iterative_prompting_4_testTTL(pkt):
    import sys
    if not isinstance(pkt, dict):
        raise TypeError('Input must be a dictionary')
    if 'IP' not in pkt:
        raise KeyError('Dictionary must contain key IP')
    if not isinstance(pkt['IP'], dict):
        raise TypeError('Dictionary key IP must correspond to another dictionary')
    try:
        ipsrc = pkt['IP'].get('src')
        ttl = pkt['IP'].get('ttl')
        if ipsrc is None or ttl is None:
            raise KeyError('Dictionary key IP must contain src and ttl keys')
    except AttributeError:
        raise TypeError('Dictionary key IP must be a dictionary')
    if sys.stderr.isatty():
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sys.stderr.write(f'{timestamp} - Warning: Invalid input supplied to iterative_prompting_4_testTTL()\n')
    return ipsrc, ttl

def iterative_prompting_5_testTTL(pkt):
    if not isinstance(pkt, dict):
        raise TypeError('Expected argument to be a dictionary representing a packet.')
    if 'IP' not in pkt:
        raise KeyError('Packet dictionary missing required')

def few_shots_prompting_testTTL(pkt):
    try:
        eth = dpkt.ethernet.Ethernet(pkt)
        ip = eth.data
        ipsrc = socket.inet_ntoa(ip.src)
        ttl = ip.ttl
    except Exception:
        pass

def cot_prompting_testTTL(pkt):
    try:
        eth = dpkt.ethernet.Ethernet(pkt)
        ip = eth.data
        ipsrc = socket.inet_ntoa(ip.src)
        ttl = ip.ttl
    except Exception as e:
        pass

def fact_check_list_testTTL(pkt):
    if pkt.haslayer(scapy.IP):
        ip_layer = pkt[scapy.IP]
        ipsrc = ip_layer.src
        ttl = ip_layer.ttl
        return (ipsrc, ttl)
    else:
        return None

def not_interactive_mix_testTTL(pkt):
    if not isinstance(pkt, IP):
        raise ValueError("The provided packet is not a valid IP packet.")
    ip_layer = getlayer(pkt[IP])
    if ip_layer.ttl < 0:
        raise ValueError("The IP packet has an invalid TTL value (must be non-negative).")
    ipsrc = ip_layer.src
    return ipsrc, ip_layer.ttl

def baseline_testTTL(pkt):
    ipsrc = pkt.src
    ttl = pkt.ttl

