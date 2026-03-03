class Persona:
    def ground_truth_code___init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def persona___init__(self, first_name, last_name, job='', social_media=None):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise ValueError("First and last name must be strings")
        if not isinstance(job, str):
            raise ValueError("Job must be a string")
        if social_media is None:
            social_media = {}
        elif not isinstance(social_media, dict):
            raise ValueError("Social media must be a dictionary")
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def template___init__(self, first_name, last_name, job='', social_media={}):
        try:
            if not isinstance(first_name, str) or not isinstance(last_name, str):
                raise ValueError("First name and last name must be strings.")
            if not isinstance(job, str):
                raise ValueError("Job must be a string.")
            if not isinstance(social_media, dict):
                raise ValueError("Social media must be a dictionary.")
            self.first_name = first_name
            self.last_name = last_name
            self.job = job
            self.social_media = social_media
        except Exception as e:
            print(f"An error occurred: {e}")

    def question_refinement___init__(self, first_name, last_name, job='', social_media=None):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError('First name must be a non-empty string.')
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError('Last name must be a non-empty string.')
        if not isinstance(job, str):
            raise ValueError('Job must be a string.')
        if social_media is None:
            social_media = {}
        if not isinstance(social_media, dict):
            raise ValueError('Social media must be a dictionary.')
        for platform, username in social_media.items():
            if not isinstance(platform, str) or not isinstance(username, str):
                raise ValueError('Social media platforms and usernames must be strings.')
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.job = job.strip()
        self.social_media = {platform.strip(): username.strip() for platform, username in social_media.items() if platform.strip() and username.strip()}

    def alternative_approaches___init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def context_manager___init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def flipped_interaction_3___init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def flipped_interaction_4___init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def flipped_interaction_5___init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def iterative_prompting_3___init__(self, first_name, last_name, job='', social_media=None):
        if not isinstance(first_name, str) or not first_name:
            raise ValueError('first_name must be a non-empty string')
        if not isinstance(last_name, str) or not last_name:
            raise ValueError('last_name must be a non-empty string')
        if not isinstance(job, str):
            raise ValueError('job must be a string')
        if social_media is None:
            social_media = {}
        elif not isinstance(social_media, dict):
            raise ValueError('social_media must be a dictionary')
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def iterative_prompting_4___init__(self, first_name, last_name, job="", social_media=None):
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        if not isinstance(job, str):
            raise TypeError("job must be a string")
        if social_media is None:
            social_media = {}
        elif not isinstance(social_media, dict):
            raise TypeError("social_media must be a dictionary")
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.job = job.strip()
        self.social_media = social_media

    def iterative_prompting_5___init__(self, first_name, last_name, job='', social_media=None):
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("first_name must be a non-empty string")
        if not isinstance(last_name, str) or not last_name:
            raise ValueError("last_name must be a non-empty string")
        if not isinstance(job, str):
            raise TypeError("job must be a string")
        if social_media is None:
            social_media = {}
        elif not isinstance(social_media, dict):
            raise TypeError("social_media must be a dictionary")
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def few_shots_prompting___init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def cot_prompting___init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def fact_check_list___init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def not_interactive_mix___init__(self, first_name, last_name, job='', social_media=None):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise ValueError("First and last names must be strings.")
        if not isinstance(job, str):
            raise ValueError("Job must be a string.")
        if social_media is None:
            social_media = {}
        elif not isinstance(social_media, dict):
            raise ValueError("Social media must be a dictionary.")
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def interactive_mix___init__(self, first_name, last_name, job="", social_media=None):
        if social_media is None:
            social_media = {}
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        if not isinstance(job, str):
            raise TypeError("job must be a string")
        if not isinstance(social_media, dict):
            raise TypeError("social_media must be a dictionary")
        for key, value in social_media.items():
            if not isinstance(key, str):
                raise TypeError("Keys in social_media must be strings")
            if not isinstance(value, str):
                raise TypeError("Values in social_media must be strings")
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def baseline___init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

