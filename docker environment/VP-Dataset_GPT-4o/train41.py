import os
import sys
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

from bs4 import BeautifulSoup

def ground_truth_code_mirrorImages(url, dir):
    ab = anonBrowser()
    ab.anonymize()
    html = ab.open(url)
    soup = BeautifulSoup(html, 'html.parser')
    image_tags = soup.findAll('img')
    
    for image in image_tags:
        filename = image['src'].lstrip('http://')
        filename = os.path.join(dir, filename.replace('/', '_'))
        data = ab.open(image['src']).read()
        ab.back()
        save = open(filename, 'wb')
        save.write(data)
        save.close()

def persona_mirrorImages(url, dir):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.HTTPError, requests.ConnectionError) as e:
        print(f'Network error: {e}')
        return
    os.makedirs(dir, exist_ok=True)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        img_url = img.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            img_data = requests.get(img_url).content
        except (requests.HTTPError, requests.ConnectionError):
            print(f'Failed to download image: {img_url}')
            continue
        img_name = os.path.basename(img_url)
        img_path = os.path.join(dir, img_name)
        with open(img_path, 'wb') as img_file:
            img_file.write(img_data)
        print(f'Successfully saved {img_name}')


def template_mirrorImages(url, dir):
    import os
    import requests
    from urllib.parse import urljoin
    from bs4 import BeautifulSoup
    import shutil
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        for img in img_tags:
            img_url = urljoin(url, img.get('src'))
            try:
                img_response = requests.get(img_url, stream=True)
                img_response.raise_for_status()
                img_name = os.path.basename(img_url)
                img_path = os.path.join(dir, img_name)
                with open(img_path, 'wb') as f:
                    shutil.copyfileobj(img_response.raw, f)
            except requests.RequestException as e:
                print(f"Error downloading {img_url}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")

def question_refinement_mirrorImages(url, dir_path):
    import os
    import re
    import requests
    from urllib.parse import urlparse, urljoin
    from bs4 import BeautifulSoup
    from pathlib import Path
    from requests.exceptions import RequestException, MissingSchema, InvalidURL
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        response.raise_for_status()
        if 'text/html' not in response.headers.get('content-type', ''):
            raise ValueError('URL does not point to an HTML page.')
    except (RequestException, ValueError, MissingSchema, InvalidURL) as e:
        print(f"Error: Invalid or inaccessible URL - {str(e)}")
        return
    path = Path(dir_path).resolve()
    try:
        path.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print("Error: Permission denied for the specified directory.")
        return
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
    except RequestException as e:
        print(f"Error: Failed to retrieve web page contents - {str(e)}")
        return
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            img_response = requests.get(img_url, stream=True, timeout=10)
            img_response.raise_for_status()
        except (RequestException, MissingSchema, InvalidURL):
            print(f"Warning: Invalid or inaccessible image URL - {img_url}")
            continue
        if 'image' not in img_response.headers.get('content-type', ''):
            print(f"Warning: Non-image content at {img_url}")
            continue
        parsed_url = urlparse(img_url)
        image_name = os.path.basename(parsed_url.path)
        image_name = re.sub(r'[^a-zA-Z0-9._-]', '_', image_name)
        image_path = path / image_name
        try:
            with image_path.open('wb') as image_file:
                for chunk in img_response.iter_content(chunk_size=8192):
                    image_file.write(chunk)
            print(f"Saved image: {image_path}")
        except (IOError, PermissionError) as e:
            print(f"Error: Could not save the image - {str(e)}")

def alternative_approaches_mirrorImages(url, dir):
    import requests
    import os
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    os.makedirs(dir, exist_ok=True)
    for img_tag in img_tags:
        img_url = urljoin(url, img_tag.get('src'))
        try:
            img_data = requests.get(img_url, timeout=10)
            img_data.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching image {img_url}: {e}")
            continue
        file_name = os.path.join(dir, os.path.basename(img_url))
        try:
            with open(file_name, 'wb') as f:
                f.write(img_data.content)
                print(f"Saved {img_url} to {file_name}")
        except OSError as e:
            print(f"Error saving image {img_url}: {e}")

def context_manager_mirrorImages(url, dir):
    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    response = requests.get(url)
    if response.status_code != 200:
        return
    if not os.path.exists(dir):
        os.makedirs(dir)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join(dir, os.path.basename(img_url))
            with open(img_name, 'wb') as img_file:
                img_file.write(img_data)
        except Exception:
            continue

import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
def flipped_interaction_3_mirrorImages(url, dir):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to access {url}")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    if not os.path.exists(dir):
        os.makedirs(dir)
    for img in img_tags:
        img_url = img.attrs.get("src")
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        if not img_url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            continue
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.basename(urlparse(img_url).path)
            img_path = os.path.join(dir, img_name)
            base, ext = os.path.splitext(img_path)
            counter = 1
            while os.path.exists(img_path):
                img_path = f"{base}_{counter}{ext}"
                counter += 1
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)
            print(f"Image saved: {img_path}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

from bs4 import BeautifulSoup
import requests
import os
import urllib.parse
from urllib.parse import urljoin
def flipped_interaction_4_mirrorImages(url, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    image_types = ['.jpg', '.jpeg', '.png', '.gif']
    images = set()
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            if any(img_url.lower().endswith(ext) for ext in image_types):
                images.add(img_url)
    for img_url in images:
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.basename(urllib.parse.urlsplit(img_url).path)
            name, extension = os.path.splitext(img_name)
            i = 0
            new_img_name = img_name
            while os.path.exists(os.path.join(dir, new_img_name)):
                i += 1
                new_img_name = f"{name}_{i}{extension}"
            with open(os.path.join(dir, new_img_name), 'wb') as handler:
                handler.write(img_data)
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def flipped_interaction_5_mirrorImages(url, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            img_response = requests.get(img_url, stream=True)
            img_response.raise_for_status()
            img_name = os.path.basename(img_url)
            img_path = os.path.join(dir, img_name)
            index = 1
            base_name, extension = os.path.splitext(img_name)
            while os.path.exists(img_path):
                img_name = f"{base_name}_{index}{extension}"
                img_path = os.path.join(dir, img_name)
                index += 1
            with open(img_path, 'wb') as f:
                for chunk in img_response.iter_content(1024):
                    f.write(chunk)
        except requests.HTTPError as e:
            print(f"Failed to download {img_url}: {e}")

def iterative_prompting_3_mirror_images(url, directory):
    import requests
    from bs4 import BeautifulSoup
    import os
    from urllib.parse import urljoin, urlparse
    if not isinstance(url, str) or not urlparse(url).scheme:
        raise ValueError("Invalid URL provided")
    if not isinstance(directory, str) or not directory:
        raise ValueError("Invalid directory provided")
    directory = os.path.abspath(directory)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Failed to retrieve the page: {e}')
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f'Failed to create directory: {e}')
        return
    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue
        full_url = urljoin(url, img_url)
        try:
            img_response = requests.get(full_url, timeout=10)
            img_response.raise_for_status()
        except requests.RequestException as e:
            print(f'Failed to download image {full_url}: {e}')
            continue
        img_name = os.path.basename(urlparse(full_url).path)
        img_path = os.path.join(directory, img_name)
        try:
            with open(img_path, 'wb') as f:
                f.write(img_response.content)
        except OSError as e:
            print(f'Failed to save image {img_name}: {e}')
    print(f"Images have been saved in the directory: {directory}")

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
def iterative_prompting_4_mirror_images(url, dir_):
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        raise ValueError('Invalid URL provided')
    if not os.path.isdir(dir_):
        raise ValueError(f'Specified path is not a directory: {dir_}')
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Error fetching the URL: {e}')
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if not img_url:
            continue
        if not img_url.startswith(('http://', 'https://')):
            img_url = urljoin(url, img_url)
        try:
            img_response = requests.get(img_url)
            img_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Error fetching the image: {img_url}, error: {e}')
            continue
        img_name = os.path.basename(urlparse(img_url).path)
        if not img_name:
            print(f'Failed to determine image name for URL: {img_url}')
            continue
        img_path = os.path.join(dir_, img_name)
        try:
            with open(img_path, 'wb') as img_file:
                img_file.write(img_response.content)
        except IOError as e:
            print(f'Error saving the image {img_name} to {img_path}: {e}')

def iterative_prompting_5_mirror_images(url, directory):
    import os
    import re
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?))'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, url) is None:
        raise ValueError('Invalid URL format')
    if not isinstance(directory, str) or directory.strip() == '':
        raise ValueError('Directory name must be a non-empty string')
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            print(f"Failed to create directory: {e}")
            return
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"An error occurred while connecting to the URL: {e}")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    if not img_tags:
        print('No images found at the given URL.')
        return
    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        img_filename = os.path.basename(img_url)
        img_extension = os.path.splitext(img_filename)[1].lower()
        if img_extension not in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            print(f"Skipping {img_filename}: Unsupported file type {img_extension}")
            continue
        if not img_filename:
            continue
        try:
            img_response = requests.get(img_url, timeout=10)
            img_response.raise_for_status()
            with open(os.path.join(directory, img_filename), 'wb') as file:
                file.write(img_response.content)
            print(f"Downloaded {img_filename}")
        except requests.RequestException as e:
            print(f"An error occurred while downloading {img_filename}: {e}")
        except OSError as e:
            print(f"An error occurred while writing to file {img_filename}: {e}")

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def few_shots_prompting_mirrorImages(url, dir):
    os.makedirs(dir, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        img_url = img.get('src')
        img_url = urljoin(url, img_url)
        img_response = requests.get(img_url)
        img_response.raise_for_status()
        img_name = os.path.basename(img_url)
        img_path = os.path.join(dir, img_name)
        with open(img_path, 'wb') as img_file:
            img_file.write(img_response.content)

def cot_prompting_mirrorImages(url, dir):
    import os
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    if not os.path.exists(dir):
        os.makedirs(dir)
    for img in images:
        img_url = img.get('src')
        if not img_url.startswith(('http://', 'https://')):
            img_url = requests.compat.urljoin(url, img_url)
        img_name = os.path.basename(img_url)
        img_response = requests.get(img_url)
        img_path = os.path.join(dir, img_name)
        with open(img_path, 'wb') as f:
            f.write(img_response.content)

def fact_check_list_mirrorImages(url, dir):
    os.makedirs(dir, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve the page: {e}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        parsed_url = urlparse(img_url)
        if parsed_url.scheme not in ['http', 'https']:
            continue
        try:
            img_response = requests.get(img_url)
            img_response.raise_for_status()
            img_name = os.path.basename(parsed_url.path)
            if not img_name:
                continue
            img_path = os.path.join(dir, img_name)
            with open(img_path, 'wb') as img_file:
                img_file.write(img_response.content)
            print(f"Image saved: {img_path}")
        except requests.RequestException as e:
            print(f"Failed to download {img_url}: {e}")

def not_interactive_mix_mirrorImages(url, dir):
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    import os
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except OSError as e:
            raise Exception(f"Error: Creating directory {dir}: {e}")
    if not url.startswith(('http://', 'https://')):
        raise ValueError("Error: Invalid URL")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise Exception(f"Error: Request failed {e}")
    try:
        soup = BeautifulSoup(response.content, "html.parser")
        img_tags = soup.find_all('img')
        for img in img_tags:
            img_url = img.get('src')
            if not img_url:
                continue
            img_url = urljoin(url, img_url)
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                img_name = os.path.join(dir, os.path.basename(urljoin(url, img_url)))
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_response.content)
            except requests.RequestException as e:
                print(f"Error: Failed to download image {img_url}: {e}")
    except Exception as e:
        raise Exception(f"Error: Processing HTML content failed: {e}")

def interactive_mix_download_images_from_url(url, dir_path):
    import os
    import requests
    from bs4 import BeautifulSoup
    import re
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        downloaded_files = set()
        for img in images:
            img_url = img.get('src')
            if img_url:
                if not re.match(r'^https?:/{2}', img_url):
                    img_url = requests.compat.urljoin(url, img_url)
                if any(img_url.lower().endswith(ext) for ext in ['jpg', 'jpeg', 'png', 'gif']):
                    img_name = os.path.basename(img_url.split('?')[0])
                    original_img_name = img_name
                    counter = 1
                    while img_name in downloaded_files or os.path.exists(os.path.join(dir_path, img_name)):
                        name_part, ext_part = os.path.splitext(original_img_name)
                        img_name = f"{name_part}_{counter}{ext_part}"
                        counter += 1
                    img_response = requests.get(img_url, timeout=10)
                    img_response.raise_for_status()
                    with open(os.path.join(dir_path, img_name), 'wb') as img_file:
                        img_file.write(img_response.content)
                    downloaded_files.add(img_name)
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def baseline_mirrorImages(url, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for img in soup.find_all('img'):
        img_url = img.get('src')
        img_url = urljoin(url, img_url)
        img_name = os.path.basename(img_url)
        img_path = os.path.join(dir, img_name)
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as handler:
            handler.write(img_data)

