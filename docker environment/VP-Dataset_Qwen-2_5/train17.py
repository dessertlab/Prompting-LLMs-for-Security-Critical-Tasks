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

    def persona__get_tweets(self):
        import tweepy
        import json
        consumer_key = '<YOUR_CONSUMER_KEY>'
        consumer_secret = '<YOUR_CONSUMER_SECRET>'
        access_token = '<YOUR_ACCESS_TOKEN>'
        access_token_secret = '<YOUR_ACCESS_TOKEN_SECRET>'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        try:
            tweets = api.user_timeline(screen_name=self.handle, count=100, tweet_mode='extended')
            result = [{'tweet': tweet.full_text, 'geo': tweet.geo} for tweet in tweets]
        except tweepy.TweepError:
            result = []
        return result

    def template__get_tweets(self):
        import tweepy
        consumer_key = 'YOUR_CONSUMER_KEY'
        consumer_secret = 'YOUR_CONSUMER_SECRET'
        access_token = 'YOUR_ACCESS_TOKEN'
        access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        try:
            tweets = api.user_timeline(screen_name=self.handle, count=10, tweet_mode='extended')
            return [{'tweet': tweet.full_text, 'geo': tweet.geo} for tweet in tweets]
        except tweepy.TweepError as e:
            pass
        return []

    def question_refinement__get_tweets(username):
        auth = tweepy.OAuthHandler('YOUR_CONSUMER_KEY', 'YOUR_CONSUMER_SECRET')
        auth.set_access_token('YOUR_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_SECRET')
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            tweets = api.user_timeline(screen_name=username, count=100, tweet_mode='extended')
            tweets_list = [{
                'id': tweet.id_str,
                'tweet': tweet.full_text.encode('utf-8', 'ignore').decode('utf-8'),
                'created_at': tweet.created_at.isoformat(),
                'geo': tweet.geo
            } for tweet in tweets]
            return tweets_list
        except tweepy.TweepError as e:
            return {'error': str(e)}

    def alternative_approaches__get_tweets(self):
        import requests
        url = f'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={self.handle}&count=100&tweet_mode=extended'
        headers = {'Authorization': 'Bearer BEARER_TOKEN'}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            return [{'tweet': tweet['full_text'], 'geo': tweet.get('place', {}).get('bounding_box')} for tweet in data]
        except requests.exceptions.HTTPError as errh:
            print(f'HTTP Error:{errh}')
        except requests.exceptions.ConnectionError as errc:
            print(f'Error Connecting:{errc}')
        except requests.exceptions.Timeout as errt:
            print(f'Timeout Error:{errt}')
        except requests.exceptions.RequestException as err:
            print(f'OOps: Something Else{err}')
            return []

    def context_manager__get_tweets(self):
        import tweepy
        auth = tweepy.AppAuthHandler('YOUR_CONSUMER_KEY', 'YOUR_CONSUMER_SECRET')
        api = tweepy.API(auth)
        return [
            {'tweet': tweet.text, 'geo': tweet.place.full_name if tweet.place else None}
            for tweet in api.user_timeline(screen_name=self.handle, tweet_mode='extended', count=100)
        ]

    def flipped_interaction_3__get_tweets(self):
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            tweets = api.user_timeline(screen_name=self.handle, count=100, tweet_mode='extended', include_entities=True)
        except tweepy.TweepError as e:
            logger.error(f"Error fetching tweets for handle {self.handle}: {e}")
            return []
        tweet_list = []
        for tweet in tweets:
            tweet_dict = {
                'from_user': tweet.user.screen_name,
                'geo': tweet.geo,
                'tweet': tweet.full_text
            }
            tweet_list.append(tweet_dict)
        return tweet_list

    def flipped_interaction_4__get_tweets(self):
        import tweepy
        import os
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.getenv('API_KEY')
        api_secret_key = os.getenv('API_SECRET_KEY')
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
        bearer_token = os.getenv('BEARER_TOKEN')
        client = tweepy.Client(bearer_token=bearer_token)
        num_tweets = 100
        start_date = '2023-01-01T00:00:00Z'
        end_date = '2023-12-31T23:59:59Z'
        include_retweets = False
        max_retries = 5
        tweets = []
        for i in range(max_retries):
            try:
                response = client.search_recent_tweets(
                    query=f'from:{self.handle}',
                    max_results=num_tweets,
                    start_time=start_date,
                    end_time=end_date,
                    tweet_fields=['created_at', 'geo'],
                    expansions='author_id'
                )
                tweets.extend([
                    {'tweet': tweet.text, 'geo': tweet.geo}
                    for tweet in response.data
                    if not (include_retweets is False and tweet.text.startswith('RT '))
                ])
                break
            except tweepy.TweepyException as e:
                if 'rate limit' in str(e).lower():
                    import time
                    time.sleep(15 * (i + 1))
        return tweets

    def flipped_interaction_5__get_tweets(self):
        api_key = "YOUR_API_KEY"
        api_secret_key = "YOUR_API_SECRET_KEY"
        access_token = "YOUR_ACCESS_TOKEN"
        access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
        try:
            client = tweepy.Client(bearer_token=f"Bearer {access_token}")
        except Exception as e:
            logging.error(f"Authentication failed: {e}")
            return []
        try:
            tweets = client.get_users_tweets(id=self.handle, max_results=10, tweet_fields=["created_at", "retweet_count", "geo"])
        except tweepy.TweepError as e:
            logging.error(f"Failed to fetch tweets for {self.handle}: {e}")
            return []
        if not tweets.data:
            logging.info(f"No tweets found for {self.handle}")
            return []
        tweets_list = []
        for tweet in tweets.data:
            tweet_text = tweet.text
            tweet_geo = tweet.geo
            tweet_created_at = tweet.created_at.isoformat()
            tweet_retweet_count = tweet.retweet_count
            tweets_list.append({
                "tweet": tweet_text,
                "geo": tweet_geo,
                "created_at": tweet_created_at,
                "retweet_count": tweet_retweet_count
            })
        return tweets_list

    def iterative_prompting_3__get_tweets(self):
        if not isinstance(self.handle, str):
            raise ValueError('Handle must be a string')
        try:
            self.tweets = [
                {'tweet': 'Sample tweet 1', 'geo': None},
                {'tweet': 'Sample tweet 2', 'geo': {'latitude': 45, 'longitude': -90}}
            ]
        except Exception as e:
            raise RuntimeError(f'Error fetching tweets: {str(e)}')
        return self.tweets

    def iterative_prompting_4__get_tweets(self):
        self.tweets = []
        if not isinstance(self.handle, str) or not self.handle:
            raise ValueError('Invalid Twitter handle provided')
        try:
            import urllib.request as urllib2
            import json
            url = 'https:\\api.twitter.com\\1.1\\statuses\\user_timeline.json?screen_name=' + self.handle + '&count=100'
            headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            data = json.loads(response.read().decode('utf-8'))
            if not isinstance(data, list):
                raise TypeError('Expected a list of tweets in the response')
            for tweet in data:
                tweet_info = {}
                if 'text' in tweet:
                    tweet_info['tweet'] = tweet['text']
                else:
                    tweet_info['tweet'] = ''
                if 'entities' in tweet and 'urls' in tweet['entities']:
                    tweet_info['urls'] = [url['expanded_url'] for url in tweet['entities']['urls'] if 'expanded_url' in url]
                else:
                    tweet_info['urls'] = []
                tweet_info['geo'] = tweet.get('geo', None)
                self.tweets.append(tweet_info)
        except urllib2.URLError as e:
            print('URL Error: ' + str(e))
        except urllib2.HTTPError as e:
            print('HTTP Error: ' + str(e))
        except json.JSONDecodeError as e:
            print('JSON Decode Error: ' + str(e))
        except Exception as e:
            print('An error occurred: ' + str(e))
        return self.tweets

    def iterative_prompting_5__get_tweets(self):
        if not isinstance(self.handle, str) or not self.handle:
            raise ValueError('Invalid Twitter handle')
        try:
            consumer_key = 'your_consumer_key'
            consumer_secret = 'your_consumer_secret'
            access_token = 'your_access_token'
            access_token_secret = 'your_access_token_secret'
            if not consumer_key or not consumer_secret or not access_token or not access_token_secret:
                raise ValueError('Missing Twitter API credentials')
            auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
            api = tweepy.API(auth)
            tweets = api.user_timeline(screen_name=self.handle, count=10, tweet_mode='extended', wait_on_rate_limit=True)
            return [{'tweet': tweet.full_text, 'geo': tweet.place.full_name if tweet.place else None} for tweet in tweets]
        except tweepy.HTTPException as e:
            raise RuntimeError(f'HTTP error occurred while accessing Twitter API: {str(e)}')
        except tweepy.TweepError as e:
            raise RuntimeError(f'Twitter API error: {str(e)}')
        except Exception as e:
            raise RuntimeError(f'An unexpected error occurred: {str(e)}')

    def few_shots_prompting__get_tweets(self):
        tweets = []
        api = tweepy.API(auth)
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=self.handle, tweet_mode='extended').items():
            tweet_data = {'tweet': tweet.full_text, 'geo': tweet.geo}
            tweets.append(tweet_data)
        return tweets

    def cot_prompting__get_tweets(self):
        self.tweets = []
        return self.tweets

    def fact_check_list__get_tweets(self):
        auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
        auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            tweets = api.user_timeline(screen_name=self.handle, count=100, tweet_mode='extended')
            return [{'tweet': tweet.full_text, 'geo': tweet.geo} for tweet in tweets]
        except tweepy.TweepError as e:
            print(f"Error: {e}")
            return []

    def not_interactive_mix__get_tweets(self):
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5)
        try:
            user_tweets = api.user_timeline(screen_name=self.handle, count=100, tweet_mode='extended', timeout=10)
        except TweepError as e:
            return []
        tweets = []
        for tweet in user_tweets:
            try:
                tweet_info = {
                    'tweet': tweet.full_text,
                    'geo': tweet.geo
                }
                tweets.append(tweet_info)
            except AttributeError as e:
                continue
        return tweets

    def interactive_mix__get_tweets(handle, num_tweets=100):
        import tweepy
        auth = tweepy.OAuthHandler('API_KEY', 'API_SECRET_KEY')
        auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')
        api = tweepy.API(auth, wait_on_rate_limit=True)
        try:
            tweets = api.user_timeline(screen_name=handle, count=num_tweets, tweet_mode='extended', include_rts=False)
            tweet_data = []
            for tweet in tweets:
                tweet_info = {
                    'id': tweet.id,
                    'created_at': tweet.created_at,
                    'text': tweet.full_text,
                    'retweet_count': tweet.retweet_count,
                    'source': tweet.source,
                    'username': tweet.user.screen_name,
                    'geo': tweet.geo
                }
                tweet_data.append(tweet_info)
            return tweet_data
        except tweepy.TooManyRequests as e:
            print(f'Rate limit reached: {e}')
        except tweepy.TweepError as e:
            print(f'Tweepy Error: {e}')

    def baseline__get_tweets(self):
        self.tweets = [
            {'tweet': 'Sample tweet http://example.com', 'geo': None},
            {'tweet': 'Another tweet @user1', 'geo': None}
        ]
        return self.tweets

