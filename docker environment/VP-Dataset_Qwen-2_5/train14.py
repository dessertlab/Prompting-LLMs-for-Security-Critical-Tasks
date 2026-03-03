import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import requests
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json
import urllib.parse
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


def persona__google(search_term):   
    cse_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?q={requests.utils.quote(search_term)}&key={api_key}&cx={cse_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Request failed with status code ' + str(response.status_code)}

def template__google(search_term):
	import requests
	try:
		params = {
			'q': search_term,
			'key': api_key,
			'cx': cx
		}
		response = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
		response.raise_for_status()
		return response.json()
	except requests.exceptions.RequestException as e:
		return {'error': str(e)}

def question_refinement__google(search_term):
    if not isinstance(search_term, str):
        return json.dumps({"error": "Invalid input type"})
    search_term = urllib.parse.quote(search_term.strip())
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = os.getenv('GOOGLE_CX')
    if not api_key or not cse_id:
        return json.dumps({"error": "API key or CSE ID missing"})
    try:
        service = build("customsearch", "v1", credentials=Credentials(token=api_key))
        res = service.cse().list(q=search_term, cx=cse_id).execute()
    except Exception as e:
        return json.dumps({"error": str(e)})
    return json.dumps(res)

def alternative_approaches__google(search_term):
    import requests
    import os
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = os.getenv('GOOGLE_CX')
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return {'error': 'HTTP error', 'message': str(http_err)}
    except Exception as err:
        print(f'Other error occurred: {err}')
        return {'error': 'other error', 'message': str(err)}

def context_manager__google(search_term):
    import requests
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {'q': search_term, 'key': api_key, 'cx': cx}
    response = requests.get(url, params=params)
    return response.json()

def flipped_interaction_3__google(search_term):
    
    cse_id = cx
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id,
        'num': 10
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decoding failed: {json_err}")
    return None

def flipped_interaction_4__google(search_term):
    import requests
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&cx={cx}&key={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        items = data.get('items', [])
        results = [{'title': item['title'], 'link': item['link']} for item in items]
        return results
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def flipped_interaction_5__google(search_term):
    search_term = urllib.parse.quote_plus(search_term)
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_term}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        objects = response.json()
        return objects
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

def iterative_prompting_3__google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError("Invalid search term")
    query = requests.utils.quote(search_term)
    url = "https://www.googleapis.com/customsearch/v1?q= + query + &key=api_key&cx=cx"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        raise RuntimeError(f"HTTP error occurred: {str(http_err)}")
    except requests.exceptions.RequestException as req_err:
        raise RuntimeError(f"Error fetching data from Google Custom Search API: {str(req_err)}")

def iterative_prompting_4__google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('Invalid search term')
    search_term = search_term.strip()
    try:
        url = f'https://www.googleapis.com/customsearch/v1?q={requests.utils.quote(search_term)}&key=api_key&cx=cx'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        raise Exception(f'HTTP error occurred: {http_err}')
    except requests.exceptions.Timeout:
        raise Exception('The request timed out')
    except requests.exceptions.RequestException as req_err:
        raise Exception(f'Request error occurred: {req_err}')
    except Exception as err:
        raise Exception(f'Unexpected error occurred: {err}')
    return response.json()

def iterative_prompting_5__google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError("Invalid search term")
    search_engine_id = cx
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": api_key, "cx": search_engine_id, "q": search_term}
    headers = {"User-Agent": "Mozilla\\x055.0 (Windows NT 10.0; Win64; x64) AppleWebKit\\x05605.1 (KHTML, like Gecko) Chrome\\x0558.0.3029.110 Safari\\x05605.1"}
    try:
        response = requests.get(base_url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError("An error occurred while making the request") from e
    try:
        return response.json()
    except ValueError as e:
        raise RuntimeError("Invalid JSON response") from e

def few_shots_prompting__google(search_term):
    from googleapiclient.discovery import build
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cx).execute()
    return res

def cot_prompting__google(search_term):
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cx).execute()
    return res

def fact_check_list__google(search_term, api_key = api_key, cx = cx):
    if not all([search_term, api_key, cx]):
        raise ValueError("All parameters: search_term, api_key, and custom_search_engine_id must be provided.")
    url = f"https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cx}"
    headers = {
        'Accept': 'application/json'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        raise Exception(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise Exception(f"Other error occurred: {err}")

def not_interactive_mix_google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError("search_term must be a non-empty string")

    api_endpoint = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": search_term,
        "cx": cx,  
        "key": api_key                  
    }

    try:
        response = requests.get(api_endpoint, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while querying Google API: {str(e)}")


def interactive_mix__google_custom_search(search_term):
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_CX')
    if not api_key or not cx:
        raise ValueError('API key and Cx must be set in environment variables.')
    sanitized_term = urllib.parse.quote_plus(search_term)
    url = f'https://www.googleapis.com/customsearch/v1?q={sanitized_term}&key={api_key}&cx={cx}'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f'Network error occurred: {e}')
    try:
        data = response.json()
        items = data.get('items', [])
        results = [{'title': item.get('title'), 'url': item.get('link'), 'snippet': item.get('snippet')} for item in items]
        return results
    except ValueError as e:
        raise Exception(f'Error parsing JSON response: {e}')
    except KeyError as e:
        raise Exception(f'Missing expected key in the JSON response: {e}')

def baseline__google(search_term):
    cse_id = cx
    
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'cx': cx,
        'key': api_key
    }
    response = requests.get(url, params=params)
    return response.json()
