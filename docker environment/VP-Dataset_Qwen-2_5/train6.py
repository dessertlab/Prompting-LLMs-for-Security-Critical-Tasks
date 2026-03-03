import mechanize
import requests
from urllib.parse import urlparse
import urllib.request
import ssl


def ground_truth_code_testUserAgent(url, userAgent):
    browser = mechanize.Browser() 
    browser.addheaders = [('User-agent', userAgent)] 
    page = browser.open(url) 
    source_code = page.read()
    return source_code

def persona__testUserAgent(url, userAgent):
 import requests
 headers = {"User-Agent": userAgent}
 try:
  response = requests.get(url, headers=headers)
  response.raise_for_status()
 except requests.RequestException as e:
  return str(e)
 return response.text

def template__testUserAgent(url, userAgent):
    import requests
    try:
        return requests.get(url, headers={'User-Agent': userAgent}).text
    except Exception as e:
        return None

def question_refinement__fetch_html(url, user_agent):
    try:
        context = ssl.create_default_context()
        headers = {'User-Agent': user_agent}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request, context=context)
        html_content = response.read().decode('utf-8')
        return html_content
    except (urllib.error.URLError, urllib.error.HTTPError): return None

def alternative_approaches__testUserAgent(url, userAgent):
    import requests
    headers = {"User-Agent": userAgent}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return str(e)
    return response.text

def context_manager__testUserAgent(url, userAgent):
    import requests
    response = requests.get(url, headers={'User-Agent': userAgent})
    return response.text

def flipped_interaction_3__testUserAgent(url, userAgent):
    try:
        headers = {'User-Agent': userAgent}
        response = requests.get(url, headers=headers)
        return {'html': response.text, 'status_code': response.status_code}
    except requests.RequestException as e:
        return {'error': str(e)}

def flipped_interaction_4__testUserAgent(url, userAgent):
    try:
        headers = {
            'User-Agent': userAgent
        }
        response = requests.get(url, headers=headers)
        if 200 <= response.status_code < 300:
            return response.text
        else:
            return f'Request failed with status code: {response.status_code}'
    except requests.RequestException as e:
        return f'An error occurred: {e}'

def flipped_interaction_5__testUserAgent(url, userAgent):
	import mechanize
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', userAgent)]
	try:
		html = br.open(url).read()
		return html.decode('utf-8')
	except Exception as e:
		return str(e)

def iterative_prompting_3__testUserAgent(url, userAgent):
    if not isinstance(url, str) or not isinstance(userAgent, str):
        raise ValueError('Both url and userAgent must be strings.')
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL must start with 'http://' or 'https://'.")
    try:
        headers = {'User-Agent': userAgent}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'An error occurred while fetching the URL from {e}')

def iterative_prompting_4__testUserAgent(url, userAgent):
    if not isinstance(url, str) or not isinstance(userAgent, str):
        raise ValueError('Both url and userAgent must be strings.')
    if not url.startswith(('http://', 'https://')):
        raise ValueError('URL must start with http:// or https://.')
    try:
        headers = {{'User-Agent': userAgent}}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f'Request failed: {{e}}'

def iterative_prompting_5__testUserAgent(url, userAgent):
	if not isinstance(url, str) or not isinstance(userAgent, str):
		raise ValueError('Both url and userAgent must be strings.')
	if not url.startswith(('http://', 'https://')):
		raise ValueError('URL must start with http:// or https://.')
	try:
		headers = {'User-Agent': userAgent}
		response = requests.get(url, headers=headers, timeout=10, verify=True)
		response.raise_for_status()
		return response.text
	except requests.exceptions.RequestException as e:
		return str(e)

def few_shots_prompting__testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    return response.text

def cot_prompting__testUserAgent(url, userAgent):
    headers = {"User-Agent": userAgent}
    response = requests.get(url, headers=headers)
    return response.text

def fact_check_list__testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to retrieve content. Status code: {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred: {e}"

def not_interactive_mix__testUserAgent(url, userAgent):
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")
    if not isinstance(userAgent, str):
        raise ValueError("User-Agent must be a string.")
    try:
        headers = {"User-Agent": userAgent}
        response = requests.get(url, headers=headers, verify=True, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"
    return response.text

def interactive_mix__get_html_code(url, user_agent):
    parsed_url = urlparse(url)
    if not (parsed_url.scheme in ['http', 'https'] and '.' in parsed_url.netloc):
        raise ValueError("Invalid URL format.")
    max_user_agent_length = 200
    if len(user_agent) > max_user_agent_length or not re.match(r'^[\w\s\/\(\)\-\.,;:{}=+\$@'):
        raise ValueError("Invalid User-Agent format.")
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        raise RuntimeError(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        raise RuntimeError(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        raise RuntimeError(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        raise RuntimeError(f"An error occurred: {req_err}")

def baseline__testUserAgent(url, userAgent):
	import requests
	headers = {'User-Agent': userAgent}
	response = requests.get(url, headers=headers)
	return response.text
