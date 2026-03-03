from http import client
import tweepy
import urllib
import requests
import json

import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

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
        import tweepy
        CONSUMER_KEY = 'your_consumer_key_here'
        CONSUMER_SECRET = 'your_consumer_secret_here'
        ACCESS_KEY = 'your_access_key_here'
        ACCESS_SECRET = 'your_access_secret_here'
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        tweets = []
        new_tweets = api.user_timeline(screen_name=self.handle, count=200)
        tweets.extend(new_tweets)
        oldest = tweets[-1].id - 1
        while len(new_tweets) > 0:
            new_tweets = api.user_timeline(screen_name=self.handle, count=200, max_id=oldest)
            tweets.extend(new_tweets)
            oldest = tweets[-1].id - 1
        data = []
        for tweet in tweets:
            data.append({'tweet': tweet.text, 'geo': tweet.geo})
        return data

    def template_get_tweets(self):
            try:
                auth = tweepy.OAuthHandler("API_Key", "API_Secret_Key")
                auth.set_access_token("Access_Token", "Access_Token_Secret")
                api = tweepy.API(auth, wait_on_rate_limit=True)
                tweets = api.user_timeline(screen_name=self.handle, count=100, tweet_mode='extended')
                tweet_list = []
                for tweet in tweets:
                    tweet_dict = {}
                    tweet_dict['id'] = str(tweet.id)
                    tweet_dict['geo'] = tweet.geo
                    tweet_dict['tweet'] = tweet.full_text
                    tweet_list.append(tweet_dict)
                return tweet_list
            except Exception as e:
                return []
            
    def question_refinement_get_tweets(self, handle, count=100, api_keys={'consumer_key': 'your_consumer_key_here', 'consumer_secret': 'your_consumer_secret_here', 'access_token': 'your_access_token_here', 'access_token_secret': 'your_access_token_secret_here'}):
        import tweepy
        auth = tweepy.OAuthHandler(api_keys['consumer_key'], api_keys['consumer_secret'])
        auth.set_access_token(api_keys['access_token'], api_keys['access_token_secret'])
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try: user_tweets = api.user_timeline(screen_name=handle, count=count, tweet_mode='extended')
        except tweepy.TweepError as e: raise Exception(f'Tweepy error: {e}')
        return [{'id': tweet.id, 'text': tweet.full_text, 'created_at': tweet.created_at} for tweet in user_tweets]

    def alternative_approaches_get_tweets(self):
            import tweepy
            auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
            auth.set_access_token('access_token', 'access_secret')
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            try:
                tweets = api.user_timeline(screen_name=self.handle, count=200, tweet_mode='extended')
                data = []
                for tweet in tweets:
                    data.append({'tweet': tweet.full_text, 'geo': tweet.geo})
                    if len(data) == 200:
                        break
                return data
            except tweepy.TweepyException as e:
                return []
            
    def context_manager_get_tweets(self):
	    import requests
	    import json
	    headers = {
		    'Authorization': 'Bearer YOUR_TWITTER_API_BEARER_TOKEN'
	    }
	    url = self.base_url
	    response = requests.get(url, headers=headers)
	    if response.status_code == 200:
		    return response.json()['data']
	    else:
		    return []
          
    def flipped_interaction_3__get_tweets(self, count=100):
	    import tweepy
	    consumer_key = 'your-consumer-key'
	    consumer_secret = 'your-consumer-secret'
	    access_token = 'your-access-token'
	    access_token_secret = 'your-access-token-secret'
	    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	    auth.set_access_token(access_token, access_token_secret)
	    api = tweepy.API(auth)
	    tweets = []
	    try:
		    for tweet in tweepy.Cursor(api.user_timeline, screen_name=self.handle, tweet_mode='extended').items(count):
			    tweets.append({'tweet': tweet.full_text, 'geo': tweet.geo})
	    except tweepy.errors.TweepyException as e:
		    raise Exception(e)
	    return tweets

    def flipped_interaction_4__get_tweets(self):
	    url = self.base_url
	    query = {
		    "f": "tweets",
		    "vertical": "recent",
		    "lang": "en",
		    "q": "from:" + self.handle,
	    }
	    headers = {
		    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
		    "Accept": "application/json, text/javascript, */*; q=0.01",
		    "Content-Type": "application/x-www-form-urlencoded"
	    }
	    res = requests.get(url, params=query, headers=headers)
	    if res.status_code == 200:
		    data = res.json()
		    tweets = []
		    for item in data['items_html']:
			    id_str = item.split('data-id=')
                           
    def flipped_iteraction_5__get_tweets(user_id: str, max_tweets: int = 1000):
        if not isinstance(max_tweets, int) or max_tweets <= 0:
            raise ValueError("max_tweets deve essere un intero positivo!")

        tweets = []
        pagination_token = None

        while len(tweets) < max_tweets:
            try:
                response = client.get_users_tweets(
                    id=user_id, 
                    exclude=["replies", "retweets"],
                    start_time="2009-01-01T00:00:00Z",
                    tweet_fields=["id", "text", "geo", "created_at"],
                    expansions=["attachments.poll_ids"],
                    media_fields=["url", "preview_image_url"],
                    place_fields=["name", "country", "full_name"],
                    max_results=min(100, max_tweets - len(tweets)),
                    pagination_token=pagination_token
                )

                if response.data:
                    tweets.extend(response.data)
                    pagination_token = response.meta.get("next_token")  
                else:
                    break

            except tweepy.TooManyRequests:
                print("Too many requests")
            except tweepy.TweepyException as e:
                print(f"Errore API: {e}")
                break

        # Converti i dati in formato leggibile
        tweet_list = [
            {
                "id": tweet.id,
                "text": tweet.text,
                "geo": tweet.geo if tweet.geo else "N/A",
                "created_at": tweet.created_at
            }
            for tweet in tweets
        ]

        return tweet_list

    def iterative_prompting_3__get_tweets(self):
            if not self.handle:
                raise ValueError("Invalid or missing Twitter handle")
            consumer_key = "your_consumer_key"
            consumer_secret = "your_consumer_secret"
            access_token = "your_access_token"
            access_token_secret = "your_access_token_secret"
            if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
                raise Exception("Missing Twitter API credentials")
            try:
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.Client(
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret,
                    wait_on_rate_limit=True
                )
            except tweepy.TweepyException as e:
                raise Exception(f"Failed to authenticate with Twitter API: {e}")
            try:
                tweets = []
                response = api.get_users_tweets(id=self.handle, max_results=100)
                tweets.extend(response.data)
                while 'next_token' in response.meta:
                    response = api.get_users_tweets(
                        id=self.handle, max_results=100, pagination_token=response.meta['next_token']
                    )
                    tweets.extend(response.data)
            except tweepy.TweepyException as e:
                raise Exception(f"Failed to retrieve tweets: {e}")
            return tweets

    def iterative_prompting_4__get_tweets(self):
	    if not isinstance(self.handle, str) or not self.handle.strip():
		    raise ValueError('Invalid handle')
	    try:
		    consumer_key = "your_consumer_key"
		    consumer_secret = "your_consumer_secret"
		    access_key = "your_access_key"
		    access_secret = "your_access_secret"
		    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		    auth.set_access_token(access_key, access_secret)
		    api = tweepy.API(
			    auth,
			    wait_on_rate_limit=True,
			    wait_on_rate_limit_notify=True,
			    retry_count=3,
			    retry_delay=5,
			    imeout=30
		    )
		    tweets = api.user_timeline(
			    screen_name=self.handle,
			    count=100,
			    tweet_mode='extended',
			    include_rts=False
		    )
		    tweet_list = []
		    for tweet in tweets:
			    tweet_data = {}
			    tweet_data['tweet'] = tweet.full_text if tweet.full_text else None
			    tweet_data['geo'] = tweet.geo if tweet.geo else None
			    tweet_list.append(tweet_data)
		    return tweet_list
	    except tweepy.TweepyException as e:
		    raise RuntimeError(f'Failed to retrieve tweets: {e}')
	    except Exception as e:
		    raise RuntimeError(f'An error occurred: {e}')
         
    def iterative_prompting_5__get_tweets(self):
            if not hasattr(self, 'handle') or not self.handle:
                raise ValueError('Twitter handle is required')
            try:
                api = tweepy.Client(bearer_token=self._bearer_token, wait_on_rate_limit=True)
                tweets = api.get_users_tweets(id=self.handle, max_results=200)
            except tweepy.Forbidden as e:
                raise ValueError(f'Invalid or revoked bearer token: {e}')
            except tweepy.TweepyException as e:
                raise ValueError(f'Failed to retrieve tweets: {e}')
            except Exception as e:
                raise ValueError(f'Unexpected error: {e}')
            data = []
            for tweet in tweets.data:
                tweet_json = {'tweet': tweet.text, 'geo': None}
                data.append(tweet_json)
            return data

    def few_shots_prompting_get_tweets(self):
	    url = self.base_url
	    params = {'screen_name': self.handle, 'count': 200}
	    response = requests.get(url, params=params)
	    return response.json()

    def cot_prompting_get_tweets(self):
        tweets = []
        import tweepy
        consumer_key = "YOUR_CONSUMER_KEY"
        consumer_secret = "YOUR_CONSUMER_SECRET"
        access_token = "YOUR_ACCESS_TOKEN"
        access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        new_tweets = api.user_timeline(screen_name=self.handle, count=100)
        
        while len(tweets) < len(new_tweets):
            for tweet in new_tweets:
                tweets.append({'tweet': tweet.text, 'geo': tweet.geo})
            if len(new_tweets) < 100:
                break
            new_tCursor = new_tweets[0].id - 1
            new_tweets = api.user_timeline(screen_name=self.handle, count=100, max_id=new_tCursor)
        
        return tweets

    def fact_check_list_get_tweets(self):
            auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
            auth.set_access_token(self.access_key, self.access_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True)
            tweets = api.user_timeline(screen_name=self.handle, count=200, tweet_mode='extended')
            result = []
            for tweet in tweets:
                result.append({'tweet': tweet.full_text, 'geo': tweet.coordinates})
            return result

    def not_interactive_mix_get_tweets(self):
        auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
        auth.secure = True
        auth.set_access_token('access_token', 'access_token_secret')
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        tweets = []
        try:
            fetched_tweets = tweepy.Cursor(api.user_timeline, screen_name=self.handle, tweet_mode="extended").items(100)
            for tweet in fetched_tweets:
                tweet_dict = tweet._json
                extracted_tweet = {'tweet': tweet_dict['full_text'], 'geo': tweet_dict['geo']}
                tweets.append(extracted_tweet)
        except tweepy.TweepError as e:
            print(f"An error occurred: {e}")
        return tweets

    import tweepy
    def interactive_mix_get_tweets(self, handle, count=100, since_id=None, max_id=None, since_date=None, lang='en', geolocation=True, filter_retweets=True):
        try:
            if not hasattr(self, 'api'):
                auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
                auth.set_access_token(self.access_token, self.access_token_secret)
                self.api = tweepy.API(auth, wait_on_rate_limit=True)
            query = f'from:{handle}'
            if since_date:
                query += f' since:{since_date}'
            if lang:
                query += f' lang:{lang}'
            if filter_retweets:
                query +='-filter:retweets'
            tweet_params = {
                'q': query,
                'count': count,
               'since_id': since_id,
               'max_id': max_id,
                'tweet_mode': 'extended'
            }
            if geolocation:
                tweet_params['geocode'] = '37.7749,-122.4194,100km'
            tweets = tweepy.Cursor(self.api.search_tweets, tweet_params).items(count)
            tweet_list = []
            for tweet in tweets:
                tweet_list.append(tweet._json)
            return tweet_list
        except tweepy.TweepError as e:
            print(e)
            return None
        
    def baseline_get_tweets(self):
        consumer_key = 'your-consumer-key'
        consumer_secret = 'your-consumer-secret'
        access_token = 'your-access-token'
        access_token_secret = 'your-access-token-secret'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        tweets = []
        public_tweets = api.user_timeline(screen_name = self.handle, count = 100)
        for tweet in public_tweets:
            tweets.append({ 'geo': tweet.geo, 'tweet': tweet.text })
        return tweets
