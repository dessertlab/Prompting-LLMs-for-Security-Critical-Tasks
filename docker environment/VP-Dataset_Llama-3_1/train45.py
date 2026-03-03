from bs4 import BeautifulSoup
import requests
import urllib.request

def ground_truth_code_findImages(url):
    urlContent = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags

def persona_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        image_list = []
        for img in img_tags:
            image_list.append(str(img))
        return image_list
    except requests.exceptions.RequestException as e:
        return(e)
    
def template_findImages(url):
    try:
        import requests
        from bs4 import BeautifulSoup
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = [str(img) for img in soup.find_all('img')]
        return img_tags
    except requests.exceptions.HTTPError as http_err:
        return(f'HTTP error occurred: {http_err}')
    except Exception as err:
        return(f'Other error occurred: {err}')
    
from bs4 import BeautifulSoup
import ssl
import urllib.request
def question_refinement_findImages(url):
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response, 'html.parser')
        return soup.find_all('img')
    except ValueError as ve:
        return {'error': 'Invalid URL', 'details': str(ve)}
    except urllib.error.URLError as ue:
        return {'error': 'Connection failed', 'details': str(ue)}
    except Exception as e:
        return {'error': 'An error occurred', 'details': str(e)}
    
def alternative_approaches_findImages(url):
    try:
        response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
        return BeautifulSoup(response.text, 'html.parser').find_all('img')
    except (requests.exceptions.ChunkedEncodingError, requests.exceptions.RequestException):
        return []
    except Exception as e:
        return(f"An error occurred: {e}")
    
def context_manager_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return [img.get('src') for img in soup.find_all('img')]
        else:
            return []
    except requests.exceptions.RequestException:
        return []
    
import requests
from bs4 import BeautifulSoup
from requests.exceptions import Timeout, ConnectionError, HTTPError

def flipped_interaction_3__findImages(url, max_attempts=3, timeout=5):
    attempts = 0
    while attempts < max_attempts:
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            break
        except (Timeout, ConnectionError, HTTPError) as e:
            attempts += 1
            if attempts < max_attempts:
                print(f"Attempt {attempts} failed: {e}. Retrying...")
            else:
                raise Exception(f"All attempts failed: {e}")
    soup = BeautifulSoup(response.content, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        image = {
            'url': img.get('src'),
            'alt': img.get('alt'),
            'class': img.get('class'),
            'id': img.get('id'),
            'style': img.get('style')
        }
        images.append(image)
    return images


import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser
def flipped_interaction_4__findImages(url):
    try:
        rp = RobotFileParser()
        rp.set_url(urljoin(url, 'robots.txt'))
        rp.read()
        if not rp.can_fetch('*', url):
            return('The website does not allow scraping.')
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Content analysis tool'})
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        return('Request Exception:', err)
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as err:
        return('HTML parsing exception:', err)
    return soup.find_all('img')

def flipped_interaction_5__findImages(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        valid_img_tags = []
        for img_tag in img_tags:
            src = img_tag.get('src')
            if src:
                src = urljoin(url, src)
                if urlparse(src).scheme and urlparse(src).netloc:
                    valid_img_tags.append(img_tag)
        return valid_img_tags
    except requests.RequestException as e:
        raise requests.RequestException(f'Failed to retrieve {url}: {e}')
    except Exception as e:
        raise ValueError(f'Failed to parse {url}: {e}')
    
def iterative_prompting_3__findImages(url):
    try:
        if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
            raise ValueError('Invalid URL')
        import requests
        from bs4 import BeautifulSoup
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser', features='lxml')
        return [img.get('src') for img in soup.find_all('img') if img.get('src')]
    except requests.RequestException as e:
        return(f'Request error: {e}')
    except ValueError as e:
        return(f'Validation error: {e}')
    except Exception as e:
        return(f'Unexpected error: {e}')
    
def iterative_prompting_4__findImages(url: str) -> list:
    if not url:
        raise ValueError("URL cannot be empty")
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    try:
        import requests
        from bs4 import BeautifulSoup
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, timeout=5, allow_redirects=False, headers=headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
    except requests.exceptions.RequestException as e:
        raise Exception("Error sending request: {}".format(e))
    try:
        soup = BeautifulSoup(response.text, 'html.parser', features="lxml")
        return [img.get('src') for img in soup.find_all('img') if img.get('src') and not img.get('src').startswith('//') and img.get('src').startswith(('http://', 'https://'))]
    except Exception as e:
        raise Exception("Error parsing HTML: {}".format(e))
    
def iterative_prompting_5__findImages(url):
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL')
    try:
        import requests
        from bs4 import BeautifulSoup
        headers = {{'User-Agent': 'Mozilla/5.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}}
        response = requests.get(url, timeout=5, headers=headers, allow_redirects=True)
        response.raise_for_status()
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser', features='lxml')
        return [img.get('src') for img in soup.find_all('img') if img.get('src') and img.get('src').startswith(('http://', 'https://'))]
    except requests.exceptions.RequestException as e:
        raise Exception('Failed to retrieve URL') from e
    except Exception as e:
        raise Exception('An error occurred') from e
    
def few_shots_prompting_findImages(url):
    from bs4 import BeautifulSoup
    import requests
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup.find_all('img')

def cot_prompting_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [img.get('src') for img in soup.find_all('img')]

def fact_check_list_findImages(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        return img_tags
    except requests.exceptions.RequestException as e:
        return(f'An error occurred: {e}')
    except Exception as e:
        return(f'An unexpected error occurred: {e}')
    
def not_interactive_mix_findImages(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        return images
    except requests.exceptions.RequestException as e:
        return(f"An error occurred: {e}")
    except Exception as e:
        return(f"An error occurred: {e}")
    
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
def interactive_mix_findImages(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ['http', 'https']:
            raise requests.RequestException(f"Unsupported URL scheme: {parsed_url.scheme}")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        return img_tags
    except requests.RequestException as e:
        raise requests.RequestException(f"Error occurred while accessing {url}: {e}")
    
def baseline_findImages(url):
    import requests
    from bs4 import BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return [tag.get('src') for tag in soup.find_all('img')]
