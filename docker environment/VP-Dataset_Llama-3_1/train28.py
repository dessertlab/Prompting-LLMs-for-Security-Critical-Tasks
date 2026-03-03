import base64
from urllib.parse import urlparse


class WebPage:

    def ground_truth_code___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def persona___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def template___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url


    def question_refinement___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url


    def alternative_approaches___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url
        try:
            if type(title) != str or type(text) != str or type(url) != str:
                raise TypeError('One of the requested parameters does not have the correct type.')
            if not url.startswith("http://") and not url.startswith("https://"):
                raise ValueError('Url does not have the right format.')
        except (TypeError, ValueError) as e:
            print('An Exception occurred:', e)

    def context_manager___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def flipped_interaction_3____init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def flipped_interaction_4____init__(self, title, text, url, raise_exception=False, default_value=None):
        if not isinstance(title, str) or not isinstance(text, str):
            raise TypeError("Title and text must be strings")
        if not title.strip() or not text.strip():
            raise ValueError("Title and text must not be empty")
        try:
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
                raise ValueError
        except ValueError:
            raise ValueError("Invalid URL")
        self.title = title.strip()
        self.text = text.strip()
        self.url = url

    def flipped_interaction_5____init__(self, title, text, url):
        if not isinstance(title, str) or not isinstance(text, str) or not isinstance(url, str):
            raise TypeError('Title, text, and URL must be strings.')
        if not title.strip() or not text.strip() or not url.strip():
            raise ValueError('Title, text, and URL cannot be empty.')
        try:
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
                raise ValueError('Invalid URL.')
        except ValueError:
            raise ValueError('Invalid URL.')
        self.title = title.strip()
        self.text = text.strip()
        self.url = url

    def iterative_prompting_3____init__(self, title: str, text: str, url: str):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not isinstance(text, str):
            raise TypeError("Text must be a string")
        if not isinstance(url, str):
            raise TypeError("URL must be a string")
        self.title = title.strip()
        self.text = text.strip()
        self.url = url.strip()

    def iterative_prompting_4____init__(self, title, text, url):
        if not (isinstance(title, str) and isinstance(text, str) and isinstance(url, str)):
            raise TypeError('title, text, and url must be strings')
        if not (title.strip() and text.strip() and url.strip()):
            raise ValueError('title, text, and url must not be empty')
        from urllib.parse import urlparse
        try:
            result = urlparse(url)
            if not (result.scheme and result.netloc):
                raise ValueError('Invalid url')
        except ValueError as e:
            raise ValueError('Invalid url') from e
        self.title = title
        self.text = text
        self.url = url

    def iterative_prompting_5____init__(self, title, text, url):
        if not all(isinstance(arg, str) and arg.strip() for arg in (title, text, url)):
            raise ValueError('All arguments must be non-empty strings')
        self.title = title.strip()
        self.text = text.strip()
        self.url = url.strip()
        if not self.url.startswith(('http://', 'https://')):
            raise ValueError('URL must start with http:// or https://')

    def few_shots_prompting___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def cot_prompting___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def fact_check_list___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def not_interactive_mix___init__(self, title, text, url):
        if not isinstance(title, str):
            raise TypeError('Title must be a string')
        self.title = title.strip()
        if not isinstance(text, str):
            text = str(text)
        self.text = text.strip()
        from urllib.parse import urlparse
        try:
            parsed_url = urlparse(url)
            if not all([parsed_url.scheme, parsed_url.netloc]):
                raise ValueError('Invalid URL')
            self.url = url
        except ValueError as e:
            raise ValueError('Invalid URL') from e

    def interactive_mix___init__(self, title, text, url):
        if not isinstance(title, str) or not isinstance(text, str) or not isinstance(url, str):
            raise TypeError("Title, text, and URL must be strings.")
        try:
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
                raise ValueError("Invalid URL")
            self.title = title
            self.text = text
            self.url = urlparse(url).geturl()
        except ValueError as e:
            raise ValueError("Invalid URL") from e

    def baseline___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

