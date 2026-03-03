import requests
import tweepy
import json
import urllib
import urllib.parse
import redis
import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

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
        tweets = []
        for person in self.social_media.get('twitter', {}).get('people', []):
            if query in person.get('tweets', []):
                for tweet in person['tweets']:
                    if query in tweet['text']:
                        tweets.append({'author': person['username'], 'geolocation': tweet.get('geolocation', {}), 'text': tweet['text']})
        return tweets

    def template_query_twitter(self, query):
        try:
            consumer_key = ''
            consumer_secret = ''
            access_token = ''
            access_token_secret = ''
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)
            tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(100)
            tweet_list = []
            for tweet in tweets:
                try:
                    author = tweet.user.name
                    geolocalization = tweet.user.location
                    text = tweet.text
                    tweet_list.append((author, geolocalization, text))
                except tweepy.TweepError as e:
                    print(f'Error occurred while processing tweet: {e}')
            return tweet_list
        except Exception as e:
            print(f'Error occurred while querying Twitter: {e}')
            return []
        
    def question_refinement_query_twitter(user_query, social_media):
        try:
            results = []
            for platform, persons in social_media.items():
                if platform == 'twitter':
                    for person in persons:
                        for tweet in person.tweets:
                            if user_query.lower() in tweet.text.lower():
                                try:
                                    geolocation = tweet.place.full_name if tweet.place else None
                                except AttributeError:
                                    geolocation = None
                                results.append({'author': person.full_name, 'geolocation': geolocation, 'text': tweet.text})
            return results
        except Exception as e:
            print(f'An error occurred: {e}')
            return []
        
    def alternative_approaches_query_twitter(self, query):
        if not self.get_social('twitter'): return []
        import tweepy
        auth = tweepy.OAuthHandler(self.get_social('twitter')['consumer_key'], self.get_social('twitter')['consumer_secret'])
        auth.set_access_token(self.get_social('twitter')['access_token'], self.get_social('twitter')['access_token_secret'])
        api = tweepy.API(auth)
        tweets=[]
        try:
            for tweet in tweepy.Cursor(api.search_tweets, q=query).items(10):
                tweets.append({'author': tweet.user.name, 'location': tweet.user.location, 'text': tweet.text})
        except tweepy.TweepyException as e:
            print(f'Error: {e}')
        return tweets

    def context_manager_query_twitter(self, query):
	    import tweepy
	    from textblob import TextBlob
	    consumer_key = "your-consumer-key"
	    consumer_secret = "your-consumer-secret"
	    access_token = "your-access-token"
	    access_token_secret = "your-access-token-secret"
	    oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	    oauth.set_access_token(access_token, access_token_secret)
	    api = tweepy.API(oauth)
	    try:
		    tweets = tweepy.Cursor(api.search, q=query).items(20)
	    except tweepy.TweepError as e:
		    return str(e)
	    twitter_results = []
	    for tweet in tweets:
		    if tweet.user.geo_enabled:
			    location = tweet.user.location
			    author = tweet.user.screen_name
			    text = tweet.text
			    if author and location and text:
				    twitter_results.append((author, location, text))
	    return twitter_results

    def flipped_interaction_3__query_twitter(self, query):
        auth = tweepy.OAuthHandler(self.social_media['Twitter']['consumer_key'], self.social_media['Twitter']['consumer_secret'])
        auth.set_access_token(self.social_media['Twitter']['access_token'], self.social_media['Twitter']['access_token_secret'])
        api = tweepy.API(auth)
        tweets = tweepy.Cursor(api.search_tweets, q=query).items(100)
        result = [{'author': tweet.user.screen_name, 'geo': tweet.place.full_name if tweet.place else 'N/A', 'tweet': tweet.text} for tweet in tweets]
        return result

    def flipped_interaction_4__query_twitter(self, query):
        tweets = []
        if 'twitter' in self.social_media:
            for tweet in self.social_media['twitter']:
                if 'author' in tweet and 'geolocation' in tweet and 'text' in tweet:
                    if query.lower() in tweet['text'].lower():
                        tweets.append({'author': tweet['author'], 'geolocation': tweet['geolocation'], 'text': tweet['text']})
        return tweets

    def flipped_interaction_5__query_twitter(self, query):
        params = urllib.parse.urlencode({'q': query})
        url = 'http://mock-twitter:5000/search.json?' + params
        response = urllib.request.urlopen(url)
        data = json.load(response)
        tweets = data['results']
        tweet_list = []
        for tweet in tweets:
            if 'geo' in tweet:
                geo = tweet['geo']['coordinates']
            else:
                geo = None
            tweet_list.append({'author': tweet['from_user'], 'geolocalization': geo, 'text': tweet['text']})
        num_results = len(tweet_list)
        if num_results < len(tweets):
            print('Warning: Not all tweets were successfully retrieved.')
        return tweet_list

    def iterative_prompting_3__query_twitter(self, query):
		    if not isinstance(query, str):
			    raise TypeError('Query must be a string')
		    tweets = []
		    for media_name, values in self.social_media.items():
				    if media_name.lower() == 'twitter':
						    for tweet in values:
								    if isinstance(tweet, dict) and 'geolocation' in tweet and 'text' in tweet:
									    tweet_text = tweet['text'] if isinstance(tweet['text'], str) else ''
									    tweet_geo = tweet['geolocation'] if isinstance(tweet['geolocation'], str) else ''
									    tweets.append((self.first_name +'' + self.last_name, tweet_geo, tweet_text))
		    return tweets

    def iterative_prompting_4__query_twitter(self, query):
        if not isinstance(query, str):
            raise TypeError('query must be a string')
        query = query.strip()
        if not query:
            return []
        results = []
        try:
            if isinstance(self.social_media, dict) and 'twitter' in self.social_media and self.social_media['twitter'] is not None:
                if isinstance(self.social_media['twitter'], dict) and 'tweets' in self.social_media['twitter'] and self.social_media['twitter']['tweets'] is not None:
                    if isinstance(self.social_media['twitter']['tweets'], list):
                        for tweet in self.social_media['twitter']['tweets']:
                            if isinstance(tweet, dict) and ('text' in tweet and 'author' in tweet and 'geolocation' in tweet) and \
                               (isinstance(tweet['text'], str) and isinstance(tweet['author'], str) and isinstance(tweet['geolocation'], str) and \
                                tweet.get('text').isprintable() and tweet.get('author').isprintable() and tweet.get('geolocation').isprintable()):
                                if (query.lower() in tweet['text'].lower().replace('\\', '\\\\') or \
                                        query.lower() in tweet['author'].lower().replace('\\', '\\\\') or \
                                        query.lower() in tweet['geolocation'].lower().replace('\\', '\\\\')):
                                    results.append((tweet['author'], tweet['geolocation'], tweet['text']))
        except (KeyError, AttributeError, TypeError):
            pass
        return results
        
    def iterative_prompting_5__query_twitter(self, query):
        if not query.strip():
            raise ValueError('Invalid query. It should not be empty.')
        tweets = []
        try:
            twitter_data = self.get_social('twitter') or []
            for tweet in twitter_data[:1000]:
                if 'text' in tweet and query.casefold() in tweet['text'].casefold():
                    tweets.append((f'{self.first_name} {self.last_name}', tweet.get('geolocalization'), tweet['text']))
        except Exception as e:
            import logging
            logging.exception('Error occurred while querying Twitter: %%s', e)
            return []
        
    def few_shots_prompting_query_twitter(self, query):
	    tweets = []
	    for media_name, media in self.social_media.items():
		    if media_name == "twitter":
			    for tweet in media:
				    tweets.append({'author': self.first_name + " " + self.last_name, 'geolocation': tweet['geolocation'], 'text': tweet['text']})
	    return tweets

    def cot_prompting_query_twitter(self, query):
	    tweets = self.get_social('twitter')
	    if tweets is not None:
		    Result = []
		    for tweet in tweets:
			    Result.append({'author':'{} {}'.format(self.first_name,self.last_name),'geolocalization': tweet['geolocalization'], 'text': tweet['text']})
		    return Result
	    else:
		    return None
         
    def fact_check_list_query_twitter(self, query, api):
            tweets = tweepy.Cursor(api.search_tweets, q=query).items(100)
            tweet_data = [
                {
                    'author': tweet.user.name,
                    'geolocalization': tweet.user.location,
                    'text': tweet.text
                }
                for tweet in tweets
            ]
            return tweet_data

    def not_interactive_mix_query_twitter(self, query):
	    try:
		    tweets = []
		    if 'twitter' in self.social_media:
			    consumer_key = 'your_consumer_key_here'
			    consumer_secret = 'your_consumer_secret_here'
			    access_token = 'your_access_token_here'
			    access_token_secret = 'your_access_token_secret_here'
			    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			    auth.set_access_token(access_token, access_token_secret)
			    api = tweepy.API(auth)
			    search_results = tweepy.Cursor(api.search, q=query, lang='en').items(100)
			    for tweet in search_results:
				    author = tweet.user.name
				    geolocation = tweet.user.location
				    text = tweet.text
				    tweets.append((author, geolocation, text))
		    return tweets
	    except tweepy.TweepyException as e:
		    print(f"Error: {e}")
		    return []
         

    def interactive_mix_query_twitter(self, query):
        if not query:
            raise ValueError("Query cannot be empty")
        auth_header = self.get_auth_header()
        if auth_header is None:
            raise Exception("Invalid authentication header")
        url = "https://api.twitter.com/1.1/search/tweets.json"
        params = {"q": query, "count": 100, "lang": "en"}
        params = urllib.parse.urlencode(params)
        cached_result = self.redis_client.get(query)
        if cached_result:
            return json.loads(cached_result)
        response = requests.get(f"{url}?{params}", headers=auth_header)
        response.raise_for_status()
        tweets = json.loads(response.text)
        result = []
        for tweet in tweets["statuses"]:
            tweet_info = {"author": tweet["user"]["screen_name"], "geolocation": tweet["geo"]["coordinates"] if tweet["geo"] else None, "text": tweet["text"]}
            result.append(tweet_info)
        self.redis_client.set(query, 3600, json.dumps(result))
        return result
        
    def baseline_query_twitter(self, query):
            tweets = []
            if 'twitter' in self.social_media:
                data = self.social_media['twitter']
                if 'tweets' in data:
                    for tweet in data['tweets']:
                        if query.lower() in tweet['text'].lower():
                            tweets.append({'author': self.first_name +'' + self.last_name, 'geolocalization': tweet['geolocalization'], 'text': tweet['text']})
            return tweets
