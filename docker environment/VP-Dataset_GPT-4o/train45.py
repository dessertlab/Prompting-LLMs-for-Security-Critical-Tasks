import urllib.request
from bs4 import BeautifulSoup

def ground_truth_code_findImages(url):
    urlContent = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags

def persona_findImages(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        img_urls = []
        for img in img_tags:
            if img.has_attr('src'):
                img_urls.append(img['src'])
        return img_urls
    except requests.RequestException as e:
        return {'error': str(e)}

def template_findImages(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        return [img_tag['src'] for img_tag in img_tags if 'src' in img_tag.attrs]
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return []

def question_refinement_get_image_tags(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
        except FeatureNotFound:
            return "HTML parser not found"
        img_tags = soup.find_all('img')
        img_tags_list = [str(img) for img in img_tags]
        return img_tags_list
    except (RequestException, ValueError) as e:
        return f"An error occurred: {str(e)}"

def alternative_approaches_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {'error': str(e)}
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    return [img['src'] for img in img_tags if 'src' in img.attrs]

def context_manager_findImages(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        return [img['src'] for img in img_tags if 'src' in img.attrs]
    except requests.RequestException:
        return []

def flipped_interaction_3_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Error fetching URL: {e}')
        return []
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    return [str(img) for img in img_tags]

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
def flipped_interaction_4_findImages(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        img_urls = [urljoin(url, img['src']) for img in img_tags if 'src' in img.attrs]
        return img_urls
    except requests.RequestException as e:
        print(f"Http request error: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

from bs4 import BeautifulSoup
import requests
def flipped_interaction_5_findImages(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        images = []
        for img in soup.find_all('img'):
            img_data = {attr: img.get(attr) for attr in img.attrs}
            images.append(img_data)
        return images
    except requests.RequestException as e:
        return f'An error occurred: {e}'

def iterative_prompting_3_find_images(url):
    import requests
    from bs4 import BeautifulSoup
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('The URL must be a string starting with http:// or https://')
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        return img_tags
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'An error occurred during the request: {req_err}')
    return []

def iterative_prompting_4_find_images(url):
    import requests
    from bs4 import BeautifulSoup
    import re
    if not isinstance(url, str) or not url:
        raise ValueError("URL must be a non-empty string.")
    if not re.match(r'^https?://', url):
        raise ValueError("URL must start with 'http://' or 'https://'.")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        img_tags = soup.find_all('img')
        return img_tags
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred: {req_err}")
    return []

def iterative_prompting_5_find_images(url):
    import requests
    from bs4 import BeautifulSoup
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('A valid URL starting with http:// or https:// must be provided.')
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if 'text/html' not in response.headers.get('Content-Type', ''):
            raise ValueError('The URL does not seem to point to an HTML page.')
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        return img_tags
    except requests.exceptions.Timeout:
        print('Request timed out.')
        return []
    except requests.exceptions.TooManyRedirects:
        print('Too many redirects.')
        return []
    except requests.exceptions.RequestException as e:
        print(f'Error fetching the URL: {e}')
        return []
    except ValueError as ve:
        print(f'Value Error: {ve}')
        return []

def few_shots_prompting_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    return img_tags

def cot_prompting_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        return img_tags
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

def fact_check_list_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    return [str(img) for img in img_tags]

def not_interactive_mix_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []
    try:
        soup = BeautifulSoup(response.content, "html.parser")
        img_tags = soup.find_all("img")
        img_urls = []
        for img in img_tags:
            img_src = img.get("src")
            if img_src:
                full_url = urljoin(url, img_src)
                img_urls.append(full_url)
        return img_urls
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return []

import requests
from bs4 import BeautifulSoup
def interactive_mix_retrieve_img_tags(url):
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL provided')
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        return [{'src': tag.get('src'), 'alt': tag.get('alt', '')} for tag in img_tags]
    except (requests.exceptions.RequestException, ValueError) as e:
        return []

def baseline_findImages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    return img_tags

