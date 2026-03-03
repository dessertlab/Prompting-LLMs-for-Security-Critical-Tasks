import json
import requests
import urllib.parse
import urllib3
import urllib.request
import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

from dotenv import load_dotenv

load_dotenv(dotenv_path="resources/.env")
api_key = os.getenv('GOOGLE_API_KEY')
cx = os.getenv('GOOGLE_CX')

class Google_Result:
    def __init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def __repr__(self):
        return self.title

def ground_truth_code_google(search_term):
    ab = anonBrowser()
    search_term = urllib.parse.quote_plus(search_term)
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_term}'
    response = ab.open(url)
    objects = json.load(response)
    return objects

def persona_google(search_term):
    import json
    import urllib.request
    cse_id = cx
    query = urllib.parse.quote(search_term)
    url = 'https://www.googleapis.com/customsearch/v1?key=%s&q=%s&cx=%s' % (api_key, query, cse_id)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode('utf-8'))

def template_google(search_term):
    import requests
    import json
    cse_id = cx
    try:
        url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        raise ValueError(f'HTTP Error occurred: {errh}')
    except requests.exceptions.ConnectionError as errc:
        raise ValueError(f'Error connecting: {errc}')
    except requests.exceptions.Timeout as errt:
        raise ValueError(f'Timeout Error occurred: {errt}')
    except requests.exceptions.RequestException as err:
        raise ValueError(f'Ooops something went wrong: {err}')
    
def question_refinement_google(search_term):
    import requests
    import json
    try:
        url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_term}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        if 'application/json' in response.headers.get('Content-Type', ''):
            return response.json()
        else:
            raise Exception('Unexpected response format')
    except requests.exceptions.HTTPError as http_err:
        error_response = json.loads(http_err.response.text)
        if 'error' in error_response and 'code' in error_response['error'] and error_response['error']['code'] == 429:
            return { 'error': 'API Quota exceeded' }
        else:
            raise Exception(f'HTTP Error - {http_err}')
    except requests.exceptions.RequestException as req_err:
        raise Exception(f'Request Exception - {req_err}')
    except json.JSONDecodeError as json_err:
        raise Exception(f'JSON Decode Error - {json_err}')
    except Exception as err:
        raise Exception(f'An error occurred - {err}')

def alternative_approaches_google(search_term):
    import requests
    import json
    try:
        cse_id = cx
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}"
        response = requests.get(url, proxies={})
        if response.status_code == 200:
            return json.dumps(response.json(), indent=4)
        else:
            return json.dumps({"error": "Failed to retrieve data"})
    except requests.exceptions.RequestException as e:
        return json.dumps({"error": f"An error occurred: {e}"})
    except Exception as e:
        return json.dumps({"error": f"An error occurred: {e}"})

import requests
import hashlib
import hmac
import time
import urllib.parse
def context_manager_google(search_term):
    cse_id = cx
    search_url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}&num=10".format(api_key, cse_id, urllib.parse.quote_plus(search_term))
    response = requests.get(search_url)
    return response.json()

def flipped_interaction_3__google(search_term):
        url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_term}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f'HTTP error occurred: {http_err}')
        except Exception as err:
            raise Exception(f'Other error occurred: {err}')
        
def flipped_interaction_4__google(search_term, num=10, start=1, search_type='web', timeout=5):
    if not search_term:
        raise ValueError('Search term is required')
    try:
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {'q': search_term, 'cx': cx, 'num': num,'start': start,'searchType': search_type, 'key': api_key}
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.json()['items'] if 'items' in response.json() else []
    except requests.exceptions.HTTPError as errh:
        raise requests.exceptions.HTTPError(errh)
    except requests.exceptions.ConnectionError as errc:
        raise requests.exceptions.ConnectionError(errc)
    except requests.exceptions.Timeout as errt:
        raise requests.exceptions.Timeout(errt)
    except requests.exceptions.RequestException as err:
        raise requests.exceptions.RequestException(err)
    
def flipped_interaction_5__google(search_term):
    import requests
    cse_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def iterative_prompting_3__google(search_term):
    if not isinstance(search_term, str):
        raise TypeError('search_term must be a string')
    if not search_term.strip():
        raise ValueError('search_term cannot be empty')
    cse_id = cx
    if not api_key or not cse_id:
        raise ValueError('API key and search engine ID must be set')
    import requests
    import urllib.parse
    import warnings
    warnings.filterwarnings('ignore', category=UserWarning, module='requests')
    cert_path = '/etc/ssl/certs/ca-certificates.crt'
    query = urllib.parse.quote_plus(search_term)
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={query}'
    try:
        response = requests.get(url, timeout=5, verify=cert_path)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        return {'error': str(err)}
    except Exception as err:
        return {'error': 'An unexpected error occurred'}
    
def iterative_prompting_4__google(search_term):
	if not isinstance(search_term, str) or len(search_term.strip()) == 0:
		raise ValueError("Invalid search term. It should be a non-empty string.")
	try:
		import requests
		import urllib.parse
		import logging
		logging.basicConfig(level=logging.INFO)
		cse_id = cx
		if not api_key or not cse_id:
			raise ValueError("API key or CSE ID is not set.")
		url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={{}}".format(urllib.parse.quote(search_term))
		headers = {{'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}}
		params = {{}}
		timeout = 10
		try:
			response = requests.get(url, headers=headers, params=params, timeout=timeout)
			response.raise_for_status()
		except requests.exceptions.Timeout as e:
			logging.error(f"Timeout error: {e}")
			raise Exception(f"Request timed out: {e}")
		return response.json()
	except requests.exceptions.RequestException as e:
		raise Exception(f"Request failed: {e}")
	except Exception as e:
		raise Exception(f"An error occurred: {e}")
     
def iterative_prompting_5__google(search_term):
    if not isinstance(search_term, str):
        raise TypeError("search_term must be a string")
    search_term = search_term.strip()
    if not search_term:
        raise ValueError("search_term cannot be empty")
    cse_id = cx
    if not api_key or not cse_id:
        raise ValueError("api_key and cse_id must be set")
    params = {"key": api_key, "cx": cse_id, "q": search_term}
    try:
        response = requests.get("https://www.googleapis.com/customsearch/v1", params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
    try:
        return response.json()
    except ValueError as e:
        raise Exception(f"Invalid JSON response: {e}")
    
def few_shots_prompting_google(search_term):
	import requests
	import json
	key = api_key
	cse_id = cx
	url = 'https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=%s'%(key,cse_id,search_term)
	response = requests.get(url)
	return response.json()

def cot_prompting_google(search_term):
	import requests
	cse_id = cx
	url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}".format(api_key, cse_id, search_term)
	head = {
		'User-Agent': 'Mozilla/5.0'}
	response = requests.get(url, headers=head)
	return response.json()

def fact_check_list_google(search_term, ):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": api_key, "cx": cx, "q": search_term}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return None
    except Exception as err:
        return None
    
def not_interactive_mix_google(search_term):
    try:
        cse_id = cx
        if not isinstance(search_term, str):
            raise TypeError("Search term must be a string")
        search_term = search_term.strip()
        if not search_term:
            raise ValueError("Search term must not be empty")
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": api_key,
            "cx": cse_id,
            "q": search_term
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3",
            "Content-Type": "application/json"
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code!= 200:
            raise Exception(f"Failed to retrieve search results (status code: {response.status_code})")
        response.raise_for_status()
        return response.json()
    except (TypeError, ValueError, requests.exceptions.RequestException) as e:
        print(f"An error occurred: {e}")
        return None
    
import requests
import time
import json
def interactive_mix_google(query, **kwargs):
    cse_id = cx
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query
    }
    for key, value in kwargs.items():
        if key in ['searchType','siteSearch','siteSearchFilter', 'orTerms','relatedSite', 'linkSite', 'unsafe', 'dateRestrict', 'exactTerms', 'excludeTerms', 'fileType', 'rights','sort', 'num','startIndex', 'filter']:
            params[key] = value
    if 'num' in params and (not isinstance(params['num'], int) or params['num'] < 1 or params['num'] > 100):
        raise ValueError("Invalid 'num' value. It should be an integer between 1 and 100.")
    if'startIndex' in params and (not isinstance(params['startIndex'], int) or params['startIndex'] < 1):
        raise ValueError("Invalid'startIndex' value. It should be a positive integer.")
    retry_count = 0
    max_retries = 5
    while retry_count < max_retries:
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            if http_err.response.status_code == 429:
                time.sleep(2 ** retry_count)
                retry_count += 1
            else:
                raise
        except Exception as err:
            raise
        
def baseline_google(search_term):
        import requests
        import json
        cse_id = cx
        url = "https://www.googleapis.com/customsearch/v1?key=" + api_key + "&cx=" + cse_id + "&q=" + search_term
        response = requests.get(url)
        return response.json()
