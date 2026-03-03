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
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media


    def question_refinement___init__(self, first_name='', last_name='', job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def alternative_approaches___init__(self, first_name, last_name, job='', social_media=None):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media if social_media is not None else dict()

    def context_manager___init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def iterative_prompting_3___init__(self, first_name, last_name, job='', social_media={}):
        if not isinstance(first_name, str) or not first_name:
            raise ValueError('first_name must be a non-empty string')
        if not isinstance(last_name, str) or not last_name:
            raise ValueError('last_name must be a non-empty string')
        if not isinstance(job, str):
            raise ValueError('job must be a string')
        if not isinstance(social_media, dict):
            raise ValueError('social_media must be a dictionary')
        if len(first_name) > 255:
            raise ValueError('first_name too long')
        if len(last_name) > 255:
            raise ValueError('last_name too long')
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def iterative_prompting_4___init__(self, first_name, last_name, job='', social_media=None):
        import sys
        if sys.version_info < (3, 6):
            raise EnvironmentError('Python 3.6 or higher is required.')
        if not isinstance(first_name, str) or not first_name:
            raise ValueError('first_name must be a non-empty string')
        if not isinstance(last_name, str) or not last_name:
            raise ValueError('last_name must be a non-empty string')
        if not isinstance(job, str):
            raise ValueError('job must be a non-empty string')
        if social_media is not None and not isinstance(social_media, dict):
            raise ValueError('social_media must be a dictionary if provided')
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media if social_media is not None else {}

    def iterative_prompting_5___init__(self, first_name, last_name, job='', social_media={}):
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("first_name must be a non-empty string")
        if not isinstance(last_name, str) or not last_name:
            raise ValueError("last_name must be a non-empty string")
        if job != '' and not isinstance(job, str):
            raise ValueError("job must be a non-empty string")
        if not isinstance(social_media, dict):
            raise ValueError("social_media must be a dictionary")

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


    def fact_check_list___init__(self, first_name, last_name, job="", social_media=None):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media if social_media is not None else {}

    def not_interactive_mix___init__(self, first_name, last_name, job="", social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def baseline___init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

