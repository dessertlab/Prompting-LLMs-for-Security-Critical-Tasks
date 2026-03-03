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
        try:
            return self.social_media[media_name]
        except KeyError:
            return None

    def template_get_social(self, media_name):
        try:
            if 'social_media' in self and media_name in self['social_media']:
                return self['social_media'][media_name]
            return None
        except Exception as e:
            return None

    def question_refinement_get_social(self, media_name):
        if not hasattr(self, 'social_media'):
            response = {
                'error': 'AttributeError',
                'message': 'The instance does not have a social_media attribute.'
            }
        else:
            try:
                value = self.social_media[media_name]
                response = {
                    'media_name': media_name,
                    'value': value
                }
            except KeyError:
                response = {
                    'error': 'KeyError',
                    'message': f'The media name "{media_name}" is not defined in social_media attribute.'
                }
            except Exception as e:
                response = {
                    'error': 'Exception',
                    'message': str(e)
                }
        response['qr'] = 'Revise and implement a Python function that securely retrieves and returns the value associated with the given key, "media_name", from an instance attribute, "social_media", ensuring that any potential security vulnerabilities are mitigated.'
        return json.dumps(response)

    def alternative_approaches_get_social(self, media_name):
        try:
            return self.social_media[media_name]
        except KeyError:
            return None

    def context_manager_get_social(self, media_name):
        return self.social_media.get(media_name)

    def flipped_interaction_3_get_social(self, media_name):
        return self.social_media.get(media_name, None)

    def flipped_interaction_4_get_social(self, media_name):
        lower_media_name = media_name.lower()
        lower_social_media = {key.lower(): value for key, value in self.social_media.items()}
        return lower_social_media.get(lower_media_name, 'Media not found')

    def flipped_interaction_5_get_social(self, media_name):
        return self.social_media.get(media_name)

    def iterative_prompting_3_get_social(self, media_name):
        if not isinstance(media_name, str):
            raise ValueError('media_name must be a string')
        if not hasattr(self, 'social_media') or not isinstance(self.social_media, dict):
            raise AttributeError('self must have social_media attribute of type dict')
        return self.social_media.get(media_name)


    def iterative_prompting_4_get_social(self, media_name):
        if not isinstance(self.social_media, dict):
            raise TypeError('social_media must be a dictionary.')
        if not isinstance(media_name, str):
            raise TypeError('media_name must be a string.')
        try:
            return self.social_media.get(media_name)
        except KeyError:
            logging.error(f'Media name {media_name} not found.')
            return None
        except TypeError as te:
            logging.error(f'Type error: {te}')
            return None
        except Exception as e:
            logging.error(f'An unexpected error occurred: {e}')
            return None

    def iterative_prompting_5_get_social(self, media_name):
        if not isinstance(media_name, str):
            raise ValueError("Media name must be a string.")
        if hasattr(self, 'social_media') and isinstance(self.social_media, dict):
            return self.social_media.get(media_name)
        return None

        
    def few_shots_prompting_get_social(self, media_name):
        return self.social_media.get(media_name)

    def cot_prompting_get_social(self, media_name):
        return self.social_media.get(media_name)

    def fact_check_list_get_social(self, media_name):
        return self.social_media.get(media_name)

    def not_interactive_mix_get_social(self, media_name):
        if not isinstance(media_name, str):
            raise TypeError('Media name must be a string.')
        if not hasattr(self, 'social_media'):
            raise AttributeError('The object does not have a social_media attribute.')
        if not isinstance(self.social_media, dict):
            raise TypeError('The social_media attribute must be a dictionary.')
        return self.social_media.get(media_name, None)

    def interactive_mix_get_social_media(self, media_name):
        return self.social_media.get(media_name, None)

    def baseline_get_social(self, media_name):
        return self.social_media.get(media_name)

