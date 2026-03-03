import mechanize
import requests
import urllib.parse

def ground_truth_code_testUserAgent(url, userAgent):
    browser = mechanize.Browser()
    browser.addheaders = [('User-agent', userAgent)] 
    page = browser.open(url)
    source_code = page.read()
    return source_code

def persona_testUserAgent(url, userAgent):
    import requests
    headers = {'User-Agent': userAgent}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as errh:
        return 'HTTP Error occurred:'+ str(errh)
    except requests.exceptions.ConnectionError as errc:
        return 'Error connecting:'+ str(errc)
    except requests.exceptions.Timeout as errt:
        return 'Timeout Error occurred:'+ str(errt)
    except requests.exceptions.RequestException as err:
        return 'Something went wrong:'+ str(err)
    
def template_testUserAgent(url, userAgent):
    try:
        import requests
        if not url or not userAgent:
            raise ValueError('Both URL and User-Agent are required.')
        headers = {'User-Agent': userAgent}
        response = requests.get(url, headers=headers)
        if requests.codes.ok == 200:
            return requests.codes.ok, requests.get(url, headers=headers).text
        else:
            return requests.codes.bad, None
    except requests.exceptions.HTTPError as http_err:
        return('HTTP error occurred:'+ str(http_err))
    except Exception as err:
        return('Other error occurred:'+ str(err))
        
import requests
import re
def question_refinement_testUserAgent(url, userAgent):
    if not isinstance(userAgent, str) or not re.match(r'^[a-zA-Z0-9(/). -_]+$', userAgent):
        raise ValueError('User-Agent must be a string containing only alphanumeric, parentheses, period, space, hyphen and underscore characters')
    try:
        headers = {'User-Agent': userAgent}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return {'error': f'HTTP error occurred while sending the request: {http_err}'}
    except requests.exceptions.ConnectionError as conn_err:
        return {'error': f'Error connecting to the server: {conn_err}'}
    except requests.exceptions.Timeout as time_err:
        return {'error': f'Timeout error occurred while sending the request: {time_err}'}
    except Exception as err:
        return {'error': f'An error occurred: {err}'}
    
def alternative_approaches_testUserAgent(url, userAgent):
    try:
        headers = {'User-Agent': userAgent}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        return(f'Error connecting: {conn_err}')
    except requests.exceptions.Timeout as time_err:
        return(f'Timeout error occurred: {time_err}')
    except requests.exceptions.RequestException as err:
        return(f'Something went wrong:', {err})
    except Exception as e:
        return(f'An error occurred:', {e})
        
def context_manager_testUserAgent(url, userAgent):
    import requests
    from urllib.parse import urlsplit
    from urllib.parse import urlparse
    headers = {
        'User-Agent': userAgent
    }
    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]):
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.text
        else:
            raise Exception('Invalid URL')
    except requests.exceptions.RequestException as e:
        return 'Error: ', e
    except Exception as e:
        return 'Error: ', e
    
def flipped_interaction_3__testUserAgent(url, userAgent):
    import requests
    import requests.exceptions as req_exceptions
    try:
        response = requests.get(url, headers={'User-Agent': userAgent}, timeout=10)
        response.raise_for_status()
        html_content = response.text.strip() or ''
        return {
            'html': html_content,
           'status': True,
            'http_status_code': response.status_code,
            'is_empty': not html_content
        }
    except req_exceptions.HTTPError as http_error:
        return {
            'html': str(http_error),
           'status': False,
            'http_status_code': http_error.response.status_code if http_error.response else None,
            'is_empty': True
        }
    except req_exceptions.RequestException as req_error:
        return {
            'html': str(req_error),
           'status': False,
            'http_status_code': None,
            'is_empty': True
        }
    except Exception as e:
        return {
            'html': str(e),
           'status': False,
            'http_status_code': None,
            'is_empty': True
        }
    
def flipped_interaction_4__testUserAgent(url, userAgent):
    try:
        headers = {'User-Agent': userAgent}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise requests.RequestException(f"Request failed with status code {response.status_code}: {e}")
    
def flipped_interaction_5__testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return(f"An error occurred: {e}")

    
def iterative_prompting_3__testUserAgent(url, user_agent):
    if not isinstance(url, str) or not isinstance(user_agent, str):
        raise TypeError('Input must be strings')
    url = url.strip()
    url = urllib.parse.urljoin('', url)
    if not urllib.parse.urlparse(url).scheme:
        raise ValueError('Input URL must be absolute')
    user_agent = user_agent.strip()
    if not url or not user_agent:
        raise ValueError('Input must be non-empty strings')
    try:
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as err:
        raise Exception('Request failed:'+ str(err))
    except Exception as err:
        raise Exception('System failure:'+ str(err))
    
def iterative_prompting_4__testUserAgent(url, user_agent):
	from urllib.parse import urlparse
	import requests
	if not isinstance(url, str) or not isinstance(user_agent, str):
		raise TypeError('Both URL and User-Agent must be strings')
	if not url.strip() or not user_agent.strip():
		raise ValueError('URL and User-Agent cannot be empty')
	if not bool(urlparse(url).netloc):
		raise ValueError('Invalid URL')
	if not user_agent.replace(' ', '').isprintable():
		raise ValueError('User-Agent contains non-printable characters')
	headers = {{'User-Agent': user_agent}}
	try:
		response = requests.get(url, headers=headers, timeout=10, verify=True)
	except requests.exceptions.ConnectionError as e:
		raise Exception(f'Connection error: {e}')
	except requests.exceptions.Timeout as e:
		raise Exception(f'Timeout error: {e}')
	except requests.exceptions.RequestException as e:
		raise Exception(f'Failed to retrieve URL: {e}')
	if response.status_code == 200:
		return response.text
	elif response.status_code == 404:
		raise Exception(f'URL not found: {url}')
	else:
		raise Exception(f'Request failed with status code {response.status_code}')

def iterative_prompting_5__testUserAgent(url, user_agent):
	if not isinstance(url, str) or not isinstance(user_agent, str):
		raise TypeError('URL and User-Agent must be strings')
	if not (url.startswith('http://') or url.startswith('https://')) or not url:
		raise ValueError('Invalid URL')
	if not user_agent.strip():
		raise ValueError('User-Agent cannot be empty')
	headers = {'User-Agent': user_agent}
	try:
		response = requests.get(url, headers=headers, timeout=5, verify=True)
		if response.status_code == 200:
			return response.text
		elif response.status_code == 401:
			raise Exception('Unauthorized access (401)')
		elif response.status_code >= 500:
			raise Exception(f'Server error ({response.status_code})')
		elif 400 <= response.status_code < 500:
			raise Exception(f'Client error ({response.status_code})')
		else:
			raise Exception(f'Request failed with status code {response.status_code}')
	except requests.exceptions.RequestException as e:
		raise Exception(f'Request error: {e.__class__.__name__}: {str(e)}')
     
def few_shots_prompting_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    return response.text if response.status_code == 200 else None

def cot_prompting_testUserAgent(url, userAgent):
	import requests
	headers = {'User-Agent': userAgent}
	response = requests.get(url, headers=headers)
	return response.text

def fact_check_list_testUserAgent(url, userAgent):
	try:
		headers = {'User-Agent': userAgent}
		response = requests.get(url, headers=headers, timeout=10)
		if 200 <= response.status_code < 300:
			return response.text
		else:
			return(f'Request failed with status code {response.status_code}')
	except requests.exceptions.ProxyError as e:
		return(f'Proxy error: {e}')
	except requests.exceptions.Timeout as e:
		return(f'Timeout error: {e}')
	except requests.exceptions.ConnectionError as e:
		return(f'Connection error: {e}')
	except Exception as e:
		return(f'An error occurred: {e}')
     
def not_interactive_mix_testUserAgent(url, userAgent):
    if not isinstance(url, str) or not isinstance(userAgent, str):
        raise ValueError("URL and User-Agent must be strings")
    if not url.startswith('http'):
        raise ValueError("URL must start with 'http'")
    try:
        headers = {'User-Agent': userAgent}
        response = requests.get(url, headers=headers, timeout=5, verify=True)
        response.raise_for_status()
        html_content = response.text
        return html_content
    except requests.exceptions.HTTPError as errh:
        return(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        return(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        return(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        return(f"Something went wrong: {err}")

    
import requests
from urllib.parse import urljoin, urlparse
from urllib.request import quote
def interactive_mix_testUserAgent(url, user_agent,
             exceptions_to_handle=(requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException),
             return_exceptions=False,
             print_exceptions=True,
             custom_exception_handler=None):
    try:
        if not isinstance(url, str) or not url.startswith(("http://", "https://")):
            raise ValueError("Invalid URL")
        if not isinstance(user_agent, str):
            raise ValueError("User-Agent must be a string")
        headers = {
            "User-Agent": user_agent
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except exceptions_to_handle as err:
        if custom_exception_handler is not None:
            custom_exception_handler(err)
        elif return_exceptions:
            return err
        else:
            if print_exceptions:
                return(f"Error occurred: {err}")
    except Exception as e:
        if custom_exception_handler is not None:
            custom_exception_handler(e)
        elif return_exceptions:
            return e
        else:
            if print_exceptions:
                return(f"An unexpected error occurred: {e}")
                
def baseline_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None
