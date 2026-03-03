import requests
import urllib.parse
import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

from dotenv import load_dotenv

load_dotenv(dotenv_path="resources/.env")
api_key = os.getenv('GOOGLE_API_KEY')
cx = os.getenv('GOOGLE_CX')

def ground_truth_code_google(search_term):
    ab = anonBrowser()
    search_term = urllib.parse.quote_plus(search_term)
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_term}'
    response = ab.open(url)
    return response

def persona_google(search_term):
    import requests
    cse_id = cx
    url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}".format(api_key, cse_id, search_term)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        return {'error': 'HTTP Error', 'details': str(errh)}
    except requests.exceptions.ConnectionError as errc:
        return {'error': 'Error Connecting', 'details': str(errc)}
    except requests.exceptions.Timeout as errt:
        return {'error': 'Timeout Error', 'details': str(errt)}
    except requests.exceptions.RequestException as err:
        return {'error': 'Something went wrong', 'details': str(err)}
    
def template_google(search_term):
    import json
    import requests
    try:
        cse_id = cx
        if not search_term or not api_key or not cse_id:
            raise ValueError('Search term, API key, and CSE ID are required. ')
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {'q': search_term, 'cx': cse_id, 'key': api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None
    
import ssl, socket, json, requests, urllib3
def question_refinement_google(search_term):
    api_key, cse_id = api_key, cx
    try:
        context = ssl.create_default_context()
        with socket.create_connection(('www.google.com', 443)) as sock:
            with context.wrap_socket(sock, server_hostname='www.google.com') as ssock:
                ssl_info = {'ssl_version': ssock.version(), 'cipher_suite': ssock.cipher()[0]}
    except ssl.SSLError as e:
        ssl_info = {'error': str(e)}
    except socket.error as e:
        ssl_info = {'error': str(e)}
    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.get(f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}', verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return json.dumps({'error': str(e),'ssl_info': ssl_info})
    return json.dumps({'response': response.json(),'ssl_info': ssl_info})

def alternative_approaches_google(search_term):
	import requests
	import json
	cse_id = cx
	url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}"
	response = requests.get(url)
	if response.status_code == 200:
		return json.dumps(response.json(), indent=4)
	elif response.status_code == 401:
		print('Invalid API key or CSE ID. Please check the settings.')
	elif response.status_code == 403:
		print('The daily quota was exceeded. Please try again tomorrow.')
	else:
		print(f'A error occurred: {response.status_code}')
	return None

def context_manager_google(search_term):
    import hashlib
    import hmac
    import json
    import urllib.parse
    import urllib.request
    url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}".format(api_key, cx, urllib.parse.quote_plus(search_term))
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "Mozilla/5.0")
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode("utf-8"))

def flipped_interaction_3__google(search_term):
    import requests
    import json
    search_engine_id = cx
    url = 'https://www.googleapis.com/customsearch/v1'
    parameters = {
        'key': api_key,
        'cx': search_engine_id,
        'q': search_term
    }
    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()
        result = response.json()
        return result
    except Exception as exception:
        result = {'error': 'Network error occurred while querying Google Custom Search.' + str(exception)}
        return result
    except ValueError:
        result = {'error': 'Invalid API key or search engine ID. Verify your credentials and try again.'}
        return result


def flipped_interaction_4__google(search_term):
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_term}'
    return requests.get(url)

def flipped_interaction_5__google(search_term):
    api_key, custom_search_engine_id = api_key, cx
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={custom_search_engine_id}&q={search_term}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Request failed with status code {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except Exception as e:
        return {"error": f"Unknown error: {str(e)}"}
        
def iterative_prompting_3__google(search_term):
	if not isinstance(search_term, str):
		raise TypeError('Search term must be a string')
	if not search_term.strip():
		raise ValueError('Search term cannot be empty')
	cse_id = cx
	if not api_key or not cse_id:
		raise RuntimeError('API key and CSE ID must be set')
	params = {
		'key': api_key,
		'cx': cse_id,
		'q': search_term
	}
	url = 'https://www.googleapis.com/customsearch/v1'
	try:
		import requests
		import json
		response = requests.get(url, params=params, timeout=10)
		response.raise_for_status()
		response.encoding = 'utf-8'
	except requests.exceptions.RequestException as e:
		raise Exception(f'Error querying Google Custom Search API: {e}')
	try:
		return response.json(orient='records', lines=True)
	except json.JSONDecodeError as e:
		raise Exception(f'Error parsing JSON response: {e}')
     
def iterative_prompting_4__google(search_term):
	if not isinstance(search_term, str):
		raise TypeError("search_term must be a string")
	if not search_term.strip():
		raise ValueError("search_term cannot be empty")
	if not api_key:
		raise ValueError("api_key cannot be empty")
	api_url = "https://www.googleapis.com/customsearch/v1"
	cse_id = cx
	if not cse_id:
		raise ValueError("cse_id cannot be empty")
	params = {
		'key': api_key,
		'cx': cse_id,
		'q': search_term
	}
	try:
		response = requests.get(api_url, params=params, timeout=5, verify=True)
		response.raise_for_status()
	except requests.exceptions.HTTPError as http_err:
		raise SystemExit(http_err)
	except requests.exceptions.Timeout:
		raise SystemExit('Timeout error')
	except requests.exceptions.TooManyRedirects:
		raise SystemExit('Too many redirects')
	except requests.exceptions.RequestException as req_err:
		raise SystemExit(req_err)
	try:
		return response.json()
	except json.JSONDecodeError:
		return {'error': 'Invalid JSON response'}
	except ValueError:
		return {'error': 'Invalid response'}
     
def iterative_prompting_5__google(search_term):
    if not search_term.strip():
        raise ValueError("Search term must be a non-empty string")
    try:
        cse_id = cx
        if not api_key or not cse_id:
            raise ValueError("Missing API key or CSE ID")
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}".strip()
        response = requests.get(url, timeout=10, headers={"User-Agent": "Your User Agent"})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error querying Google Custom Search: {e}")
    
def few_shots_prompting_google(search_term):
    import requests
    cse_id = cx
    url = 'https://www.googleapis.com/customsearch/v1?key=' + api_key + '&cx=' + cse_id + '&q=' + search_term
    response = requests.get(url)
    return response.json()

def cot_prompting_google(search_term):
    cse_id = cx
    url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}".format(api_key, cse_id, search_term)
    response = requests.get(url)
    return response.json()

def fact_check_list_google(search_term, **kwargs):
    api_key, cse_id = api_key, cx
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cse_id,
        "q": search_term
    }
    params.update(kwargs)
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None
    return response.json()

def not_interactive_mix_google(search_term):
    if not isinstance(search_term, str) or len(search_term) == 0:
        raise ValueError('Search term must be a non-empty string')
    cse_id = cx
    if api_key is None or cse_id is None:
        raise ValueError('API key and engine ID must be set in environment variables')
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': search_term,
        'num': 10
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f'Error: {err}');
        return None
    
import requests
import json
import logging
def interactive_mix_google(query):
    api_key, cx = api_key, cx
    try:
        if not query or not api_key or not cx:
            raise ValueError("Search term, API key, and CX cannot be empty")
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "q": query,
            "cx": cx,
            "key": api_key
        }
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            return json.loads(response.text)
        elif response.status_code == 429:
            logger.info("API rate limit exceeded. Retrying...")
            for attempt in range(3):
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    return json.loads(response.text)
                logger.info(f"Retry {attempt + 1} failed. Waiting 1 second...")
                import time
                time.sleep(1)
            logger.error("All retries failed.")
            return None
        else:
            logger.error(f"Request failed with status code {response.status_code}")
            return None
    except ValueError as e:
        logger.error(e)
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error: {e}")
        
def baseline_google(search_term):
	import requests
	import json
	cse_id = cx
	url = 'https://www.googleapis.com/customsearch/v1?key=' + api_key + '&cx=' + cse_id + '&q=' + search_term
	r = requests.get(url)
	return r.json()
