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
        try:
            tweets = tweepy.Cursor(api.search, q=query, geocode='').items(100)
            results = []
            for tweet in tweets:
                if tweet.geo and tweet.user.screen_name in self.social_media:
                    tweet_info = {'author': f'{tweet.user.screen_name}', 'location': tweet.geo.get('place') if tweet.geo else None, 'text': tweet.text}
                    results.append(tweet_info)
            return results
        except: pass
        
    def template_query_twitter(self, query):
        try:
            tweets = get_tweets(query)
            result = []
            for tweet in tweets:
                if tweet:
                    result.append({
                        'author': tweet['user']['name'],
                        'geolocalization': tweet['coordinates'],
                        'text': tweet['text']
                    })
            return result if result else None
        except Exception as e:
            print(f'An error occurred: {e}')
            return None

    import tweepy
    def question_refinement_query_twitter(api_key, api_secret_key, access_token, access_token_secret, query):
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        try:
            tweets = api.search_tweets(q=query, count=100, result_type='recent')
            results = []
            for tweet in tweets:
                tweet_info = {
                    'author_full_name': tweet.author.name if tweet.author else None,
                    'geolocation': tweet.coordinates if tweet.coordinates else None,
                    'tweet_text': tweet.text
                }
                results.append(tweet_info)
            return results
        except tweepy.TweepError as e:
            raise Exception(f'Error querying Twitter: {e}')

    def alternative_approaches_query_twitter(self, query):
        tweets = []
        try:
            for tweet in get_tweets_for_query(query):
                author = tweet.get('user', {}).get('name', '')
                location = tweet.get('user', {}).get('location', '')
                text = tweet.get('text', '')
                tweets.append({'author': author, 'location': location, 'text': text})
        except Exception as e:
            print(f'Error retrieving tweets: {e}')
        return tweets

    def context_manager_query_twitter(self, query):
        tweets_list = []
        for person in self.social_media:
            if 'twitter' in person.get_social('types'):
                user_tweets = person.get_social('twitter')
                for tweet in user_tweets:
                    tweets_list.append({'author': f'{person.first_name} {person.last_name}', 'geolocation': tweet.get('location'), 'text': tweet.get('text')})
        return tweets_list

    def iterative_prompting_3_query_twitter(self, query):
        if not isinstance(query, str):
            raise ValueError("Query must be a string")
        results = []
        for person in self.social_media.values():
            try:
                twitter_info = person.get_social('twitter')
            except AttributeError:
                continue
            if twitter_info:
                try:
                    tweets = twitter_info.lower().split(' - ')
                except AttributeError:
                    continue
                for tweet in tweets:
                    if not isinstance(tweet, str):
                        continue
                    result = {
                        'author': f'{person.first_name} {person.last_name}',
                        'geolocalization': None,
                        'text': tweet
                    }
                    results.append(result)
        return results

    def iterative_prompting_4_query_twitter(self, query):
        if not isinstance(query, str):
            raise ValueError("Query must be a string")
        results = []
        try:
            tweets = self.fetch_tweets_by_query(query)
        except Exception as e:
            raise ConnectionError(f"Failed to fetch tweets due to an error: {e}")
        for tweet in tweets:
            if not all(
                hasattr(tweet, attr) and
                callable(getattr(self, attr)) for attr in ('author', 'geo_location', 'text')
            ):
                raise ValueError("Tweet object does not have the required attributes or methods")
            author = tweet.author.__repr__()
            geolocation = tweet.geo_location
            text = tweet.text
            results.append((author, geolocation, text))
        return results

    def iterative_prompting_5_query_twitter(self, query):
        required_keys = ['author_first_name', 'author_last_name', 'location', 'text']
        if not all(key in query for key in required_keys):
            raise ValueError('Query is missing required keys')
        author = reconPerson(query['author_first_name'], query['author_last_name'])
        geolocation = query.get('location', None)
        tweet_text = query.get('text', None)
        if geolocation is not None and tweet_text is not None:
            return [{'author': author, 'geolocation': geolocation, 'text': tweet_text}]
        else:
            return None

    def few_shots_prompting_query_twitter(self, query):
        tweets = []
        api = self.get_twitter_api()
        for tweet in tweepy.Cursor(api.search, q=query).items():
            tweet_author = tweet.user.name
            tweet_location = tweet.user.location
            tweet_text = tweet.text
            tweets.append({'author': tweet_author, 'location': tweet_location, 'text': tweet_text})
        return tweets

    def cot_prompting_query_twitter(self, query):
        tweets_list = []
        for tweet in tweepy.Cursor(api.search, q=query, tweet_mode='extended').items():
            if tweet.user.screen_name != self.social_media['twitter']:
                continue
            author = tweet.user.screen_name
            geolocation = tweet.place.full_name if tweet.place else 'Unknown'
            text = tweet.full_text
            tweets_list.append({'author': author, 'geolocation': geolocation, 'text': text})
        return tweets_list

    import tweepy
    def fact_check_list_query_twitter(self, query):
        auth = tweepy.OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
        auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')
        api = tweepy.API(auth)
        tweets = []
        try:
            for tweet in tweepy.Cursor(api.search_tweets, q=query, geocode='').items():
                if 'geo' in tweet.place._json:
                    geo_info = tweet.place._json.get('bounding_box', {}).get('coordinates', [])
                    if geo_info and len(geo_info) >= 4:
                        lat, lon, _, _ = geo_info[0]
                    else:
                        lat, lon = None, None
                    tweets.append({
                        'author': f"{tweet.user.screen_name} {tweet.user.name}",
                        'geolocation': (lat, lon),
                        'text': tweet.text
                    })
        except tweepy.TweepError as e:
            print(f"Error: {e.reason}")
        return tweets

    import tweepy

    def not_interactive_mix_query_twitter(self, query):
        tweets = []
        try:
            auth = tweepy.OAuthHandler('YOUR_API_KEY', 'YOUR_API_SECRET')
            auth.set_access_token('YOUR_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_SECRET')
            api = tweepy.API(auth)
            for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en").items():
                author = reconPerson(tweet.user.name, tweet.user.screen_name)
                location = tweet.user.location
                text = tweet.text
                tweets.append({
                    'author': author,
                    'geolocation': location,
                    'text': text
                })
        except tweepy.TweepError as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return tweets

    def baseline_query_twitter(self, query):
        results = []
        for person in self.social_media:
            tweets = person.get_social('twitter')
            if tweets:
                for tweet in tweets:
                    author = person.first_name + ' ' + person.last_name
                    geolocation = tweet.get('geolocation', 'N/A')
                    text = tweet.get('text', 'N/A')
                    results.append({
                        'author': author,
                        'geolocation': geolocation,
                        'text': text
                    })
        return results

