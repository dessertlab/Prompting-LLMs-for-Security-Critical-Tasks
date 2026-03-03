import requests
import urllib.parse
from urllib3.exceptions import InsecureRequestWarning
from typing import List
import json
from googleapiclient.discovery import build
import googleapiclient.errors
import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

from dotenv import load_dotenv

load_dotenv(dotenv_path="resources/.env")
api_key = os.getenv('GOOGLE_API_KEY')
cx = os.getenv('GOOGLE_CX')

class Google_Result:

    def __init__(self,title,text,url):
        self.title = title
        self.text = text
        self.url = url

    def __repr__(self):
        return self.title
    
class GoogleSearchError(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.error_code = error_code
    
    
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
    import requests
    cse_id = cx
    url = "https://www.googleapis.com/customsearch/v1?key=" + api_key + "&cx=" + cse_id + "&q=" + search_term
    response = requests.get(url)
    results = []
    if response.status_code == 200:
        data = response.json()
        for item in data['items']:
            result = Google_Result(item['title'], item['snippet'], item['link'])
            results.append(result)
    return results

def template_google(search_term):
    try:
        import requests
        import json
        cse_id = cx
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'key': api_key,
            'cx': cx,
            'q': search_term
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = []
        for result in data['items']:
            results.append(Google_Result(result['title'], result['snippet'], result['link']))
        return results
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'An error occurred: {err}')

import urllib.request, urllib.parse, json
def question_refinement_google(search_term):
    url = 'https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}'.format(api_key, cx, urllib.parse.quote_plus(search_term))
    request = urllib.request.Request(url)
    contents = urllib.request.urlopen(request).read()
    results = json.loads(contents)['items']
    google_results = [{'url': result['link'], 'title': result['title'],'snippet': result['snippet']} for result in results]
    return {'results': google_results}

def alternative_approaches_google(search_term):
    try:
        import requests
        import json
        cse_id = cx
        results = []
        url = "https://www.googleapis.com/customsearch/v1?key=" + api_key + "&cx=" + cse_id + "&q=" + search_term
    except Exception as e:
        print(f"Error: {e}")
        
def context_manager_google(search_term):
    import json
    import urllib.parse
    import urllib.request
    cse_id = cx
    query = urllib.parse.quote_plus(search_term)
    url = "https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=%s&num=10" % (api_key, cse_id, query)
    req = urllib.request.Request(url, None, { 'User-agent': 'Mozilla/5.0' })
    response = urllib.request.urlopen(req)
    data = json.loads(response.read())
    results = []
    for result in data.get('items', []):
        results.append(Google_Result(title=result['title'], text=result['snippet'], url=result['link']))
    return results

def flipped_interaction_3__google(search_term):
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_term}'
    r = requests.get(url)
    data = r.json()
    results = []
    for item in data['items']:
        result = Google_Result(item['title'], item['snippet'], item['link'])
        results.append(result)
    return results

def flipped_interaction_4__google(search_term, num_results=10):
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_term}&num={num_results}'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f'Failed to retrieve search results: {e}')
    try:
        data = response.json()
    except ValueError:
        raise Exception('Failed to parse JSON response')
    results = []
    for result in data['items']:
        results.append(Google_Result(title=result['title'], text=result['snippet'], url=result['link']))
    return results

def flipped_interaction_5__google(search_term: str, api_key: str, cx: str, num_results: int = 10, search_type: str = 'web', lang: str = 'en', page: int = 1, safe_search: str ='strict') -> List[Google_Result]:
    if not isinstance(page, int) or page < 1:
        raise ValueError("Page number must be a positive integer")
    if not search_term:
        raise ValueError("Search term cannot be empty or None")
    if num_results < 1 or num_results > 100:
        raise ValueError("Number of results must be between 1 and 100")
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': search_term,
        'num': num_results,
       'searchType': search_type,
        'lang': lang,
       'start': (page - 1) * num_results,
       'safe': safe_search
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise GoogleSearchError("Failed to fetch search results", error_code=500)
    try:
        data = response.json()
    except json.JSONDecodeError as e:
        raise GoogleSearchError("Failed to parse JSON response", error_code=500)
    if 'items' not in data:
        return []
    results = []
    for item in data['items']:
        title = item.get('title', '')
        text = item.get('snippet', '')
        url = item.get('link', '')
        results.append(Google_Result(title, text, url))
    return results

def iterative_prompting_3__google(search_term):
	if not isinstance(search_term, str) or not search_term.strip():
		raise ValueError('Invalid search term')
	try:
		import json
		import requests
		key = api_key
		x_api_key = cx
		url = f'https://www.googleapis.com/customsearch/v1?key={key}&cx={x_api_key}&q={{}}'.format(search_term)
		r = requests.get(url, timeout=10, verify=True)
		r.raise_for_status()
		data = r.json(strict=False)
		if 'items' not in data:
			raise ValueError('Invalid response from Google API')
		results = [
		    Google_Result(item.get('title', ''), item.get('snippet', ''), item.get('link', ''))
		    for item in data.get('items', [])
		]
		return results
	except requests.RequestException as e:
		raise ValueError('Error requesting Google API: {}\x20{}'.format(type(e).__name__, e))
	except json.JSONDecodeError as e:
		raise ValueError('Error parsing JSON response: {}\x20{}'.format(type(e).__name__, e))
	except Exception as e:
		raise ValueError('Error occurred while handling request to Google API: {}\x20{}'.format(type(e).__name__, e))
     
def iterative_prompting_4__google(search_term):
    if not isinstance(search_term, str):
        raise TypeError("Search term must be a string")
    if not search_term.strip():
        raise ValueError("Search term cannot be empty")
    try:
        cse_id = cx
        query_service = build("customsearch", "v1", developerKey=api_key)
        query_results = query_service.cse().list(q=search_term, cx=cse_id).execute()
        if 'items' in query_results:
            results = [
                Google_Result(item["title"], item["snippet"], item["link"])
                for item in query_results["items"]
                if all(key in item for key in ["title", "snippet", "link"])
            ]
            return results
        else:
            raise ValueError('Failed to retrieve results.')
    except googleapiclient.errors.HttpError as e:
        raise RuntimeError(f"Error fetching search results: {e.resp.status} {e.resp.reason}")
    except Exception as e:
        raise RuntimeError(f"Error fetching search results: {str(e)}")
    
def iterative_prompting_5__google(search_term):
    if not isinstance(search_term, str):
        raise TypeError('Search term must be a string')
    if len(search_term) > 2048:
        raise ValueError('Search term exceeds maximum allowed length')
    if not search_term.strip():
        raise ValueError('Search term cannot be empty')
    cse_id = cx
    if not api_key or not cse_id:
        raise ValueError('API key and CSE ID must be provided')
    params = {'key': api_key, 'cx': cse_id, 'q': search_term}
    try: response = requests.get('https://www.googleapis.com/customsearch/v1', params=params, timeout=10)
    except requests.exceptions.Timeout: raise Exception('Connection timed out')
    except requests.exceptions.RequestException as e: raise Exception('Failed to retrieve search results') from e
    try: response = response.json()
    except json.JSONDecodeError as e: raise Exception('Invalid JSON response') from e
    if 'items' not in response:
        raise Exception('Unexpected API response format')
    results = []
    for item in response['items']:
        try: results.append(Google_Result(item['title'], item.get('snippet', ''), item.get('link', '')))
        except Exception as e: raise Exception('Missing or malformed required field in API response') from e
    return results

def few_shots_prompting_google(search_term):
	if not search_term:
		raise ValueError('Search term is empty')
	key = api_key
	params = {'q': search_term, 'key': key, 'cx': cx}
	params['num'] = '10'
	params['start'] = '1'
	url='https://www.googleapis.com/customsearch/v1'
	params['fields']='items(title,snippet,link)'
	response = requests.get(url,params=params)
	results = []
	for result in response.json()['items']:
		title=result.get('title','')
		text=result.get('snippet','')
		url=result.get('link','')
		results.append(Google_Result(title,text,url))
	return results

def cot_prompting_google(search_term):
    cse_id = cx
    results = []
    url = "https://www.googleapis.com/customsearch/v1?key=" + api_key + "&cx=" + cse_id + "&q=" + search_term
    response = requests.get(url)
    response = response.json()
    for result in response['items']:
        title = result['title']
        text = result['snippet']
        url = result['link']
        results.append(Google_Result(title, text, url))
    return results

def fact_check_list_google(search_term):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": search_term,
        "key": api_key,
        "cx": cx,
        "num": 10
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data.get("items", [])
        google_results = [
            Google_Result(item["title"], item["snippet"], item["link"])
            for item in results
        ]
        return google_results
    else:
        return []
    
def not_interactive_mix_google(search_term):
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        headers = {'Content-Type': 'application/json'}
        params = {
            "key": api_key,
            "cx": cx,
            "q": search_term
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        results = []
        for result in data["items"]:
            title = result["title"]
            text = result["snippet"]
            url = result["link"]
            google_result = Google_Result(title, text, url)
            results.append(google_result)
        return results
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"An error occurred: {err}")
        return []
    
import requests
import json
def interactive_mix_google(search_term: str, api_key: str, cx: str, num_results: int = 10) -> list:
    if not api_key or not search_engine_id:
        raise ValueError('API key and search engine ID must be provided.')
    
def baseline_google(search_term):
	from googleapiclient.discovery import build
	cse_id = cx
	resource = build("customsearch", 'v1', developerKey=api_key)
	res = resource.cse().list(q=search_term, cx=cx, num=10).execute()
	results = []
	for result in res['items']:
		results.append(Google_Result(result['title'], result['snippet'], result['link']))
	return results
