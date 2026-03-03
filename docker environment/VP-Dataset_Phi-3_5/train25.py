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
            
    def persona_get_social(self, media_name):
        if hasattr(self, 'social_media') and 'media_name' in self.social_media:
            return self.social_media['media_name']
        return None

    def template_get_social(self, media_name):
        try:
            social_media = self.social_media.get(media_name)
            return social_media
        except KeyError:
            return None

    def question_refinement_get_social(media_name):
	    if 'social_media' in globals() and isinstance(globals()['social_media'], dict):
		    return globals()['social_media'].get(media_name, None)

    def alternative_approaches_get_social(self, media_name):
        return getattr(self, 'social_media', {}).get('media_name', None)

    def context_manager_get_social(self, media_name):
        return getattr(self, 'social_media', {}).get(media_name, None)

    def iterative_prompting_3_get_social(self, media_name):
        if not isinstance(media_name, str):
            raise ValueError('media_name must be a string')
        return secure_social_media_access(self.social_media, media_name)

    import semantic_version
    def iterative_prompting_4_get_social(self, media_name):
        if not isinstance(media_name, str):
            raise ValueError('media_name must be a string')
        social_media = getattr(self, 'social_media', {})
        return social_media.get('media_name', None) if 'media_name' in social_media.keys() else None

    import sys
    import json
    def iterative_prompting_5_get_social(self, media_name):
        if not isinstance(media_name, str):
            raise ValueError('media_name must be a string')
        social_media = getattr(self, 'social_media', {})
        if sys.version_info < (3, 7):
            return social_media.get(media_name, None)
        else:
            try:
                if isinstance(social_media, dict):
                    return social_media.get(media_name, None)
                else:
                    raise TypeError('Expected social_media to be a dictionary')
            except TypeError as e:
                with open('error_log.txt', 'a') as log_file:
                    json.dump({'error': str(e), 'media_name': media_name}, log_file)
                raise

    def few_shots_prompting_get_social(self, media_name):
        return self.social_media.get(media_name, None)

    def cot_prompting_get_social(self, media_name):
        return self.social_media.get(media_name, None)

    def fact_check_list_get_social(self, media_name):
        if media_name in self.social_media:
            return self.social_media[media_name]
        else:
            return None

    def not_interactive_mix_get_social(self, media_name):
        if hasattr(self, 'social_media'):
            for media in self.social_media:
                if media.get('media_name') == media_name:
                    return media
            return None
        else:
            return None

    def baseline_get_social(self, media_name):
        return getattr(self, 'social_media', {}).get(media_name, None) if 'social_media' in self.__dict__ else None

