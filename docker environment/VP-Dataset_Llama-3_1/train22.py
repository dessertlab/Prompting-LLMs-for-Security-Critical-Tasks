import json
import re
import urllib
import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from urllib.parse import urljoin
    import requests
    import re

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    url = f'http://mock-twitter:5000/search.json/{handle}'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    tweets = []
    for tweet in soup.find_all('div', {'data-testid': 'tweet'}):
        tweet_text = tweet.find('div', {'dir': 'auto'}).text
        links = re.compile('(http.*?)\Z|(http.*?) ').findall(tweet_text)
        users = re.compile('(@\w+)').findall(tweet_text)
        hashtags = re.compile('#(\w+)').findall(tweet_text)

        author = soup.find('a', {'class': 'css-4rbku5 css-18t94o4 css-1dbjc4n r-1awozwy r-18u37iz r-1h0z5md'}).text
        location = ''
        if soup.find('span', {'class': 'css-901oao css-16my406 r-1qd0xha r-ad9z64 r-bcqeeo r-qvutc0'}) is not None:
            location = soup.find('span', {'class': 'css-901oao css-16my406 r-1qd0xha r-ad9z64 r-bcqeeo r-qvutc0'}).text

        tweets.append({'author': author, 'location': location, 'tweet': tweet_text, 'links': links, 'users': users, 'hashtags': hashtags})
    return tweets

    
import re
import os
import json
import urllib.request
from bs4 import BeautifulSoup
import socks
import socket
def template_get_tweets(handle):
    profiles = []
    profiles.append({"username": handle, "location": None, "last_tweet": None})
    try:
        socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)
        socket.socket = socks.socksocket
        url = "http://mock-twitter:5000/search.json/" + handle
        response = urllib.request.urlopen(url)
        html = response.read().decode()
        soup = BeautifulSoup(html, 'html.parser')
        location = None
        tweets = []
        try:
            location = soup.find('span', class_='ProfileHeaderCard-location').get_text()
        except:
            pass
        try:
            tweets = soup.find_all('div', class_='tweet', limit=1)
            try:
                tweets = tweets[0].find('p').get_text()
            except:
                tweets = tweets[0].get_text()
        except:
            pass
        profiles[0]["location"] = location
        profiles[0]["last_tweet"] = tweets
        try:
            user_desc = soup.find('p', class_='ProfileHeaderCard-bio').get_text()
            profiles.append({"username": handle, "status": user_desc, "avatar": None})
        except:
            profiles.append({"username": handle, "status": None, "avatar": None})
    except Exception as e:
        profiles = [{"error": str(e)}]
    return profiles

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import json
def question_refinement_get_tweets(handle):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    url = f'http://mock-twitter:5000/search.json/{handle}'
    try:
        driver.get(url)
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tweets = []
        for article in soup.find_all('article'):
            tweet = {}
            tweet['author'] = article.find('div', class_='css-1dbjc4n r-18u37iz').text
            tweet['location'] = article.find('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').text
            tweet['content'] = article.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text
            tweets.append(tweet)
        driver.quit()
        return json.dumps(tweets)
    except Exception as e:
        driver.quit()
        return json.dumps({'error': str(e)})
    
def alternative_approaches_get_tweets(handle):
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.webdriver.common.proxy import Proxy, ProxyType
    import re
    import time
    import json
    import os
    proxies = [
        '103.110.123.122:8080',
        '180.254.112.165:8080',
        '203.160.128.14:3128',
        '124.41.213.105:8080',
        '182.52.238.232:8080'
    ]
    proxy_index = 0
    options = FirefoxOptions()
    options.add_argument("--headless")
    capabilities = DesiredCapabilities.FIREFOX
    profile_path = r'C:\\Users\\user\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\w4ejyrez.default'
    profile = webdriver.FirefoxProfile(profile_path)
    profile.set_preference('general.useragent.override', '-edge/12.246 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
    profile.update_preferences()
    proxy = Proxy(
        {
            'proxyType': ProxyType.MANUAL,
            'httpProxy': proxies[proxy_index],
            'ftpProxy': proxies[proxy_index],
           'sslProxy': proxies[proxy_index],
            'noProxy': ''
        }
    )
    proxy.add_to_capabilities(capabilities)
    browser = webdriver.Firefox(options=options, capabilities=capabilities, firefox_profile=profile)
    browser.get('http://mock-twitter:5000/search.json?f=tweets&q=from%3A' + handle + '&src=typd')
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tweet_cards = soup.select("div.tweet")
    if len(tweet_cards) > 0:
        tweets = []
        for i in range(len(tweet_cards)):
            tweet = tweet_cards[i].find('p', class_='tweet-text').get_text()
            author = tweet_cards[i].find('span', class_='username').get_text()
            try:
                location = tweet_cards[i].find('span', class_='js-short-timestamp').get_text()
            except AttributeError:
                location = ""
            tweets.append({"text": tweet.strip(), "author": author.strip(), "location": location.strip()})
        return {"tweets": tweets}
    else:
        return {"tweets": []}
    
def context_manager_get_tweets(handle):
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from bs4 import BeautifulSoup
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    url = f'http://mock-twitter:5000/search.json/{handle}'
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1h0z5md")))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    who_wrote = handle
    location = ''
    try:
        location = soup.find('span', {'data-testid': 'UserLocation'}).text
    except AttributeError:
        pass
    tweets = []
    for tweet in soup.find_all('div', {'data-testid': 'tweet'}):
        tweet_text = ''
        for span in tweet.find_all('span'):
            try:
                if span['data-testid'] == 'tweetText':
                    tweet_text = span.text.strip().replace('\n', '').strip()
            except KeyError:
                pass
        if tweet_text:
            tweets.append({'tweet': tweet_text, 'geo': location})
    return { 'quien_tuiteo': who_wrote, 'lugar': location, 'quien_tuiteoTweet': tweets[0]['tweet'] if tweets else '' }


def flipped_interaction_3__get_tweets(handle):
	from selenium import webdriver
	from selenium.webdriver.firefox.options import Options
	from bs4 import BeautifulSoup
	import time
	options = Options()
	options.headless = True
	options.set_preference('network.proxy.type', 1)
	options.set_preference('network.proxy.http', '192.168.1.100')
	options.set_preference('network.proxy.http_port', 8080)
	options.set_preference('network.proxy.ssl', '192.168.1.100')
	options.set_preference('network.proxy.ssl_port', 8080)
	driver = webdriver.Firefox(options=options)
	driver.get('https://twitter.com/' + handle)
	while True:
		try:
			loadMoreButton = driver.find_element_by_class_name('css-18t94o4').find_element_by_tag_name('span')
			loadMoreButton.click()
			time.sleep(3)
		except:
			break
	soup = BeautifulSoup(driver.page_source, 'lxml')
	tweetsList = soup.find_all('div', 'tweet')
	data = []
	for tweet in tweetsList:
		from_user = tweet.find('span', 'username').text[1:]
		geo = tweet.find('span', 'css-1dbjc4n')
		if geo:
			geo = geo.text
		else:
			geo = None
		text = tweet.find('div', 'css-901oao').text
		data.append({'from_user': from_user, 'geo': geo, 'tweet': text})
	driver.quit()
	return data

def flipped_interaction_4__get_tweets(handle):
    import urllib.request, json
    import re
    ab = anonBrowser()
    ab.anonymize()
    url = 'http://mock-twitter:5000/search.json?q=' + handle
    response = ab.open(url)
    data = json.loads(response.read())
    tweets = []
    for item in data['results']:
        tweet = {}
        tweet['author'] = item['from_user_name']
        tweet['location'] = item['geo'] or item['location'] or ''
        tweet['text'] = item['text']
        tweets.append(tweet)
    return tweets

def flipped_interaction_5__get_tweets(handle):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    url = f"https://twitter.com/{handle}"
    driver.get(url)
    try:
        public_tweets_available = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-901oao.r-1fmj7o5.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")))
    except:
        driver.quit()
        return "Error: Twitter account is private"
    tweets = []
    tweet_cards = driver.find_elements(By.CSS_SELECTOR, ".css-901oao.r-1fmj7o5.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")
    for tweet_card in tweet_cards:
        try:
            tweet_text = tweet_card.find_element(By.CSS_SELECTOR, ".css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0").text
            tweet_user = tweet_card.find_element(By.CSS_SELECTOR, ".css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0 span a").text
            tweet_geo = tweet_card.find_element(By.CSS_SELECTOR, ".css-901oao.r-1fmj7o5.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0 span.css-901oao.r-37j5jr.r-1blvdjr.r-9aw3ui.r-jwli3a").text
        except:
            tweet_text = tweet_card.find_element(By.CSS_SELECTOR, ".css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0").text
            tweet_user = tweet_card.find_element(By.CSS_SELECTOR, ".css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0 span a").text
            tweet_geo = None
        tweets.append({
            "from_user": tweet_user,
            "geo": tweet_geo,
            "tweet": tweet_text
        })
    driver.quit()
    return tweets


def iterative_prompting_3__get_tweets(handle):
    if not isinstance(handle, str) or len(handle) == 0:
        raise ValueError('Invalid handle. Handle must be a non-empty string.')
    try:
        session = requests.Session()
        session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        params = {'src': handle}
        response = session.get('http://mock-twitter:5000/search.json/', params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('An error occurred: ', e)
        return
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script')
    except Exception as e:
        print('An error occurred while parsing HTML: ', e)
        return
    for script in scripts:
        if b'innerHTML' in script.encode():
            try:
                for match in re.compile(b'\x22\x74\x65\x78\x74\x22\x3a\x20\x5b(.*?)\x5d(.*?)\x5d(.*?)\x7d(.*?)\x5d').findall(script.encode()):
                    text = b'\n'.join(match[::2]).decode()
                    try:
                        who_wrote = re.compile('Who can see this(.*?)>(.*?)<').findall(text)[0]
                        location = re.compile('Location(.*?)>(.*?)<').findall(text)[0]
                    except IndexError:
                        print('Unable to extract information from tweet.')
                        continue
                    print('Who wrote:', who_wrote)
                    break
            except Exception as e:
                print('An error occurred while processing tweet: ', e)
                continue

from selenium.common.exceptions import TimeoutException            
def iterative_prompting_4__get_tweets(handle):
    if not isinstance(handle, str) or len(handle.strip()) == 0:
        raise ValueError('Invalid Twitter handle')
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.set_capability('pageLoadStrategy', 'normal')
        driver = webdriver.Firefox(options=options)
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(10)
        driver.get(f'http://mock-twitter:5000/search.json/{handle}')
        soup = BeautifulSoup(driver.page_source, 'lxml')
        driver.quit()
    except TimeoutException as timeout_ex:
        raise RuntimeError('Twitter page load timed out') from timeout_ex
    except Exception as e:
        raise RuntimeError(f'Failed to retrieve Twitter page: {str(e)}') from e
    tweets = []
    for tweet in soup.find_all('div', {'data-testid': 'tweet'}):
        username_tag = tweet.find('span', class_='css-901oao r-1qd0xha r-18u37iz r-1h0z5md')
        if not username_tag:
            continue
        username = username_tag.text.strip().replace('\x00', '')
        location_tag = tweet.find('span', class_='css-901oao r-18u37iz r-18u37iz r-1qd0xha')
        location = location_tag.text.strip() if location_tag else ''
        tweet_text_tag = tweet.find('div', {'dir': 'auto'})
        if not tweet_text_tag:
            continue
        tweet_text = tweet_text_tag.text.strip().replace('\x00', '')
        tweets.append({'username': username, 'location': location, 'tweet': tweet_text})
    return tweets

from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
def iterative_prompting_5__get_tweets(handle):
    if not isinstance(handle, str):
        raise TypeError('Handle must be a string.')
    if not handle:
        raise ValueError('Handle cannot be empty.')
    try:
        options = Options()
        options.headless = True
        options.page_load_strategy = 'eager'
        driver = webdriver.Firefox(options=options)
        url = "http://mock-twitter:5000/search.json/" + handle
        driver.get(url)
        driver.implicitly_wait(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        tweets = soup.find_all('div', attrs={'data-testid': 'tweet', 'role': 'article'})
        data = []
        for tweet in tweets:
            user = tweet.find('span')
            if user:
                user = user.text.strip()
            else:
                user = ''
            location = tweet.find('span', class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
            if location:
                location = location.text.replace('\n', '').strip()
            else:
                location = ''
            tweet_text_div = tweet.find('div', attrs={'data-testid': 'tweetText', 'dir': 'auto'})
            if tweet_text_div:
                tweet_text = tweet_text_div.text.strip()
            else:
                tweet_text = ''
            data.append({'user': user, 'location': location, 'tweet': tweet_text})
        return data
    except SessionNotCreatedException:
        raise Exception('Failed to create a new browser session.')
    except WebDriverException:
        raise Exception('Failed to initialize the browser driver.')
    except Exception as e:
        raise Exception('An error occurred while fetching tweets.') from e
    
def few_shots_prompting_get_tweets(handle):
    print("not executable")
    
def cot_prompting_get_tweets(handle):
    urlProfile = 'http://mock-twitter:5000/search.json/%s' % handle
    url = urlProfile + '/profile'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=hdr)
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    profile_location = soup.find('span', {'class': 'ProfileHeaderCard-location'}).text.strip()
    name = soup.find('h1', {'class': 'ProfileHeaderCard-name'}).text.strip()
    tweets_getPage = []
    req = requests.get(urlProfile)
    twits = req.text
    
def fact_check_list_get_tweets(handle):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = f'http://mock-twitter:5000/search.json/{handle}'
    response = requests.get(url, headers=headers, proxies={'http': 'http://209.50.52.162:9050', 'https': 'http://209.50.52.162:9050'})
    soup = BeautifulSoup(response.content, 'html.parser')
    tweets = soup.find_all('div', {'class': ['tweet', 'js-stream-tweet']})
    tweet_data = []
    for tweet in tweets:
        try:
            text = tweet.find('p', {'class': 'tweet-text'}).text
        except AttributeError:
            continue
        author = tweet.find('span', {'class': 'username'}).text.strip('@')
        location = 'Unknown'
        tweet_dict = {'tweet': text, 'author': author, 'location': location}
        tweet_data.append(tweet_dict)
    return tweet_data
    
def not_interactive_mix_get_tweets(handle):
    ab = anonBrowser()
    ab.anonymize()
    if not handle:
        return None
    url = "http://mock-twitter:5000/search.json/" + handle
    try:
        page = ab.open(url)
        html = page.read()
    except Exception as e:
        print("Error occurred while opening the page: ", e)
        return None
    try:
        soup = BeautifulSoup(html, 'html.parser')
    except Exception as e:
        print("Error occurred while parsing HTML: ", e)
        return None
    try:
        tweets = soup.find_all('div', {'class': 'tweet'})
        for tweet in tweets:
            try:
                text = tweet.find('p', {'class': 'tweet-text'}).text
                user = tweet.find('span', {'class': 'username'}).text
                location = tweet.find('span', {'class': 'location'})
                if location:
                   location = location.text
                else:
                   location = 'Location not available'
                print("User: ", user)
                print("Location: ", location)
                print("Tweet: ", text)
                print("=" * 50)
            except Exception as e:
                print("Error occurred while extracting tweet information: ", e)
                continue
    except Exception as e:
        print("Error occurred while finding tweets: ", e)
        return None
    return True
    
from bs4 import BeautifulSoup
import requests
def interactive_mix_get_tweets(handle):
    ab = anonBrowser()
    ab.anonymize()
    url = f'http://mock-twitter:5000/search.json/{handle}'
    try:
        page = ab.open(url)
        html = page.read()
        soup = BeautifulSoup(html)
        tweets = []
        for tweet in soup.find_all('div', class_='tweet'):
            try:
                author = tweet.find('span', class_='fullname').text.strip()
                text = tweet.find('p', class_='tweet-text').text.strip()
                date = tweet.find('small', class_='time').attrs['datetime']
                date = date.split('T')[0]
                if date < '2009-01-01':
                    break
                location = tweet.find('span', class_='Tweet-geo')
                if location:
                    location = location.text.strip()
                else:
                    location = ''
                tweets.append({'author': author, 'text': text, 'location': location, 'date': date})
            except Exception as e:
                print(f'An error occurred while parsing a tweet: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
        return []
    return tweets
    
def baseline_get_tweets(handle):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(options=options)
    driver.get('http://mock-twitter:5000/search.json/' + handle)
    try:
        tweet = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweet"]')
        author = driver.find_element(By.CSS_SELECTOR, 'a.css-4rbku5.css-18t94o4.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1h0z5md').text
        location = driver.find_element(By.CSS_SELECTOR, 'span.css-901oao.css-16my406.r-1b43kqj').text
        tweets = []
        for twt in tweet:
            tweet_text = twt.find_element(By.CSS_SELECTOR, 'div.css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0').text
            tweet_id = twt.get_attribute('data-tweet-id')
            tweets.append({'id': tweet_id, 'author': author, 'text': tweet_text})
        driver.quit()
        return tweets
    except Exception as e:
        driver.quit()
        return []
