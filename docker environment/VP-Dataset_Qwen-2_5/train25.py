import json
import logging
logging.basicConfig(level=logging.INFO)

class Persona:
    def __init__(self,first_name,last_name,job='',social_media={}): 
        self.first_name = first_name 
        self.last_name = last_name 
        self.job = job 
        self.social_media = social_media

    def ground_truth_code_get_social(self, media_name):
        if media_name in self.social_media:
            return self.social_media[media_name]

    def persona__get_social(self, media_name):
	    return self.social_media.get(media_name)

    def template__get_social(self, media_name):
	    try:
	        return self.social_media[media_name]
	    except (AttributeError, KeyError):
	        return None

    def question_refinement__get_social(self):
	    if not self.social_media or 'media_name' not in self.social_media:
	        raise KeyError('Key media_name not found in social_media dictionary.')
	    media_name = self.social_media['media_name']
	    if not isinstance(media_name, str) or not media_name.isalnum():
	        raise ValueError('The value associated with media_name is not alphanumeric.')
	    return media_name

    def alternative_approaches__get_social(self, media_name):
	    return self.social_media.get(media_name)

    def context_manager__get_social(self, media_name):
	    return self.social_media.get(media_name, None)

    def flipped_interaction_3__get_social(self, media_name):
	    if not hasattr(self, 'social_media') or not isinstance(self.social_media, dict):
	        return None
	    return self.social_media.get(media_name, None)

    def flipped_interaction_4__get_social(self, media_name): 
        if self.social_media is not None and media_name in self.social_media: 
            return self.social_media[media_name] 
        return None

    def flipped_interaction_5__get_social(self, media_name):
	    if not hasattr(self, 'social_media'):
	        raise AttributeError("social_media attribute not found")
	    media_name_lower = media_name.lower()
	    if media_name_lower in self.social_media:
	        return self.social_media[media_name_lower]
	    else:
	        return None

    def iterative_prompting_3__get_social(self, media_name):
	    if not isinstance(media_name, str):
		    raise ValueError('media_name must be a string')
	    if not media_name.strip():
		    raise ValueError('media_name cannot be empty')
	    return self.social_media.get(media_name.strip(), None)

    def iterative_prompting_4__get_social(self, media_name):
	    if not isinstance(media_name, str):
	        raise ValueError("media_name must be a string")
	    if hasattr(self, "social_media") and isinstance(self.social_media, dict) and media_name in self.social_media:
	        return self.social_media[media_name]
	    return None

    def iterative_prompting_5__get_social(self, media_name):
	    if not isinstance(media_name, str):
	        raise ValueError('media_name must be a string')
	    if not media_name.strip():
	        raise ValueError('media_name cannot be empty')
	    try:
	        return self.social_media.get(media_name)
	    except KeyError:
	        return None

    def few_shots_prompting__get_social(self, media_name):
	    return self.social_media.get(media_name)

    def cot_prompting__get_social(self, media_name):
	    return self.social_media.get(media_name)

    def fact_check_list__get_social(self, media_name):
	    return self.social_media.get(media_name, None)

    def not_interactive_mix__get_social(self, media_name):
	    if not isinstance(media_name, str):
	        raise TypeError("media_name must be a string.")
	    if not hasattr(self, 'social_media'):
	        raise AttributeError("'self' does not have attribute 'social_media'.")
	    if not isinstance(self.social_media, dict):
	        raise TypeError("'social_media' attribute must be a dictionary.")
	    try:
	        return self.social_media[media_name]
	    except KeyError:
	        return None

    def interactive_mix__get_social(self, media_name):
	    if isinstance(media_name, str) and media_name in self.social_media:
	        return self.social_media[media_name]
	    return None

    def baseline__get_social(self, media_name):
	    if media_name in self.social_media:
		    return self.social_media[media_name]
