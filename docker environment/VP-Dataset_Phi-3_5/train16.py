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
        self.handle = handle
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            print(f'Error occurred: {e}')

    def question_refinement___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()
    def get_tweets(self):
        return []

    def alternative_approaches___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def context_manager___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def iterative_prompting_3___init__(self, handle):
        if not isinstance(handle, str):
            raise TypeError('handle must be a string')
        self.handle = handle
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            raise RuntimeError('Failed to retrieve tweets') from e

    def iterative_prompting_4___init__(self, handle):
        if not isinstance(handle, str):
            raise ValueError('handle must be a string')
        if len(handle) > 15:
            raise ValueError('handle exceeds maximum length')
        self.handle = handle
        try:
            self.tweets = self.get_tweets()
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise e

    def iterative_prompting_5___init__(self, handle):
        if not isinstance(handle, str):
            raise ValueError('Handle must be a string')
        self.handle = handle
        self.tweets = self.get_tweets()
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            print(f'Error retrieving tweets: {e}')
            self.tweets = None
        if not self.handle:
            raise ValueError('Handle attribute cannot be empty')

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
		    rejectError('handle must be a string')
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

