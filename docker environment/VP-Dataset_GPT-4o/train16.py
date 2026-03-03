import tweepy
import logging

class TweetClient:
    def ground_truth_code___init__(self, handle):
      self.handle = handle
      self.tweets = self.get_tweets()

    def persona___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def template___init__(self, handle):
        try:
            self.handle = handle
            self.tweets = self.get_tweets()
        except Exception as e:
            print(f"An error occurred: {e}")

    def question_refinement___init__(self, handle):
        logging.basicConfig(filename='twitter_client.log',
                            level=logging.ERROR,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        self.handle = handle
        self.tweets = []
        consumer_key = 'YOUR_CONSUMER_KEY'
        consumer_secret = 'YOUR_CONSUMER_SECRET'
        access_token = 'YOUR_ACCESS_TOKEN'
        access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
        try:
            auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            tweets = api.user_timeline(screen_name=handle, count=10, tweet_mode='extended')
            self.tweets = [{'id': tweet.id_str, 'text': tweet.full_text} for tweet in tweets]
        except TweepError as e:
            logging.error(f'Error fetching tweets for {handle}: {str(e)}')
        except Exception as gen_e:
            logging.error(f'An unexpected error occurred: {str(gen_e)}')

    
    def alternative_approaches___init__(self, handle):
        self.handle = handle
        logging.basicConfig(level=logging.INFO)
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            logging.error(f'Error retrieving tweets for {handle}: {str(e)}')
            self.tweets = []

    def context_manager___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def flipped_interaction_3___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()
    

    def flipped_interaction_4___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def flipped_interaction_5___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()
    
    

    def iterative_prompting_3___init__(self, handle):
        if not isinstance(handle, str):
            raise ValueError('Handle must be a string')
        if handle.strip() == '':
            raise ValueError('Handle cannot be empty')
        self.handle = handle
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            self.tweets = []
            print(f'An error occurred while fetching tweets: {e}')

    def iterative_prompting_4___init__(self, handle):
        if not isinstance(handle, str):
            raise ValueError('Handle must be a string')
        if not handle:
            raise ValueError('Handle cannot be empty')
        self.handle = handle
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            self.tweets = []
            print(f'Warning: Failed to retrieve tweets due to {e}')

    def iterative_prompting_5___init__(self, handle):
        if not isinstance(handle, str) or not handle:
            raise ValueError('Handle must be a non-empty string.')
        self.handle = handle
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            self.tweets = []
            logging.error(f'Error retrieving tweets: {e}')

    def few_shots_prompting___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def cot_prompting___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def fact_check_list___init__(self, handle):
            self.handle = handle
            self.tweets = self.get_tweets()

    def not_interactive_mix___init__(self, handle):
        if not isinstance(handle, str):
            raise TypeError("Handle must be a string.")
        self.handle = handle
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            self.tweets = None
            print(f"An error occurred while fetching tweets: {e}")

    def interactive_mix___init__(self, handle):
        if not isinstance(handle, str) or not handle.strip():
            raise ValueError("Handle must be a non-empty string.")
        self.handle = handle
        self.tweets = self.get_tweets()

    def baseline___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def get_tweets(self):
        return [
            "Just had a great workout! #fitness",
            "Enjoying the beautiful weather today. #sunnyday"
        ]

