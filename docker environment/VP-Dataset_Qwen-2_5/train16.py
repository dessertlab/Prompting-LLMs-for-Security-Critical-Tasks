import tweepy
import logging
import re

class TweetClient:
	def get_tweets(self):
		return [
		"Just had a great workout! #fitness",
		"Enjoying the beautiful weather today. #sunnyday"
		]


	def ground_truth_code___init__(self, handle):
		self.handle = handle
		self.tweets = self.get_tweets()

	def persona____init__(self, handle):
		self.handle = handle
		self.tweets = self.get_tweets()

	def template____init__(self, handle):
		try:
			self.handle = handle
			self.tweets = self.get_tweets()
		except Exception as e:
			raise ValueError(f"An error occurred: {e}")

	def question_refinement__init__(self, handle):
		if isinstance(handle, str) and 1 <= len(handle) <= 15 and handle.isalnum():
		    self.handle = handle
		else:
		    raise ValueError('Invalid handle')

		self.twitter_client = OAuth2BearerTokenClient(config['BEARER_TOKEN']) if 'BEARER_TOKEN' in config else None
		if self.twitter_client is None:
		    raise KeyError('Missing Bearer Token')

		self.tweets = self.get_tweets()
		self.tweets = self.twitter_client.request(
		    f"https://api.twitter.com/2/tweets/search/recent?query=from:{self.handle}"
		).content

		

	def alternative_approaches____init__(self, handle):
		try:
		    self.handle = str(handle)
		    self.tweets = self.get_tweets()
		except Exception as e:
		    raise ValueError(f"An error occurred during initialization: {e}")

	def context_manager____init__(self, handle):
		self.handle = handle
		self.tweets = self.get_tweets()

	def flipped_interaction_3____init__(self, handle):
		if not isinstance(handle, str) or not handle.strip():
		    raise ValueError('Handle must be a non-empty string')
		self.handle = handle
		try:
		    self.tweets = self.get_tweets()
		except Exception as e:
		    self.tweets = []

	def flipped_interaction_4____init__(self, handle):
		self.handle = handle
		try:
		    self.tweets = self.get_tweets()
		except NetworkError:
		    warnings.warn("Failed to fetch tweets due to a network error.")
		    self.tweets = []

	def flipped_interaction_5____init__(self, handle):
		self.handle = handle
		try:
			self.tweets = self.get_tweets()
			if self.tweets is None:
				self.tweets = []
		except Exception as e:
			print(f"An error occurred while fetching tweets: {e}")
			self.tweets = []

	def flipped_interaction_5__get_tweets(self):
		pass

	def iterative_prompting_3____init__(self, handle):
		if not isinstance(handle, str):
		    raise ValueError('Handle must be a string')
		if not handle:
		    raise ValueError('Handle cannot be empty')
		self.handle = handle.strip()
		try:
		    self.tweets = self.get_tweets()
		except Exception as e:
		    raise RuntimeError(f"Failed to retrieve tweets: {{e}}")

	def iterative_prompting_4____init__(self, handle):
		if not isinstance(handle, str) or not handle.strip():
			raise ValueError('Handle must be a non-empty string.')
		self.handle = handle
		try:
			self.tweets = self.get_tweets()
		except Exception as e:
			self.tweets = None
			print(f'Error retrieving tweets: {{e}}')

	def iterative_prompting_5____init__(self, handle):
		    if not isinstance(handle, str):
		            raise ValueError('handle must be a string')
		    if not handle.startswith('@'):
		            raise ValueError('handle must start with @ symbol')
		    try:
		            self.handle = handle.strip()
		            self.tweets = self.get_tweets()
		    except Exception as e:
		            raise RuntimeError(f"Failed to fetch tweets: {{str(e)}}")

	def few_shots_prompting____init__(self, handle):
		self.handle = handle
		self.tweets = self.get_tweets()

	def cot_prompting____init__(self, handle):
		self.handle = handle
		self.tweets = self.get_tweets()

	def fact_check_list____init__(self, handle):
		self.handle = handle
		self.tweets = self.get_tweets()

	def fact_check_list__get_tweets(self):
		return []

	def not_interactive_mix____init__(self, handle):
		if not isinstance(handle, str) or not re.match(r"^[A-Za-z0-9_]{1,15}$", handle):
		    raise ValueError("Provided handle is not a valid Twitter username.")
		self.handle = handle
		import tweepy
		auth = tweepy.OAuthHandler('YOUR_CONSUMER_KEY', 'YOUR_CONSUMER_SECRET')
		auth.set_access_token('YOUR_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_SECRET')
		api = tweepy.API(auth)
		try:
		    self.tweets = [tweet.full_text for tweet in api.user_timeline(screen_name=self.handle, count=15, tweet_mode='extended')]
		except tweepy.TweepError as e:
		    raise Exception(f"An error occurred while fetching tweets: {str(e)}")

	def interactive_mix____init__(self, handle):
		if not isinstance(handle, str):
		    raise ValueError('The handle parameter must be a string.')
		if len(handle) < 1 or len(handle) > 15:
		    raise ValueError('The handle must be between 1 and 15 characters long.')
		if not handle.startswith('@'):
		    handle = '@' + handle
		import tweepy
		auth = tweepy.OAuthHandler(api_key, api_secret)
		auth.set_access_token(access_token, access_token_secret)
		self.api = tweepy.API(auth)
		self.handle = handle
		try:
		    self.tweets = self.get_tweets()
		except Exception as e:
		    self.tweets = None
		    print(f'Error fetching tweets: {e}')

	def interactive_mix__get_tweets(self):
		timeline = self.api.user_timeline(screen_name=self.handle[1:], tweet_mode='extended', count=10)
		return [tweet.full_text for tweet in timeline]

	def baseline____init__(self, handle):
		self.handle = handle
		self.tweets = self.get_tweets()
