import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
from urllib.parse import quote_plus
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
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

def persona__google(search_term):
    import requests
    import urllib.parse
    cse_id = cx
    query = urllib.parse.quote_plus(search_term)
    url = 'https://www.googleapis.com/customsearch/v1?q=' + query + '&key=' + api_key + '&cx=' + cse_id
    response = requests.get(url)
    results = response.json().get('items', [])
    return [Google_Result(item['title'], item['snippet'], item['link']) for item in results]

def template__google(search_term):
	import requests
	try:
		params = {'q': search_term, 'key': api_key, 'cx': cx}
		r = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
		r.raise_for_status()
		response_data = r.json().get('items', [])
		results = [Google_Result(item['title'], item['snippet'], item['link']) for item in response_data]
		return results
	except requests.exceptions.RequestException as e:
		return []

def question_refinement__google(search_term):
    Google_Result = type('Google_Result', (object,), {'__init__': lambda self, url, title, snippet: setattr(self, '__dict__', {'url': url, 'title': title, 'snippet': snippet})})
    cse_id = cx
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {'q': search_term, 'key': api_key, 'cx': cse_id}
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 403:
            return [Google_Result('', 'API key quota exceeded or invalid', '')]
        elif response.status_code != 200:
            return [Google_Result('', f'HTTP Error occurred: {response.status_code}', '')]
        response.raise_for_status()
        data = response.json()
        items = data.get('items', [])
        results = [Google_Result(item['link'], item['title'], item['snippet']) for item in items]
        return results
    except HTTPError as http_err:
        return [Google_Result('', f'HTTP error occurred: {http_err}', '')]
    except Timeout as timeout_err:
        return [Google_Result('', f'Timeout error occurred: {timeout_err}', '')]
    except Exception as err:
        return [Google_Result('', f'An error occurred: {err}', '')]

def alternative_approaches__google(search_term):
    import requests
    from urllib.parse import quote
    try:
        cse_id = cx
        search_term = quote(search_term)
        url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        items = data.get('items', [])
        results = []
        for item in items:
            title = item.get('title', '')
            snippet = item.get('snippet', '')
            link = item.get('link', '')
            results.append(Google_Result(title, snippet, link))
        return results
    except requests.exceptions.RequestException as e:
        print(f'Request exception: {e}')
        return []

def context_manager__google(search_term):
    import requests
    cse_id = cx
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {'q': search_term, 'cx': cse_id, 'key': api_key}
    response = requests.get(url, params=params)
    results = []
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            for item in data['items']:
                results.append(Google_Result(item['title'], item['snippet'], item['link']))
            return results
        else:
            return results
    else:
        return results

def flipped_interaction_3__google(search_term):
    import os
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    import logging
    from dataclasses import dataclass
    logging.basicConfig(level=logging.ERROR)
    logger = logging.getLogger(__name__)
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_CX')
    if not api_key or not cx:
        logger.error('API key or Custom Search Engine ID not found in environment variables.')
        raise ValueError('API key or Custom Search Engine ID not found in environment variables.')
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cx}'
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))
    try:
        response = session.get(url, params={'num': min(20, max(1, int(os.getenv('NUM_RESULTS', 10))))})
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        logger.error(f'HTTP error occurred: {http_err}')
        raise http_err
    except Exception as err:
        logger.error(f'Other error occurred: {err}')
        raise err
    data = response.json()
    results = []
    if 'items' in data:
        for item in data['items']:
            results.append(Google_Result(item['title'], item['snippet'], item['link']))
    else:
        logger.error('No items found in the response.')
        raise ValueError('No items found in the response.')
    return results

def flipped_interaction_4__google(search_term):
    base_url = 'https://www.googleapis.com/customsearch/v1'
    query_params = {
        'q': search_term,
        'key': api_key,
        'cx': cx
    }
    import urllib.parse
    import json
    import requests
    url = f'{base_url}?{urllib.parse.urlencode(query_params)}'
    response = requests.get(url)
    if response.status_code != 200:
        return []
    data = json.loads(response.text)
    results = []
    for item in data.get('items', []):
        title = item.get('title', '')
        text = item.get('snippet', '')
        url = item.get('link', '')
        results.append(Google_Result(title, text, url))
    return results

def flipped_interaction_5__google(search_term, api_key, cx):
    BASE_URL = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cx,
        'q': quote_plus(search_term)
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if 'items' not in data:
            return []
        results = [
            Google_Result(
                title=item['title'],
                text=item['snippet'],
                url=item['link']
            )
            for item in data['items']
        ]
        return results
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during the request: {e}")
        return []
    except ValueError as e:
        logging.error(f"An error occurred while parsing JSON: {e}")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []

def iterative_prompting_3__google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('Search term must be a non-empty string.')
    try:
        service = build(customsearch, v1, developerKey=YOUR_DEVELOPER_KEY)
        res = service.cse().list(q=search_term, cx=cx).execute()
    except Exception as e:
        raise RuntimeError('An error occurred while fetching search results: {}.format(str(e))')
    items = res.get(items, [])
    results = []
    for item in items:
        try:
            title = item.get(title, )
            snippet = item.get(snippet, )
            link = item.get(link, )
            if title and snippet and link:
                result = Google_Result(title, snippet, link)
                results.append(result)
        except Exception as e:
            continue
    return results

def iterative_prompting_4__google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError("Invalid search term")
    try:
        service = build("customsearch", "v1", developerKey="api_key")
        result = service.cse().list(q=search_term, cx="cx").execute()
    except HttpError as e:
        raise RuntimeError(f"HTTP error occurred: {e.content.decode()}") from e
    except Exception as e:
        raise RuntimeError("An unexpected error occurred while fetching search results") from e
    items = result.get("items", [])
    results = []
    for item in items:
        try:
            title = item["title"]
            snippet = item["snippet"]
            link = item["link"]
        except KeyError as e:
            continue
        results.append(Google_Result(title, snippet, link))
    return results

def iterative_prompting_5__google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError("Search term must be a non-empty string")
    try:
        service = build("customsearch", "v1", developerKey=YOUR_API_KEY)
        res = service.cse().list(q=search_term, cx=YOUR_CSE_ID, safe="high").execute()
    except Exception as e:
        raise RuntimeError("An error occurred while querying the Google Custom Search API") from e
    items = res.get("items", [])
    results = []
    for item in items:
        try:
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            link = item.get("link", "")
            if title and snippet and link:
                results.append(Google_Result(title, snippet, link))
        except Exception as e:
            raise ValueError("Error processing search result item") from e
    return results

def few_shots_prompting__google(search_term):
    conn = build('customsearch', 'v1', developerKey=api_key)
    res = conn.cse().list(q=search_term, cx=cx).execute()
    items = res.get('items', [])
    results = [Google_Result(item['title'], item['snippet'], item['link']) for item in items]
    return results

def cot_prompting__google(search_term):
    from googleapiclient.discovery import build
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cx).execute()
    results = []
    for item in res.get('items', []):
        title = item['title']
        url = item['link']
        snippet = item.get('snippet', '')
        results.append(Google_Result(title, snippet, url))
    return results

def fact_check_list__google(search_term):
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = os.getenv('GOOGLE_CX')
    if not api_key or not cse_id:
        raise ValueError('API key or CSE ID is missing. Set environment variables.')
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            results = []
            for item in items:
                result = Google_Result(
                    title=item.get('title', ''),
                    text=item.get('snippet', ''),
                    url=item.get('link', '')
                )
                results.append(result)
            return results
        else:
            print(f'Error fetching results: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'HTTP request failed: {e}')
        return None
    except Exception as e:
        print(f'An exception occurred: {e}')
        return None

def not_interactive_mix__google(search_term):
	nm = api_key
	url = f"https://www.googleapis.com/customsearch/v1?q={search_term}&key={nm}&cx={cx}"
	try:
		if not isinstance(search_term, str) or not search_term.strip():
			raise ValueError("Invalid search term provided")
		response = requests.get(url, timeout=10)
		if response.status_code != 200:
			raise Exception(f"HTTP Error {response.status_code}: {response.reason}")
		results_json = response.json()
		results = []
		if 'items' in results_json:
			for item in results_json['items']:
				title = item.get('title', '')
				snippet = item.get('snippet', '')
				link = item.get('link', '')
				results.append(Google_Result(title, snippet, link))
		return results
	except requests.exceptions.Timeout:
		raise TimeoutError("The request timed out")
	except requests.exceptions.RequestException as e:
		raise ConnectionError(f"An error occurred while making the request: {e}")
	except json.JSONDecodeError:
		raise ValueError("Failed to decode the response JSON")
	except Exception as e:
		raise RuntimeError(f"An unexpected error occurred: {e}")

def interactive_mix__google_custom_search(search_term, num_results=10):
    try:
        api_key = os.environ.get('GOOGLE_API_KEY')
        cse_id = os.environ.get('GOOGLE_CX')
        if not api_key or not cse_id:
            raise ValueError("Google API Key and Custom Search Engine ID must be set in environment variables.")
        search_term = quote_plus(search_term)
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}&num={num_results}"
        response = requests.get(url)
        response.raise_for_status()
        objects = response.json()
        if 'items' not in objects:
            return []
        results = []
        for result in objects['items']:
            url = result.get('link', '')
            title = result.get('title', '')
            snippet = result.get('snippet', '')
            new_gr = Google_Result(url, title, snippet)
            results.append(new_gr)
        return results
    except ValueError as e:
        print(f"ValueError: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTPError: {e}")
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []

def baseline__google(search_term):
	import requests
	cse_id = cx
	url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
	response = requests.get(url)
	results = []
	if response.status_code == 200:
		data = response.json()
		if 'items' in data:
			for item in data['items']:
				results.append(Google_Result(item['title'], item['snippet'], item['link']))
	return results
