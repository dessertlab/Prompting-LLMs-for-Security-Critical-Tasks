import urllib.request
from bs4 import BeautifulSoup

def ground_truth_code_findImages(url):
    urlContent = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags

import requests
from bs4 import BeautifulSoup
def persona_findImages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', src=True)
    return img_tags

def template_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        return img_tags
    except requests.exceptions.RequestException as e:
        return {'error': 'Failed to retrieve or parse the URL. Reason: ' + str(e)}

import requests
from bs4 import BeautifulSoup
def question_refinement_findImages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_srcs = [(tag.get('src') or None) for tag in img_tags]
    return img_srcs

def alternative_approaches_findImages(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        return img_tags
    except requests.exceptions.RequestException as e:
        return(f'An error occurred: {e}')

def context_manager_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    return img_tags

def iterative_prompting_3_find_images(url):
    import requests
    from bs4 import BeautifulSoup
    if not isinstance(url, str) or not url.strip().startswith('http'):
        raise ValueError('Invalid URL provided')
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return(f'An error occurred while fetching the URL: {e}')
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    return images

def iterative_prompting_4_find_images(url):
    import requests
    from bs4 import BeautifulSoup
    if not isinstance(url, str) or not url.strip().startswith(('http://', 'https://')):
        raise ValueError('Invalid URL provided')
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f'Failed to retrieve data from {url}: {e}')
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    return img_tags

def iterative_prompting_5_find_images(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return []
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
    except Exception as e:
        return []
    return images

def few_shots_prompting_findImages(url):
    import requests
    import bs4
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    return img_tags

import requests
from bs4 import BeautifulSoup
def cot_prompting_findImages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    return img_tags

import requests
from bs4 import BeautifulSoup
def fact_check_list_find_images(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        img_srcs = [img['src'] for img in img_tags if 'src' in img.attrs]
        return img_srcs
    else:
        response.raise_for_status()

import requests
from bs4 import BeautifulSoup
def not_interactive_mix_findImages(url):
	try:
		response = requests.get(url)
		response.raise_for_status()
		soup = BeautifulSoup(response.text, 'html.parser')
		img_tags = soup.find_all('img')
		img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
		return img_urls
	except requests.RequestException as e:
		return(f"An error occurred while fetching the URL: {e}")
	except Exception as e:
		return(f"An unexpected error occurred: {e}")

def baseline_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    return img_tags

