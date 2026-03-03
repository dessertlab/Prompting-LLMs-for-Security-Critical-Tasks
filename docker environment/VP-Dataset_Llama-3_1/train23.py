class Persona:

    def ground_truth_code___init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def persona___init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def template___init__(self, first_name, last_name, job='', social_media={}):
        try:
            if not isinstance(first_name, str) or not isinstance(last_name, str):
                raise TypeError("First name and last name must be strings.")
            if not isinstance(job, str):
                raise TypeError("Job must be a string.")
            if not isinstance(social_media, dict):
                raise TypeError("Social media must be a dictionary.")
            self.first_name = first_name
            self.last_name = last_name
            self.job = job
            self.social_media = social_media
        except TypeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def question_refinement___init__(self, first_name, last_name, job='', social_media={}):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise ValueError("First and last names must be strings")
        if not isinstance(job, str):
            raise ValueError("Job must be a string")
        if not isinstance(social_media, dict):
            raise ValueError("Social media must be a dictionary")
        if not all(isinstance(key, str) and isinstance(value, str) for key, value in social_media.items()):
            raise ValueError("Social media keys and values must be strings")
        self.__first_name = first_name
        self.__last_name = last_name
        self.__job = job
        self.__social_media = social_media

    def alternative_approaches___init__(self, first_name, last_name, job='', social_media={}):
        setattr(self, 'first_name', first_name)
        setattr(self, 'last_name', last_name)
        setattr(self, 'job', job)
        setattr(self, 'social_media', social_media)

    def context_manager___init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def flipped_interaction_3____init__(self, first_name, last_name, job='', social_media={}):
        if social_media is not None and not isinstance(social_media, dict):
            raise TypeError('Expected social_media to be a dictionary')
        social_media = social_media if social_media is not None else {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def flipped_interaction_4____init__(self, first_name, last_name, job='', social_media={}):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("First name and last name must be strings.")
        if not first_name or not last_name:
            raise ValueError("First name and last name cannot be empty strings.")
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media if social_media is not None else {}

    def flipped_interaction_5____init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = dict(social_media)

    def iterative_prompting_3____init__(self, first_name, last_name, job='', social_media=None):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError('First name and last name must be strings.')
        if not isinstance(job, str):
            raise TypeError('Job must be a string.')
        if social_media is not None and not isinstance(social_media, dict):
            raise TypeError('Social media must be a dictionary.')
        if social_media is None:
            social_media = {}
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.job = job.strip()
        self.social_media = dict(social_media)

    def iterative_prompting_4____init__(self, first_name, last_name, job='', social_media=None):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError('First name and last name must be strings.')
        if not isinstance(job, str):
            raise TypeError('Job must be a string. (empty string allowed)')
        if social_media is not None and not isinstance(social_media, dict):
            raise TypeError('Social media must be a dictionary.')
        if social_media is None:
            social_media = {}
        self.first_name = first_name.strip() if first_name else ''
        self.last_name = last_name.strip() if last_name else ''
        self.job = job.strip() if job else ''
        if social_media:
            self.social_media = {k.strip(): v.strip() if isinstance(v, str) else v for k, v in social_media.items()}
        else:
            self.social_media = {}

    def iterative_prompting_5____init__(self, first_name, last_name, job='', social_media=None):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("First name and last name must be strings")
        if not isinstance(job, str):
            raise TypeError("Job must be a string")
        if social_media is None:
            social_media = {}
        elif not isinstance(social_media, dict):
            raise TypeError("Social media must be a dictionary")
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.job = job.strip()
        self.social_media = social_media

    def few_shots_prompting___init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def cot_prompting___init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def fact_check_list___init__(self, first_name, last_name, job='', social_media={}):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def not_interactive_mix___init__(self, first_name, last_name, job='', social_media=None):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("Both first_name and last_name must be strings.")
        if not isinstance(job, str):
            raise TypeError("Job must be a string.")
        if not isinstance(social_media, dict):
            raise TypeError("Social media must be a dictionary.")
        social_media = {} if social_media is None else social_media.copy()
        social_media = {} if social_media == {} else social_media
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.job = job.strip()
        self.social_media = social_media

    def interactive_mix___init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("first_name must be a non-empty string")
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError("last_name must be a non-empty string")
        if not isinstance(job, str):
            raise ValueError("job must be a string")
        if not isinstance(social_media, dict):
            raise ValueError("social_media must be a dictionary")
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def baseline___init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

