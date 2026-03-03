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

def persona__get_tweets(handle):
    import requests
    from bs4 import BeautifulSoup
    import random
    import string
    import json
    headers = {
        'User-Agent': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    session = requests.Session()
    url = 'https://mobile.twitter.com/' + handle
    response = session.get(url, headers=headers)
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    tweets = []
    for tweet_container in soup.find_all('div', class_='tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable original-tweet'):
        tweet_text = tweet_container.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
        geo_info = tweet_container.find('a', class_='Tweet-geo Tweet-geo-link u-hidden')
        geo = geo_info['title'] if geo_info else None
        tweets.append({'tweet': tweet_text, 'geo': geo})
    user_info_container = soup.find('div', class_='ProfileHeaderCard-name')
    name = user_info_container.text.strip() if user_info_container else 'Unknown'
    location_info_container = soup.find('div', class_='ProfileHeaderCard-location')
    location = location_info_container.find('a').text.strip() if location_info_container and location_info_container.find('a') else 'Unknown'
    return {'name': name, 'location': location, 'tweets': tweets}

def template__get_tweets(handle):
	try:
		from seleniumwire import webdriver
		from selenium.webdriver.chrome.options import Options
		from selenium.common.exceptions import NoSuchElementException, TimeoutException
		import json
		chrome_options = Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
		driver = webdriver.Chrome(options=chrome_options)
		driver.set_page_load_timeout(15)
		driver.get(f'http://twitter.com/{handle}')
		tweets = []
		for request in driver.requests:
			if request.response:
				if 'adaptive.json' in request.url:
					response_data = request.response.body
					data = json.loads(response_data)
					instruction = lambda x: {'tweet': x.get('full_text', ''), 'geo': x.get('user', {}).get('location', None)}
					tweets.extend(instruction(tweet) for tweet in data.get('globalObjects', {}).get('tweets', {}).values())
		driver.quit()
		return tweets
	except (NoSuchElementException, TimeoutException) as e:
		driver.quit()
		return []
	except Exception as ex:
		driver.quit()
		return []

def question_refinement__get_tweets(handle):
    from seleniumwire import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    import json
    import time
    options = Options()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    url = f'https://twitter.com/{handle}'
    driver.get(url)
    time.sleep(5)
    tweets = []
    try:
        tweet_elements = driver.find_elements(By.CSS_SELECTOR, 'article[data-testid="tweet"]')
        for tweet_element in tweet_elements:
            tweet = {}
            tweet['text'] = tweet_element.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]').text if tweet_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweetText"]').text else None
            author_info = tweet_element.find_element(By.CSS_SELECTOR, 'a[role="link"]').get_attribute('href')
            tweet['author'] = author_info.split('/')[-1] if author_info else None
            user_element = driver.find_element(By.XPATH, '//div[@data-testid=')
    except: raise
    
def alternative_approaches__get_tweets(handle):
    import requests
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count=100&tweet_mode=extended'.format(handle)
    headers = {'Authorization': 'Bearer YOUR_BEARER_TOKEN'}
    proxies = {'http': 'http://your_anonymous_proxy', 'https': 'http://your_anonymous_proxy'}
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()
        tweets = response.json()
    except requests.exceptions.HTTPError as errh:
        print(f'HTTP Error: {errh}')
        tweets = []
    except requests.exceptions.ConnectionError as errc:
        print(f'Error Connecting: {errc}')
        tweets = []
    except requests.exceptions.Timeout as errt:
        print(f'Timeout Error: {errt}')
        tweets = []
    except requests.exceptions.RequestException as err:
        print(f'Unknown Error: {err}')
        tweets = []
    formatted_tweets = [{'user': tweet['user']['name'], 'location': tweet['user']['location'], 'tweet': tweet['full_text'], 'geo': tweet['geo']} for tweet in tweets]
    return formatted_tweets

def context_manager__get_tweets(handle):
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    import json
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://twitter.com/' + handle)
    tweets = []
    elements = driver.find_elements_by_xpath('//article[@data-testid=')

def flipped_interaction_3__get_tweets(handle):
	import tweepy
	client = tweepy.Client(bearer_token='YOUR_BEARER_TOKEN')
	tweets = []
	paginator = tweepy.Paginator(client.get_users_tweets, id=client.get_user(username=handle).data.id, tweet_fields=['location'], expansions=['author_id'], max_results=100)
	for page in paginator.iter_pages(limit=3):
		if not page.data:
			break
		for tweet in page.data:
			user = page.includes['users'][0]
			tweets.append({'from_user': user.username, 'geo': tweet.geo, 'tweet': tweet.text})
	return tweets

def flipped_interaction_4__get_tweets(handle):
    api_key = os.getenv('TWITTER_API_KEY')
    api_secret_key = os.getenv('TWITTER_API_SECRET_KEY')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
    if not all([api_key, api_secret_key, access_token, access_token_secret, bearer_token]):
        logging.error("Twitter API credentials are not set.")
        raise ValueError("Twitter API credentials are not set.")
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key,
        consumer_secret=api_secret_key,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True
    )
    try:
        user_id = client.get_user(username=handle).data.id
    except tweepy.TweepyException as e:
        logging.error(f"Failed to get user ID for handle @{handle}: {e}")
        return []
    try:
        response = client.get_users_tweets(
            id=user_id,
            max_results=10,
            tweet_fields=["geo"]
        )
    except tweepy.TweepyException as e:
        logging.error(f"Failed to retrieve tweets for handle @{handle}: {e}")
        return []
    tweets = []
    for tweet in response.data:
        tweet_info = {
            "tweet": tweet.text,
            "geo": tweet.geo
        }
        tweets.append(tweet_info)
    logging.info(f"Successfully retrieved {len(tweets)} tweets for handle @{handle}")
    return tweets

def flipped_interaction_5__get_tweets(handle):
	import tweepy
	import time
	import json
	with open('credentials.json') as f:
		creds = json.load(f)
	auth = tweepy.OAuth1UserHandler(creds['API_KEY'], creds['API_SECRET_KEY'], creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])
	api = tweepy.API(auth, wait_on_rate_limit=True)
	try:
		tweets = api.user_timeline(screen_name=handle, count=10, tweet_mode='extended', include_rts=False)
		return [{'tweet': tweet.full_text, 'geo': tweet.geo} for tweet in tweets]
	except tweepy.TweepError as e:
		print(f'Error: {e.reason}')
		return []

def iterative_prompting_3__get_tweets(handle):
    if not isinstance(handle, str) or not handle:
        return []
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(30)
        driver.get(f'https://twitter.com/{handle}')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//article')))
        tweets = []
        articles = driver.find_elements(By.XPATH, '//article')
        for article in articles:
            try:
                geo_info = article.find_element(By.XPATH, './/span[@aria-label="   ,   "]').get_attribute('title')
            except Exception: geo_info = None
            try:
                tweet_text = article.find_element(By.XPATH, './/div[@data-testid="tweetText"]//span').text
            except Exception: tweet_text = ''
            tweets.append({'geo': geo_info, 'tweet': tweet_text})
    except Exception:
        tweets = []
    finally:
        if driver:
            driver.quit()
    return tweets


def iterative_prompting_4__get_tweets(handle):
    if not isinstance(handle, str) or not handle.strip():
        raise ValueError('Handle must be a non-empty string')
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.binary_location = '/path/to/chrome/binary'
        service = Service('/path/to/chromedriver')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(30)
        driver.get(f'https://twitter.com/{handle}')
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        tweets = []
        tweet_tags = soup.find_all(attrs={'data-testid': 'tweetText'})
        author_tags = soup.find_all(class_=re.compile('full-name'))
        geo_tags = soup.find_all(attrs={'aria-label': re.compile('Location')})
        author = author_tags[0].get_text().strip() if author_tags else None
        for tweet_tag, geo_tag in zip(tweet_tags, geo_tags):
            tweet = tweet_tag.get_text().strip() if tweet_tag else ''
            geo = geo_tag.get_text().strip() if geo_tag else None
            tweets.append({'tweet': tweet, 'geo': geo})
    except TimeoutException:
        tweets = []
        author = None
    except Exception as e:
        tweets = []
        author = None
    finally:
        try:
            driver.quit()
        except NameError:
            pass
    return author, tweets


def iterative_prompting_5__get_tweets(handle):
    if not isinstance(handle, str) or not handle.strip():
        raise ValueError('Handle must be a non-empty string.')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--remote-debugging-port=9222')
    try:
        driver = webdriver.Chrome(options=chrome_options)
        url = f'https://api.twitter.com/2/tweets/search/recent?query=from%3A{handle}'
        driver.get(url)
        tweets = []
        for request in driver.requests:
            if request.response:
                body = request.response.body.decode('utf-8', errors='replace')
                try:
                    data = json.loads(body)
                except json.JSONDecodeError:
                    continue
                for tweet in data.get('data', []):
                    tweet_text = tweet.get('text', '')
                    geo_data = tweet.get('geo', {})
                    geo_coordinates = geo_data.get('coordinates', {}).get('coordinates', None)
                    tweets.append({'tweet': tweet_text, 'geo': geo_coordinates})
        return tweets
    except Exception as e:
        raise RuntimeError(f'An error occurred while retrieving tweets: {str(e)}')
    finally:
        try:
            driver.quit()
        except NameError:
            pass

def few_shots_prompting__get_tweets(handle):
    pass
    """
    conn = pyppeteer.launch(headless=True)
    browser = await conn
    page = await browser.newPage()
    await page.goto(f'https://twitter.com/{handle}')
    tweets = await page.evaluate()
    await browser.close()
    return tweets
    """

def cot_prompting__get_tweets(handle):
	import snscrape.modules.twitter as sntwitter
	import requests
	from bs4 import BeautifulSoup
	tweets = []
	for tweet in sntwitter.TwitterSearchScraper(f'from:{handle}').get_items():
		if tweet.geo:
			locations = tweet.user.location
		else:
			locations = None
		tweets.append({
			'tweet': tweet.content,
			'fullname': tweet.user.displayname,
			'skypename': tweet.user.username,
			'city': locations,
			'country': locations,
			'geo': tweet.geo
		})
	return tweets

def fact_check_list__get_tweets(self, handle):
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    tweets = api.user_timeline(screen_name=handle, count=100, tweet_mode='extended')
    tweet_data = []
    for tweet in tweets:
        tweet_text = tweet.full_text
        geo_info = tweet.place.name if tweet.place else None
        tweet_data.append({'tweet': tweet_text, 'geo': geo_info})
    return tweet_data

def not_interactive_mix__get_tweets(handle):
    ab = anonBrowser()
    ab.anonymize()
    search_url = f"https://twitter.com/{urllib.parse.quote(handle)}"
    try:
        response = ab.open(search_url)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and len(script.string.strip()) > 0 and 'window.YTD.tweet.part0' in script.string:
                tweets_json_string = script.string.replace('window.YTD.tweet.part0 =', '').strip().rstrip(';')
                tweets_data = json.loads(tweets_json_string)
                tweets = [{'author': tweet['tweet']['core']['user_info']['screen_name'],'location': tweet['tweet']['legacy']['user_location'],'tweet': tweet['tweet']['legacy']['full_text']} for tweet in tweets_data.values()]
        sanitized_tweets = []
        for tweet in tweets:
            sanitized_tweet = {'author': re.sub(r'[^-]', '', tweet['author']),'location': re.sub(r'[^-]', '', tweet['location']),'tweet': re.sub(r'[^-]', '', tweet['tweet'])}
            sanitized_tweets.append(sanitized_tweet)
        return sanitized_tweets
    except:
        return []

def interactive_mix__get_tweets(handle):
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=handle, count=10, tweet_mode='extended', include_entities=True, include_rts=True)
    except tweepy.TweepError as e:
        return [str(e)]
    tweet_list = []
    for tweet in tweets:
        user_info = tweet.user.name
        geo_info = tweet.place.full_name if tweet.place else None
        tweet_content = tweet.full_text
        tweet_details = {
            'from_user': user_info,
            'geo': geo_info,
            'tweet': tweet_content
        }
        tweet_list.append(tweet_details)
    return tweet_list

def baseline__get_tweets(handle):
    import requests
    from bs4 import BeautifulSoup
    import re
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    url = f'http://twitter.com/{handle}'
    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    timeline = soup.select('')
    tweets = []
    for item in timeline[0].select('.tweet'):
        tweet_text = item.select('.tweet-text')[0].get_text()
        geo_span = item.find('span', {'class': re.compile('ProfileTweet-location')})
        geo = geo_span.text if geo_span else None
        tweets.append({'tweet': tweet_text, 'geo': geo})
    return tweets
