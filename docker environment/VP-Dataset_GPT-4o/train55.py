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
    try:
        ipsrc = pkt.getlayer(IP).src
        ttl = pkt.getlayer(IP).ttl
        return ipsrc, ttl
    except Exception as e:
        return None, None

def template_testTTL(pkt):
    try:
        ipsrc = pkt.getlayer(IP).src if pkt.haslayer(IP) else None
        ttl = pkt.getlayer(IP).ttl if pkt.haslayer(IP) else None
        return {'ipsrc': ipsrc, 'ttl': ttl}
    except Exception as e:
        print(f'An error occurred: {e}')

def question_refinement_testTTL(pkt):
    try:
        if not isinstance(pkt, (bytes, bytearray)):
            raise ValueError("Invalid packet format")
        if len(pkt) < 20:
            raise ValueError( "Packet too short")
        ip_header = pkt[0:20]
        unpacked_header = struct.unpack('!BBHHHBBH4s4s', ip_header)
        ttl = unpacked_header[5]
        src_ip_raw = unpacked_header[8]
        src_ip = socket.inet_ntoa(src_ip_raw)
        return {
            'ipsrc': src_ip,
            'ttl': ttl
        }
    except (struct.error, binascii.Error) as e:
        raise ValueError(f"Error processing packet: {str(e)}")

def alternative_approaches_testTTL(pkt):
    try:
        ipsrc = pkt.getlayer(1).src
        ttl = pkt.getlayer(1).ttl
        return (ipsrc, ttl)
    except AttributeError:
        raise ValueError("Packet does not contain required layer information")
    except Exception as e:
        raise ValueError(f"An error occurred: {str(e)}")

def context_manager_testTTL(pkt):
    try:
        if isinstance(pkt, bytes) and len(pkt) >= 20:
            ipsrc = '.'.join(map(str, pkt[12:16]))
            ttl = pkt[8]
            return ipsrc, ttl
        else:
            raise ValueError("Invalid packet")
    except Exception as e:
        raise ValueError(str(e))


def flipped_interaction_3_testTTL(pkt):
    if IP in pkt:
        ipsrc = pkt[IP].src
        ttl = pkt[IP].ttl
        return ipsrc, ttl
    else:
        raise ValueError("The provided packet does not contain an IP layer.")


def flipped_interaction_4_testTTL(pkt):
    try:
        if IP in pkt:
            ipsrc = pkt[IP].src
            ttl = pkt[IP].ttl
            return (ipsrc, ttl)
        else:
            raise ValueError("The packet does not contain an IP layer.")
    except Exception as e:
        return f"Error processing packet: {str(e)}"


def flipped_interaction_5_testTTL(pkt):
    ipsrc = pkt[IP].src
    ttl = pkt[IP].ttl
    return ipsrc, ttl

def iterative_prompting_3_test_ttl(pkt):
    if pkt is None:
        raise ValueError("Packet cannot be None.")
    try:
        if IP in pkt:
            return pkt[IP].src, pkt[IP].ttl
    except Exception as e:
        print(f"Error extracting IP and TTL: {e}")
    return None


def iterative_prompting_4_test_ttl(pkt):
    if not hasattr(pkt, 'getlayer'):
        raise TypeError('Input must be a Scapy packet')
    try:
        ip_layer = pkt.getlayer('IP')
        if ip_layer is None:
            raise ValueError('Packet does not contain an IP layer')
    except Exception as e:
        raise RuntimeError(f'Error accessing packet layer: {e}')
    try:
        ipsrc = ip_layer.src
        ttl = ip_layer.ttl
    except AttributeError as e:
        raise RuntimeError(f'Error extracting IP src or TTL: {e}')
    return ipsrc, ttl

def iterative_prompting_5_test_ttl(pkt):
    if pkt is None:
        raise ValueError("Packet cannot be None.")
    try:
        if IP in pkt:
            return pkt[IP].src, pkt[IP].ttl
    except Exception:
        pass
    return None


def few_shots_prompting_testTTL(pkt):
    ipsrc = pkt[IP].src
    ttl = pkt[IP].ttl
    return ipsrc, ttl

def cot_prompting_testTTL(pkt):
    ipsrc = pkt[IP].src
    ttl = pkt[IP].ttl
    print(f'Source IP: {ipsrc}, TTL: {ttl}')

def fact_check_list_testTTL(pkt):
    if IP in pkt:
        ipsrc = pkt[IP].src
        ttl = pkt[IP].ttl
        return {"ipsrc": ipsrc, "ttl": ttl}
    else:
        return None

def not_interactive_mix_testTTL(pkt):
    try:
        import scapy.all as scapy
    except ImportError as e:
        raise ImportError("Scapy must be installed to use this function.") from e
    if not isinstance(pkt, scapy.IP):
        raise ValueError("The provided packet must be an IP packet.")
    try:
        ipsrc = pkt.src
        ttl = pkt.ttl
        return ipsrc, ttl
    except AttributeError as e:
        raise AttributeError("The given packet does not have IP fields.") from e

def interactive_mix_extract_ip_ttl(pkt):
    try:
        if IP in pkt:
            source_ip = pkt[IP].src
            ttl = pkt[IP].ttl
            return (source_ip, ttl)
        else:
            return (None, None)
    except Exception:
        return (None, None)

def baseline_testTTL(pkt):
    ipsrc = pkt["IP"].src
    ttl = pkt["IP"].ttl
    return ipsrc, ttl

