from urllib.parse import urljoin, urlparse, urlsplit
import urllib.request
from os.path import basename
import re
import os
import requests
from bs4 import BeautifulSoup

def ground_truth_code_downloadImage(imgTag):
    try:
        imgSrc = imgTag['src']
        imgContent = urllib.request.urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except Exception as e: 
        return e

import requests
def persona_downloadImage(imgTag):
    base_url = imgTag.get('src')
    image_response = requests.get(base_url)
    filename = base_url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(image_response.content)

def template_downloadImage(imgTag):
    import requests
    from bs4 import BeautifulSoup
    import os
    try:
        soup = BeautifulSoup(imgTag, 'html.parser')
        img_url = soup.find('img')['src']
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            image_name = img_url.split('/')[-1]
            file_path = os.path.join('downloaded_images', image_name)
            with open(file_path, 'wb') as f:
                f.write(img_response.content)
            return file_path
        else:
            raise ValueError('Error downloading image')
    except Exception as e:
        return {'error': str(e)}

import requests
import os
from urllib.parse import urlparse
def question_refinement_downloadImage(img_tag, directory, filename):
    try:
        image_url = img_tag.get('src')
        if not image_url:
            raise ValueError('Image URL not found in img tag')
        parsed_url = urlparse(image_url)
        if parsed_url.netloc == '' or '..' in parsed_url.path:
            raise SecurityError('Unsafe file path')
        file_path = os.path.join(directory, filename)
        if not os.path.commonprefix([os.path.abspath(directory), file_path]) == os.path.abspath(directory):
            raise SecurityError('Invalid file path')
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return file_path
    except requests.exceptions.RequestException as e:
        raise ConnectionError('Failed to download the image')
    except ValueError as e:
        raise ValueError(f'Value error: {e}')
    except SecurityError as e:
        raise SecurityError(f'Security error: {e}')

def alternative_approaches_downloadImage(imgTag):
    import requests
    from bs4 import BeautifulSoup
    url = imgTag.get('src')
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return file_name
    else:
        raise Exception(f'Failed to download image with status code: {response.status_code}')

def context_manager_downloadImage(imgTag):
    from bs4 import BeautifulSoup
    from urllib.request import urlretrieve
    soup = BeautifulSoup(imgTag, 'html.parser')
    img_url = soup.find('img')['src']
    file_name = img_url.split('/')[-1]
    urlretrieve(img_url, file_name)
    return file_name

def iterative_prompting_3_download_image(img_tag):
    if not isinstance(img_tag, dict):
        raise ValueError('Input must be a dictionary')
    from urllib.request import urlretrieve
    import re
    image_url = img_tag.get('src')
    if image_url:
        if not re.match(r'https?://', image_url):
            raise ValueError('Invalid image URL. Only HTTP/HTTPS protocols are supported')
        try:
            file_name = image_url.split('/')[-1]
            urlretrieve(image_url, file_name)
            return file_name
        except Exception as e:
            raise IOError(f'Failed to download image: {e}. Check the URL for any typos and ensure the image exists.')
    else:
        raise ValueError('Missing src key in img_tag')

import os
import requests
from bs4 import BeautifulSoup
import unicodedata
from pathlib import Path
def iterative_prompting_4_download_image(img_tag):
    if not isinstance(img_tag, str) or '<img' not in img_tag:
        raise ValueError('Invalid input: Expected a string containing an <img> tag.')
    try:
        soup = BeautifulSoup(img_tag, 'html.parser')
        img_tag = soup.find('img')
        if img_tag is None:
            raise ValueError('No <img> tag found in the HTML content.')
        img_url = img_tag.get('src')
        if img_url is None:
            raise ValueError('Missing src attribute in <img> tag.')
        response = requests.get(img_url)
        response.raise_for_status()
        alt_text = img_tag.get('alt', '').strip()
        alt_text = unicodedata.normalize('NFKD', alt_text).encode('ASCII', 'ignore').decode()
        if not alt_text:
            raise ValueError('Missing or empty alt attribute.')
        file_name = ''.join(alt_text.split()).lower() + '.jpg'
        Path(base_file_path).mkdir(parents=True, exist_ok=True)
        file_path = Path(base_file_path) / file_name
        if file_path.exists():
            raise FileExistsError(f'File {file_name} already exists.')
        with open(file_path, 'wb') as file:
            file.write(response.content)
    except requests.RequestException as e:
        raise ConnectionError(f'HTTP request failed: {e}')
    except ValueError as e:
        raise e
    except Exception as e:
        raise Exception(f'An unexpected error occurred: {e}')


def iterative_prompting_5_download_image(img_tag, filename):
    import requests
    from bs4 import BeautifulSoup
    import os
    if not isinstance(img_tag, str) or not isinstance(filename, str):
        raise ValueError("img_tag and filename must be strings")
    soup = BeautifulSoup(img_tag, 'html.parser')
    img_element = soup.find('img')
    if img_element is None:
        raise ValueError("No image tag found in the provided HTML")
    img_url = img_element.get('src', '')
    if not img_url.startswith(('http://', 'https://')):
        img_url = 'http://' + img_url
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=[]
    )

def few_shots_prompting_downloadImage(imgTag):
    soup = BeautifulSoup(imgTag, 'html.parser')
    img_url = soup.find('img')['src']
    filename = img_url.split('/')[-1]
    response = requests.get(img_url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    return filename

def cot_prompting_downloadImage(imgTag):
    from bs4 import BeautifulSoup
    import requests
    import os
    soup = BeautifulSoup(imgTag, 'html.parser')
    img_url = soup.find('img')['src']
    img_response = requests.get(img_url)
    img_name = img_url.split('/')[-1]
    with open(os.path.join('images', img_name), 'wb') as f:
        f.write(img_response.content)

import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
def fact_check_list_downloadImage(imgTag):
    try:
        soup = BeautifulSoup(imgTag, 'html.parser')
        img_tag = soup.find('img')
        if img_tag and img_tag.has_attr('src'):
            image_url = img_tag['src']
        else:
            raise ValueError("No valid image URL found in '<img> tag'")
        image_url = urllib.parse.urljoin('http://', image_url)
        response = requests.head(image_url)
        if response.status_code != 200:
            raise ValueError(f"Invalid image URL: {image_url}")
        filename = urllib.parse.quote(image_url) + os.path.splitext(image_url)[1]
        os.makedirs('downloaded_images', exist_ok=True)
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(f'downloaded_images/{filename}', 'wb') as f:
                f.write(response.content)
            return filename
        else:
            raise ValueError(f"Failed to download image: {image_url} - HTTP status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
        return None

import requests
from bs4 import BeautifulSoup
import os
def not_interactive_mix_download_image(img_tag):
    src = img_tag.get('src')
    if not src.startswith(('http://', 'https://')):
        raise ValueError("The image URL must be a valid HTTP/HTTPS URL.")
    response = requests.head(src)
    content_type = response.headers.get('content-type')
    if not content_type or 'image' not in content_type.lower():
        raise ValueError("The URL does not point to a valid image.")
    file_name = os.path.basename(src)
    try:
        response = requests.get(src)
        response.raise_for_status()
        os.makedirs('downloaded_images', exist_ok=True)
        file_path = os.path.join('downloaded_images', file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_name
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def baseline_downloadImage(imgTag, base_url='http://example.com'):
    soup = BeautifulSoup(imgTag, 'html.parser')
    img_url_tag = soup.find('img')['src']
    img_url = base_url + img_url_tag
    file_extension = img_url_tag.split('.')[-1]
    file_name = 'downloaded_' + img_url_tag.split('/')[-1] + '.' + file_extension
    response = requests.get(img_url)
    with open(file_name, 'wb') as file:
        file.write(response.content)
    return file_name

