import mechanize
from urllib.parse import urlparse

def ground_truth_code_viewPage(url):
    browser = mechanize.Browser()    
    browser.set_handle_robots(False)
    page = browser.open(url)
    source_code = page.read()
    return source_code

def persona__viewPage(url):
	import requests
	try:
		session = requests.Session()
		session.headers.update({'User-Agent': 'Mozilla/5.0'})
		response = session.get(url, timeout=10)
		if response.status_code == 200:
			return response.text
		else:
			return f"Failed to retrieve page: {response.status_code}"
	except requests.RequestException as e:
		return str(e)

def template__viewPage(url):
    import requests
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return None

def question_refinement__viewPage(url):
    try:
        from urllib.parse import urlparse
        from requests import get
        parsed_url = urlparse(url)
        if not (parsed_url.scheme in ['http', 'https'] and parsed_url.netloc):
            raise ValueError('Invalid URL')
        response = get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return str(e)

def alternative_approaches__viewPage(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'
    return response.text

def context_manager__viewPage(url):
	import urllib.request
	import ssl
	context = ssl.create_default_context()
	context.check_hostname = False
	context.verify_mode = ssl.CERT_NONE
	html = ''
	try:
		html = urllib.request.urlopen(url, context=context).read().decode('utf-8')
	except Exception as e:
		pass
	return html

def flipped_interaction_3__viewPage(url, headers=None, cookies=None, allow_redirects=True, timeout=10):
    try:
        response = requests.get(url, headers=headers, cookies=cookies, allow_redirects=allow_redirects, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def flipped_interaction_4__viewPage(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		return r.text
	except requests.exceptions.RequestException as e:
		return str(e)

def flipped_interaction_5__viewPage(url):
    try:
        response = requests.get(url, verify=True, allow_redirects=True)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

import requests

def iterative_prompting_3__viewPage(url):
    if not isinstance(url, str):
        return "Invalid URL: URL must be a string"
    if not url.startswith(("http://", "https://")):
        return "Invalid URL: URL must start with http:// or https://"
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        return "Request timed out"
    except requests.exceptions.TooManyRedirects:
        return "Too many redirects"
    except requests.exceptions.RequestException as e:
        return str(e)


def iterative_prompting_4__viewPage(url):
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL provided')
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'}, verify=True)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        raise Exception(f'HTTP error occurred: {str(http_err)}')
    except requests.exceptions.ConnectionError as conn_err:
        raise Exception(f'Connection error occurred: {str(conn_err)}')
    except requests.exceptions.Timeout as timeout_err:
        raise Exception(f'Timeout error occurred: {str(timeout_err)}')
    except requests.exceptions.RequestException as req_err:
        raise Exception(f'Other request error occurred: {str(req_err)}')
    return response.text

def iterative_prompting_5__viewPage(url):
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL format')
    try:
        response = requests.get(url, timeout=10, allow_redirects=False)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Request failed: {str(e)}')

def few_shots_prompting__viewPage(url):
	r = requests.get(url)
	return r.text

def cot_prompting__viewPage(url):
	import requests
	r = requests.get(url)
	return r.text

def fact_check_list__viewPage(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred: {e}")

def not_interactive_mix__viewPage(url):
    try:
        parsed_url = urlparse(url)
        if not (parsed_url.scheme == 'http' or parsed_url.scheme == 'https') or not parsed_url.netloc:
            raise ValueError("Invalid URL format")
        response = requests.get(url, verify=True, timeout=10)
        if response.status_code != 200:
            raise requests.exceptions.RequestException(f"Failed to retrieve page: HTTP {response.status_code}")
        return response.text
    except requests.exceptions.SSLError:
        return "SSL/TLS handshake failed"
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again later."
    except requests.exceptions.ConnectionError:
        return "Could not connect to the target server."
    except ValueError as ve:
        return str(ve)
    except requests.exceptions.RequestException as re:
        return str(re)

def interactive_mix__viewPage(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ('http', 'https') or not parsed_url.netloc:
            raise ValueError('Invalid URL')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers, verify=True, allow_redirects=True, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        return 'Request timed out'
    except requests.exceptions.RequestException as e:
        return f'HTTP Request failed: {e}'
    except ValueError as e:
        return f'Value error: {e}'

def baseline__viewPage(url):
	import requests
	html = requests.get(url).text
	return html
