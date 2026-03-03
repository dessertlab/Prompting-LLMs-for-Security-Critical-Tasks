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
    SEARCH_ENGINE_ID = cx
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={API_KEY}&cx={SEARCH_ENGINE_ID}'
    response = requests.get(url)
    results = []
    if response.status_code == 200:
        search_results = response.json()
        for item in search_results.get('items', []):
            title = item.get('title')
            snippet = item.get('snippet')
            link = item.get('link')
            result = Google_Result(title, snippet, link)
            results.append(result)
    return results

def template_google(search_term):
    try:
        api_key = os.getenv('GOOGLE_API_KEY')
        cse_id = os.getenv('GOOGLE_CX')
        if not api_key or not cse_id:
            raise EnvironmentError('API key or CSE ID not set')
        url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
        response = requests.get(url)
        response.raise_for_status()
        search_results = response.json()
        results = []
        for item in search_results.get('items', []):
            result = Google_Result(
                title=item.get('title', ''),
                text=item.get('snippet', ''),
                url=item.get('link', '')
            )
            results.append(result)
        return results
    except Exception as e:
        print(f'An error occurred: {e}')

def question_refinement_query_google_custom_search(search_term):
    import os
    import requests
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv('GOOGLE_API_KEY')
    if not API_KEY:
        raise ValueError("API Key not found in environment variables.")
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': API_KEY,
        'cx': cx,
        'q': search_term
    }
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        if 'items' in data:
            return [Google_Result(url=item['link'], title=item['title'], snippet=item['snippet'])
                    for item in data['items']]
        else:
            return []
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"An error occurred: {e}")
    except ValueError as e:
        raise RuntimeError(f"An error occurred: {e}")

def alternative_approaches_google(search_term):
    import requests
    import json
    from requests.exceptions import HTTPError, Timeout
    search_engine_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={search_term}'
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        results = []
        if 'items' in data:
            for item in data['items']:
                title = item.get('title', '')
                snippet = item.get('snippet', '')
                link = item.get('link', '')
                results.append(Google_Result(title, snippet, link))
        return results
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Timeout:
        print('The request timed out')
    except Exception as err:
        print(f'An error occurred: {err}')
    return []

def context_manager_google(search_term):
    import requests
    import os
    api_key = os.getenv('GOOGLE_API_KEY')
    custom_search_engine_id = os.getenv('GOOGLE_CX')
    if not api_key or not custom_search_engine_id:
        return []
    params = {
        'q': search_term,
        'key': api_key,
        'cx': custom_search_engine_id
    }
    response = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
    if response.status_code != 200:
        return []
    search_results = []
    for item in response.json().get('items', []):
        title = item.get('title')
        text = item.get('snippet')
        url = item.get('link')
        if title and text and url:
            search_results.append(Google_Result(title, text, url))
    return search_results

import requests
from urllib.parse import urlencode

def flipped_interaction_3_google(search_term):
    cse_id = cx
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    response = requests.get(base_url, params=params)
    search_results = []
    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])
        for item in items:
            title = item.get('title')
            snippet = item.get('snippet')
            url = item.get('link')
            result = Google_Result(title, snippet, url)
            search_results.append(result)
    else:
        raise Exception(f"API request failed with status code {response.status_code}")
    return search_results

import requests

def flipped_interaction_4_google(search_term):
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cx}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        results = []
        if 'items' in data:
            for item in data['items']:
                title = item.get('title', 'No Title')
                snippet = item.get('snippet', 'No Snippet')
                link = item.get('link', '')
                results.append(Google_Result(title, snippet, link))
        return results
    except Exception as e:
        print(f'An error occurred: {e}')
        return []



def flipped_interaction_5_google(search_term):
    api_key = os.getenv('GOOGLE_API_KEY')
    search_engine_id = os.getenv('GOOGLE_CX')
    if not api_key or not search_engine_id:
        raise ValueError('API key and Search Engine ID (CX) must be provided')
    url = f'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': search_term
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception('Failed to retrieve results: ' + str(response.status_code))
    data = response.json()
    search_items = data.get('items')
    results = []
    if not search_items:
        return results
    for item in search_items:
        title = item.get('title')
        snippet = item.get('snippet')
        link = item.get('link')
        results.append(Google_Result(title=title, text=snippet, url=link))
    return results

def iterative_prompting_3_google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError("search_term must be a non-empty string")
    cse_id = cx
    try:
        url = (
            f'https://www.googleapis.com/customsearch/v1?'
            f'q={requests.utils.quote(search_term)}&key={api_key}&cx={cse_id}'
        )
        with requests.get(url, timeout=10) as response:
            response.raise_for_status()
            results = response.json()
        google_results = []
        if 'items' in results:
            for item in results['items']:
                title = item.get('title', 'No title')
                text = item.get('snippet', 'No snippet available')
                url = item.get('link', 'No URL available')
                result = GoogleResult(title, text, url)
                google_results.append(result)
        return google_results
    except requests.RequestException as e:
        print(f'Request error: {e}')
    except ValueError as e:
        print(f'Value error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    return []

def iterative_prompting_4_google(search_term):
    import requests
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('Search term must be a non-empty string.')
    SEARCH_ENGINE_ID = cx
    API_KEY = api_key
    if not API_KEY or not SEARCH_ENGINE_ID:
        raise EnvironmentError('api_key and SEARCH_ENGINE_ID must be set.')
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': SEARCH_ENGINE_ID
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return []
    try:
        search_results = response.json().get('items', [])
        if not isinstance(search_results, list):
            print("Unexpected response data format.")
            return []
        results = []
        for item in search_results:
            title = item.get('title', '')
            snippet = item.get('snippet', '')
            link = item.get('link', '')
            if title and snippet and link:
                results.append(Google_Result(title, snippet, link))
        return results
    except ValueError:
        print("Failed to parse response JSON.")
        return []

def iterative_prompting_5_google(search_term):
    import requests
    from requests.exceptions import Timeout, HTTPError, RequestException
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('Search term must be a non-empty string.')
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cx
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
    except Timeout:
        raise TimeoutError('The request timed out, please try again later.')
    except HTTPError as http_err:
        raise ConnectionError(f'HTTP error occurred: {http_err}')
    except RequestException as e:
        raise ConnectionError(f'An error occurred while fetching data: {str(e)}')
    try:
        results = response.json()
    except ValueError as ve:
        raise ValueError('Failed to parse JSON response') from ve
    google_results = []
    items = results.get('items', [])
    if not items:
        return google_results
    for item in items:
        title = item.get('title', 'No title')
        snippet = item.get('snippet', 'No snippet available')
        url = item.get('link')
        result = Google_Result(title=title, text=snippet, url=url)
        google_results.append(result)
    return google_results

def few_shots_prompting_google(search_term):
    import requests
    cse_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
    response = requests.get(url)
    results_json = response.json()
    results = []
    for item in results_json.get('items', []):
        title = item.get('title')
        snippet = item.get('snippet')
        url = item.get('link')
        result = Google_Result(title, snippet, url)
        results.append(result)
    return results

def cot_prompting_google(search_term):
    import requests
    cse_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
    response = requests.get(url)
    results = response.json().get('items', [])
    google_results = [Google_Result(item['title'], item['snippet'], item['link']) for item in results]
    return google_results

def fact_check_list_google(search_term):
    import os
    import requests
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_CX')
    if not api_key or not cx:
        raise ValueError("API key and Custom Search Engine ID must be set.")
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cx
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        results = response.json().get('items', [])
        search_results = [Google_Result(item['title'], item['snippet'], item['link']) for item in results]
        return search_results
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def not_interactive_mix_google(search_term):
    import requests
    import json
    if not isinstance(search_term, str) or len(search_term) == 0:
        raise ValueError("Invalid search term. Please provide a non-empty string.")
    cse_id = cx
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = []
        if 'items' in data:
            for item in data['items']:
                title = item.get('title', 'No title')
                snippet = item.get('snippet', 'No snippet')
                link = item.get('link', 'No URL')
                results.append(Google_Result(title, snippet, link))
        return results
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return []

def interactive_mix_google_custom_search(query,  max_results=10):
    import requests
    try:
        if not isinstance(query, str) or not query.strip():
            raise ValueError("Search query must be a non-empty string.")
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": api_key,
            "cx": cx,
            "q": query,
            "num": min(max_results, 10)
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = []
        search_items = response.json().get("items", [])
        for item in search_items:
            if item.get("title") and item.get("link") and item.get("snippet"):
                result = {
                    "title": item["title"],
                    "url": item["link"],
                    "snippet": item["snippet"]
                }
                results.append(result)
        return results
    except ValueError as ve:
        print(f"Input error: {ve}")
    except requests.HTTPError as httpe:
        print(f"HTTP error occurred: {httpe}")
    except requests.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def baseline_google(search_term):
    cse_id = cx
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    response = requests.get(url, params=params)
    results = response.json()
    search_results = []
    if 'items' in results:
        for item in results['items']:
            title = item.get('title')
            text = item.get('snippet')
            url = item.get('link')
            search_results.append(Google_Result(title, text, url))
    return search_results

