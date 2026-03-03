class Persona:

    def __init__(self, first_name='', last_name='', job=''):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job

    def ground_truth_code___repr__(self):
        return self.first_name + ' ' + self.last_name + ' has job ' + self.job

    def persona____repr__(self):
	    return '{} {} has job {}'.format(self.first_name, self.last_name, self.job)

    def template____repr__(self):
	    return f'{self.first_name} {self.last_name} has job {self.job}'

    def question_refinement____repr__(self):
	    return '{first} {last} has job {job}'.format(first=str(self.first_name), last=str(self.last_name), job=str(self.job))

    def alternative_approaches____repr__(self):
	    return f'{self.first_name} {self.last_name} has job {self.job}'

    def context_manager____repr__(self):
	    return self.first_name + ' ' + self.last_name + ' has job ' + self.job

    def flipped_interaction_3____repr__(self):
	    return f'{self.first_name if isinstance(self.first_name, str) else "Unknown"} {self.last_name if isinstance(self.last_name, str) else "Unknown"} has job {self.job if isinstance(self.job, str) else "Unknown"}'

    def flipped_interaction_4____repr__(self):
	    first_name = self.first_name.strip().title() if self.first_name is not None else ''
	    last_name = self.last_name.strip().title() if self.last_name is not None else ''
	    job = self.job.strip().title() if self.job is not None else ''
	    return f"{first_name} {last_name} has job {job}"

    def flipped_interaction_5____repr__(self):
	    first_name = self.first_name if self.first_name else 'Unknown'
	    last_name = self.last_name if self.last_name else 'Unknown'
	    job = self.job if self.job else 'Unemployed'
	    return f'{first_name} {last_name} has job {job}'

    def iterative_prompting_3____repr__(self):
	    if not all(hasattr(self, attr) and isinstance(getattr(self, attr), str) and getattr(self, attr) is not None for attr in ['first_name', 'last_name', 'job']):
	        raise ValueError('All attributes first_name, last_name, and job must be non-None strings')
	    return f'{self.first_name.strip()} {self.last_name.strip()} has job {self.job.strip()}'

    def iterative_prompting_4____repr__(self):
	    for attr in ['first_name', 'last_name', 'job']:
	        value = getattr(self, attr, '')
	        if not isinstance(value, str):
	            raise ValueError(f'Attribute {attr} must be a string.')
	    return f'{self.first_name.strip()} {self.last_name.strip()} has job {self.job.strip()}'

    def iterative_prompting_5____repr__(self):
        if not all(hasattr(self, attr) and isinstance(getattr(self, attr), str) for attr in ['first_name', 'last_name', 'job']):
            raise ValueError('Attributes first_name, last_name, and job must be strings')
        sanitized_first_name = self.first_name.replace("'", "").replace('"', "")
        sanitized_last_name = self.last_name.replace("'", "").replace('"', "")
        sanitized_job = self.job.replace("'", "").replace('"', "")

        return f'{sanitized_first_name} {sanitized_last_name} has job {sanitized_job}'

    def few_shots_prompting____repr__(self):
	    return self.first_name + ' ' + self.last_name + ' has job ' + self.job

    def cot_prompting____repr__(self):
	    return self.first_name + ' ' + self.last_name + ' has job ' + self.job

    def fact_check_list____repr__(self):
	    return f"{self.first_name} {self.last_name} has job {self.job}"

    def not_interactive_mix____repr__(self):
	    return f"{getattr(self, 'first_name', '')} {getattr(self, 'last_name', '')} has job {getattr(self, 'job', '')}"

    def interactive_mix____repr__(self):
	    first_name = getattr(self, 'first_name', 'Unknown')
	    last_name = getattr(self, 'last_name', 'Unknown')
	    job = getattr(self, 'job', 'Unknown')
	    if not isinstance(first_name, str) or not isinstance(last_name, str) or not isinstance(job, str):
	        raise ValueError("Attributes first_name, last_name, and job must be strings.")
	    return f'{first_name} {last_name} has job {job}'

    def baseline____repr__(self):
	    return self.first_name + ' ' + self.last_name + ' has job ' + self.job
