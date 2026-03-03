class Book:
    def __init__(self, title):
        self.title = title

    def ground_truth_code___repr__(self):
        return self.title

    def persona___repr__(self):
        return self.title

    def template___repr__(self):
        try:
            return self.title
        except AttributeError:
            return 'Attribute Error: Title is not defined'

    def question_refinement___repr__(title):
        return Book(title)

    def alternative_approaches___repr__(self):
        return self.title if isinstance(self.title, str) else 'Invalid Title'

    def context_manager___repr__(self):
        return str(self.title)

    def flipped_interaction_3___repr__(self):
        return repr(self.title)

    def flipped_interaction_4___repr__(self):
        return self.title

    def flipped_interaction_5___repr__(self):
        return self.title

    def iterative_prompting_3___repr__(self):
        if not hasattr(self, 'title'):
            raise AttributeError("'title' attribute is missing")
        if not isinstance(self.title, str):
            raise TypeError("'title' attribute must be a string")
        return f'{self.title}'

    def iterative_prompting_4___repr__(self):
        if not hasattr(self, 'title'):
            return "<No title attribute>"
        if not isinstance(self.title, str):
            return "<Invalid title type>"
        return f"{self.title}"

    def iterative_prompting_5___repr__(self):
        if isinstance(getattr(self, 'title', None), str) and self.title:
            return self.title
        return '<UnnamedInstance>'

    def few_shots_prompting___repr__(self):
        return self.title

    def cot_prompting___repr__(self):
        return self.title

    def fact_check_list___repr__(self):
        return f'Book(title="{self.title}")'

    def not_interactive_mix___repr__(self):
        return repr(self.title)

    def interactive_mix___repr__(self):
        if hasattr(self, 'title') and isinstance(self.title, str):
            return self.title
        raise AttributeError('The object does not have a valid title attribute.')

    def baseline___repr__(self):
        return self.title

