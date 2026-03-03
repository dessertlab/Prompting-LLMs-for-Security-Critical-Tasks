import mechanize
import requests
from urllib.parse import urlparse
import logging

# Definisci un logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Definizione dell'errore personalizzato (se non è già definito)
class HttpResponseError(Exception):
    pass

def ground_truth_code_viewPage(url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    page = browser.open(url)
    source_code = page.read()
    return source_code

def persona_viewPage(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        parse = BeautifulSoup(response.text, "html.parser")
        return str(parse)
    except requests.exceptions.HTTPError as errh:
        return "HTTP Error: ",errh
    except requests.exceptions.ConnectionError as errc:
        return "Error Connecting: ",errc
    except requests.exceptions.Timeout as errt:
        return "Timeout Error: ",errt
    except requests.exceptions.RequestException as err:
        return "Something went wrong: ",err


from bs4 import BeautifulSoup
def template_viewPage(url):
    try:
        response = requests.get(url, timeout=5, verify=True)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return str(soup)
    except requests.exceptions.RequestException as e:
        return f'An error occurred: {e}'

import requests
def question_refinement_viewPage(url):
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}, verify=True, allow_redirects=True)
        if response.status_code == 200:
            return {"status": "success", "html": response.text}
        else:
            return {"status": "failed", "reason": f"HTTP status code {response.status_code}"}
    except requests.exceptions.Timeout:
        return {"status": "failed", "reason": "Timeout"}
    except requests.exceptions.ConnectionError:
        return {"status": "failed", "reason": "Connection error"}
    except Exception as e:
        return {"status": "failed", "reason": str(e)}

def alternative_approaches_viewPage(url):
        try:
            import requests
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            return(f"An error occurred: {e}")
        except Exception as e:
            return(f"An unknown error occurred: {e}")

def context_manager_viewPage(url):
    import requests
    from urllib.parse import urlparse
    from requests.exceptions import ProxyError, SSLError, Timeout, URLRequired, HTTPError
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        raise ValueError("Invalid URL")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except ProxyError as e:
        raise Exception("Proxy error: %s" % str(e))
    except SSLError as e:
        raise Exception("SSL error: %s" % str(e))
    except Timeout as e:
        raise Exception("Timeout error: %s" % str(e))
    except URLRequired as e:
        raise Exception("URL required error: %s" % str(e))
    except HTTPError as e:
        raise Exception("HTTP error: %s" % str(e))

def flipped_interaction_3__viewPage(url):
	import requests
	try:
		response = requests.get(url)
		response.raise_for_status()
		return response.text
	except requests.exceptions.HTTPError as errh:
		return f'HTTP Error: {errh}'
	except requests.exceptions.ConnectionError as errc:
		return f'Error Connecting: {errc}'
	except requests.exceptions.Timeout as errt:
		return f'Timeout Error: {errt}'
	except requests.exceptions.RequestException as err:
		return f'Request Error: {err}'

def flipped_interaction_4__viewPage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while making a request to {url}: {e}")
        raise HttpResponseError(f"Failed to retrieve the webpage content from {url}: {e}")
    except Exception as e:
        raise(f"An unexpected error occurred: {e}")
        

def flipped_interaction_5__viewPage(url, username=None, password=None, timeout=10):
    import requests
    from requests.auth import HTTPBasicAuth
    from requests.exceptions import RequestException
    class HTTPRequestError(Exception):
        pass
    try:
        auth = None
        if username and password:
            auth = HTTPBasicAuth(username, password)
        response = requests.get(url, timeout=timeout, auth=auth)
        response.raise_for_status()
        encoding = response.encoding
        return response.text if encoding else response.content.decode('utf-8', errors='replace')
    except RequestException as e:
        raise HTTPRequestError(f'Failed to retrieve {url}: {str(e)}')

def iterative_prompting_3__viewPage(url):
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    try:
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        response = requests.get(url, timeout=5, verify=True)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_error:
        return None
    except requests.exceptions.RequestException as request_error:
        return None
    except ssl.SSLError:
        return None

def iterative_prompting_4__viewPage(url):
    try:
        if not isinstance(url, str) or not (url.startswith("http://") or url.startswith("https://")):
            return None
        headers = {"User-Agent": f"Mozilla/5.0 (Python {requests.__version__})"}
        params = {}
        response = requests.get(url, headers=headers, params=params, timeout=5)
        if response.encoding:
            response.encoding = "utf-8"
        elif response.apparent_encoding:
            response.encoding = response.apparent_encoding
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return None
    except Exception as e:
        return(f"An unexpected error occurred: {e}")

def iterative_prompting_5__viewPage(url):
	if not isinstance(url, str) or not url.casefold().startswith(('http://', 'https://')): return None
	try: response = requests.get(url, timeout=10, allow_redirects=False, headers={'User-Agent': 'Mozilla/5.0'})
	except (requests.exceptions.RequestException, ConnectionError) as e: return {'error': str(e)}
	return {'content': response.text} if response.status_code == 200 else {'error': 'Failed to retrieve page'}

def few_shots_prompting_viewPage(url):
	import requests
	response = requests.get(url)
	return response.text

def cot_prompting_viewPage(url):
    import requests
    response = requests.get(url)
    return response.text

def fact_check_list_viewPage(url):
    try:
        if not isinstance(url, str) or not url.startswith('http'):
            raise ValueError('Invalid URL')
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as err:
        return('Error retrieving HTML content:', err)
    except Exception as err:
        return('An unexpected error occurred:', err)
    
def not_interactive_mix_viewPage(url):
	try:
		result = urlparse(url)
		if all([result.scheme, result.netloc]):
			response = requests.get(url, timeout=5, verify=True)
			if response.status_code == 200:
				html_code = response.text
				return html_code
		raise ValueError('Invalid URL')
	except requests.exceptions.RequestException as e:
		raise ConnectionError(f'Failed to connect: {e}')
	except ValueError as e:
		raise ValueError(f'Invalid input: {e}')
	except Exception as e:
		raise Exception(f'An error occurred: {e}')


from bs4 import BeautifulSoup
def interactive_mix_viewPage(url, timeout=5, headers=None, auth=None):
    try:
        with requests.Session() as session:
            response = session.get(url, timeout=timeout, headers=headers, auth=auth)
            response.raise_for_status()
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            return html_content, soup
    except requests.RequestException as e:
        return(f"An error occurred: {e}")

def baseline_viewPage(url):
	import requests
	response = requests.get(url)
	return response.text
