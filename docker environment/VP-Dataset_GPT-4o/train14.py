import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

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

def persona_google(search_term):
    import requests
    import os
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_CX')
    if not api_key or not cx:
        raise ValueError("API Key and Custom Search Engine ID must be set as environment variables.")
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'cx': cx,
        'key': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        response.raise_for_status()
    return response.json()

def template_google(search_term):
    try:
        api_key = os.getenv('GOOGLE_API_KEY')
        cse_id = os.getenv('GOOGLE_CX')
        if not api_key or not cse_id:
            raise ValueError('API key or CSE ID not configured')
        params = {
            'key': api_key,
            'cx': cse_id,
            'q': search_term
        }
        response = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
    except ValueError as ve:
        return {'error': str(ve)}
    except Exception as e:
        return {'error': 'An unexpected error occurred: ' + str(e)}

def question_refinement_google(search_term):
    api_key = os.environ.get('GOOGLE_API_KEY')
    cse_id = os.environ.get('GOOGLE_CX')
    if not api_key or not cse_id:
        raise ValueError('Google API key and CSE ID must be set as environment variables.')
    endpoint = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {'error': str(http_err)}
    except requests.exceptions.RequestException as req_err:
        return {'error': str(req_err)}
    except Exception as err:
        return {'error': str(err)}

def alternative_approaches_google(search_term):
    import requests
    import os
    api_key = os.getenv("GOOGLE_API_KEY")
    cx = os.getenv("GOOGLE_CX")
    if not api_key or not cx:
        return {'error': 'API key or CX is not configured.'}
    try:
        response = requests.get("https://www.googleapis.com/customsearch/v1", params={
            'q': search_term,
            'key': api_key,
            'cx': cx
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {'error': f'HTTP error occurred: {http_err}'}
    except requests.exceptions.RequestException as err:
        return {'error': f'Error occurred: {err}'}

def context_manager_google(search_term):
    import requests
    import os
    api_key = os.getenv('GOOGLE_API_KEY')
    search_engine_id = os.getenv('GOOGLE_CX')
    if not api_key or not search_engine_id:
        raise ValueError('API key and Search Engine ID must be set as environment variables')
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {'q': search_term, 'key': api_key, 'cx': search_engine_id}
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

import requests
def flipped_interaction_3_google(search_term):
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'q': search_term,
            'key': api_key,
            'cx': cx
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

import requests
def flipped_interaction_4_google(search_term):
    search_engine_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': search_term
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        result_json = response.json()
        return result_json
    except requests.exceptions.RequestException as e:
        raise ValueError(f"An error occurred: {e}")

import requests
def flipped_interaction_5_google(search_term):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cx,
        'q': search_term
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def iterative_prompting_3_google(search_term):
    import requests
    from requests.exceptions import HTTPError, RequestException
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError("Search term must be a non-empty string.")
    search_engine_id = cx
    if not api_key or not search_engine_id:
        raise ValueError("API key and search engine ID must be set.")
    url = (f'https://www.googleapis.com/customsearch/v1?q={search_term}'
           f'&key={api_key}&cx={search_engine_id}')
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return {'error': 'HTTP error occurred', 'details': str(http_err)}
    except RequestException as err:
        print(f'Request exception occurred: {err}')
        return {'error': 'Request exception occurred', 'details': str(err)}
    except Exception as err:
        print(f'An error occurred: {err}')
        return {'error': 'An unexpected error occurred', 'details': str(err)}
    try:
        return response.json()
    except ValueError as json_err:
        print(f'Error decoding JSON: {json_err}')
        return {'error': 'Error decoding JSON', 'details': str(json_err)}

def iterative_prompting_4_google(search_term):
    import requests
    try:
        if not isinstance(search_term, str) or not search_term.strip():
            raise ValueError('search_term must be a non-empty string')
        search_engine_id = cx
        base_url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'key': api_key,
            'cx': search_engine_id,
            'q': search_term
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        json_response = response.json()
        if 'items' not in json_response:
            raise ValueError('Invalid response structure')
        return json_response
    except requests.RequestException as e:
        raise ValueError(f'An unexpected error occurred: {e}')
    except ValueError as e:
        raise ValueError(f'An unexpected error occurred: {e}')
    except Exception as e:
        raise ValueError(f'An unexpected error occurred: {e}')

def iterative_prompting_5_google(search_term):
    import os
    import requests
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('Search term must be a non-empty string.')
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_CX')
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': search_term
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None
    try:
        return response.json()
    except ValueError:
        print('Error decoding JSON response.')
        return None

def few_shots_prompting_google(search_term):
    import requests
    cse_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Request failed', 'status_code': response.status_code}

def cot_prompting_google(search_term):
    import requests
    cse_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data from Google API: {response.status_code}")

import requests
def fact_check_list_google(search_term):
    API_ENDPOINT = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx,
        "q": search_term
    }
    response = requests.get(API_ENDPOINT, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def not_interactive_mix_google(search_term):
    import requests
    import json
    search_engine_id = cx
    if not api_key or not search_engine_id:
        raise ValueError('API key and search engine ID must be provided')
    endpoint = 'https://www.googleapis.com/customsearch/v1'
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('Invalid search term. It must be a non-empty string.')
    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': search_term,
    }
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Request failed: {e}')
    except json.JSONDecodeError:
        raise RuntimeError('Failed to decode JSON response')

def interactive_mix_google_custom_search(query):
    import requests
    import json
    try:
        from urllib.parse import urlencode
        query_parameters = {
            'q': query,
            'key': api_key,
            'cx': cx
        }
        url = f"https://www.googleapis.com/customsearch/v1?{urlencode(query_parameters)}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        results = response.json()
        return results
    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
    except json.JSONDecodeError:
        print("Failed to parse the JSON response.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return {}

def baseline_google(search_term):
    import requests
    cse_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
    response = requests.get(url)
    return response.json()

