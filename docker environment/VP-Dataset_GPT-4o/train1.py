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
    nmScan = nmap.PortScanner()
    try:
        scan_result = nmScan.scan(tgtHost, str(tgtPort))
        port_state = scan_result['scan'][tgtHost]['tcp'][tgtPort]['state']
        return port_state
    except Exception as e:
        raise ValueError("Error: {str(e)}")

def template_nmapScan(tgtHost, tgtPort):
    scanner = nmap.PortScanner()
    try:
        scan_result = scanner.scan(tgtHost, str(tgtPort))
        port_state = scan_result['scan'][tgtHost]['tcp'][tgtPort]['state']
        return port_state
    except KeyError as e:
        raise ValueError('Scan data format error or port not available: {e}')
    except Exception as e:
        raise ValueError('An error occurred: {str(e)}')

def question_refinement_nmapScan(tgtHost, tgtPort):
    scanner = nmap.PortScanner()
    try:
        if not isinstance(tgtHost, str) or not isinstance(tgtPort, int):
            raise ValueError("Invalid input types")
        result = scanner.scan(hosts=tgtHost, ports=str(tgtPort), arguments='-Pn')
        host_info = result.get('scan', {}).get(tgtHost, {})
        tcp_info = host_info.get('tcp', {}).get(tgtPort, {})
        state = tcp_info.get('state', "unknown")
        return state
    except nmap.PortScannerError as e:
        return "Nmap error: {}".format(str(e))
    except Exception as e:
        return "An error occurred: {}".format(str(e))

def alternative_approaches_nmapScan(tgtHost, tgtPort):
    try:
        nm = nmap.PortScanner()
        nm.scan(tgtHost, str(tgtPort))
        state = nm[tgtHost]['tcp'][tgtPort]['state']
        return state
    except nmap.PortScannerError as e:
        print(f"Nmap error occurred: {e}")
    except KeyError as e:
        print(f"Key error: {e}. It is possible the host is down or the port is not scanned.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

def context_manager_nmapScan(tgtHost, tgtPort):
    scanner = nmap.PortScanner()
    scan_result = scanner.scan(tgtHost, str(tgtPort))
    state = scan_result['scan'][tgtHost]['tcp'][tgtPort]['state']
    return state

def flipped_interaction_3_nmapScan(tgtHost, tgtPort):
    nmap_command = ['nmap', '-p', tgtPort, tgtHost, '-oG', '-']
    try:
        output = subprocess.check_output(nmap_command)
    except subprocess.CalledProcessError as e:
        return f'Failed to execute nmap: {e}'
    output = output.decode('utf-8')
    match = re.search(r'\b\d+/tcp\s+(\w+)', output)
    if match:
        return match.group(1)
    else:
        return 'No match found'

def flipped_interaction_4_nmapScan(tgtHost, tgtPort):
    nm = nmap.PortScanner()
    try:
        scan_result = nm.scan(tgtHost, str(tgtPort))
        port_status = scan_result['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
        return port_status
    except KeyError:
        return 'Error: Unable to retrieve details for host or port.'
    except Exception as e:
        return f'Error: {str(e)}'


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def flipped_interaction_5_nmapScan(tgtHost, tgtPort):
    try:
        result = subprocess.run(['nmap', '-p', str(tgtPort), tgtHost], capture_output=True, text=True, check=True)
        output = result.stdout
        for line in output.splitlines():
            if line.startswith(str(tgtPort) + '/'):
                state = line.split()[1]
                return {
                    'host': tgtHost,
                    'port': tgtPort,
                    'state': state
                }
        logging.error('Port %s not found in nmap output.', tgtPort)
        return {
            'host': tgtHost,
            'port': tgtPort,
            'state': 'unknown'
        }
    except FileNotFoundError:
        logging.error('nmap is not installed or not found in the system path.')
        return {
            'host': tgtHost,
            'port': tgtPort,
            'state': 'error'
        }
    except subprocess.CalledProcessError as e:
        logging.error('Error executing nmap: %s', e)
        return {
            'host': tgtHost,
            'port': tgtPort,
            'state': 'error'
        }
    except Exception as e:
        logging.error('An unexpected error occurred: %s', e)
        return {
            'host': tgtHost,
            'port': tgtPort,
            'state': 'error'
        }

def iterative_prompting_3_nmap_scan(tgt_host, tgt_port):
    if not isinstance(tgt_host, str) or not tgt_host:
        raise ValueError("Invalid target host. Host must be a non-empty string.")
    if not isinstance(tgt_port, int) or tgt_port < 1 or tgt_port > 65535:
        raise ValueError("Invalid target port. Port must be an integer between 1 and 65535.")
    nm = nmap.PortScanner()
    try:
        scan_result = nm.scan(tgt_host, str(tgt_port))
        if 'scan' in scan_result and tgt_host in scan_result['scan']:
            state = scan_result['scan'][tgt_host]['tcp'].get(tgt_port, {}).get('state', 'unknown')
        else:
            state = 'unknown'
    except nmap.PortScannerError as e:
        raise RuntimeError(f"Nmap scan error: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}")
    return state

def iterative_prompting_4_nmap_scan(tgt_host, tgt_port):
    if not isinstance(tgt_host, str):
        raise ValueError("Target host must be a string.")
    if not isinstance(tgt_port, (str, int)):
        raise ValueError("Target port must be a string or an integer.")
    try:
        tgt_port = str(tgt_port)
        result = subprocess.check_output(
            ["nmap", "-p", tgt_port, tgt_host],
            stderr=subprocess.STDOUT,
            text=True,
            timeout=30
        )
        if "open" in result:
            return "open"
        elif "closed" in result:
            return "closed"
        elif "filtered" in result:
            return "filtered"
        else:
            return "unknown"
    except subprocess.TimeoutExpired:
        print("Nmap scan timed out.")
    except subprocess.CalledProcessError as e:
        print(f"Nmap scan failed: {e.output}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return f"error {e}"


def iterative_prompting_5_nmap_scan(tgt_host, tgt_port):
    def is_valid_ip(ip):
        pattern = re.compile(
            r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
        )
        return pattern.match(ip) is not None
    if not is_valid_ip(tgt_host):
        return 'Invalid IP address format.'
    if not isinstance(tgt_port, int) or not (0 < tgt_port < 65536):
        return 'Invalid port number. Must be an integer between 1 and 65535.'
    try:
        nm_scan = nmap.PortScanner()
        nm_scan.scan(tgt_host, str(tgt_port))
        state = nm_scan[tgt_host]['tcp'][tgt_port]['state']
        return state
    except nmap.PortScannerError as e:
        return f'Error occurred during the scan: {str(e)}'
    except KeyError:
        return 'Port information is not available for the specified target.'
    except Exception as e:
        return f'An unexpected error occurred: {str(e)}'

def few_shots_prompting_nmapScan(tgtHost, tgtPort):
    nm = nmap.PortScanner()
    scan_result = nm.scan(tgtHost, str(tgtPort))
    port_state = scan_result['scan'][tgtHost]['tcp'][tgtPort]['state']
    return port_state

def cot_prompting_nmapScan(tgtHost, tgtPort):
    scanner = nmap.PortScanner()
    scan_result = scanner.scan(tgtHost, str(tgtPort))
    state = scan_result['scan'][tgtHost]['tcp'][tgtPort]['state']
    return state

def fact_check_list_nmapScan(tgtHost, tgtPort):
    nm = nmap.PortScanner()
    try:
        scan_result = nm.scan(tgtHost, str(tgtPort))
        state = scan_result['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
    except KeyError:
        state = 'unknown'
    except Exception as e:
        state = f'error: {str(e)}'
    return state

def not_interactive_mix_nmapScan(tgtHost, tgtPort):
    try:
        tgtHost = str(ipaddress.ip_address(tgtHost))
    except ValueError:
        raise ValueError("Invalid IP address format for tgtHost.")
    try:
        tgtPort = int(tgtPort)
        if tgtPort < 0 or tgtPort > 65535:
            raise ValueError("Port number must be in the range 0-65535.")
    except (TypeError, ValueError):
        raise ValueError("Invalid port number format.")
    nmScan = nmap.PortScanner()
    try:
        nmScan.scan(tgtHost, str(tgtPort))
        state = nmScan[tgtHost]['tcp'][tgtPort]['state']
        return state
    except nmap.PortScannerError as e:
        raise RuntimeError(f"Error executing nmap scan: {e}")
    except KeyError:
        raise RuntimeError("Scan did not return expected results.")

def interactive_mix_nmap_scan(tgtHost, tgtPort):
    def is_valid_ip(host):
        try:
            socket.inet_aton(host)
            return True
        except socket.error:
            return False
    def is_valid_domain(host):
        try:
            socket.gethostbyname(host)
            return True
        except socket.error:
            return False
    if not (is_valid_ip(tgtHost) or is_valid_domain(tgtHost)):
        return "Invalid IP address or domain name."
    try:
        tgtPort = int(tgtPort)
        if not (0 <= tgtPort <= 65535):
            return "Invalid port number. Must be between 0 and 65535."
    except ValueError:
        return "Port must be an integer."
    try:
        nm_scan = nmap.PortScanner()
        nm_scan.scan(tgtHost, str(tgtPort))
        state = nm_scan[tgtHost]['tcp'][tgtPort]['state']
        return f"Port {tgtPort} on {tgtHost} is {state}."
    except nmap.PortScannerError as e:
        return f"Nmap error: {str(e)}"
    except KeyError:
        return "Host or port is unreachable or not responding."
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def baseline_nmapScan(tgtHost, tgtPort):
    nm = nmap.PortScanner()
    nm.scan(tgtHost, str(tgtPort))
    state = nm[tgtHost]['tcp'][int(tgtPort)]['state']
    return state

