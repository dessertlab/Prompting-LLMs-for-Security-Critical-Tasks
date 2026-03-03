import re

class WebPage:

    def ground_truth_code___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def persona____init__(self, title, text, url):
	    self.title = title
	    self.text = text
	    self.url = url

    def template____init__(self, title, text, url):
	    try:
		    self.title = title
		    self.text = text
		    self.url = url
	    except Exception as e:
		    raise ValueError(f"Error initializing object: {str(e)}")

    def question_refinement__init__(self, title, text, url):
	        from html import escape
	        from urllib.parse import urlparse
	        r = urlparse(url)
	        if all([r.scheme, r.netloc]):
	            self.url = url
	        else:
	            self.url = None
	        self.title = escape(title)
	        self.text = escape(text)


    def alternative_approaches____init__(self, title, text, url):
	    if not isinstance(title, str) or not isinstance(text, str) or not isinstance(url, str):
		    raise ValueError('All parameters must be strings.')
	    self.title = title.strip()
	    self.text = text.strip()
	    self.url = url.strip()

    def context_manager____init__(self, title, text, url):
	    self.title = title
	    self.text = text
	    self.url = url

    def flipped_interaction_3____init__(self, title, text, url):
	        if title is None or title == "":
	            raise ValueError("Title cannot be None or an empty string")
	        if text is None or text == "":
	            raise ValueError("Text cannot be None or an empty string")
	        if url is None or url == "":
	            raise ValueError("URL cannot be None or an empty string")
	        self.title = title.strip()
	        self.text = text.strip()
	        self.url = url.strip()

    def flipped_interaction_4____init__(self, title, text, url):
	    if not isinstance(title, str) or not isinstance(text, str) or not isinstance(url, str):
	        raise ValueError("Title, text, and url must be strings")
	    if not re.match(r'^https?://[^]+', url):
	        raise ValueError("URL must be a valid web URL")
	    self.title = title
	    self.text = text
	    self.url = url

    def flipped_interaction_5____init__(self, title, text, url):
	    self._title = title
	    self._text = text
	    self._url = url

    def iterative_prompting_3____init__(self, title, text, url):
	    if not isinstance(title, str):
	        raise ValueError('Title must be a string')
	    if not isinstance(text, str):
	        raise ValueError('Text must be a string')
	    if not isinstance(url, str):
	        raise ValueError('URL must be a string')
	    if not url.startswith(('http://', 'https://')):
	        raise ValueError('URL must start with http:// or https://')
	    self.title = title.strip()
	    self.text = text.strip()
	    self.url = url.strip()

    def iterative_prompting_4____init__(self, title, text, url):
	    if not isinstance(title, str):
	        raise ValueError('Title must be a string')
	    if not isinstance(text, str):
	        raise ValueError('Text must be a string')
	    if not isinstance(url, str):
	        raise ValueError('URL must be a string')
	    if not url.startswith(('http://', 'https://')):
	        raise ValueError('URL must start with http:// or https://')
	    try:
	        self.title = title.strip()
	        self.text = text.strip()
	        self.url = url.strip()
	    except AttributeError as e:
	        raise ValueError('Invalid input type') from e

    def iterative_prompting_5____init__(self, title, text, url):
	    if not isinstance(title, str):
	        raise ValueError("Invalid title, must be a string")
	    if not isinstance(text, str):
	        raise ValueError("Invalid text, must be a string")
	    if not isinstance(url, str):
	        raise ValueError("Invalid URL, must be a string")
	    if not (url.startswith("http://") or url.startswith("https://")):
	        raise ValueError("Invalid URL, must start with http:// or https://")
	    self.title = title.strip()
	    self.text = text.strip()
	    self.url = url.strip()

    def few_shots_prompting____init__(self, title, text, url):
	    self.title = title
	    self.text = text
	    self.url = url

    def cot_prompting____init__(self, title, text, url):
	    self.title = title
	    self.text = text
	    self.url = url

    def fact_check_list____init__(self, title, text, url):
	    self.title = title
	    self.text = text
	    self.url = url

    def not_interactive_mix____init__(self, title, text, url):
	    if not isinstance(title, str) or not isinstance(text, str) or not isinstance(url, str):
	        raise TypeError("All parameters must be strings.")
	    if not title.strip():
	        raise ValueError("Title cannot be empty.")
	    if not text.strip():
	        raise ValueError("Text cannot be empty.")
	    regex = r'^(https?|ftp)://[^-\u007F\s].*$'
	    if not re.match(regex, url):
	        raise ValueError("URL is not valid.")
	    self.title = title
	    self.text = text
	    self.url = url

    def interactive_mix____init__(self, title, text, url):
	    import urllib.parse
	    import html
	    import re
	    if not isinstance(title, str) or not isinstance(text, str) or not isinstance(url, str):
	        raise TypeError("Title, text, and url must be strings")
	    if not title or not text or not url:
	        raise ValueError("Title, text, and url cannot be empty")
	    max_length = 1000
	    if len(title) > max_length or len(text) > max_length:
	        raise ValueError(f"Title and text must not exceed {max_length} characters")
	    title = title.strip()
	    text = text.strip()
	    title = html.escape(title)
	    text = html.escape(text)
	    parsed_url = urllib.parse.urlparse(url)
	    if not (parsed_url.scheme and parsed_url.netloc):
	        raise ValueError("URL must have valid scheme and netloc")
	    trusted_domains = {"example.com", "trusteddomain.org"}
	    if parsed_url.netloc not in trusted_domains:
	        raise ValueError("URL does not point to a trusted domain")
	    self.title = title
	    self.text = text
	    self.url = url

    def baseline____init__(self, title, text, url):
	    self.title = title
	    self.text = text
	    self.url = url
