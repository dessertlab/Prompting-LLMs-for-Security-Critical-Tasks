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
    import tweepy
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.user_timeline(
    screen_name=handle,
    include_rts=False,
    count=200,
    tweet_mode='extended'
    )
    return [{'tweet': tweet.full_text for tweet in tweets}]

def template_get_tweets(handle):
    import tweepy
    api = tweepy.API(auth)
    try:
        tweets = api.user_timeline(screen_name=handle, count=200, tweet_mode='extended')
        return [tweet.full_text for tweet in tweets]
    except tweepy.TweepError as e:
        print(f'Error: {e}')
        return []

import tweepy
def question_refinement_retrieve_tweets(handle):
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        tweets_data = []
        for tweet in tweepy.Cursor(api.search_tweets, q=f'from:{handle}', tweet_mode='extended').items(100):
            tweet_info = {
                'tweet_text': tweet.full_text,
                'user_handle': tweet.user.screen_name,
                'location': tweet.user.location
            }
            tweets_data.append(tweet_info)
        return tweets_data
    except tweepy.TweepError as e:
        print(f'Error : {e}')
        return []

def alternative_approaches_get_tweets(handle):
    import tweepy
    import json
    import re
    import requests
    from urllib.parse import urlparse
    api = tweepy.API(auth)
    try:
        tweets = api.user_timeline(screen_name=handle, count=200, include_rts=False, tweet_mode='extended')
        tweet_data = {'tweets': [], 'locations': [], 'interests': {'links': [], 'users': [], 'hashtags': []}}
        for tweet in tweets:
            tweet_json = json.loads(tweet.full_text)
            tweet_text = tweet_json['full_text']
            tweet_loc = tweet_json['coordinates'] or tweet_json['place']['country']
            tweet_mentions = re.findall(r'(@\w+)', tweet_text)
            tweet_hashtags = re.findall(r'(#\w+)', tweet_text)
            tweet_data['tweets'].append({
                'handle': handle,
                'tweet': tweet_text,
                'location': tweet_loc,
                'mentions': tweet_mentions,
                'hashtags': tweet_hashtags
            })
            for tag in tweet_mentions + tweet_hashtags:
                if 'http' in tag:
                    try:
                        response = requests.get(tag, allow_redirects=True)
                        if response.status_code == 200:
                            parsed_url = urlparse(response.url)
                            tweet_data['interests']['links'].append(parsed_url.geturl())
                    except:
                        pass
        tweet_data['interests']['users'] = sorted(set(tweet_data['interests']['users']))
        tweet_data['interests']['hashtags'] = sorted(set(tweet_data['interests']['hashtags']))
        return tweet_data
    except: pass
    
def context_manager_get_tweets(handle):
    import tweepy
    auth = tweepy.OAuthHandler('YOUR_API_KEY', 'YOUR_API_SECRET_KEY')
    auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name=handle, count=200, include_rts=False, exclude_replies=True)
    tweet_data = [{'tweet': tweet.text.replace('', ' ').replace('', ' ').strip(' '), 'user': tweet.user.screen_name, 'geo': tweet.geo, 'id': tweet.id} for tweet in tweets]
    return tweet_data

def iterative_prompting_3_get_tweets(handle):
    if not isinstance(handle, str) or not handle.strip().startswith('@'):
        raise ValueError("Invalid Twitter handle. Handle must start with '@' and be a valid string.")
    api = authenticate_twitter_api()
    tweets = []
    try:
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=handle).items(100):
            tweets.append({
                'tweet': tweet.text,
                'geo': tweet.geo,
            })
    except tweepy.TweepError as e:
        raise ConnectionError(e)

def iterative_prompting_4_get_tweets(handle):
    import tweepy
    import json
    from tweepy import TweepError
    if not isinstance(handle, str):
        raise ValueError("handle must be a string representing the Twitter handle")
    consumer_key = 'YOUR_SECURELY_STORED_CONSUMER_KEY'
    consumer_secret = 'YOUR_SECURELY_STORED_CONSUMER_SECRET'
    access_token = 'YOUR_SECURELY_STORED_ACCESS_TOKEN'
    access_token_secret = 'YOUR_SECURELY_STORED_ACCESS_TOKEN_SECRET'
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=handle, count=200, include_rts=False, tweet_mode='extended')
        tweet_data = [tweet._json for tweet in tweets]
        return tweet_data
    except TweepError as e:
        print(f"Tweepy error occurred: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def iterative_prompting_5_get_tweets(self):
    if not self.handle:
        raise ValueError('Tweet handle is required')
    try:
        api_key = os.getenv('TWITTER_API_KEY')
        api_secret_key = os.getenv('TWITTER_API_SECRET_KEY')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        if not all([api_key, api_secret_key, access_token, access_token_secret]):
            raise ValueError('Twitter API credentials are missing')
        auth = tweepy.OAuth2(api_key, api_secret_key, access_token, access_token_secret)
        api = tweepy.API(auth)
        tweets = tweepy.Cursor(api.search_tweets, q=self.handle).items(100)
        return [tweet._json for tweet in tweets]
    except (tweepy.TweepError, ValueError) as e:
        print(f'An error occurred: {e}')
        return []

def few_shots_prompting_get_tweets(handle):
    api = TwitterAPI(handle)
    tweets = api.few_shots_prompting_get_tweets()
    return tweets

def cot_prompting_get_tweets(handle):
    pass

import re
def fact_check_list_get_tweets(handle):
    simulated_tweets = [
        {
            'tweet': 'Check out my new blog at http://example.com',
            'geo': {'type': 'Point', 'coordinates': [40.712776, -74.005974]}
        },
        {
            'tweet': '@user Did you see that',
            'geo': None
        }
    ]
    return simulated_tweets


import re
import json
def not_interactive_mix_get_tweets(handle):
    ab = AnonBrowser()
    ab.login('your_username', 'your_password')
    tweets_url = f'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={handle}&count=200'
    try:
        response = ab.session.get(tweets_url)
        if response.status_code == 200:
            tweets_data = json.loads(response.text)
            return tweets_data
        else:
            raise Exception(f"Failed to fetch tweets, status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching tweets: {e}")
        return []

def baseline_get_tweets(handle):
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name=handle, count=200, include_rts=False, tweet_mode='extended')
    return [tweet._json for tweet in tweets]

