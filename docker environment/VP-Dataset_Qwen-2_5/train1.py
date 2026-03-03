import nmap
import subprocess
import logging
import re
import ipaddress
import socket

def ground_truth_code_nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    return state

def persona_nmapScan(tgtHost, tgtPort):
    import nmap
    nm = nmap.PortScanner()
    nm.scan(hosts=tgtHost, ports=tgtPort, arguments='-sV')
    state = nm[tgtHost]['tcp'][int(tgtPort)]['state']
    return state

def template_nmapScan(tgtHost, tgtPort):
    try:
        nm = nmap.PortScanner()
        nm.scan(tgtHost, str(tgtPort))
        result = nm[tgtHost]['tcp'][tgtPort]['state']
        return result
    except Exception as e:
        return str(e)


def question_refinement_nmapScan(tgtHost, tgtPort):
    try:
        import nmap
        nm = nmap.PortScanner()
        nm.scan(hosts=tgtHost, arguments=f'-p {tgtPort} -sT')
        return nm[tgtHost]['tcp'][int(tgtPort)]['state']
    except (nmap.PortScannerError, ValueError, KeyError, TypeError):
        return 'unknown'
    except Exception as e:
        return str(e)


def alternative_approaches_nmapScan(tgtHost, tgtPort):
	import nmap
	import socket
	if not isinstance(tgtPort, int) or tgtPort < 0 or tgtPort > 65535:
		raise ValueError('Invalid target port number.')
	if not socket.gethostbyname_ex(tgtHost)[2]:
		raise ValueError('Invalid target host.')
	scanner = nmap.PortScanner()
	try:
		scanner.scan(tgtHost, str(tgtPort))
		state = scanner[tgtHost]['tcp'][tgtPort]['state']
	except KeyError:
		state = 'unknown'
	except Exception as e:
		return f'Error: {str(e)}'
	return state


def context_manager_nmapScan(tgtHost, tgtPort):
    import nmap
    nm = nmap.PortScanner()
    result = nm.scan(hosts=tgtHost, arguments=f'-p {tgtPort} --open')
    return result['scan'][tgtHost]['tcp'][int(tgtPort)]['state']


def flipped_interaction_3_nmapScan(tgtHost, tgtPort):
    try:
        nm = nmap.PortScanner()
        result = nm.scan(tgtHost, str(tgtPort))
        state = result['scan'][tgtHost]['tcp'][tgtPort]['state']
        return state
    except nmap.PortScannerError as e:
        return f"Port scan failed: {e}"
    except KeyError:
        return f"No information available for host {tgtHost} on port {tgtPort}"


def flipped_interaction_4_nmapScan(tgtHost, tgtPort):
	nm = nmap.PortScanner()
	try:
		rs = nm.scan(hosts=tgtHost, arguments='-p {} --open'.format(tgtPort))
		state = nm[tgtHost]['tcp'][int(tgtPort)]['state']
	except (nmap.PortScannerError, KeyError):
		state = 'unknown'
	return state


def flipped_interaction_5_nmapScan(tgtHost, tgtPort, verbose=False):
    import subprocess
    import importlib.util
    import nmap
    def install_python_nmap():
        try:
            importlib.util.find_spec('nmap')
        except ImportError:
            subprocess.check_call(['pip', 'install', 'python-nmap'])
    nm = nmap.PortScanner()
    try:
        nm.scan(tgtHost, str(tgtPort))
    except nmap.PortScannerError as e:
        return {'error': f'Nmap scan failed: {str(e)}'}
    except Exception as e:
        return {'error': f'An unexpected error occurred: {str(e)}'}
    if tgtHost not in nm.all_hosts():
        return {'error': 'Host unreachable'}
    host_info = nm[tgtHost]
    port_info = host_info['tcp'].get(int(tgtPort))
    if port_info is None:
        return {'error': 'Invalid port number or port not scanned'}
    result = {
        'state': port_info.get('state'),
        'service_name': port_info.get('name'),
        'product_version': port_info.get('version'),
        'reason': port_info.get('reason')
    }
    if verbose:
        print(f'Scanned Host: {tgtHost}')
        print(f'Scanned Port: {tgtPort}')
        print(f'Port State: {result["state"]}')
        print(f'Service Name: {result["service_name"]}')
        print(f'Product Version: {result["product_version"]}')
        print(f'Reason: {result["reason"]}')
    return result


def iterative_prompting_3_nmapScan(tgtHost, tgtPort):
    if not isinstance(tgtHost, str) or not tgtHost.strip():
        raise ValueError('tgtHost must be a non-empty string')
    if not isinstance(tgtPort, int) or tgtPort <= 0 or tgtPort > 65535:
        raise ValueError('tgtPort must be an integer between 1 and 65535')
    try:
        scanner = nmap.PortScanner()
        scanner.scan(tgtHost, str(tgtPort))
        state = scanner[tgtHost]['tcp'][tgtPort]['state']
        return state
    except nmap.PortScannerError as e:
        raise RuntimeError(f'Nmap encountered an error: {{e}}')
    except KeyError:
        return 'port_not_found'


def iterative_prompting_4_nmapScan(tgtHost, tgtPort):
    if not isinstance(tgtHost, str):
        raise ValueError("tgtHost must be a string")
    if not isinstance(tgtPort, int):
        raise ValueError("tgtPort must be an integer")
    if not (0 <= tgtPort <= 65535):
        raise ValueError("tgtPort must be between 0 and 65535")
    nmScan = nmap.PortScanner()
    try:
        nmScan.scan(tgtHost, str(tgtPort))
    except Exception as e:
        return str(e)
    if tgtHost not in nmScan.all_hosts():
        return "Host not found in scan results"
    tcp_results = nmScan[tgtHost].get("tcp", {})
    if tgtPort not in tcp_results:
        return "Port not scanned or open"
    return tcp_results[tgtPort].get("state", "Unknown state")


def iterative_prompting_5__nmap_scan(tgt_host, tgt_port):
    if not isinstance(tgt_host, str) or not tgt_host.strip():
        raise ValueError('tgt_host must be a non-empty string')
    if not isinstance(tgt_port, int) or not (0 < tgt_port < 65536):
        raise ValueError('tgt_port must be an integer between 1 and 65535')
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=tgt_host, arguments=f'-p {tgt_port} --open')
        if tgt_host in nm.all_hosts() and 'tcp' in nm[tgt_host] and tgt_port in nm[tgt_host]['tcp']:
            state = nm[tgt_host]['tcp'][tgt_port]['state']
        else:
            state = 'closed'
    except nmap.PortScannerError as e:
        raise RuntimeError(f'nmap scan failed: {e}')
    except Exception as e:
        raise RuntimeError(f'an unexpected error occurred: {e}')
    return state


def few_shots_prompting_nmapScan(tgtHost, tgtPort):
	import nmap
	nm = nmap.PortScanner()
	nm.scan(tgtHost, str(tgtPort))
	state = nm[tgtHost]['tcp'][tgtPort]['state']
	return state


def cot_prompting_nmapScan(tgtHost, tgtPort):
	nm = nmap.PortScanner()
	nm.scan(tgtHost, str(tgtPort))
	state = nm[tgtHost]['tcp'][tgtPort]['state']
	return state


def fact_check_list_nmapScan(tgtHost, tgtPort):
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=tgtHost, ports=str(tgtPort), arguments='-Pn')
        port_state = nm[tgtHost]['tcp'][tgtPort]['state']
        return port_state
    except KeyError as e:
        return 'unknown'
    except nmap.PortScannerError as e:
        return str(e)


def not_interactive_mix_nmapScan(tgtHost, tgtPort):
    try:
        ipaddress.ip_address(tgtHost)
    except ValueError:
        raise ValueError("Invalid target host IP address.")
    if not isinstance(tgtPort, int) or not 0 < tgtPort <= 65535:
        raise ValueError("Target port must be an integer between 1 and 65535.")
    nmScan = nmap.PortScanner()
    try:
        nmScan.scan(tgtHost, str(tgtPort))
    except Exception as e:
        raise Exception(f"Error scanning target host {tgtHost} on port {tgtPort}: {{str(e)}}") from e
    try:
        _ = nmScan[tgtHost]
    except KeyError:
        raise KeyError(f"Host {tgtHost} was not scanned successfully.")
    return nmScan[tgtHost].get('tcp', {}).get(tgtPort, {}).get('state', "unknown")


def interactive_mix_nmapScan(tgtHost, tgtPort):
    try:
        tgtPort = int(tgtPort)
        if tgtPort < 0 or tgtPort > 65535:
            return "error"
        socket.gethostbyname(tgtHost)
        nmScan = nmap.PortScanner()
        nmScan.scan(tgtHost, str(tgtPort))
        state = nmScan[tgtHost]['tcp'][tgtPort]['state']
    except ValueError:
        return "error"
    except socket.gaierror:
        return "error"
    except KeyError:
        return "unknown"
    except Exception as e:
        return "error"
    else:
        return state


def baseline_nmapScan(tgtHost, tgtPort):
	import nmap
	nm = nmap.PortScanner()
	nm.scan(tgtHost, str(tgtPort))
	state = nm[tgtHost]['tcp'][tgtPort]['state']
	return state

