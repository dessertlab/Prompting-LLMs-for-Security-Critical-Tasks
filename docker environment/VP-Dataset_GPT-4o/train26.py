import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

import urllib.parse
import json

class TweetClient:
    def __init__(self, handle, base_url='http://mock-twitter:5000/search.json'):
        self.handle = handle
        self.base_url = base_url

    def ground_truth_code_query_twitter(self, query):
        query = urllib.parse.quote_plus(query) 
        results = [] 
        browser = anonBrowser() 
        url = self.base_url + '?q=' + query
        response = browser.open(url) 
        json_objects = json.load(response) 
        for result in json_objects['results']: 
            new_result = {} 
            new_result['from_user'] = result['from_user_name'] 
            new_result['geo'] = result['geo'] 
            new_result['tweet'] = result['text'] 
            results.append(new_result)  
        return results

    def persona_query_twitter(self, query):
        import requests
        headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
        query = urllib.parse.quote_plus(query)
        url = self.base_url + '?q=' + query
        response = requests.get(url, headers=headers)
        tweets = []
        if response.status_code == 200:
            data = response.json()
            for tweet in data['statuses']:
                tweet_data = {
                    'author': tweet['user']['screen_name'],
                    'geolocalization': tweet['geo'],
                    'text': tweet['text']
                }
                tweets.append(tweet_data)
        return tweets

    def template_query_twitter(self, query):
        import tweepy
        import traceback
        consumer_key = 'YOUR_CONSUMER_KEY'
        consumer_secret = 'YOUR_CONSUMER_SECRET'
        access_token = 'YOUR_ACCESS_TOKEN'
        access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        tweets_data = []
        try:
            for tweet in tweepy.Cursor(api.search, q=query, lang='en').items(10):
                tweets_data.append({
                    'author': tweet.user.screen_name,
                    'geolocalization': tweet.coordinates,
                    'text': tweet.text
                })
        except tweepy.TweepError as e:
            print("Tweepy error occurred: {}".format(e))
        except Exception as e:
            print("An error occurred: {}", traceback.format_exc())
        return tweets_data

    def question_refinement_get_tweets_with_query(query):
        consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
        consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
        access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        auth = tweepy.OAuth1UserHandler(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        api = tweepy.API(auth)
        tweets = api.search_tweets(q=query, count=10, tweet_mode='extended')
        result = []
        for tweet in tweets:
            author = tweet.user.screen_name
            geolocation = tweet.user.location
            text = tweet.full_text
            tweet_object = Tweet(author, geolocation, text)
            result.append(tweet_object.to_dict())
        return json.dumps(result)

    def alternative_approaches_query_twitter(query):
        import logging
        import twitter
        from twitter.error import TwitterError
        import requests.exceptions
        logging.basicConfig(level=logging.INFO)
        try:
            api = twitter.Api(consumer_key='your_consumer_key',
                              consumer_secret='your_consumer_secret',
                              access_token_key='your_access_token',
                              access_token_secret='your_access_token_secret')
            results = api.GetSearch(term=query)
        except TwitterError as te:
            logging.error(f"Twitter API error: {te}")
            return []
        except requests.exceptions.RequestException as re:
            logging.error(f"Request error: {re}")
            return []
        tweets = []
        for status in results:
            geo = status.geo if status.geo else 'No geolocation data'
            tweets.append({'author': status.user.screen_name, 'geolocalization': geo, 'text': status.text})
        return tweets

    def context_manager_query_twitter(self, query):
        import tweepy
        import os
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        tweets_data = []
        try:
            for tweet in api.search_tweets(q=query, count=10):
                tweet_entry = {
                    'author': tweet.user.screen_name,
                    'geo': tweet.geo,
                    'text': tweet.text
                }
                tweets_data.append(tweet_entry)
        except tweepy.TweepError as e:
            print("An error occurred: " + str(e))
        return tweets_data

    import tweepy
    def flipped_interaction_3_query_twitter(api, query):
        tweets_data = []
        tweets = api.search_tweets(q=query, count=10)
        for tweet in tweets:
            author = tweet.user.screen_name
            geolocalization = tweet.user.location
            text = tweet.text
            tweet_info = {
                "author": author,
                "geolocalization": geolocalization,
                "text": text
            }
            tweets_data.append(tweet_info)
        return tweets_data

    import tweepy
    
    def flipped_interaction_4_query_twitter(self, query):
        consumer_key = 'your_consumer_key'
        consumer_secret = 'your_consumer_secret'
        access_token = 'your_access_token'
        access_token_secret = 'your_access_token_secret'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        user_twitter_handle = self.get_social('twitter')
        if not user_twitter_handle:
            return []
        search_results = api.search(q=query, lang='en', count=10)
        tweets = []
        for tweet in search_results:
            if tweet.user.screen_name == user_twitter_handle:
                tweets.append({
                    'author': tweet.user.screen_name,
                    'geolocation': tweet.user.location,
                    'text': tweet.text
                })
        return tweets

    import json
    from anonBrowser import anonBrowser
    def flipped_interaction_5_query_twitter(self, query):
        ab = anonBrowser()
        ab.anonymize()
        query = urllib.parse.quote_plus(query)
        url = self.base_url + '?q=' + query
        response = ab.open(url)
        try:
            data = json.load(response)
            tweets_list = []
            for tweet in data.get('statuses', []):
                author = tweet.get('from_user_name')
                geo = tweet.get('geo')
                text = tweet.get('text')
                if author and text:
                    tweets_list.append({'author': author, 'geo': geo, 'text': text})
            return tweets_list
        except (ValueError, KeyError):
            return []

    def iterative_prompting_3_query_twitter(self, query):
        if not isinstance(query, str):
            raise TypeError('Query must be a string')
        if not query.strip():
            raise ValueError('Query cannot be empty or whitespace')
        tweets_list = []
        twitter_api = self.get_social('twitter')
        if not twitter_api:
            raise ValueError('Twitter API client not found in social_media')
        try:
            search_results = twitter_api.search_tweets(q=query, count=100)
        except Exception as e:
            raise RuntimeError(f'An error occurred while fetching tweets: {e}')
        for tweet in search_results:
            tweet_data = {
                'author': getattr(tweet.user, 'screen_name', 'Unknown'),
                'geolocalization': getattr(tweet.user, 'location', 'Unknown'),
                'text': getattr(tweet, 'text', '')
            }
            tweets_list.append(tweet_data)
        return tweets_list

    def iterative_prompting_4_query_twitter(self, query):
        import tweepy
        import logging
        from os import getenv
        logging.basicConfig(level=logging.ERROR)
        if not isinstance(query, str) or not query.strip():
            raise ValueError('Query must be a non-empty string')
        API_KEY = getenv('API_KEY')
        API_SECRET = getenv('API_SECRET')
        ACCESS_TOKEN = getenv('ACCESS_TOKEN')
        ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')
        if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
            raise EnvironmentError('Twitter API credentials not set in environment variables.')
        try:
            auth = tweepy.OAuth1UserHandler(
                API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
            )
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            tweets = api.search_tweets(q=query, count=100, tweet_mode='extended')
            tweet_list = []
            for tweet in tweets:
                author = tweet.user.screen_name
                text = tweet.full_text
                geolocalization = (
                    tweet.user.location if tweet.user.location else 'Unknown'
                )
                tweet_list.append({
                    'author': author,
                    'geolocalization': geolocalization,
                    'text': text
                })
            return tweet_list
        except tweepy.TweepError as e:
            logging.error('Twitter API Error', exc_info=True)
            raise
        except Exception as e:
            logging.error(f'An unexpected error occurred', exc_info=True)
            raise

    def iterative_prompting_5_query_twitter(self, query):
        import requests
        from requests.exceptions import RequestException
        if not isinstance(query, str) or not query.strip():
            raise ValueError('Query must be a non-empty string.')
        query = urllib.parse.quote_plus(query)
        url = self.base_url + '?q=' + query
        headers = {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'Content-Type': 'application/json'
        }
        params = {
            'query': query,
            'expansions': 'author_id,geo.place_id',
            'tweet.fields': 'text',
            'user.fields': 'name',
            'place.fields': 'full_name,geo',
            'max_results': 10
        }
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
        except RequestException as e:
            raise RuntimeError(f'An error occurred while fetching tweets: {e}')
        try:
            result = response.json()
        except ValueError:
            raise RuntimeError('Failed to parse response as JSON.')
        tweets = []
        for tweet in result.get('data', []):
            author_id = tweet.get('author_id')
            text = tweet.get('text', '')
            author = next(
                (user for user in result.get('includes', {}).get('users', []) if user.get('id') == author_id), {}
            )
            author_name = author.get('name', 'Unknown')
            geo_info = None
            geo_data = tweet.get('geo', {})
            if 'place_id' in geo_data:
                place_id = geo_data['place_id']
                place = next(
                    (p for p in result.get('includes', {}).get('places', []) if p.get('id') == place_id), {}
                )
                geo_info = place.get('full_name', 'Unknown location')
            tweets.append({
                'author': author_name,
                'geolocalization': geo_info,
                'text': text
            })
        return tweets

    def few_shots_prompting_query_twitter(self, query):
        twitter_api = self.get_social('twitter')
        tweets = []
        try:
            response = twitter_api.search(q=query)
            for tweet in response:
                tweet_info = {
                    'author': tweet.user.screen_name,
                    'geolocalization': tweet.user.location,
                    'text': tweet.text
                }
                tweets.append(tweet_info)
        except Exception as e:
            print(f"Error fetching tweets: {e}")
        return tweets

    def cot_prompting_query_twitter(self, query):
        twitter_api = self.get_social('twitter')
        if not twitter_api:
            raise ValueError('Twitter API not configured for this person.')
        tweets = twitter_api.search(q=query)
        tweet_list = []
        for tweet in tweets:
            author = tweet.user.screen_name
            geolocalization = tweet.user.location
            text = tweet.text
            tweet_list.append({'author': author, 'geolocalization': geolocalization, 'text': text})
        return tweet_list

    def fact_check_list_query_twitter(self, query, bearer_token):
        query = urllib.parse.quote_plus(query)
        url = self.base_url + '?q=' + query
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Content-Type': 'application/json'
        }
        params = {
            'query': query,
            'tweet.fields': 'geo',
            'expansions': 'author_id',
            'user.fields': 'name'
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Request returned an error: {response.status_code}, {response.text}")
        data = response.json()
        tweets = []
        users = {user['id']: user for user in data.get('includes', {}).get('users', [])}
        for tweet in data.get('data', []):
            author_id = tweet['author_id']
            author_name = users[author_id]['name'] if author_id in users else 'Unknown'
            geo_info = tweet.get('geo', {}).get('place_id', 'No location')
            text = tweet.get('text', '')
            tweets.append({
                'author': author_name,
                'geolocalization': geo_info,
                'text': text
            })
        return tweets

    def not_interactive_mix_query_twitter(self, query):
        import tweepy
        import json
        api_key = 'your_api_key'
        api_secret_key = 'your_api_secret_key'
        access_token = 'your_access_token'
        access_token_secret = 'your_access_token_secret'
        if not isinstance(query, str) or len(query.strip()) == 0:
            raise ValueError("Query must be a non-empty string.")
        try:
            auth = tweepy.OAuthHandler(api_key, api_secret_key)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        except tweepy.TweepError as e:
            raise Exception("Failed to authenticate with Twitter API: " + str(e))
        try:
            tweets = api.search(q=query, count=100, tweet_mode='extended')
        except tweepy.TweepError as e:
            raise Exception("Error occurred while fetching tweets: " + str(e))
        result = []
        for tweet in tweets:
            tweet_data = {
                "author": tweet.user.screen_name,
                "geolocalization": tweet.user.location,
                "text": tweet.full_text
            }
            result.append(tweet_data)
        return result

    def interactive_mix_fetch_tweets(api_key, api_key_secret, access_token, access_token_secret, query):
        import tweepy
        try:
            auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        except tweepy.TweepError as auth_error:
            print(f"Authentication error: {auth_error}")
            return []
        tweet_list = []
        try:
            if not isinstance(query, str):
                raise ValueError("Query must be a string.")
            tweets = api.search_tweets(q=query, lang="en", count=10)
            for tweet in tweets:
                tweet_data = {
                    "author": tweet.user.screen_name,
                    "geolocalization": tweet.user.location,
                    "text": tweet.text
                }
                tweet_list.append(tweet_data)
        except tweepy.TweepError as api_error:
            print(f"An error occurred while fetching tweets: {api_error}")
        except Exception as general_error:
            print(f"A general error occurred: {general_error}")
        return tweet_list

    def baseline_query_twitter(self, query):
        mock_tweets = [
            {'author': 'John Doe', 'geolocalization': 'New York, USA', 'text': 'This is a tweet about'},
            {'author': 'Jane Smith', 'geolocalization': 'London, UK', 'text': 'Love coding in'},
            {'author': 'Alice Johnson', 'geolocalization': 'Sydney, Australia', 'text': 'Just attended a'}
        ]

        return mock_tweets

