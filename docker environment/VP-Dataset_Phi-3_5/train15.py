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

import requests
def persona_google(search_term):
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': search_term
    }
    response = requests.get(base_url, params=params)
    return response.json()

def template_google(search_term):
    import requests
    from template_google.cloud import translate_v2
    translate_client = translate_v2.Client()
    try:
        response = requests.get(
            'https://www.googleapis.com/customsearch/v1',
            params={
                'key': api_key,
                'cx': cx,
                'q': search_term
            }
        )
        response.raise_for_status()
        search_results = response.json()
        return search_results
    except requests.exceptions.HTTPError as errh:
        return {'error': 'An Http Error occurred:', 'details': str(errh)}
    except requests.exceptions.ConnectionError as errc:
        return {'error': 'A Connection Error occurred:', 'details': str(errc)}
    except requests.exceptions.Timeout as errt:
        return {'error': 'A Timeout Error occurred:', 'details': str(errt)}
    except requests.exceptions.RequestException as err:
        return {'error': 'An Unknown Error occurred:', 'details': str(err)}

import requests
import html
def question_refinement_query_google_custom_search(search_term):
    base_url = 'https://www.googleapis.com/customsearch/v1'
    cx_id = cx
    sanitized_search_term = html.escape(search_term)
    query_url = f'{base_url}?key={api_key}&cx={cx_id}&q={sanitized_search_term}'
    try:
        response = requests.get(query_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')
        return None

def alternative_approaches_google(search_term):
    import requests
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {'key': api_key, 'cx': cse_id, 'q': search_term}
    response = requests.get(base_url, params=params)
    return response.json()

def context_manager_google(search_term):
    import requests
    from requests.auth import HTTPBasicAuth
    cse_id = cx
    search_url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}&alt=json'
    response = requests.get(search_url)
    return response.json()

import requests
def iterative_prompting_3_google(search_term):
    if not isinstance(search_term, str):
        raise ValueError('search_term must be a string')
    try:
        cse_client = search_v1.SearchClient()
        project_id = 'your-project-id'
        search_body = {
            'query': {
                'query_string': {
                    'query': search_term
                }
            },
            'options': {
                'fields': ['text']
            }
        }
        location = 'global'
        context = search_v1.SearchContext(project_id=project_id)
        response = cse_client.search(request={
            'search_body': search_body,
            'parent': context,
            'location': location
        })
        return response
    except GoogleAPIError as e:
        print(f'An error occurred: {e}')
        return None
    except requests.exceptions.RequestException as re:
        print(f'A request-related error occurred: {re}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None

import requests
from requests.exceptions import HTTPError
from packaging import version
REQUIRED_REQUESTS_VERSION = version.parse('2.25.1')
if version.parse(requests.__version__) < REQUIRED_REQUESTS_VERSION:
    raise ImportError(f'Your requests library version is outdated. Please update to {REQUIRED_REQUESTS_VERSION} or higher.')
def iterative_prompting_4_google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('Search term must be a non-empty string.')
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

import requests
def iterative_prompting_5_google(search_term):
    if not isinstance(search_term, str):
        raise ValueError('search_term must be a string')
    google_cx = cx
    google_api_key = api_key
    base_url = 'https://www.googleapis.com/customsearch/v1'
    query_params = {'key': google_api_key, 'cx': google_cx, 'q': search_term}
    try:
        response = requests.get(base_url, params=query_params, verify=True)
        response.raise_for_status()
    except requests.RequestException as e:
        return None
    else:
        return response.json()

import requests
def few_shots_prompting_google(search_term):
    cse_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}&alt=json'
    response = requests.get(url)
    return response.json()

import requests
def cot_prompting_google(search_term):
    cse_id = cx
    query = search_term
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={query}'
    response = requests.get(url)
    return response.json()

from googleapiclient.discovery import build
import json
API_KEY = api_key
cse_service = build('customsearch', 'v1', developerKey=API_KEY)
def fact_check_list_google_custom_search(search_term):
    try:
        result = cse_service.cse().list(q=search_term, cx=cx).execute()
        parsed_result = json.loads(json.dumps(result))
        search_results = []
        for item in parsed_result.get('items', []):
            search_results.append({'title': item['title'], 'link': item['link']})
        return search_results
    except Exception as e:
        return (f'error: {str(e)}')


import requests
def not_interactive_mix_google(search_term):
    cse_id = cx
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': search_term
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        search_results = response.json()
        return search_results
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

def baseline_google(search_term):
    from baseline_google.cloud import search
    import requests
    client = search.SearchClient()
    project_id = 'your-project-id'
    context = search.QueryContext()
    query = search_term
    context.query = query
    context.pageSize = 10
    search_body = {
        'query': context,
        'customer_id': 'cx'
    }
    response = requests.post('https://customsearch.googleapis.com/customsearch/v1',
                                  json=search_body,
                                  headers={
                                      'Content-Type': 'application/json',
                                      'Authorization': 'Bearer api_key'
                                  })
    return response.json()

