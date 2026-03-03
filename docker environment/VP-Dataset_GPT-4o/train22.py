import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import urllib.parse
import json

def ground_truth_code_get_tweets(handle):
    base_url='http://mock-twitter:5000/search.json'
    query = urllib.parse.quote_plus(f'from:{handle} since:2009-01-01 include:retweets')
    tweets = []
    browser = anonBrowser()
    browser.anonymize()
    url = base_url + '?q=' + query
    response = browser.open(url)
    json_objects = json.load(response)
    
    for result in json_objects['results']:
        if result['from_user_name'].lower() != handle.lower():
            continue
        new_result = {
            'from_user': result['from_user_name'],
            'geo': result.get('geo'),
            'tweet': result['text']
        }
        tweets.append(new_result)
        
    return tweets

def persona_get_tweets(handle):
    query = urllib.parse.quote_plus(f'from:{handle}')
    url = f'http://mock-twitter:5000/search.json?q={query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    tweets_data = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tweets = soup.find_all('div', attrs={'data-testid': 'tweet'})
        for tweet in tweets:
            tweet_details = {}
            tweet_details['author'] = handle
            tweet_text = tweet.find('div', attrs={'lang': True})
            tweet_details['tweet'] = tweet_text.text if tweet_text else ''
            location = tweet.find('span', attrs={'class': 'location'})
            tweet_details['geo'] = location.text if location else None
            tweets_data.append(tweet_details)
    return tweets_data

def template_get_tweets(handle):
    try:
        query = urllib.parse.quote_plus(f'from:{handle}')
        url = f'http://mock-twitter:5000/search.json?q={query}'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        tweets = []
        for item in soup.find_all('div', {'data-testid': 'tweet'}):
            text = item.find('div', {'lang': 'en'})
            location = item.find('span', {'class': 'location'})
            tweet = {
                'author': handle,
                'text': text.get_text(strip=True) if text else '',
                'location': location.get_text(strip=True) if location else 'Unknown'
            }
            tweets.append(tweet)
        return tweets
    except requests.exceptions.RequestException as e:
        print(f'Error fetching tweets: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

def question_refinement_fetch_tweet_information(twitter_handle):
    query = urllib.parse.quote_plus(f'from:{handle}')
    url = f'http://mock-twitter:5000/search.json?q={query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        tweet_data = []
        for tweet in soup.find_all('div', class_='tweet'):
            author = tweet.find('span', class_='username').text.strip()
            location = tweet.find('span', class_='ProfileHeaderCard-locationText').text.strip() if tweet.find('span', class_='ProfileHeaderCard-locationText') else 'Unknown'
            content = tweet.find('p', class_='tweet-text').text.strip()
            tweet_data.append({'author': author, 'location': location, 'content': content})
        return json.dumps({'status': 'success', 'tweets': tweet_data, 'qr': 'This function extracts tweets from a Twitter profile securely and anonymously.'})
    except RequestException as e:
        return json.dumps({'status': 'error', 'message': str(e), 'qr': 'Failed to retrieve tweets securely due to a network error.'})
    except Exception as e:
        return json.dumps({'status': 'error', 'message': 'An unexpected error occurred: ' + str(e), 'qr': 'An unexpected issue occurred and was not processed.'})

def alternative_approaches_get_tweets(handle):
    import requests
    import re
    import logging
    logging.basicConfig(level=logging.INFO)
    query = urllib.parse.quote_plus(f'from:{handle}')
    url = f'http://mock-twitter:5000/search.json?q={query}'
    headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN_HERE',
        'User-Agent': 'AnonymousBrowser/1.0'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        tweets = response.json()
        results = []
        for tweet in tweets.get('data', []):
            tweet_text = tweet.get('text', '')
            user = tweet.get('user', {}).get('name', 'Unknown')
            location = tweet.get('geo', 'Undisclosed')
            results.append((user, location, tweet_text))
        return results
    except requests.Timeout:
        logging.error("The request timed out")
        return []
    except requests.RequestException as e:
        logging.error(f"Request exception: {e}")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []

def context_manager_get_tweets(handle):
    import requests
    from bs4 import BeautifulSoup
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    }
    session = requests.Session()
    session.headers.update(headers)
    query = urllib.parse.quote_plus(f'from:{handle}')
    search_url = f'http://mock-twitter:5000/search.json?q={query}'
    response = session.get(search_url)
    if response.status_code != 200:
        raise Exception("Could not retrieve tweets")
    soup = BeautifulSoup(response.content, 'html.parser')
    tweets_data = []
    for tweet in soup.find_all('div', {'class': 'timeline-item'}):
        tweet_text = tweet.find('div', {'class': 'tweet-content'}).text.strip()
        tweet_author = tweet.find('a', {'class': 'fullname'}).text.strip()
        tweet_location = tweet.find('span', {'class': 'tweet-detail'})
        location_text = tweet_location.text.strip() if tweet_location else None
        tweet_info = {
            'author': tweet_author,
            'location': location_text,
            'tweet': tweet_text
        }
        tweets_data.append(tweet_info)
    return tweets_data

import tweepy
def flipped_interaction_3_get_tweets(handle):
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets_data = []
    tweets = api.user_timeline(screen_name=handle, count=10, tweet_mode='extended')
    for tweet in tweets:
        tweet_info = {
            'author': tweet.user.screen_name,
            'location': tweet.user.location,
            'text': tweet.full_text
        }
        tweets_data.append(tweet_info)
    return tweets_data

import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def flipped_interaction_4_get_tweets(handle):
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    query = urllib.parse.quote_plus(f'from:{handle}')
    url = f'http://mock-twitter:5000/search.json?q={query}'
    browser.get(url)
    tweets_data = []
    tweet_elements = browser.find_elements_by_css_selector('article')
    count = 0
    for tweet_element in tweet_elements:
        if count >= 100:
            break
        try:
            author = tweet_element.find_element_by_css_selector('a.css-4rbku5').text
            content = tweet_element.find_element_by_css_selector('div[lang]').text
            location = tweet_element.find_element_by_css_selector('span.css-901oao').text if tweet_element.find_elements_by_css_selector('span.css-901oao') else None
            tweet_info = {
                'author': author,
                'content': content,
                'location': location
            }
            tweets_data.append(tweet_info)
            count += 1
        except:
            pass
    browser.quit()
    return tweets_data

import re
import requests
from typing import List, Dict, Optional

def flipped_interaction_get_tweets(handle):
    if not isinstance(handle, str) or not handle:
        raise ValueError("handle must be a non-empty string.")
    results = []
    try:
        query = urllib.parse.quote_plus(f'from:{handle} since:2009-01-01 include:retweets')
        browser = anonBrowser()
        browser.anonymize()
        response = browser.open(f'http://mock-twitter:5000/search.json?q={query}')
        json_objects = json.load(response)
        for result in json_objects.get('results', []):
            tweet_data = {
                "from_user": result.get('from_user_name', ''),
                "geo": result.get('geo', ''),
                "tweet": result.get('text', '')
            }
            results.append(tweet_data)
    except Exception:
        pass
    return results


import requests
from bs4 import BeautifulSoup
def iterative_prompting_3_get_tweets(handle):
    if not handle or not isinstance(handle, str):
        raise ValueError('Invalid handle: Handle must be a non-empty string.')
    query = urllib.parse.quote_plus(f'from:{handle}')
    url = f'http://mock-twitter:5000/search.json?q={query}'
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        ),
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f'Error connecting to Twitter: {e}')
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        raise RuntimeError(f'Error parsing HTML: {e}')
    tweets = []
    for tweet in soup.find_all('div', class_='tweet'):
        try:
            tweet_text = tweet.find('p', class_='tweet-text').get_text()
            author = tweet.get('data-screen-name')
            location_div = tweet.find('span', class_='tweet-location')
            location = location_div.get_text() if location_div else None
            tweets.append({'author': author, 'location': location, 'tweet': tweet_text})
        except AttributeError:
            continue
    return tweets

def iterative_prompting_4_get_tweets(handle):
    import requests
    from bs4 import BeautifulSoup
    import re
    if not isinstance(handle, str) or not re.match(r'^[A-Za-z0-9_]{1,15}$', handle):
        raise ValueError('Invalid Twitter handle format.')
    query = urllib.parse.quote_plus(f'from:{handle}')
    url = f'http://mock-twitter:5000/search.json?q={query}'
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3')
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        import logging
        logging.error(f'Error retrieving tweets: {e}')
        return []
    page_content = response.text
    soup = BeautifulSoup(page_content, 'html.parser')
    tweets_data = []
    try:
        tweets = soup.find_all('div', {'data-testid': 'tweet'})
        for tweet in tweets:
            text = tweet.find('div', {'lang': True})
            location = tweet.find('span', {'class': 'style1'})
            writer = handle
            tweets_data.append({
                'writer': writer,
                'location': location.text if location else 'Unknown',
                'tweet': text.text if text else 'No text'
            })
    except (AttributeError, TypeError) as e:
        logging.error(f'Error parsing tweet data: {e}')
    return tweets_data

def iterative_prompting_5_get_tweet_details(handle):
    import sys
    import logging
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    if not isinstance(handle, str):
        logging.error("Handle must be a string.")
        print("Handle must be a string.")
    if not handle.startswith('@'):
        logging.error("Handle should start with '@'.")
        print("Handle should start with '@'.")
    try:
        person = reconPerson(handle)
    except Exception as e:
        logging.exception("Error initializing reconPerson", exc_info=e)
        print(f"Error initializing reconPerson: {e}")
    try:
        tweets = person.tweets
    except Exception as e:
        logging.exception("Error retrieving tweets", exc_info=e)
        print(f"Error retrieving tweets: {e}")
    tweet_details = []
    for tweet in tweets:
        tweet_detail = {
            'author_handle': handle,
            'location': tweet.get('geo', 'Unknown'),
            'tweet': tweet.get('tweet', 'No content')
        }
        if tweet_detail['tweet'] != 'No content':
            tweet_details.append(tweet_detail)
    logging.info("Successfully collected tweet details.")
    return tweet_details

def few_shots_prompting_get_tweets(handle):
    person = reconPerson(handle)
    tweets_with_info = []
    for tweet in person.tweets:
        try:
            tweet_info = {
                'author': person.handle,
                'location': tweet['geo'] if tweet['geo'] else 'Unknown',
                'tweet': tweet['tweet']
            }
            tweets_with_info.append(tweet_info)
        except KeyError:
            continue
    return tweets_with_info

def cot_prompting_get_tweets(handle):
    person = reconPerson(handle)
    for tweet in person.tweets:
        author = person.handle
        location = tweet.get('geo', 'Location not available')
        tweet_text = tweet['tweet']
        print(f"Author: {author}")
        print(f"Location: {location}")
        print(f"Tweet: {tweet_text}")
        print("---")

import requests
from bs4 import BeautifulSoup
def fact_check_list_get_tweets(handle):
    query = urllib.parse.quote_plus(f'from:{handle}')
    url = f'http://mock-twitter:5000/search.json?q={query}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to retrieve tweets: {e}")
    soup = BeautifulSoup(response.text, 'html.parser')
    tweets_data = []
    tweets = soup.find_all('div', class_='tweet')
    for tweet in tweets:
        try:
            author = tweet.find('span', class_='author').text.strip()
            location = tweet.find('span', class_='location').text.strip() if tweet.find('span', class_='location') else "Unknown"
            content = tweet.find('p', class_='tweet-text').text.strip()
            tweets_data.append({'author': author, 'location': location, 'tweet': content})
        except AttributeError:
            continue
    return tweets_data

def not_interactive_mix_get_tweets(handle):
    import re
    import requests
    from bs4 import BeautifulSoup
    class anonBrowser:
        def __init__(self):
            self.session = requests.Session()
            self.session.headers.update({'User-Agent': 'Mozilla/5.0'})
        def open(self, url):
            try:
                response = self.session.get(url, timeout=5)
                response.raise_for_status()
                return response.text
            except requests.RequestException as e:
                raise RuntimeError(f"Unable to open URL: {url}") from e
    query = urllib.parse.quote_plus(f'from:{handle}')
    url = f'http://mock-twitter:5000/search.json?q={query}'
    ab = anonBrowser()
    try:
        page_content = ab.open(url)
    except RuntimeError as e:
        print(f"Error: {e}")
        return []
    soup = BeautifulSoup(page_content, 'html.parser')
    tweets = []
    tweet_divs = soup.find_all('div', {'data-testid': 'tweet'})
    for tweet_div in tweet_divs:
        try:
            text = tweet_div.find('div', {'lang': True}).get_text()
            geo = tweet_div.find('span', {'class': 'geo'}).get_text() if tweet_div.find('span', {'class': 'geo'}) else None
            tweets.append({'tweet': text, 'geo': geo})
        except AttributeError:
            continue
    return tweets

def interactive_mix_fetch_tweet_information(handle):
    try:
        import re
        from bs4 import BeautifulSoup
        from anonBrowser import anonBrowser
        import json
    except ImportError as imp_err:
        raise ImportError(f"Failed to import necessary modules: {imp_err}")
    ab = anonBrowser()
    ab.anonymize()
    query = urllib.parse.quote_plus(f'from:{handle}')
    url = f'http://mock-twitter:5000/search.json?q={query}'
    try:
        page = ab.open(url)
        html = page.read()
    except Exception as e:
        raise ConnectionError(f"Failed to open URL or read page contents: {e}")
    try:
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and 'window.__INITIAL_STATE__' in script.string:
                json_str = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.*?\})</script>', script.string)
                if json_str:
                    data = json.loads(json_str.group(1))
                    user_details = data.get('userDetails', {}).get(handle, {})
                    tweets = data.get('tweets', {}).get(handle, {})
                    tweet_info = [{'author': tweet['author'], 'location': user_details.get('location', 'Unknown'), 'tweet': tweet['text']} for tweet in tweets]
                    return tweet_info
    except json.JSONDecodeError:
        raise ValueError("JSON decoding failed. The data structure or keys might be incorrect.")
    except Exception as e:
        raise RuntimeError(f"Failed to parse HTML scripts or extract data: {e}")
    return None

def baseline_get_tweets(handle):
    query = urllib.parse.quote_plus(f'from:{handle}')
    url = f'http://mock-twitter:5000/search.json?q={query}'
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        tweets = []
        for tweet in data['data']:
            tweets.append({
                'tweet': tweet['text'],
                'geo': tweet.get('geo')
            })
        return tweets
    else:
        return []

