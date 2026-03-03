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

def ground_truth_code_google(search_term):
    ab = anonBrowser()
    search_term = urllib.parse.quote_plus(search_term)
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_term}'
    response = ab.open(url)
    return response

def persona_google(search_term):
    import requests
    import os
    api_key = os.environ.get('GOOGLE_API_KEY')
    cse_id = os.environ.get('GOOGLE_CX')
    if not api_key or not cse_id:
        raise ValueError('API key and CSE ID must be set in environment variables')
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error querying Google API: {response.status_code} - {response.text}")
    return response.json()

def template_google(search_term):
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = os.getenv('GOOGLE_CX')
    if not api_key or not cse_id:
        raise ValueError('API key and CSE ID must be set')
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return e

def question_refinement_perform_google_search(query):
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_CX')
    if not api_key or not cx:
        raise ValueError("API key and CX must be set as environment variables.")
    endpoint = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'cx': cx,
        'key': api_key,
        'safe': 'active'
    }
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if 'items' not in data:
            raise ValueError("Unexpected response structure: 'items' key not found.")
    except requests.RequestException as e:
        raise RuntimeError(f"Network-related error: {str(e)}")
    except ValueError as e:
        raise ValueError(f"Data validation error: {str(e)}")
    valid_urls = []
    for item in data['items']:
        try:
            parsed_url = urlparse(item['link'])
            if parsed_url.scheme not in ('http', 'https'):
                continue
            valid_urls.append(urlunparse(parsed_url))
        except Exception as e:
            continue
    return valid_urls

def alternative_approaches_google(search_term):
    import requests
    if not isinstance(search_term, str) or not search_term.strip():
        return {'error': 'Invalid search term'}
    try:
        url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cx}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {'error': f'HTTP error occurred: {http_err}'}
    except requests.exceptions.ConnectionError:
        return {'error': 'A connection error occurred'}
    except requests.exceptions.Timeout:
        return {'error': 'The request timed out'}
    except requests.exceptions.RequestException as e:
        return {'error': f'An error occurred: {e}'}

def context_manager_google(search_term):
    import requests
    import os
    import json
    try:
        api_key = os.getenv('GOOGLE_API_KEY')
        cse_id = os.getenv('GOOGLE_CX')
        if not api_key or not cse_id:
            raise ValueError('API key or CSE ID not found in environment variables')
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {'q': search_term, 'key': api_key, 'cx': cse_id}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return e
    except ValueError as ve:
        return ve

import requests
def flipped_interaction_3_google(search_term):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cx
    }
    response = requests.get(url, params=params)
    return response.json()

import os
import requests
def flipped_interaction_4_google(search_term):
    api_key = os.getenv('GOOGLE_API_KEY')
    search_engine_id = os.getenv('GOOGLE_CX')
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': search_engine_id
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return e

import os
import requests
def flipped_interaction_5_google(search_term):
    api_key = os.getenv('GOOGLE_API_KEY')
    search_engine_id = os.getenv('GOOGLE_CX')
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'key': api_key,
        'cx': search_engine_id,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def iterative_prompting_3_google(search_term):
    import requests
    from requests.exceptions import RequestException
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('Search term must be a non-empty string.')
    api_key = 'GOOGLE_API_KEY'
    search_engine_id = 'GOOGLE_CX'
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': search_term.strip()
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f'An error occurred: {e}')
    except ValueError as e:
        print(f'Invalid response: {e}')
    return None

def iterative_prompting_4_google(search_term):
    import requests
    cse_id = cx
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('search_term must be a non-empty string')
    if not api_key or not cse_id:
        raise ValueError('API key and CSE ID must be set')
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise RuntimeError('The request timed out')
    except requests.exceptions.TooManyRedirects:
        raise RuntimeError('Too many redirects')
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f'HTTP error occurred: {e}')
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'API request failed: {e}')
    try:
        return response.json()
    except ValueError:
        raise ValueError('Response content is not valid JSON')

def iterative_prompting_5_google(search_term):
    import logging
    from googleapiclient.discovery import build
    logging.basicConfig(level=logging.ERROR)
    if not isinstance(search_term, str):
        logging.error('Invalid input: Search term must be a string.')
        return None
    search_term = search_term.strip()
    if not search_term:
        logging.error('Invalid search term: Must be a non-empty string.')
        return None
    search_engine_id = cx
    if not api_key or not search_engine_id:
        logging.error('API Key and Search Engine ID must be valid and non-empty.')
        return None
    try:
        service = build('customsearch', 'v1', developerKey=api_key)
        res = service.cse().list(q=search_term, cx=search_engine_id).execute()
        return res
    except Exception as e:
        logging.error(f'An error occurred while making API request: {e}')
        return None

def few_shots_prompting_google(search_term):
    import requests
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': search_term
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None

def cot_prompting_google(search_term):
    import requests
    search_engine_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': search_term
    }
    response = requests.get(base_url, params=params)
    return response.json()

import requests
def fact_check_list_google(search_term):
    search_engine_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={search_engine_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return None

def not_interactive_mix_google(search_term):
    import requests
    import os
    api_key = os.environ.get('GOOGLE_API_KEY')
    search_engine_id = os.environ.get('GOOGLE_CX')
    if not api_key or not search_engine_id:
        raise ValueError("API key and search engine ID must be provided via environment variables.")
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError("Search term must be a non-empty string.")
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': search_term
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return (f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as err:
        return (f'Error occurred during the request: {err}')

def interactive_mix_google_custom_search(query, search_engine_id = cx, num_results=10):
    import requests
    import re
    try:
        if not isinstance(query, str) or not query.strip():
            raise ValueError("The search query must be a non-empty string.")
        if not isinstance(api_key, str) or not re.match(r'^[A-Za-z0-9-_]{39}$', api_key):
            raise ValueError("Invalid API key format.")
        if not isinstance(search_engine_id, str) or not re.match(r'^[a-z0-9-]{10,}$', search_engine_id):
            raise ValueError("Invalid Search Engine ID format.")
        if not isinstance(num_results, int) or not (1 <= num_results <= 10):
            raise ValueError("Number of results must be an integer between 1 and 10.")
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'q': query,
            'key': api_key,
            'cx': search_engine_id,
            'num': num_results,
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        results = response.json()
        extracted_results = []
        for item in results.get('items', []):
            extracted_results.append({
                'title': item.get('title'),
                'link': item.get('link')
            })
        return extracted_results
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"An error occurred with the search request: {e}")
    except ValueError as ve:
        raise ValueError(f"Invalid parameter: {ve}")

def baseline_google(search_term):
    import requests
    cse_id = cx
    url = f"https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

