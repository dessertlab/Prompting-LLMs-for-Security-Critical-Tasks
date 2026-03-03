import re

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
        try:
            if not isinstance(title, str):
                raise ValueError('Title must be a string')
            if not isinstance(text, str):
                raise ValueError('Text must be a string')
            if not isinstance(url, str):
                raise ValueError('URL must be a string')
            self.title = title
            self.text = text
            self.url = url
        except Exception as e:
            raise ValueError(f'Error during initialization: {e}')

    def question_refinement___init__(self, title, text, url):
        if not isinstance(title, str) or not title:
            raise ValueError('Invalid title. Title must be a non-empty string.')
        self.title = title.strip()
        if not isinstance(text, str):
            raise ValueError('Invalid text. Text must be a string.')
        self.text = text.strip()
        url_pattern = re.compile(r'^(https?://)?(www\.)?[-a-zA-Z0-9@:%._\+~')
        if not isinstance(url, str) or not url_pattern.match(url):
            raise ValueError('Invalid URL. Please provide a valid URL.')
        self.url = url.strip()

    def alternative_approaches___init__(self, title, text, url):
        import re
        from urllib.parse import urlparse
        if not isinstance(title, str) or not isinstance(text, str):
            raise TypeError('Title and text must be strings.')
        if not isinstance(url, str) or not re.match(r'^(http|https)://', url) or not urlparse(url).scheme:
            raise ValueError('Invalid URL format.')
        self.title = title
        self.text = text
        self.url = url

    def context_manager___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def flipped_interaction_3___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def flipped_interaction_4___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url
    

    def flipped_interaction_5___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def iterative_prompting_3___init__(self, title, text, url):
        if not isinstance(title, str):
            raise TypeError('Title must be a string.')
        if not isinstance(text, str):
            raise TypeError('Text must be a string.')
        if not isinstance(url, str):
            raise TypeError('URL must be a string.')
        if not title:
            raise ValueError('Title cannot be empty.')
        if not url.strip().startswith(('http://', 'https://')):
            raise ValueError('URL must start with "http://" or "https://".')
        self.title = title
        self.text = text
        self.url = url

    def iterative_prompting_4___init__(self, title, text, url):
        if not isinstance(title, str):
            raise TypeError('Title must be a string')
        if not isinstance(text, str):
            raise TypeError('Text must be a string')
        if not isinstance(url, str):
            raise TypeError('URL must be a string')
        if not title.strip():
            raise ValueError('Title cannot be empty or whitespace only')
        if not text.strip():
            raise ValueError('Text cannot be empty or whitespace only')
        if not url.strip():
            raise ValueError('URL cannot be empty or whitespace only')
        self.title = title.strip()
        self.text = text.strip()
        self.url = url.strip()

    def iterative_prompting_5___init__(self, title, text, url):
        if not isinstance(title, str):
            raise ValueError('Title must be a string')
        if not isinstance(text, str):
            raise ValueError('Text must be a string')
        if not isinstance(url, str):
            raise ValueError('URL must be a string')
        url_pattern = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[a-zA-Z0-9\-]{1,}\.)+(?:[a-zA-Z]{2,6}|[a-zA-Z0-9\-]{2,}))'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if not re.match(url_pattern, url):
            raise ValueError('Invalid URL format')
        self.title = title
        self.text = text
        self.url = url

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
        if not isinstance(title, str) or not title.strip():
            raise ValueError('Title must be a non-empty string')
        if not isinstance(text, str) or not text.strip():
            raise ValueError('Text must be a non-empty string')
        if not isinstance(url, str) or not url.strip():
            raise ValueError('URL must be a non-empty string')
        self.title = title.strip()
        self.text = text.strip()
        self.url = url.strip()

    def interactive_mix___init__(self, title, text, url):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Text must be a non-empty string.")
        if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
            raise ValueError("URL must be a valid HTTP or HTTPS string.")
        self.title = title
        self.text = text
        self.url = url

    def baseline___init__(self, title, text, url): 
        self.title = title 
        self.text = text    
        self.url = url

