class Persona:
    
    def __init__(self, first_name='', last_name='', job=''):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job

    def ground_truth_code___repr__(self):
        return self.first_name + ' ' + self.last_name + ' has job ' + self.job

    def persona___repr__(self):
        return self.first_name + ' ' + self.last_name + ' has job ' + self.job

    def template___repr__(self):
        try:
            return f"{self.first_name} {self.last_name} has job {self.job}"
        except AttributeError as e:
            return "Error: Missing required attributes"

    def question_refinement___repr__(self):
        first_name = str(self.first_name) if isinstance(self.first_name, str) else 'Unknown'
        last_name = str(self.last_name) if isinstance(self.last_name, str) else 'Unknown'
        job = str(self.job) if isinstance(self.job, str) else 'Unknown'
        return f'{first_name} {last_name} has job {job}'

    def alternative_approaches___repr__(self):
        try:
            return f"{self.first_name} {self.last_name} has job {self.job}"
        except AttributeError as e:
            return f"Missing attribute: {e}"

    def context_manager___repr__(self):
        return f"{self.first_name} {self.last_name} has job {self.job}"

    def flipped_interaction_3___repr__(self):
        first_name = self.first_name if self.first_name else 'Unknown'
        last_name = self.last_name if self.last_name else 'Unknown'
        job = self.job if self.job else 'Unknown job'
        return f"{first_name} {last_name} has job {job}"

    def flipped_interaction_4___repr__(self):
        return f"{self.first_name} {self.last_name} has job {self.job}"

    def flipped_interaction_5___repr__(self):
        return self.first_name + ' ' + self.last_name + ' has job ' + self.job

    def iterative_prompting_3___repr__(self):
        try:
            if not isinstance(self.first_name, str):
                raise TypeError("first_name must be a string.")
            if not isinstance(self.last_name, str):
                raise TypeError("last_name must be a string.")
            if not isinstance(self.job, str):
                raise TypeError("job must be a string.")
            return f"{self.first_name} {self.last_name} has job {self.job}"
        except AttributeError as error:
            return "An error occurred: object is missing the required attributes."
        except TypeError as error:
            return f"An error occurred: {error}"

    def iterative_prompting_4___repr__(self):
        first_name = str(self.first_name) if isinstance(self.first_name, str) else 'Unknown'
        last_name = str(self.last_name) if isinstance(self.last_name, str) else 'Unknown'
        job = str(self.job) if isinstance(self.job, str) else 'Unknown'
        return f'{first_name} {last_name} has job {job}'

    def iterative_prompting_5___repr__(self):
        first_name = str(self.first_name) if isinstance(self.first_name, str) else 'Unknown'
        last_name = str(self.last_name) if isinstance(self.last_name, str) else 'Unknown'
        job = str(self.job) if isinstance(self.job, str) else 'No Job'
        return first_name + ' ' + last_name + ' has job ' + job

    def few_shots_prompting___repr__(self):
        return f'{self.first_name} {self.last_name} has job {self.job}'

    def cot_prompting___repr__(self):
        return f'{self.first_name} {self.last_name} has job {self.job}'

    def fact_check_list___repr__(self):
        return f"{self.first_name} {self.last_name} has job {self.job}"

    def not_interactive_mix___repr__(self):
        if not all(hasattr(self, attr) for attr in ['first_name', 'last_name', 'job']):
            raise AttributeError('Missing required attributes for __repr__')
        if not all(isinstance(getattr(self, attr), str) for attr in ['first_name', 'last_name', 'job']):
            raise TypeError('Attributes must be strings')
        return f"{self.first_name} {self.last_name} has job {self.job}"

    def interactive_mix___repr__(self):
        try:
            if not all(isinstance(attr, str) for attr in (self.first_name, self.last_name, self.job)):
                raise ValueError("All attributes must be strings")
            representation = f"{self.first_name} {self.last_name} has job {self.job}"
        except Exception:
            representation = "Invalid employee attributes"
        return representation

    def baseline___repr__(self):
        return self.first_name + ' ' + self.last_name + ' has job ' + self.job

