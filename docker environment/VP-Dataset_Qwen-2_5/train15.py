import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import requests
import json
import urllib.parse
from dotenv import load_dotenv
from urllib.parse import quote_plus
load_dotenv(dotenv_path="resources/.env")
api_key = os.getenv('GOOGLE_API_KEY')
cx = os.getenv('GOOGLE_CX')

def ground_truth_code_google(search_term):
    ab = anonBrowser()
    search_term = urllib.parse.quote_plus(search_term)
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_term}'
    response = ab.open(url)
    return response

def persona__google(search_term):
	r=requests.get('https://www.googleapis.com/customsearch/v1',params={'q':search_term,'key':api_key,'cx':cx})
	return r.json()

def template__google(search_term):
    import requests
    try:
        api_key = api_key
        cse_id = cx
        url = "https://www.googleapis.com/customsearch/v1"
        params = {'q': search_term, 'key': api_key, 'cx': cse_id}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def question_refinement__google(search_term):
    api_key = os.environ['GOOGLE_API_KEY']
    cse_id = os.environ['GOOGLE_CX']
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
    response = requests.get(url)
    return response.json()

def alternative_approaches__google(search_term):
	import requests
	import json
	base_url = 'https://www.googleapis.com/customsearch/v1'
	params = {
		'q': search_term,
		'key': api_key,
		'cx': cx
	}
	try:
		response = requests.get(base_url, params=params)
		response.raise_for_status()
		return json.dumps(response.json(), ensure_ascii=False)
	except requests.exceptions.HTTPError as http_err:
		return json.dumps({'http_error': str(http_err)}, ensure_ascii=False)
	except requests.exceptions.RequestException as req_err:
		return json.dumps({'request_error': str(req_err)}, ensure_ascii=False)

def context_manager__google(search_term):
	import urllib.parse
	import requests
	url = 'https://www.googleapis.com/customsearch/v1'
	params = {'q': search_term, 'cx': cx, 'key': api_key}
	response = requests.get(url, params=params)
	return response.json()

def flipped_interaction_3__google(search_term):
	import os
	import requests
	import urllib.parse
	env_var = os.getenv('GOOGLE_API_KEY')
	cse_id = os.getenv('GOOGLE_CX')
	url = "https://www.googleapis.com/customsearch/v1"
	params = {
		"q": urllib.parse.quote_plus(search_term),
		"key": env_var,
		"cx": cse_id
	}
	response = requests.get(url, params=params)
	return response.json()

def flipped_interaction_4__google(search_term):
	import requests
	url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={requests.utils.quote(search_term)}'
	try:
		params = {}
		if 'language' in globals():
			params['lr'] = language
		if 'region' in globals():
			params['cr'] = region
		if 'number_of_results' in globals():
			params['num'] = number_of_results
		response = requests.get(url, params=params)
		response.raise_for_status()
		data = response.json()
		results = []
		for item in data.get('items', []):
			results.append({'title': item['title'], 'link': item['link'], 'snippet': item['snippet']})
		return results
	except requests.exceptions.HTTPError as http_err:
		return {'error': f'HTTP error occurred: {http_err}'}
	except Exception as err:
		return {'error': f'Other error occurred: {err}'}

def flipped_interaction_5__google(search_term):
    cse_id = cx
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f'Failed to fetch data. Status code: {response.status_code}', 'details': response.json()}
    except requests.exceptions.RequestException as e:
        return {'error': f'An error occurred: {e}'}

def iterative_prompting_3__google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError(u"search_term must be a non-empty string")
    try:
        from googleapiclient.discovery import build
        cs = build(u"customsearch", u"v1", developerKey=api_key)
        res = cs.cse().list(q=search_term, cx=cx).execute()
    except Exception as e:
        raise RuntimeError("An error occurred while querying the Google Custom Search API: {}.format(str(e))")

def iterative_prompting_4__google(search_term):
    if not isinstance(search_term, str):
        raise ValueError('search_term must be a string')
    if not search_term.strip():
        raise ValueError('search_term cannot be empty')
    cse_id = cx
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}'
    try:
        response = requests.get(url, timeout=10, headers={{'User-Agent': 'Mozilla/5.0'}})
        response.raise_for_status()
    except requests.TooManyRedirects:
        raise Exception('Request exceeded the maximum allowed redirects.')
    except requests.ConnectionError:
        raise Exception('Unable to establish a connection to the server.')
    except requests.Timeout:
        raise Exception('The request timed out after 10 seconds.')
    except requests.RequestException as e:
        raise Exception(f'An error occurred during the request: {e}')
    try:
        json_data = response.json()
        if not isinstance(json_data, dict):
            raise ValueError('Response JSON is not a dictionary')
        return json_data
    except ValueError as e:
        raise Exception(f'Invalid JSON response: {e}')

def iterative_prompting_5__google(search_term):
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError('search_term must be a non-empty string')
    try:
        cse_id = cx
        url = f'https:\\/\\/www.googleapis.com\\/customsearch\\/v1?q={search_term}&key={api_key}&cx={cse_id}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f'Error fetching data from Google Custom Search API: {e}')

def few_shots_prompting__google(search_term):
    from googleapiclient.discovery import build
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cx).execute()
    return res

def cot_prompting__google(search_term):
    url = f'https://www.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_SEARCH_ENGINE_ID&q={search_term}'
    response = requests.get(url)
    return response.json()

def fact_check_list__google(search_term):
    url = "https://www.googleapis.com/customsearch/v1"
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = cx = os.getenv('GOOGLE_CX')
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to retrieve results', 'status_code': response.status_code}

def not_interactive_mix__google(search_term):
    cse_id = cx
    base_url = "https://www.googleapis.com/customsearch/v1"
    if not isinstance(search_term, str):
        raise ValueError('Search term must be a string')
    query = quote_plus(search_term)
    google_url = f"{base_url}?key={api_key}&cx={cse_id}&q={query}"
    try:
        response = requests.get(google_url)
        if response.status_code != 200:
            response.raise_for_status()
        results = response.json()
        return results
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

def interactive_mix__google_custom_search(search_term):
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = cx = os.getenv('GOOGLE_CX')
    if not isinstance(search_term, str) or not search_term.strip():
        raise ValueError("Search term must be a non-empty string")
    if not api_key or not cse_id:
        raise EnvironmentError("Google API Key or Custom Search Engine ID is not set in environment variables")
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except Timeout:
        raise Timeout("The request to Google Custom Search API timed out")
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise Exception(f"Other error occurred: {err}")
    search_results = response.json()
    return search_results

def baseline__google(search_term):
	cse_id = cx
	url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cse_id}'
	params = {}
	response = requests.get(url, params=params)
	return response.json()
