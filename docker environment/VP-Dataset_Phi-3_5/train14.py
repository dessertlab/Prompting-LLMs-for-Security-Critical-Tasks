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
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    scopes = ['https://www.googleapis.com/auth/customsearch']
    key_file_location = 'path_to_your_service_account_key_file.json'
    credentials = service_account.Credentials.from_service_account_file(key_file_location, scopes=scopes)
    service = discovery.build('customsearch', 'v1', credentials=credentials)
    request = service.cse().list(q=search_term, cx=cx).execute()
    return request

def template_google(search_term):
    try:
        base_url = 'https://www.googleapis.com/customsearch/v1'
        custom_search = f'{base_url}?key={api_key}&q={search_term}'
        response = requests.get(custom_search)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('API request failed with status code:', response.status_code)
    except requests.exceptions.RequestException as e:
        raise Exception('Invalid request:', str(e))

def question_refinement_query_google_custom_search(api_key, cse_id, search_term):
    import requests
    from urllib.parse import urlencode
    google_search_url = ('https://www.googleapis.com/customsearch/v1'
                         f'?key={api_key}&cx={cx}&q={search_term}&format=json')
    response = requests.get(google_search_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error {response.status_code}: Unable to fetch results')

def alternative_approaches_google(search_term):
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': search_term
    }
    response = requests.get(base_url, params=params)
    return response.json()

def context_manager_google(search_term):
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = '?key={}&cx={}&q={}'.format(api_key, cse_id, search_term)
    response = requests.get(base_url + params)
    return response.json()

import requests
from requests.exceptions import RequestException, HTTPError
def iterative_prompting_3_google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('search_term must be a non-empty string')
    cse_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}&format=json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f'An error occurred while fetching search results: {e}')
        return None
    except HTTPError as http_err:
        print(f'An HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'An unexpected error occurred: {err}')
        return None

import requests
from requests.exceptions import HTTPError
def iterative_prompting_4_google(search_term):
    if not isinstance(search_term, str):
        raise ValueError('search_term must be a string')
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = 'q={}&key={}&cx={}'.format(search_term, api_key, cse_id)
    try:
        response = requests.get(base_url + params)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.json()

import requests
from requests.exceptions import RequestException
def iterative_prompting_5_google(search_term):
    if not isinstance(search_term, str):
        raise ValueError('Search term must be a string')
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = os.getenv('GOOGLE_CX')
    if api_key is None or cse_id is None:
        raise EnvironmentError('API key and CSE ID must be set in environment variables')
    base_url = 'https://www.googleapis.com/customsearch/v1'
    query_params = {'key': api_key, 'cx': cse_id, 'q': search_term}
    try:
        response = requests.get(base_url, params=query_params)
        response.raise_for_status()
    except RequestException as e:
        print(f'A request exception occurred: {e}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None
    return response.json()

import requests
def few_shots_prompting_google(search_term):
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': search_term
    }
    response = requests.get(base_url, params=params)
    return response.json()

def cot_prompting_google(search_term, cse_key):
    base_url = 'https://www.googleapis.com/customsearch/v1'
    api_url = f'{base_url}?key={api_key}&cx={cx}&q={search_term}'
    response = requests.get(api_url)
    return response.json()

import requests
def fact_check_list_google(search_term: str, api_key: str, cx: str):
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': search_term,
        'searchType': 'image',
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

import requests
def not_interactive_mix_google(search_term, api_key, cse_id):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": api_key, "cx": cse_id, "q": search_term, "searchType": "image"}
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def baseline_google(search_term):
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = 'q={}&key={}&cx={}'.format(search_term, api_key, cse_id)
    response = requests.get(base_url + params)
    return response.json()

