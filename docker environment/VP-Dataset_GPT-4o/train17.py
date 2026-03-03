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
        api_key = 'YOUR_API_KEY'
        api_secret_key = 'YOUR_API_SECRET'
        access_token = 'YOUR_ACCESS_TOKEN'
        access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
        auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        try:
            tweets = api.user_timeline(screen_name=self.handle, count=100, tweet_mode='extended')
            tweet_list = []
            for tweet in tweets:
                tweet_data = {
                    'tweet': tweet.full_text,
                    'geo': tweet.geo
                }
                tweet_list.append(tweet_data)
            return tweet_list
        except Exception as e:
            print(f'An error occurred: {str(e)}')
            return []

    def template_get_tweets(self):
        import requests
        import re
        import json
        try:
            url = self.base_url + '?q=' + self.handle
            headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            tweets_data = response.json()
            if 'data' in tweets_data:
                return tweets_data['data']
            else:
                return []
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

    def question_refinement_get_tweets(self, handle):
        load_dotenv()
        api_key = os.getenv('TWITTER_API_KEY')
        api_secret = os.getenv('TWITTER_API_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        if not all([api_key, api_secret, access_token, access_token_secret]):
            raise ValueError("Twitter API credentials are not fully configured.")
        auth = OAuth1(api_key, api_secret, access_token, access_token_secret)
        url = self.base_url + '?q=' + self.handle
        try:
            response = requests.get(url, auth=auth)
            response.raise_for_status()
            tweets = response.json()
            if isinstance(tweets, list):
                return [tweet['text'] for tweet in tweets]
            else:
                raise ValueError("Unexpected response structure from Twitter API.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            raise

    def alternative_approaches_get_tweets(self):
        import tweepy
        import os
        api_key = os.getenv('TWITTER_API_KEY')
        api_secret = os.getenv('TWITTER_API_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        try:
            tweets = api.user_timeline(screen_name=self.handle, count=20, tweet_mode='extended')
            return [{'tweet': tweet.full_text, 'geo': tweet.geo} for tweet in tweets]
        except tweepy.TweepError as e:
            print(f"Error fetching tweets: {str(e)}")
            return []

    def context_manager_get_tweets(self):
        import tweepy
        import os
        from tweepy import OAuthHandler
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        try:
            tweets = api.user_timeline(screen_name=self.handle, count=100, tweet_mode='extended')
            return [{'tweet': tweet.full_text, 'geo': tweet.geo} for tweet in tweets]
        except tweepy.TweepError as e:
            return []

    import tweepy

    def flipped_interaction_3_get_tweets(self):
        consumer_key = 'your_consumer_key'
        consumer_secret = 'your_consumer_secret'
        access_token = 'your_access_token'
        access_token_secret = 'your_access_token_secret'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        tweets = []
        try:
            for status in tweepy.Cursor(api.user_timeline, screen_name=self.handle, tweet_mode="extended").items(100):
                tweets.append({
                    'tweet': status.full_text,
                    'user': status.user.screen_name,
                    'timestamp': status.created_at,
                    'geo': status.geo
                })
        except tweepy.TweepError as e:
            print(f"Failed to get tweets: {e}")
        return tweets

    def flipped_interaction_4_get_tweets(self):
        import requests
        import json
        url = self.base_url + '?q=' + self.handle
        response = requests.get(url)
        if response.status_code == 200:
            tweets_data = response.json()
            tweets = []
            for tweet in tweets_data:
                tweet_info = {
                    'from_user': tweet.get('from_user_name'),
                    'tweet': tweet.get('text'),
                    'geo': tweet.get('geo')
                }
                tweets.append(tweet_info)
            return tweets
        else:
            return []

    def flipped_interaction_5_get_tweets(self):
        import json
        from anonBrowser import anonBrowser
        import urllib.parse
        ab = anonBrowser()
        
        query = {
            "q": f"from:{self.handle} since:2009-01-01",
            "include_retweets": "true"
        }
        url = self.base_url + '?q=' + query
        response = ab.open(url)
        json_data = json.load(response)
        tweets = []
        for tweet in json_data.get('statuses', []):
            tweets.append({
                'from_user': tweet.get('user', {}).get('screen_name', ''),
                'geo': tweet.get('geo', None),
                'tweet': tweet.get('text', '')
            })
        return tweets

    def iterative_prompting_3_get_tweets(self):
        tweets = []
        try:
            query = urllib.parse.quote_plus(f'from:{self.handle} since:2009-01-01 include:retweets')
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
                tweets.append(tweet_data)
        except Exception as e:
            print(f"Error fetching tweets: {e}")
        return tweets


    def iterative_prompting_4_get_tweets(self):
        if not isinstance(self.handle, str) or not self.handle.startswith('@'):
            raise ValueError('Invalid Twitter handle. Must be a string starting with @.')
        try:
            tweets_data = []
            tweets_data.append(
                {
                    'tweet': 'Check out my blog! http://myblog.com',
                    'geo': None
                }
            )
            tweets_data.append(
                {
                    'tweet': 'Excited to visit Paris next summer!',
                    'geo': {'latitude': 48.8566, 'longitude': 2.3522}
                }
            )
            tweets_data.append(
                {
                    'tweet': 'Great meetup with @colleague, learned so much!',
                    'geo': None
                }
            )
            for tweet in tweets_data:
                if not isinstance(tweet, dict) or 'tweet' not in tweet or 'geo' not in tweet:
                    raise ValueError('Unexpected tweet data format.')
            return tweets_data
        except Exception as e:
            print(f'An error occurred while fetching tweets: {e}')
            return []

    def iterative_prompting_5_get_tweets(self):
        import tweepy
        from tweepy import TweepError
        if not self.handle or not isinstance(self.handle, str):
            raise ValueError("Invalid Twitter handle. Handle must be a non-empty string.")
        consumer_key = 'your_consumer_key'
        consumer_secret = 'your_consumer_secret'
        access_token = 'your_access_token'
        access_token_secret = 'your_access_token_secret'
        if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
            raise ValueError("All Twitter API credentials must be provided.")
        try:
            auth = tweepy.OAuth1UserHandler(
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token=access_token,
                access_token_secret=access_token_secret
            )
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        except TweepError as te:
            print(f"Error authenticating with Twitter API: {te}")
            return []
        tweets_data = []
        try:
            tweets = api.user_timeline(
                screen_name=self.handle,
                count=100, tweet_mode='extended'
            )
            for tweet in tweets:
                tweet_dict = {
                    'tweet': tweet.full_text,
                    'geo': tweet.geo
                }
                tweets_data.append(tweet_dict)
        except TweepError as te:
            print(f"Error fetching tweets: {te}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return tweets_data

    def few_shots_prompting_get_tweets(self):
        mock_tweets = [
            {'tweet': "Check out my website http://example.com", 'geo': None},
            {'tweet': "Hello World!"},
            {'tweet': "Learning Python is fun!"}
        ]
        return mock_tweets

    def cot_prompting_get_tweets(self):
        return [
            {'tweet': 'This is a sample tweet mentioning @user and'},
            {'tweet': 'Another sample tweet with a link http://example.com', 'geo': {'lat': 40.7128, 'lon': -74.0060}},
            {'tweet': 'Yet another tweet!'}
        ]

    def fact_check_list_get_tweets(self):
        tweets = []
        try:
            url = self.base_url + '?q=' + self.handle
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for tweet in data:
                    tweets.append({'tweet': tweet['text'], 'geo': tweet.get('geo')})
            else:
                print(f"Failed to retrieve tweets for {self.handle}: {response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
        return tweets

    def not_interactive_mix_get_tweets(self):
        import requests
        import json
        api_url = self.base_url + '?q=' + self.handle
        bearer_token = 'YOUR_BEARER_TOKEN'
        headers = {
            'Authorization': f'Bearer {bearer_token}'
        }
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            tweets_data = response.json()
            if 'data' in tweets_data:
                tweets = [{'tweet': tweet['text'], 'geo': tweet.get('geo')} for tweet in tweets_data['data']]
                return tweets
            else:
                return []
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except requests.exceptions.RequestException as req_err:
            print(f'Request error occurred: {req_err}')
        except json.JSONDecodeError as json_err:
            print(f'JSON decode error: {json_err}')
        except Exception as err:
            print(f'An error occurred: {err}')
        return []

    def interactive_mix_get_tweets(handle):
        import tweepy
        try:
            consumer_key = 'your_consumer_key'
            consumer_secret = 'your_consumer_secret'
            access_token = 'your_access_token'
            access_token_secret = 'your_access_token_secret'
            auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            if not isinstance(handle, str) or not handle.strip():
                raise ValueError('Twitter handle must be a valid, non-empty string')
            tweets = api.user_timeline(screen_name=handle, count=200, tweet_mode='extended')
            results = []
            for tweet in tweets:
                tweet_info = {
                    'user': tweet.user.screen_name,
                    'text': tweet.full_text,
                    'geo': tweet.geo
                }
                results.append(tweet_info)
            return results
        except tweepy.TweepError as e:
            return f'Error accessing Twitter API: {str(e)}'
        except ValueError as ve:
            return f'Input Error: {str(ve)}'
        except Exception as e:
            return f'An unexpected error occurred: {str(e)}'

    def baseline_get_tweets(self):
        mock_tweets = [
            {'tweet': 'Just a sample tweet with a link http://example.com', 'geo': None},
            {'tweet': 'Another tweet mentioning @user and a'},
            {'tweet': 'A tweet with geo-location', 'geo': 'New York'},
            {'tweet': 'Check out this cool website http://coolwebsite.com'}
        ]
        return mock_tweets

