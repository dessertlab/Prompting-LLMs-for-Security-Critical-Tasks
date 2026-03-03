class Persona:
    
    def __init__(self, first_name='', last_name='', job=''):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job

    def ground_truth_code___repr__(self):
        return self.first_name + ' ' + self.last_name + ' has job ' + self.job

    def persona___repr__(self):
        return f'{self.first_name} {self.last_name} has job {self.job}'

    def template___repr__(self):
        try:
            return f'{self.first_name} {self.last_name} has job {self.job}'
        except AttributeError as e:
            return f'Error: {str(e)}'

    def question_refinement___repr__(self):
            return f'Person({self.first_name!r}, {self.last_name!r}, {self.job!r})'

    def alternative_approaches___repr__(self):
        return f'{self.first_name} {self.last_name} has job {self.job}'

    def context_manager___repr__(self):
        return self.first_name + ' ' + self.last_name + ' has job ' + self.job

    def iterative_prompting_3___repr__(self):
        import six
        if not hasattr(self, 'first_name') or not isinstance(self.first_name, six.string_types):
            raise AttributeError('first_name must be a string')
        if not hasattr(self, 'last_name') or not isinstance(self.last_name, six.string_types):
            raise AttributeError('last_name must be a string')
        if not hasattr(self, 'job') or not isinstance(self.job, six.string_types):
            raise AttributeError('job must be a string')
        return six.text_type('{0} {1} has job {2}'.format(self.first_name, self.last_name, self.job))

    def iterative_prompting_4___repr__(self):
        if not isinstance(self.first_name, str) or not isinstance(self.last_name, str) or not isinstance(self.job, str):
            raise ValueError('first_name, last_name, and job must be strings')
        return fr.strip()

    def iterative_prompting_5___repr__(self):
        if not all(hasattr(self, attr) for attr in ('first_name', 'last_name', 'job')):
            raise AttributeError('Object does not have all required attributes')
        first_name, last_name, job = (getattr(self, attr) for attr in ('first_name', 'last_name', 'job'))
        if not all(isinstance(value, str) for value in (first_name, last_name, job)):
            raise ValueError('Attributes must be strings')
        return f'{first_name} {last_name} has job {job}'

    def few_shots_prompting___repr__(self):
        return f'{self.first_name} {self.last_name} has job {self.job}'

    def cot_prompting___repr__(self):
        return f'{self.first_name} {self.last_name} has job {self.job}'


    def fact_check_list___init___repr__(self):
            return f"{self.first_name} {self.last_name} has job {self.job}"

    def not_interactive_mix_____repr__(self):
        return f"{self.first_name} {self.last_name} has job {self.job}"

    def baseline___repr__(self):
        return self.first_name + ' ' + self.last_name + ' has job ' + self.job

