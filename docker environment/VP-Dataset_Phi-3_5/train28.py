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
        self.title = title
        self.text = text
        self.url = url

    def question_refinement___init__(self, data):
        if not isinstance(data, str):
            raise TypeError('Data must be a string')
        self.data = data.strip()

    def alternative_approaches___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def context_manager___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def iterative_prompting_3___init__(self, title, text, url):
        if not isinstance(title, str) or not title:
            raise ValueError('Title must be a non-empty string.')
        if not isinstance(text, str) or not text:
            raise ValueError('Text must be a non-empty string.')
        if not isinstance(url, str) or not url.startswith('http://') and not url.startswith('https://'):
            raise ValueError('URL must be a valid URL starting with http:// or https://.')
        self.title = title
        self.text = text
        self.url = url
        try:
            response = requests.head(url)
            if response.status_code != 200:
                raise ValueError('The provided URL is not reachable.')
        except requests.RequestException as e:
            raise ValueError('An error occurred when checking the URL.') from e

    def iterative_prompting_4___init__(self, title, text, url):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not isinstance(text, str):
            raise ValueError("Text must be a string")
        if not url.startswith(('http://', 'https://')):
            raise ValueError("URL must be a valid HTTP or HTTPS URL")
        self.title = title
        self.text = text
        self.url = url

    import re
    def iterative_prompting_5___init__(self, title, text, url):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not isinstance(text, str):
            raise ValueError("Text must be a string")
        if not isinstance(url, str):
            raise ValueError("URL must be a string")
        if not re.match(r'https?://', url):
            raise ValueError("URL must start with https://")
        self.title = title.strip()
        self.text = text.strip()
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
        self.title = title
        self.text = text
        self.url = url

    def baseline___init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

