class Book:
    def __init__(self, title):
        self.title = title

    def ground_truth_code___repr__(self):
        return self.title

    def persona____repr__(self):
        return self.title

    def template____repr__(self):
        try:
            return self.title
        except AttributeError:
            return "<instance has no title attribute>"

    def question_refinement____repr__(self):
        return str(self.title).encode("utf-8").decode("ascii", "ignore")

    def alternative_approaches____repr__(self):
        if isinstance(getattr(self, "title", None), str):
            return f"Title: {self.title}"
        else:
            return "<invalid_title>"

    def context_manager____repr__(self):
        return self.title

    def flipped_interaction_3____repr__(self):
        return f"'{self.title}'"

    def flipped_interaction_4____repr__(self):
        class_name = self.__class__.__name__
        title = self.title if self.title is not None else "No Title"
        return f'<{class_name}: "{title}">'

    def flipped_interaction_5____repr__(self):
        return self.title

    def iterative_prompting_3____repr__(self):
        if not hasattr(self, "title") or self.title is None:
            return "<TitleNotSet>"
        return str(self.title)

    def iterative_prompting_4____repr__(self):
        if not hasattr(self, "title") or not isinstance(self.title, str):
            raise ValueError("title must be a string")
        return self.title

    def iterative_prompting_5____repr__(self):
        if not hasattr(self, "title") or self.title is None:
            return "<Title Not Set>"
        return str(self.title)

    def few_shots_prompting____repr__(self):
        return self.title

    def cot_prompting____repr__(self):
        return self.title

    def fact_check_list____repr__(self):
        return f"Book(title={self.title!r})"

    def not_interactive_mix____repr__(self):
        return repr(self.title) if hasattr(self, "title") else "UnknownTitle"

    def interactive_mix____repr__(self):
        title = self.title.encode("unicode_escape").decode("utf-8")
        return f"Title({title})"

    def baseline____repr__(self):
        return self.title

