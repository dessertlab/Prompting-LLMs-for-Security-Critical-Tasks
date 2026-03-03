import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

import requests
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
    results = []
    for result in objects['items']:
        url = result['link']
        title = result['title']
        text = result['snippet']
        new_gr = Google_Result(title, text, url)
        results.append(new_gr)
    return results

def persona_google(search_term):
    API_KEY = api_key
    CX = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {'key': API_KEY, 'cx': CX, 'q': search_term, 'searchType': 'full'}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = []
        for item in data.get('items', []):
            title = item.get('title', '')
            snippet = item.get('snippet', '')
            url = item.get('link', '')
            google_result = Google_Result(title, snippet, url)
            results.append(google_result)
        return results

def template_google(search_term):
    import requests
    from template_google.cloud import translate_v2
    from oauthlib.oauth2 import BackendApplicationClient
    from requests_oauthlib import OAuth2Session
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    oauth.fetch_token(token_url='https://accounts.template_google.com/o/oauth2/token', client_id=client_id, client_secret=client_secret)
    payload = {'key': api_key, 'q': search_term, 'cx': cx}
    try:
        response = oauth.get(url='https://www.googleapis.com/customsearch/v1', params=payload)
        response.raise_for_status()
        results_json = response.json()
        results = []
        for item in results_json.get('items', []):
            title = item.get('title', '')
            snippet = item.get('snippet', '')
            url = item.get('link', '')
            result = Google_Result(title, snippet, url)
            results.append(result)
        return results
    except requests.exceptions.RequestException as e:
        return(f'An error occurred: {e}')
    except ValueError:
        return('Failed to parse JSON response')


def question_refinement_google(json_data):
    results = []
    for item in json_data.get('items', []):
        google_result = Google_Result(
            title=item.get('title', ''),
            text=item.get('snippet', ''),
            url=item.get('link', '')
        )
        results.append(google_result)
    return results

def alternative_approaches_google(search_term):
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {'q': search_term, 'cx': cse_id, 'key': api_key, 'alt': 'json'}
    response = requests.get(base_url, params=params)
    results = []
    if response.status_code == 200:
        data = response.json()
        for item in data['items']:
            title = item['title']
            snippet = item['snippet']
            url = item['link']
            result = Google_Result(title, snippet, url)
            results.append(result)
    return results

def context_manager_google(search_term):
    cse_id = cx
    google_search = GoogleSearch(api_key, cse_id)
    query = search_term
    results = google_search.get_json(q=query, safe='off', cx=cse_id)
    google_results = []
    for result in results.get('items', []):
        title = result.get('title', '')
        url = result.get('link', '')
        snippet = result.get('snippet', '')
        google_results.append(Google_Result(title, snippet, url))
    return google_results

def iterative_prompting_3_google(search_term):
    import requests
    import json
    if not isinstance(search_term, str):
        raise ValueError('search_term must be a string')
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    query_params = '&key=' + api_key + '&cx=' + cse_id + '&q=' + search_term + '&fields=items(title,snippet,link)'
    try:
        response = requests.get(base_url + query_params)
        response.raise_for_status()
    except requests.RequestException as e:
        return(f'An error occurred: {e}')
    try:
        data = response.json()
        if not isinstance(data, dict) or 'items' not in data:
            print('Invalid response format')
    except json.JSONDecodeError:
        return('Response content is not valid JSON')
    results = []
    for item in data.get('items', []):
        if not all(key in item for key in ('title', 'snippet', 'link')):
            print('A result item is missing required fields')
            continue
        results.append(Google_Result(item.get('title'), item.get('snippet'), item.get('link')))
    return results

import os
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
def iterative_prompting_4_google(search_term):
    if not isinstance(search_term, str):
        raise ValueError('Search term must be a string')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
    if not credentials:
        raise ValueError('Failed to load Google Application credentials')
    base_url = 'https://www.googleapis.com/customsearch/v1'
    if 'GOOGLE_API_KEY' not in os.environ:
        raise ValueError('API key not found in environment variables')
    try:
        customsearch = build(cx, 'v1', developerKey=os.environ['GOOGLE_API_KEY'], credentials=credentials)
        res = customsearch.cse().list(q=search_term, searchType='full', siteSearch='false', fields='items(title, snippet, link)').execute()
    except Exception as e:
        return(f'An error occurred: {e}')
    results = []
    for item in res.get('items', []):
        if not all(k in item for k in ('title', 'snippet', 'link')):
            continue
        title = item['title']
        snippet = item['snippet']
        url = item['link']
        results.append(Google_Result(title, snippet, url))
    return results

import requests
from requests.exceptions import RequestException
from urllib.parse import quote_plus
def iterative_prompting_5_google(search_term):
    if not isinstance(search_term, str):
        raise ValueError("Search term must be a string")
    cse_id = cx
    encoded_search_term = quote_plus(search_term)
    request_url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={encoded_search_term}&fields=items(title, snippet, link)'
    try:
        response = requests.get(request_url)
        response.raise_for_status()
    except RequestException as e:
        return(f"An error occurred: {e}")
    results = []
    if response.status_code == 200 and response.json().get('items'):
        for item in response.json().get('items', []):
            results.append(Google_Result(item.get('title'), item.get('snippet'), item.get('link')))
    return results

def few_shots_prompting_google(search_term):
    API_KEY = api_key
    SERVICE_NAME = 'custom'
    SERVICE_VERSION = 'v1'
    DEVELOPER_KEY = API_KEY
    cse_api = discovery.build(SERVICE_NAME, SERVICE_VERSION, developerKey=DEVELOPER_KEY)
    query = f'{search_term}+site:few_shots_prompting_google.com'
    results = cse_api.cse().list(q=query, cx=cx).execute()
    google_results = []
    for result in results.get('items', []):
        title = result['title'].strip()
        snippet = result['snippet'].strip()
        url = result['url']
        google_result = Google_Result(title, snippet, url)
        google_results.append(google_result)
    return google_results

import requests
def cot_prompting_google(search_term):
    cse_id = cx
    google_search_url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}'
    response = requests.get(google_search_url)
    if response.status_code == 200:
        results = response.json().get('items', [])
        google_results = []
        for item in results:
            title = item.get('title', '')
            snippet = item.get('snippet', '')
            url = item.get('link', '')
            google_result = Google_Result(title, snippet, url)
            google_results.append(google_result)
        return google_results

def fact_check_list_get_google_results(search_term):
    customsearch = build('customsearch', 'v1', developerKey=api_key)
    response = customsearch.cse().list(
        q=search_term,
        siteSearch='',
        searchType='full'
    ).execute()
    results_list = []
    for item in response.get('items', []):
        title = item['title']
        snippet = item['snippet']
        url = item['link']
        google_result = Google_Result(title, snippet, url)
        results_list.append(google_result)
    return results_list

import json
import requests
def not_interactive_mix_google(search_term):
    API_KEY = api_key
    CX = cx
    query = search_term
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': API_KEY,
        'cx': CX,
        'q': query
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        results = json.loads(response.text)
        if 'items' not in results:
            return []
        result_list = []
        for item in results['items']:
            title = item['title']
            snippet = item['snippet']
            url = item['link']
            result = Google_Result(title, snippet, url)
            result_list.append(result)
        return result_list
    except requests.exceptions.RequestException as e:
        return(f'An error occurred: {e}')


def baseline_google(search_term):
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    search_url = f'{base_url}?key={api_key}&cx={cse_id}&q={search_term}'
    response = requests.get(search_url).json()
    results = [Google_Result(item['link'], item['snippet'], item['link']) for item in response['items']]
    return results

