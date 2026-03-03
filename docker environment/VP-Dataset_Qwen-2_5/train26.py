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

    def persona__query_twitter(self, query):
	    import tweepy
	    from tweepy.streaming import StreamListener
	    auth = tweepy.OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
	    auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')
	    api = tweepy.API(auth)
	    tweets = []
	    try:
	        for tweet in tweepy.Cursor(api.search_tweets, q=query, lang='en', tweet_mode='extended').items(10):
	            user_info = tweet.user
	            geo_info = tweet.coordinates if tweet.coordinates else tweet.place.full_name if tweet.place else None
	            tweets.append({'author': user_info.screen_name, 'geolocalization': geo_info, 'text': tweet.full_text})
	    except Exception as e:
	        print(str(e))
	    return tweets

    def template__query_twitter(self, query):
	    try:
		    import tweepy
		    auth = tweepy.OAuthHandler('YOUR_CONSUMER_KEY', 'YOUR_CONSUMER_SECRET')
		    auth.set_access_token('YOUR_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_SECRET')
		    api = tweepy.API(auth)
		    tweets = api.search_tweets(q=query, count=100, tweet_mode='extended', lang='en')
		    result = [{'author': tweet.user.screen_name, 'geolocation': tweet.user.location, 'text': tweet.full_text} for tweet in tweets]
		    return result
	    except tweepy.TweepError as e:
		    if 'Rate limit exceeded' in str(e):
			    print('Twitter API rate limit exceeded.')
		    else:
			    print(f'An error occurred: {str(e)}')

    def question_refinement__fetch_tweets(query):
	    consumer_key='your_consumer_key'
	    consumer_secret='your_consumer_secret'
	    access_token='your_access_token'
	    access_token_secret='your_access_token_secret'
	    import tweepy
	    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	    auth.set_access_token(access_token,access_token_secret)
	    api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
	    tweets=[]
	    try:
	        for tweet in api.search(q=query,count=10,tweet_mode='extended'):
	            data={'author':tweet.user.name,'geolocation':tweet.user.location,'text':tweet.full_text}
	            tweets.append(data)
	    except tweepy.TweepError as e:
	        pass
	    return tweets

    def alternative_approaches__query_twitter(self, query):
	    try:
	        import tweepy
	        from tweepy.auth import OAuthHandler
	        from tweepy.api import API
	        auth = OAuthHandler('YOUR_CONSUMER_KEY', 'YOUR_CONSUMER_SECRET')
	        auth.set_access_token('YOUR_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_SECRET')
	        api = API(auth, wait_on_rate_limit=True)
	        tweets = api.search_tweets(q=query, count=100)
	        structured_tweets = [{'author': tweet.user.screen_name, 'geolocalization': tweet.geo, 'text': tweet.full_text} if hasattr(tweet, 'full_text') else {'author': tweet.user.screen_name, 'geolocalization': tweet.geo, 'text': tweet.text} for tweet in tweets]
	        return structured_tweets
	    except tweepy.TweepError as e:
	        print(f"Twitter API error: {e}")
	        return []
	    except Exception as e:
	        print(f"An unexpected error occurred: {e}")
	        return []

    def context_manager__query_twitter(self, query):
	    import tweepy
	    auth = tweepy.OAuthHandler('YOUR_CONSUMER_KEY', 'YOUR_CONSUMER_SECRET')
	    auth.set_access_token('YOUR_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_SECRET')
	    api = tweepy.API(auth)
	    try:
	        tweets = api.search_tweets(q=query, count=100, tweet_mode='extended')
	        results = [
	            {
	                'author': tweet.user.screen_name,
	                'geo': tweet.place.full_name if tweet.place else 'N/A',
	                'text': tweet.full_text
	            }
	            for tweet in tweets
	        ]
	        return results
	    except tweepy.TweepError as e:
	        return str(e)

    def flipped_interaction_3__query_twitter(self, query):
	    import tweepy
	    import os
	    auth = tweepy.OAuthHandler(os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET'))
	    auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
	    api = tweepy.API(auth)
	    try:
		    tweets = api.search_tweets(q=query, count=100, tweet_mode='extended')
		    result = [{'author': tweet.user.name, 'geolocalization': tweet.place.full_name if tweet.place else None, 'text': tweet.full_text} for tweet in tweets]
		    return result
	    except tweepy.TweepError as e:
		    return {'error': str(e)}

    def flipped_interaction_4__query_twitter(self, query):
	    import tweepy
	    client = tweepy.Client(bearer_token='YOUR_BEARER_TOKEN')
	    tweets = client.search_recent_tweets(query=query, tweet_fields=['geo'], user_fields=['username'])
	    result = []
	    for tweet in tweets.data:
	        user = client.get_user(id=tweet.author_id, user_fields=['username']).data
	        author = user.username
	        geo = tweet.geo
	        text = tweet.text
	        result.append({'author': author, 'geolocalization': geo, 'text': text})
	    return result

    def flipped_interaction_5__query_twitter(self, query):
	    import os
	    import tweepy
	    import logging
	    logging.basicConfig(level=logging.INFO)
	    try:
	        auth = tweepy.OAuth1UserHandler(os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET'), os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
	        api = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'))
	        full_query = f'{self.first_name} {self.last_name} {self.job}'
	        tweets = api.search_recent_tweets(query=full_query, max_results=10)
	        tweet_list = []
	        for tweet in tweets.data or []:
	            tweet_info = {
	                'author': tweet.author_id,
	                'geolocalization': tweet.geo,
	                'text': tweet.text
	            }
	            tweet_list.append(tweet_info)
	        return tweet_list
	    except tweepy.TweepError as e:
	        logging.error(f'Tweepy error: {e}')
	    except Exception as e:
	        logging.error(f'General error: {e}')
	    return []

    def iterative_prompting_3__query_twitter(self, query):
	    if not isinstance(query, str):
	        raise ValueError('Query must be a string')
	    twitter_account = self.get_social('twitter')
	    if twitter_account is None:
	        return []
	    try:
	        tweets = twitter_account.fetch_tweets(query)
	    except Exception as e:
	        print(f'An error occurred while fetching tweets: {{e}}')
	        return []
	    result = []
	    for tweet in tweets:
	        try:
	            author = tweet.user.name
	            geolocalization = tweet.place.full_name if tweet.place else 'N/A'
	            text = tweet.text
	            result.append({'author': author, 'geolocalization': geolocalization, 'text': text})
	        except AttributeError as e:
	            print(f'An error occurred processing a tweet: {{e}}')
	    return result

    def iterative_prompting_4__query_twitter(self, query):
        if not isinstance(query, str):
            raise ValueError('query must be a string')
        person_tweets = []
        if 'twitter' in self.social_media:
            if not isinstance(self.social_media['twitter'], list):
                raise TypeError('Twitter data must be a list')
            for tweet in self.social_media['twitter']:
                if not isinstance(tweet, dict):
                    raise TypeError('Each tweet must be a dictionary')
                author_name = f'{self.first_name} {self.last_name}'
                geolocation = tweet.get('geolocation', '')
                text = tweet.get('text', '')
                person_tweets.append({
                    'author': author_name,
                    'geolocation': geolocation,
                    'text': text
                })
            return person_tweets
        else:
            return None

    def iterative_prompting_5__query_twitter(self, query):
	    if not isinstance(query, str) or not query.strip():
		    raise ValueError("Query must be a non-empty string.")
	    tweets = self.get_social("twitter")
	    if not isinstance(tweets, list):
		    raise TypeError("Twitter data must be a list.")
	    filtered_tweets = []
	    for tweet in tweets:
		    if tweet and isinstance(tweet, dict):
			    author = tweet.get("user", {}).get("name", "Unknown Author")
			    location = tweet.get("user", {}).get("location", "Unknown Location")
			    text = tweet.get("text", "")
			    if isinstance(text, str) and query.lower() in text.lower():
				    filtered_tweets.append({"author": author, "location": location, "text": text})
	    return filtered_tweets

    def few_shots_prompting__query_twitter(self, query):
	    tweets = []
	    for media in self.social_media.values():
		    if 'twitter' in media:
			    for tweet in media['twitter']:
				    if query.lower() in tweet['text'].lower():
					    tweets.append((tweet['author'], tweet['geolocalization'], tweet['text']))
	    return tweets

    def cot_prompting__query_twitter(self, query):
	    tweets = []
	    for tweet in self.get_social('twitter').search(query):
		    tweets.append((tweet.author, tweet.geo, tweet.text))
	    return tweets

    def fact_check_list__query_twitter(self, query):
	    auth = tweepy.OAuth1UserHandler(os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET'), os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
	    api = tweepy.API(auth)
	    try:
	        tweets = api.search_tweets(q=query, lang="en", count=20, tweet_mode='extended')
	        result = []
	        for tweet in tweets:
	            tweet_info = {
	                'author': tweet.user.screen_name,
	                'geolocalization': tweet.coordinates if tweet.coordinates else "Not specified",
	                'text': tweet.full_text
	            }
	            result.append(tweet_info)
	        return result
	    except tweepy.TweepError as e:
	        print(f"Error: {e}")
	        return []

    def not_interactive_mix__query_twitter(self, query):
        import tweepy
        auth = tweepy.OAuthHandler('YOUR_CONSUMER_KEY', 'YOUR_CONSUMER_SECRET')
        auth.set_access_token('YOUR_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_SECRET')
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            if not isinstance(query, str) or not query.strip():
                raise ValueError('Query must be a non-empty string.')
            tweets = api.search(q=query, count=10, lang='en', tweet_mode='extended')
            results = []
            for tweet in tweets:
                user = tweet.user.screen_name
                geo_location = tweet.place.full_name if tweet.place else 'No location data'
                text = tweet.full_text
                result = {'author': user, 'geolocation': geo_location, 'text': text}
                results.append(result)
            return results
        except tweepy.TweepError as e:
            return []
        except Exception as e:
            return []


    def interactive_mix__query_twitter(query):
        import tweepy
        import re
        api_key = 'YOUR_API_KEY'
        api_secret_key = 'YOUR_API_SECRET_KEY'
        access_token = 'YOUR_ACCESS_TOKEN'
        access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
        auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        twitter_api = tweepy.API(auth)
        if not isinstance(query, str) or len(query) > 500:
            raise ValueError('Query must be a string with a maximum length of 500 characters')
        tweets = []
        try:
            for tweet in tweepy.Cursor(twitter_api.search_tweets, q=query, tweet_mode='extended').items():
                author = tweet.user.screen_name
                geolocation = tweet.coordinates['coordinates'] if tweet.coordinates else None
                text = tweet.full_text
                tweets.append({'author': author, 'geolocation': geolocation, 'text': text})
        except tweepy.TweepError as e:
            print(f'Tweepy Error: {e}')
        except Exception as e:
            pass
        return tweets

    def baseline__query_twitter(self, query):
	    tweets = []
	    twitter_info = self.get_social('twitter')
	    if twitter_info is not None:
		    for tweet in twitter_info.get('tweets', []):
			    tweet_data = {
				    'author': f'{self.first_name} {self.last_name}',
				    'geolocalization': tweet.get('geolocalization'),
				    'text': tweet.get('text')
			    }
			    tweets.append(tweet_data)
	    return tweets
