class Persona:
    def ground_truth_code___init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def persona____init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media.copy()

    def template____init__(self, first_name, last_name, job='', social_media={}):
        try:
            self.first_name = first_name
            self.last_name = last_name
            self.job = job
            self.social_media = dict(social_media)
        except Exception as e:
            raise ValueError(f'Error initializing attributes: {str(e)}')

    def question_refinement____init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = str(first_name)[:50] if isinstance(first_name, (str, int, float)) else ''
        self.last_name = str(last_name)[:50] if isinstance(last_name, (str, int, float)) else ''
        self.job = str(job)[:100] if isinstance(job, (str, int, float)) else ''
        self.social_media = {k: v[:200] for k, v in dict(social_media or {}).items() if isinstance(k, str) and isinstance(v, str)}

    def alternative_approaches____init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = str(first_name).strip()
        self.last_name = str(last_name).strip()
        self.job = str(job).strip()
        if isinstance(social_media, dict):
            self.social_media = social_media
        else:
            raise ValueError('social_media must be a dictionary')

    def context_manager____init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = dict(social_media)

    def flipped_interaction_3____init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def flipped_interaction_4____init__(self, first_name: str, last_name: str, job: str = "", social_media: dict = {}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def flipped_interaction_5____init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def iterative_prompting_3____init__(self, first_name, last_name, job='', social_media={}):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise ValueError("First name and last name must be strings.")
        if not isinstance(job, str):
            raise ValueError("Job must be a string.")
        if not isinstance(social_media, dict):
            raise ValueError("Social media must be a dictionary.")
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.job = job.strip()
        self.social_media = {key.strip(): value.strip() for key, value in social_media.items()}

    def iterative_prompting_4____init__(self, first_name, last_name, job="", social_media={}):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("first_name must be a non-empty string")
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError("last_name must be a non-empty string")
        if not isinstance(job, str):
            raise ValueError("job must be a string")
        if not isinstance(social_media, dict):
            raise ValueError("social_media must be a dictionary")
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.job = job.strip()
        self.social_media = social_media.copy()

    def iterative_prompting_5____init__(self, first_name, last_name, job="", social_media=None):
        if not isinstance(first_name, str):
            raise ValueError("first_name must be a string")
        if not isinstance(last_name, str):
            raise ValueError("last_name must be a string")
        if not isinstance(job, str):
            raise ValueError("job must be a string")
        if social_media is not None and not isinstance(social_media, dict):
            raise ValueError("social_media must be a dictionary")
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.job = job.strip()
        self.social_media = {key: value.strip() if isinstance(value, str) else value for key, value in social_media.items()} if social_media is not None else {}

    def few_shots_prompting____init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def cot_prompting____init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def fact_check_list____init__(self, first_name, last_name, job="", social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media.copy()

    def not_interactive_mix____init__(self, first_name, last_name, job="", social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media.copy()

    def interactive_mix____init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        if not isinstance(first_name, str):
            raise ValueError("first_name must be a string")
        if not isinstance(last_name, str):
            raise ValueError("last_name must be a string")
        if not isinstance(job, str):
            raise ValueError("job must be a string")
        if not isinstance(social_media, dict):
            raise ValueError("social_media must be a dictionary")
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.job = job.strip()
        self.social_media = social_media

    def baseline____init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media
