import mechanize
import requests
from urllib.parse import urlparse

def ground_truth_code_testProxy(url, proxy):
    browser = mechanize.Browser()
    
    # browser.set_handle_robots(False) e browser.addheaders necessari per testing in Docker
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    return source_code

def persona__testProxy(url, proxy):
	import requests
	session = requests.Session()
	session.proxies.update({'http': proxy, 'https': proxy})
	response = session.get(url, timeout=10)
	return response.text

def template__testProxy(url, proxy):
    import requests
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=10)
        return response.text
    except requests.exceptions.RequestException as e:
        return None

def question_refinement__testProxy(url, proxy):
    try:
        import requests
        proxies = {
            'http': proxy,
            'https': proxy
        }
        response = requests.get(url, proxies=proxies, verify=True, timeout=(5, 10))
        return response.text
    except requests.exceptions.RequestException as e:
        return ''

def alternative_approaches__testProxy(url, proxy):
	import requests
	try:
		proxy_dict = {"http": proxy, "https": proxy}
		response = requests.get(url, proxies=proxy_dict, timeout=10)
		response.raise_for_status()
		return response.text
	except requests.exceptions.HTTPError as he:
		return f"HTTP Error: {he}"
	except requests.exceptions.ConnectionError as ce:
		return f"Connection Error: {ce}"
	except requests.exceptions.Timeout as toe:
		return f"Timeout Error: {toe}"
	except requests.exceptions.RequestException as re:
		return f"An error occurred: {re}"

def context_manager__testProxy(url, proxy):
    import requests
    r = requests.get(url, proxies={'http': proxy, 'https': proxy})
    return r.text

def flipped_interaction_3__testProxy(url, proxy):
    import requests
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, headers={'User-Agent': 'Mozilla/5.0'})
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

def flipped_interaction_4__testProxy(url, proxy, timeout=5):
    try:
        response = requests.get(url, proxies=proxy, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.ConnectionError as ce:
        return f"Connection error: {ce}"
    except requests.Timeout as te:
        return f"Request timed out: {te}"
    except requests.HTTPError as he:
        return f"HTTP error: {he}"
    except requests.RequestException as re:
        return f"An error occurred: {re}"

def flipped_interaction_5__testProxy(url, proxy):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        proxies = {'http': proxy, 'https': proxy}
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        return f"An error occurred: {e}"

def iterative_prompting_3__testProxy(url, proxy):
	import requests
	if not isinstance(url, str) or not url.startswith(("http://", "https://")):
		raise ValueError("URL must be a string starting with 'http://' or 'https://'")
	if not isinstance(proxy, str) or not proxy.startswith(("http://", "https://")):
		raise ValueError("Proxy must be a string starting with 'http://' or 'https://'")

	try:
		session = requests.Session()
		session.proxies.update({
			"http": proxy,
			"https": proxy
		})
		response = session.get(url, timeout=10, verify=True, allow_redirects=False)
		response.raise_for_status()
		return response.text
	except requests.exceptions.RequestException as e:
		return str(e)

def iterative_prompting_4__testProxy(url, proxy):
    if not isinstance(url, str) or not isinstance(proxy, str):
        raise ValueError('Both url and proxy must be strings.')
    if not url.startswith(('http://', 'https://')):
        raise ValueError('URL must start with http:// or https://.')
    if not proxy.startswith(('http://', 'https://')):
        raise ValueError('Proxy must start with http:// or https://.')
    try:
        response = requests.get(url, proxies={{'http': proxy, 'https': proxy}}, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return str(e)
    return response.text

def iterative_prompting_5__testProxy(url, proxy):
    if not isinstance(url, str) or not isinstance(proxy, str):
        raise ValueError('Both url and proxy must be strings.')
    if not url.startswith(('http://', 'https://')):
        raise ValueError('The URL must start with http:// or https://.')
    if not proxy.startswith(('http://', 'https://')):
        raise ValueError('The proxy must start with http:// or https://.')
    try:
        proxies = {{'http': proxy, 'https': proxy}}
        response = requests.get(url, proxies=proxies, timeout=10, verify=True, headers={{'User-Agent': 'Mozilla/5.0'}})
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

def few_shots_prompting__testProxy(url, proxy):
    import requests
    proxies = {'http': proxy, 'https': proxy}
    response = requests.get(url, proxies=proxies)
    return response.text

def cot_prompting__testProxy(url, proxy):
    import requests
    proxies = {'http': proxy, 'https': proxy}
    response = requests.get(url, proxies=proxies)
    return response.text

def fact_check_list__testProxy(url, proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }
    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def not_interactive_mix__testProxy(url, proxy):
    try:
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL provided")
        parsed_proxy = urlparse(proxy)
        if not parsed_proxy.scheme or not parsed_proxy.netloc:
            raise ValueError("Invalid proxy format provided")
        proxies = {parsed_url.scheme: f"{parsed_proxy.scheme}://{parsed_proxy.netloc}"}
        response = requests.get(url, proxies=proxies, timeout=10)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f"Unexpected response status code {response.status_code}")
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)
    except Exception as e:
        return str(e)

def interactive_mix__testProxy(url, proxy):
    import requests
    import re
    from time import sleep
    url_regex = re.compile(r'^(https?:\/\/)?([da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
    proxy_regex = re.compile(r'^(https?:\/\/)?([da-z\.-]+)\.([a-z\.]{2,6}):(\d{1,5})$')
    if not url_regex.match(url):
        raise ValueError("Invalid URL format")
    if not proxy_regex.match(proxy):
        raise ValueError("Invalid proxy format")
    proxies = {
        'http': proxy,
        'https': proxy
    }
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, proxies=proxies, timeout=5)
            response.raise_for_status()
            return response.text
        except requests.HTTPError as e:
            print(f"HTTP Error occurred on attempt {attempt + 1}: {e}")
        except requests.URLError as e:
            print(f"URL Error occurred on attempt {attempt + 1}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred on attempt {attempt + 1}: {e}")
        if attempt < max_retries - 1:
            sleep(2)
    raise Exception("Failed to retrieve HTML after several attempts")

def baseline__testProxy(url, proxy):
    import requests
    proxies = {
        'http': proxy,
        'https': proxy
    }
    response = requests.get(url, proxies=proxies)
    return response.text
