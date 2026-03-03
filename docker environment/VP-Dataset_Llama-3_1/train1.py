import nmap

class ScanException(Exception):
    pass

class HostDownException(Exception):
    pass

class PortScannerError(Exception):
    pass


def ground_truth_code_nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    return state

def persona_nmapScan(tgtHost, tgtPort):
	import nmap
	try:
		nmScan = nmap.PortScanner()
		nmScan.scan(tgtHost, tgtPort)
		state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
		return state
	except Exception as e:
		print(f'{e}')
		return 'Failed to retrieve the state'
      
def template_nmapScan(tgtHost, tgtPort):
    try:
        import subprocess
        resp = subprocess.check_output(['nmap', '-F', '-PN', tgtHost + '/' + tgtPort]).decode('utf-8')
        state = 'Open' if tgtPort in resp else 'Closed'
        print(resp)
        return state
    except subprocess.CalledProcessError as e:
        return(f'Scanning error: {e}')
    except Exception as e:
        return(f'An error occurred: {e}')
    

from json import dumps
def question_refinement_nmapScan(host, port):
    nm = nmap.PortScanner()
    nm.scan(hosts=host, ports=str(port), arguments="-sS -T5 --host-timeout 201")
    return {"port": port, "state": nm[host]["tcp"][port]["state"]}

def alternative_approaches_nmapScan(tgtHost, tgtPort):
    import nmap
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    return state


def context_manager_nmapScan(tgtHost, tgtPort):
    nm = nmap.PortScanner()
    nm.scan(hosts=tgtHost, arguments='-sT -p'+ tgtPort)
    state = nm[tgtHost]['tcp'][int(tgtPort)]['state']
    return state

def flipped_interaction_3__nmapScan(tgtHost, tgtPort):
    import nmap
    nmScanner = nmap.PortScanner()
    result = nmScanner.scan(tgtHost, str(tgtPort))
    state = result['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
    return state

def flipped_interaction_4__nmapScan(tgtHost, tgtPort):
	try:
		nm = nmap.PortScanner()
		nm.scan(tgtHost, str(tgtPort))
		scan_results = nm[tgtHost]['tcp'][int(tgtPort)]
		results = {
			'host': tgtHost,
			'port': tgtPort,
			'state': scan_results['state'],
			'service': scan_results.get('name', 'unknown'),
			'version': scan_results.get('version', 'unknown')
		}
		runtime = nm.get_nmap_last_output()
		start_idx = runtime.find('Initiating')
		end_idx = runtime.find('Scanning completed')
		runtime = runtime[start_idx:end_idx]
		time_taken = runtime.split('Seconds ')[1]
		results['scan_time'] = time_taken
		packet_loss_start_idx = runtime.find('packet loss =')
		packet_loss_end_idx = packet_loss_start_idx + len('packet loss = 100%')
		packet_loss = runtime[packet_loss_start_idx:packet_loss_end_idx]
		results['packet_loss'] = packet_loss
		split_runtime = runtime.split('\n')
		warnings_idx = [idx for idx, elt in enumerate(split_runtime) if elt.startswith('Warning')]
		results['warnings'] = split_runtime[warnings_idx[0]:]
		return results
	except nmap.PortScannerError as e:
		raise ScanException(f"Error occurred during scan: {e}")
	except KeyError:
		raise HostDownException(f"Target host {tgtHost} is down or unreachable")

def flipped_intercation_5__nmapScan(tgtHost, tgtPort):
        try:
            nmScan = nmap.PortScanner()
            nmScan.scan(tgtHost, tgtPort, '-sS')
            return nmScan[tgtHost]['tcp'][tgtPort]['state']
        except nmap.nmap.PortScannerError as e:
            raise PortScannerError('Exception occurred while scanning: {} {}', format(tgtHost, e))
        except ValueError as e:
            raise ValueError('Invalid port range: {} {}', format(tgtPort, e))
        except Exception as e:
            raise Exception('An unexpected error occurred while scanning: {} {}', format(tgtPort, e))
        
def iterative_prompting_3__nmapScan(tgtHost, tgtPort):
	import nmap
	import logging
	logging.basicConfig(level=logging.INFO)
	if not isinstance(tgtHost, str) or not isinstance(tgtPort, str):
		raise TypeError('Host and port must be strings')
	try:
		nmap_scanner = nmap.PortScanner()
		nmap_scanner.scan(hosts=tgtHost, arguments='-sT -p' + tgtPort +'--script-updatedb')
		if tgtHost not in nmap_scanner.all_hosts():
			raise ValueError('Host not found')
		if tgtPort not in nmap_scanner[tgtHost]['tcp']:
			raise ValueError('Port not found')
		state = nmap_scanner[tgtHost]['tcp'][int(tgtPort)]['state']
	except nmap.PortScannerError as e:
		logging.error(f'Nmap error: {e}')
		raise RuntimeError(f'Nmap error: {e}')
	except Exception as e:
		logging.error(f'Error: {e}')
		raise RuntimeError(f'Error: {e}')
	return state

def iterative_prompting_4__nmapScan(tgt_host, tgt_port):
	import importlib
	import nmap
	import logging
	logging.basicConfig(level=logging.INFO)
	if not isinstance(tgt_host, str) or not isinstance(tgt_port, int):
		return "Error: Invalid input type. Host should be string and port should be integer."
	try:
		nmap_spec = importlib.util.find_spec('python-nmap')
		if nmap_spec is None:
			logging.error("python-nmap library not installed")
			raise ImportError("python-nmap library not installed")
		nm_scan = nmap.PortScanner()
		nm_scan.scan(tgt_host, str(tgt_port))
		if tgt_host in nm_scan.all_hosts() and tgt_port in nm_scan[tgt_host]["tcp"]:
			state = nm_scan[tgt_host]['tcp'][tgt_port]['state']
			return state
		else:
			logging.warning("Scan result not found for host or port.")
			return "Error: Scan result not found for host or port."
	except nmap.PortScannerError as e:
		raise(f"Error: {e}")
      
def iterative_prompting_5__nmapScan(tgt_host, tgt_port):
    if not isinstance(tgt_host, str) or not isinstance(tgt_port, (int, str)):
        raise TypeError("Host and port must be string and integer/string respectively")
    if not tgt_host or not tgt_host.strip():
        raise ValueError("Host cannot be empty")
    if not tgt_port or not tgt_port.strip():
        raise ValueError("Port cannot be empty")
    try:
        nm_scan = nmap.PortScanner()
        result = nm_scan.scan(tgt_host, tgt_port)
        state = result['host'][tgt_host]['ports'][int(tgt_port)]['state']
        return state
    except nmap.PortScannerError as e:
        return f"PortScanner Error: {e}"
    except KeyError as e:
        return 'Error: Unable to get the state of the port'
    except Exception as e:
        return str(e)

def few_shots_prompting_nmapScan(tgtHost, tgtPort):
	args = '-sS -p'+ tgtPort
	result = nmap.scan(hosts=tgtHost, arguments=args)
	state = result['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
	return state

def cot_prompting_nmapScan(tgtHost, tgtPort):
	scanner = nmap.PortScanner()
	scanner.scan(hosts=tgtHost, ports=tgtPort)
	state = scanner[tgtHost]['tcp'][int(tgtPort)]['state']
	return state

def fact_check_list_nmapScan(tgtHost, tgtPort):
    try:
        nmScan = nmap.PortScanner()
        nmScan.scan(tgtHost, tgtPort, '-sT')
        state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
        return state
    except Exception as e:
        return str(e)

def not_interactive_mix_nmapScan(tgtHost, tgtPort):
    if not isinstance(tgtHost, str) or not (isinstance(tgtPort, int) and 0 <= tgtPort <= 65535):
        raise ValueError("Invalid input: tgtHost must be a string and tgtPort must be an integer between 0 and 65535")
    try:
        nmScan = nmap.PortScanner()
        nmScan.scan(tgtHost, str(tgtPort))
        state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
        return state
    except nmap.PortScannerError as e:
        raise e
    except KeyError as e:
        raise ValueError("Error: Host is down, port is not a TCP port or Port Scan not successful") 

def interactive_mix_nmapScan(tgtHost, tgtPort):
    try:
        if not isinstance(tgtPort, int) or tgtPort < 0 or tgtPort > 65535:
            raise ValueError("Invalid port number. Port must be an integer between 0 and 65535.")
        if not isinstance(tgtHost, str) or not tgtHost.replace('.', '', 4).isdigit() or len(tgtHost.split('.'))!= 4:
            raise ValueError("Invalid IP address. Must be a valid IPv4 address.")
        nmScan = nmap.PortScanner()
        nmScan.scan(tgtHost, str(tgtPort))
        if tgtHost in nmScan.all_hosts():
            state = nmScan[tgtHost]['tcp'][tgtPort]['state']
            return state
        else:
            return "Host not found."
    except nmap.PortScannerError:
        return "Nmap scan failed. Is Nmap installed and in the system's PATH?"
    except Exception as e:
        return f"An error occurred: {e}"

def baseline_nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    results = nmScan.scan(hosts=tgtHost, ports=tgtPort)
    state=results['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
    return state
