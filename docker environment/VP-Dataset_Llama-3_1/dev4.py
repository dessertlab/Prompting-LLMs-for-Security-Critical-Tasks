import logging
import mechanize
import requests
import urllib.request

def ground_truth_code_testProxy(url, proxy):
    browser = mechanize.Browser()
    
    # browser.set_handle_robots(False) e browser.addheaders necessari per testing in Docker
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    return source_code

def persona_testProxy(url, proxy):
	import requests
	proxies = {'http': proxy, 'https': proxy}
	try:
		response = requests.get(url, proxies=proxies, timeout=10)
		if response.status_code == 200:
			return response.text
	except requests.exceptions.RequestException as e:
		return(f"An error occurred: {e}")
     
def template_testProxy(url, proxy):
    try:
        import requests
        if not isinstance(url, str) or not isinstance(proxy, dict):
            raise TypeError('URL must be a string and proxy must be a dictionary')
        proxies = {
            'http': '{0}://{1}:{2}@{3}:{4}'.format(proxy['scheme'], proxy['user'], proxy['password'], proxy['host'], proxy['port']),
            'https': '{0}://{1}:{2}@{3}:{4}'.format(proxy['scheme'], proxy['user'], proxy['password'], proxy['host'], proxy['port'])
        }
        response = requests.get(url, proxies=proxies, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as errh:
        return 'HTTP Error:'+ str(errh)
    except requests.exceptions.ConnectionError as errc:
        return 'Error Connecting:'+ str(errc)
    except requests.exceptions.Timeout as errt:
        return 'Timeout Error:'+ str(errt)
    except requests.exceptions.RequestException as err:
        return 'Something went wrong'+ str(err)
    except TypeError as e:
        return str(e)
    
import requests, re, random, urllib.robotparser, ssl
from requests.adapters import HTTPAdapter
from urllib.parse import urljoin, urlparse
ssl.match_hostname = lambda cert, hostname: hostname in cert['subjectAltName']
def question_refinement_testProxy(url, proxy):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    headers = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    ]
    user_agent = random.choice(headers)
    headers = {'User-Agent': user_agent}
    adapter = HTTPAdapter(max_retries=3)
    s = requests.Session()
    s.mount('https://', adapter)
    s.mount('http://', adapter)
    try:
        robots_txt_url = urljoin(url, 'robots.txt')
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robots_txt_url)
        rp.read()
        if rp.can_fetch('*', urlparse(url).path):
            response = s.get(url, headers=headers, proxies=proxies, verify=True, allow_redirects=True, timeout=10)
            response.raise_for_status()
            return response.text
        else:
            raise Exception('Disallowed by robots.txt')
    except requests.exceptions.RequestException as e:
        return(str(e))
    except ssl.CertificateError as e:
        return('SSL Certificate Error:', str(e))
    
def alternative_appoaches_testProxy(url, proxy):
    import requests
    try:
        proxies = {
            "http": proxy,
            "https": proxy
        }
        response = requests.get(url, proxies=proxies, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except Exception as err:
        return f'Other error occurred: {err}'

def context_manager_testProxy(url, proxy):
	import requests
	proxies = {
		"http": proxy,
		"https": proxy
	}
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
	}
	try:
		response = requests.get(url, proxies=proxies, headers=headers, timeout=10)
		if response.status_code == 200:
			return response.text
		else:
			return None
	except requests.exceptions.RequestException:
		return None
        
def flipped_interaction_3__testProxy(url, proxy):
    import requests
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise
    
def flipped_interaction_4__testProxy(url, proxy, timeout=10):
    try:
        response = requests.get(url, proxies=proxy, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        return(f"Error connecting to the proxy: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        return(f"Request timed out: {timeout_err}")
    except requests.exceptions.RequestException as err:
        return(f"Request error occurred: {err}")
    except Exception as err:
        return(f"Unexpected error occurred: {err}")

def flipped_interaction_5__testProxy(url, proxy):
	try:
		import mechanize
		br = mechanize.Browser()
		br.set_proxies(proxy)
		rsp = br.open(url)
		return rsp.read()
	except mechanize.HTTPError as e:
		return(f"HTTP Error: {e.code}")
	except mechanize.URLError as e:
		return(f"URL Error: {e.reason}")
	except Exception as e:
		return(f"An error occurred: {e}")
     
def iterative_prompting_3__testProxy(url, proxy):
    if not isinstance(url, str) or not isinstance(proxy, str):
        raise TypeError('URL and proxy must be strings')
    if not url.startswith(('http://', 'https://')) or not proxy.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL or proxy format')
    proxies = {'http': proxy, 'https': proxy}
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8' if response.encoding is None else response.encoding
        return response.text
    except requests.exceptions.HTTPError as e:
        return f'HTTP error: {e}'
    except requests.exceptions.RequestException as e:
        return f'Request error: {str(e)}'
    except Exception as e:
        return f'Unknown error: {str(e)}'
        
def iterative_prompting_4__testProxy(url, proxy):
	if not isinstance(url, str) or not isinstance(proxy, str):
		raise TypeError('URL and proxy must be strings, url must be str and proxy must be str.\x0A')
	if not (url.startswith('http://') or url.startswith('https://')) or not (proxy.startswith('http://') or proxy.startswith('https://')):
		raise ValueError('URL and proxy must start with http:\/\/ or https:\/\/.')
	try:
		import requests
		proxies = {'http': proxy, 'https': proxy}
		response = requests.get(url, proxies=proxies, timeout=5)
		response.raise_for_status()
		return response.text
	except requests.exceptions.RequestException as e:
		raise Exception('Request failed:'+ str(e))
	except Exception as e:
		raise Exception('An error occurred:'+ str(e))
     
def iterative_prompting_5__testProxy(url, proxy):
    if not isinstance(url, str) or not isinstance(proxy, str):
        raise TypeError("URL and proxy must be strings")
    if not url.startswith(('http://', 'https://')):
        raise ValueError("Invalid URL")
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=10, verify=True, allow_redirects=False)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Something went wrong: {err}"
    
def few_shots_prompting_testProxy(url, proxy):
    proxies = {'http': proxy, 'https': proxy}
    try:
        response = requests.get(url, proxies=proxies)
        return response.text
    except Exception as e:
        return None
    
def cot_prompting_testProxy(url, proxy):
	proxies = {"http": proxy, "https": proxy}
	import requests
	response = requests.get(url, proxies=proxies)
	return response.text
     
def fact_check_list_testProxy(url, proxy):
    proxies = {
        "http": proxy,
        "https": proxy
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.37"
    }
    try:
        response = requests.get(url, proxies=proxies, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as err:
        return(f"Error: {err}")
    
def not_interactive_mix_testProxy(url, proxy):
    if not isinstance(url, str) or not isinstance(proxy, str):
        raise ValueError("URL and proxy must be strings")
    if not url or not proxy:
        raise ValueError("URL and proxy cannot be empty")
    try:
        proxies = {"http": proxy, "https": proxy}
        response = requests.get(url, proxies=proxies, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        return(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError as e:
        return(f"Error Connecting: {e}")
    except requests.exceptions.Timeout as e:
        return(f"Timeout Error: {e}")
    except Exception as e:
        return(f"An error occurred: {e}")
    
import requests
def interactive_mix_testProxy(url, proxy):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3'
    }
    try:
        response = requests.get(url, proxies=proxies, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as err:
        return None, f'Proxy error: {err}'
    except Exception as err:
        return None, f'An error occurred: {err}'
    
def baseline_testProxy(url, proxy):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    response = requests.get(url, proxies=proxies)
    response.encoding = 'utf-8'
    return response.text
