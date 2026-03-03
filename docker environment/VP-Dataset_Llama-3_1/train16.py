import logging

import requests

class TweetClient:

    def ground_truth_code___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def persona___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def template___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def question_refinement___init__(self, handle):
        if not isinstance(handle, str):
            raise TypeError("Handle must be a string")
        self.handle = handle.strip() or None
        if self.handle is None:
            raise ValueError("Handle must not be empty")
        self.tweets = []

    def alternative_approaches___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def context_manager___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def flipped_interaction_3___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()


    def flipped_interaction_4____init__(self, handle):
        if handle is None or handle == '':
            raise ValueError('Handle cannot be empty or None')
        try:
            self.handle = handle
            self.tweets = self.get_tweets()
        except Exception as e:
            raise Exception(f'Failed to initialize: {str(e)}')

    def flipped_interaction_5___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()


    def iterative_prompting_3____init__(self, handle):
        if not isinstance(handle, str):
            raise TypeError("Handle must be a string")
        if not handle.strip():
            raise ValueError("Handle cannot be empty")
        self.handle = handle
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            raise Exception("Failed to retrieve tweets: " + str(e)) from e

    def iterative_prompting_4____init__(self, handle):
        if not isinstance(handle, str):
            raise TypeError("handle must be a string")
        handle = handle.strip()
        if not handle:
            raise ValueError("handle cannot be empty")
        self.handle = handle
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            import logging
            logging.exception("Failed to get tweets")
            raise RuntimeError(f"Failed to get tweets for handle '{handle}'") #controllare

    def iterative_prompting_5____init__(self, handle):
        if not isinstance(handle, str):
            raise TypeError("handle must be a string")
        self.handle = handle.strip()
        if not self.handle:
            raise ValueError("handle cannot be empty")
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            import logging
            logging.error(f"Failed to fetch tweets: {str(e)}")
            raise RuntimeError(f"Failed to fetch tweets: {str(e)}")

    def few_shots_prompting___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def cot_prompting___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def fact_check_list___init__(self, handle):
        self._handle = handle
        self._tweets = self.get_tweets()

    def fact_check_list_get_tweets(self):
        pass

    def not_interactive_mix___init__(self, handle):
        self.handle = handle
        if hasattr(self, 'get_tweets') and callable(self.get_tweets):
            try:
                self.tweets = self.get_tweets()
            except Exception as e:
                print(f"Error occurred: {e}")
                raise AttributeError("Failed to get tweets")
        else:
            raise AttributeError("get_tweets method is not defined or is not callable")

    def interactive_mix___init__(self, handle):
        if not isinstance(handle, str) or len(handle) == 0:
            raise ValueError("Invalid handle: must be a non-empty string")
        self.handle = handle
        try:
            self.tweets = self.get_tweets()
        except Exception as e:
            logging.error(f"Error retrieving tweets: {str(e)}")
            self.tweets = None

    def baseline___init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()


    def get_tweets(self):
        return [
            "Just had a great workout! #fitness",
            "Enjoying the beautiful weather today. #sunnyday"
        ]
