from urllib.parse import urljoin, urlparse, urlsplit
import urllib.request
from os.path import basename
import re
import os
import requests

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

def persona_downloadImage(imgTag):
    url_match = re.search(r'src=["\'](.*?)["\']', imgTag)
    if url_match:
        img_url = url_match.group(1)
        try:
            response = requests.get(img_url, stream=True, timeout=10)
            response.raise_for_status()
            extension = os.path.splitext(img_url)[1] if os.path.splitext(img_url)[1] else '.jpg'
            file_name = os.path.basename(urlsplit(img_url).path)
            with open(file_name, 'wb') as img_file:
                for chunk in response.iter_content(1024):
                    img_file.write(chunk)
            return file_name
        except requests.RequestException as e:
            raise Exception(f"Failed to download the image: {e}")
    else:
        raise ValueError("No valid image URL found in the img tag.")

def template_downloadImage(imgTag):
    try:
        soup = BeautifulSoup(imgTag, 'html.parser')
        img = soup.find('img')
        if not img or 'src' not in img.attrs:
            raise ValueError('No valid image URL found.')
        img_url = img['src']
        if not re.match(r'^https?:\/\/', img_url):
            raise ValueError('Invalid URL format.')
        response = requests.get(img_url, stream=True)
        response.raise_for_status()
        file_name = os.path.basename(img_url)
        with open(file_name, 'wb') as out_file:
            out_file.write(response.content)
        return file_name
    except Exception as e:
        raise RuntimeError(f"An error occurred while downloading the image: {str(e)}")

def question_refinement_download_image_from_tag(img_tag, base_url):
    try:
        match = re.search(r'<img\s+[^>]*src=["\"](.*?)["\"][^>]*>', img_tag)
        if not match:
            raise ValueError("No image URL found in the provided tag.")
        image_url = match.group(1)
        parsed_url = urlparse(image_url)
        if not parsed_url.netloc:
            image_url = urljoin(base_url, image_url)
        if parsed_url.scheme not in ("http", "https"):
            raise ValueError("Invalid URL scheme: only HTTP and HTTPS are allowed.")
        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status()
        filename = os.path.basename(parsed_url.path)
        filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)
        save_path = os.path.join(os.getcwd(), filename)
        with open(save_path, 'wb') as image_file:
            for chunk in response.iter_content(chunk_size=8192):
                image_file.write(chunk)
        return save_path
    except Exception as e:
        raise RuntimeError(f"An error occurred while downloading the image: {str(e)}")

def alternative_approaches_downloadImage(imgTag):
    try:
        from bs4 import BeautifulSoup
        import requests
        import logging
        logging.basicConfig(level=logging.INFO)
        soup = BeautifulSoup(imgTag, 'html.parser')
        img = soup.find('img')
        url = img['src'] if img and 'src' in img.attrs else None
        if not url:
            logging.error('No image src found in img tag')
            raise ValueError('No image src found')
        file_name = url.split('/')[-1]
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        logging.info(f'Image saved as {file_name}')
        return file_name
    except requests.RequestException as e:
        logging.error(f'Request failed: {str(e)}')
        return f'Error: {str(e)}'
    except Exception as e:
        logging.error(f'Unexpected error: {str(e)}')
        return f'Error: {str(e)}'

def context_manager_downloadImage(imgTag):
    import re
    import requests
    from urllib.parse import urlparse
    match = re.search(r'src\s*=\s*"([^"]+)"', imgTag)
    if not match:
        return None
    image_url = match.group(1)
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return None
    parsed_url = urlparse(image_url)
    file_name = parsed_url.path.split('/')[-1] or 'downloaded_image'
    try:
        with open(file_name, 'wb') as file:
            file.write(response.content)
    except IOError:
        return None
    return file_name

import requests
import os
from datetime import datetime
from urllib.parse import urlparse
def flipped_interaction_3_downloadImage(imgTag):
    url_start = imgTag.find('src="') + len('src="')
    url_end = imgTag.find('"', url_start)
    url = imgTag[url_start:url_end]
    try:
        response = requests.get(url)
        response.raise_for_status()
        parsed_url = urlparse(url)
        extension = os.path.splitext(parsed_url.path)[1]
        file_name = datetime.now().strftime('%Y%m%d%H%M%S') + extension
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return file_name
    except Exception as e:
        return None

import os
import requests
from urllib.parse import urlparse
def flipped_interaction_4_downloadImage(imgTag):
    start = imgTag.find('src=') + 5
    end = imgTag.find('"', start)
    img_url = imgTag[start:end]
    response = requests.get(img_url)
    if response.status_code == 200:
        parsed_url = urlparse(img_url)
        file_name = os.path.basename(parsed_url.path)
        with open(file_name, 'wb') as img_file:
            img_file.write(response.content)
        return file_name
    return None

from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urlparse
def flipped_interaction_5_downloadImage(imgTag):
    soup = BeautifulSoup(imgTag, 'html.parser')
    img = soup.find('img')
    if img and 'src' in img.attrs:
        img_url = img['src']
        parsed_url = urlparse(img_url)
        file_name = os.path.basename(parsed_url.path)
        try:
            response = requests.get(img_url, timeout=10)
            response.raise_for_status()
            with open(file_name, 'wb') as f:
                f.write(response.content)
            return file_name
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while downloading the image: {e}")
            return None
    else:
        print("Invalid <img> tag or missing 'src' attribute.")
        return None

def iterative_prompting_3_download_image(img_tag):
    import re
    import requests
    from urllib.parse import urlparse
    from requests.exceptions import RequestException
    import os
    if not isinstance(img_tag, str):
        raise TypeError("Input must be a string representing an HTML img tag")
    url_match = re.search(r'src\s*=\s*"(.*?)"', img_tag)
    if not url_match:
        raise ValueError("No valid 'src' attribute found in the img tag")
    img_url = url_match.group(1)
    if not urlparse(img_url).scheme:
        raise ValueError("Malformed URL, must be absolute with scheme (http or https)")
    try:
        response = requests.get(img_url, timeout=10)
        response.raise_for_status()
    except RequestException as e:
        raise ConnectionError(f"Failed to download image from the provided URL: {e}")
    parsed_url = urlparse(img_url)
    file_name = parsed_url.path.split('/')[-1] or 'downloaded_image'
    safe_file_name = os.path.basename(file_name)
    try:
        with open(safe_file_name, 'wb') as file:
            file.write(response.content)
    except IOError as e:
        raise IOError(f"Failed to write the image to a file: {e}")
    return safe_file_name

def iterative_prompting_4_download_image(img_tag):
    import re
    import requests
    from urllib.parse import urlparse
    from requests.exceptions import RequestException
    import os
    if not isinstance(img_tag, str):
        raise TypeError('The img_tag must be a string.')
    img_url_match = re.search(r'src=["\']?([^"\'>]+)', img_tag)
    if not img_url_match:
        raise ValueError('No valid image URL found in the provided img tag.')
    img_url = img_url_match.group(1)
    parsed_url = urlparse(img_url)
    if parsed_url.scheme not in ('http', 'https'):
        raise ValueError('Unsupported URL scheme. Only http and https are allowed.')
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(img_url, headers=headers, timeout=10)
        response.raise_for_status()
    except RequestException as e:
        raise Exception(f'Failed to download image due to network issue: {e}')
    image_name = os.path.basename(parsed_url.path)
    if not image_name:
        raise ValueError('Invalid image name extracted from URL.')
    try:
        with open(image_name, 'wb') as file:
            file.write(response.content)
    except IOError as e:
        raise Exception(f'Failed to save the image to file: {e}')
    return image_name

def iterative_prompting_5_download_image(img_tag):
    from urllib.parse import urlparse
    if not isinstance(img_tag, str):
        raise TypeError('img_tag must be a string')
    match = re.search(r'<img [^>]*src="(https?://[^"]+)"', img_tag)
    if not match:
        raise ValueError('Invalid <img> tag or no valid src attribute found')
    img_url = match.group(1)
    try:
        response = requests.get(img_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise Exception(f'Failed to download image: {e}')
    parsed_url = urlparse(img_url)
    file_name = os.path.basename(parsed_url.path)
    if not file_name:
        raise ValueError('Failed to extract file name from URL')
    file_name = os.path.normpath(file_name)
    try:
        with open(file_name, 'wb') as file:
            file.write(response.content)
    except IOError as e:
        raise Exception(f'Failed to write image to file: {e}')
    return file_name

def few_shots_prompting_downloadImage(imgTag):
    import re
    import requests
    from urllib.parse import urlparse
    match = re.search(r'src=["\']?([^"\'>]+)', imgTag)
    if not match:
        raise ValueError('No image URL found in the img tag.')
    image_url = match.group(1)
    response = requests.get(image_url)
    response.raise_for_status()
    parsed_url = urlparse(image_url)
    file_name = os.path.basename(parsed_url.path)
    with open(file_name, 'wb') as file:
        file.write(response.content)
    return file_name

def cot_prompting_downloadImage(imgTag):
    from bs4 import BeautifulSoup
    import requests
    import os
    soup = BeautifulSoup(imgTag, 'html.parser')
    img = soup.find('img')
    if not img or not img.has_attr('src'):
        raise ValueError('No valid <img> tag or src attribute found.')
    img_url = img['src']
    response = requests.get(img_url)
    if response.status_code != 200:
        raise Exception('Failed to download the image.')
    filename = os.path.basename(img_url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename

def fact_check_list_downloadImage(imgTag):
    import requests
    from bs4 import BeautifulSoup
    import os
    soup = BeautifulSoup(imgTag, 'html.parser')
    img_element = soup.find('img')
    if not img_element or not img_element.get('src'):
        raise ValueError("Invalid <img> tag or missing 'src' attribute")
    img_url = img_element['src']
    if not img_url.startswith(('http://', 'https://')):
        raise ValueError("Image URL must be absolute")
    try:
        response = requests.get(img_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to download image: {e}")
    img_name = os.path.basename(img_url)
    if not img_name:
        raise ValueError("Could not determine file name from URL")
    with open(img_name, 'wb') as file:
        file.write(response.content)
    return img_name

def not_interactive_mix_downloadImage(imgTag):
    import re
    import requests
    from urllib.parse import urljoin
    from bs4 import BeautifulSoup
    if not isinstance(imgTag, str) or '<img ' not in imgTag:
        raise ValueError('Invalid image tag provided.')
    try:
        soup = BeautifulSoup(imgTag, 'html.parser')
        img = soup.find('img')
        if not img or not img.has_attr('src'):
            raise ValueError('No valid src attribute found in the image tag.')
        img_url = img['src']
        if not re.match(r'^https?:\/\/', img_url):
            img_url = urljoin('http://example.com', img_url)
        if not img_url.startswith(('http://', 'https://')):
            raise ValueError('The extracted URL is not a valid HTTP URL.')
        response = requests.get(img_url, stream=True)
        response.raise_for_status()
        file_name = re.sub(r'[\/*?"<>|]', '_', img_url.split('/')[-1])
        with open(file_name, 'wb') as img_file:
            for chunk in response.iter_content(chunk_size=8192):
                img_file.write(chunk)
        return file_name
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f'Problem fetching the image: {e}')
    except Exception as e:
        raise RuntimeError(f'An error occurred: {e}')

def interactive_mix_download_image_from_tag(img_tag, directory='.'):
    try:
        if not img_tag or not isinstance(img_tag, dict) or 'src' not in img_tag:
            raise ValueError('Invalid img tag or no src attribute found in the provided img tag.')
        url = img_tag['src']
        response = requests.get(url, allow_redirects=True, timeout=10)
        response.raise_for_status()
        image_name = os.path.basename(url)
        file_path = os.path.join(directory, image_name)
        if not os.path.abspath(file_path).startswith(os.path.abspath(directory)):
            raise ValueError('Invalid file path.')
        with open(file_path, 'wb') as image_file:
            image_file.write(response.content)
        return file_path
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"An error occurred while downloading the image: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while downloading the image: {str(e)}")

def baseline_downloadImage(imgTag):
    import requests
    from bs4 import BeautifulSoup
    import os
    soup = BeautifulSoup(imgTag, 'html.parser')
    img = soup.find('img')
    img_url = img['src'] if img else None
    if not img_url:
        return None
    response = requests.get(img_url)
    if response.status_code == 200:
        filename = os.path.basename(img_url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename
    else:
        return None

