import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import urllib.parse
import json
import tweepy
import requests


class TweetClient:
    def __init__(self, handle, base_url='http://mock-twitter:5000/search.json'):
        self.handle = handle
        self.base_url = base_url

    def ground_truth_code_get_tweets(self):
        query = urllib.parse.quote_plus(f'from:{self.handle} since:2009-01-01 include:retweets')
        tweets = []
        browser = anonBrowser()
        browser.anonymize()
        url = self.base_url + '?q=' + query
        response = browser.open(url)
        json_objects = json.load(response)
        for result in json_objects['results']:
            new_result = {}
            new_result['from_user'] = result['from_user_name']
            new_result['geo'] = result.get('geo')
            new_result['tweet'] = result['text']
            tweets.append(new_result)
        return tweets

    def persona_get_tweets(self):
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=self.handle, count=200, include_rts=False, tweet_mode='extended')
        return [{'tweet': tweet.full_text} for tweet in tweets]

    import re
    def template_get_tweets(self):
        tweets = []
        try:
            simulated_tweets = [{'tweet': 'Trying out this new Python library. http://example.com'}]
            for tweet_data in simulated_tweets:
                tweet = {'tweet': tweet_data['tweet']}
                tweets.append(tweet)
        except Exception as e:
            print(f'Error fetching tweets: {e}')
        return tweets

    def question_refinement_get_tweets(api_key, api_secret, access_token, access_token_secret, username):
        import tweepy
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            tweets = api.user_timeline(screen_name=username, count=100, tweet_mode='extended', include_rts=False)
            return [{'text': tweet.full_text, 'geolocation': getattr(tweet, 'coordinates', {}), 'screen_name': tweet.user.screen_name, 'created_at': tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')} for tweet in tweets]
        except tweepy.TweepError as e:
            print(f'Error: {str(e)}')
            return None

    def alternative_approaches_get_tweets(self):
        try:
            api = tweepy.API(auth)
            tweets = api.user_timeline(screen_name=self.handle, count=200, include_rts=False, tweet_mode='extended')
            return [{'tweet': tweet.full_text, 'geo': tweet._json['place'] if tweet._json['place'] else None} for tweet in tweets]
        except tweepy.TweepError as e:
            print(f'Error: {e}')
            return []

    def context_manager_get_tweets(self):
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=self.handle, count=200, include_rts=False, tweet_mode='extended')
        return [{'id': tweet.id, 'tweet': tweet.full_text} for tweet in tweets]

    def iterative_prompting_3_get_tweets(self):
        try:
            auth = self.api_authenticated()
            if not auth:
                raise ValueError("Authentication failed")
            tweets = tweepy.API(auth=auth).user_timeline(screen_name=self.handle, count=200, tweet_mode='extended', wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            return [tweet._json for tweet in tweets]
        except tweepy.TweepError as e:
            print(f"An error occurred: {e}")
            return []
        except ValueError as e:
            print(f"{e}: Could not authenticate. Please check your credentials.")
            return []
    def api_authenticated(self):
        try:
            auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
            auth.set_access_token(self.access_token, self.access_token_secret)
            return auth
        except tweepy.TweepError as e:
            print(f"An error occurred during Twitter API authentication: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def iterative_prompting_4_get_tweets(self):
        try:
            api = TwitterAPI(consumer_key='YOUR_CONSUMER_KEY', consumer_secret='YOUR_CONSUMER_SECRET', access_token='YOUR_ACCESS_TOKEN', access_token_secret='YOUR_ACCESS_TOKEN_SECRET')
            tweets = api.get_user_timeline(screen_name=self.handle, count=200)
            return tweets
        except requests.exceptions.HTTPError as e:
            print(f'HTTP error occurred: {e}')
            return None
        except requests.exceptions.ConnectionError as e:
            print(f'Connection error occurred: {e}')
            return None
        except requests.exceptions.Timeout as e:
            print(f'Timeout error occurred: {e}')
            return None
        except requests.exceptions.RequestException as e:
            print(f'A request-related error occurred: {e}')
            return None
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return None

    def iterative_prompting_5_get_tweets(self):
        try:
            api = TwitterAPI(self.handle)
            tweets = api.get_user_tweets(count=100)
            return tweets
        except Exception as e:
            return []

    def few_shots_prompting_get_tweets(self):
        api = get_api_instance()
        tweets = api.user_timeline(screen_name=self.handle, count=200, exclude_replies=True)
        for tweet in tweets:
            tweet['tweet'] = tweet.text
        return tweets

    def cot_prompting_get_tweets(self):
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=self.handle, count=200, include_rts=False, tweet_mode='extended')
        return [{ 'tweet_id': tweet.id_str, 'tweet': tweet.full_text } for tweet in tweets if hasattr(tweet, 'full_text')]

    import tweepy
    import re
    from urllib.parse import urlparse
    import os

    def fact_check_list_get_tweets(self):
        tweets_count = 100
        tweets_lookup = []
        for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=self.handle, tweet_mode='extended').items(tweets_count):
            tweets_lookup.append(tweet._json)
        return tweets_lookup

    def not_interactive_mix_get_tweets(self, text):
        links = re.findall('(http.*?)(?:\Z| )\1', text)
        return [link[0] for link in links if link[0]]

    def baseline_get_tweets(self):
        api = TwitterAPI(self.handle)
        tweets = api.get_user_tweets()
        return tweets

