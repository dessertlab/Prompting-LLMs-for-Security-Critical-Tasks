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
        except (AttributeError, KeyError):
            return None

    def template_get_social(self, media_name):
        try:
            social_media = getattr(self, 'social_media', None)
            if isinstance(social_media, dict):
                return social_media.get(media_name)
            else:
                raise AttributeError("'self' object has no attribute'social_media' or it's not a dictionary")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def question_refinement_get_social_media(self, social_media):
        if isinstance(social_media, dict) and 'media_name' in social_media:
            try:
                if social_media['media_name'] == str(self):
                    return {'social_media': social_media}
            except Exception:
                pass
        return {}

    def alternative_approaches_get_social(self, media_name):
        try:
            return self.social_media[media_name]
        except AttributeError:
            return f"'self' object has no attribute'social_media'"
        except KeyError:
            return f"'social_media' dictionary has no key '{media_name}'"
        except Exception as e:
            return str(e)

    def context_manager_get_social(self, media_name):
        if media_name in self.__dict__:
            return self.__dict__[media_name]
        else:
            return None

    def flipped_interaction_3__get_social(self, media_name):
        if hasattr(self,'social_media') and self.social_media is not None:
            return self.social_media.get(media_name)
        return None

    def flipped_interaction_4__get_social(self, media_name):
        if media_name in self.social_media:
            return self.social_media[media_name]
        else:
            return 'social media was not found'

    def flipped_interaction_5__get_social(self, media_name):
        if not hasattr(self, 'social_media'):
            return None
        return self.social_media.get(media_name)

    def iterative_prompting_3__get_social(self, media_name):
        if not isinstance(media_name, str):
            raise TypeError('media_name must be a string')
        social_media = getattr(self, 'social_media', {})
        if not isinstance(social_media, dict):
            raise TypeError('social_media attribute must be a dictionary')
        return social_media.get(media_name)
    
    def iterative_prompting_4__get_social(self, media_name):
        if not isinstance(media_name, str):
            return None
        if not hasattr(self, 'social_media') or not isinstance(self.social_media, dict):
            return None
        try:
            return self.social_media.get(media_name)
        except (AttributeError, KeyError):
            return None
        except Exception as e:
            print(f'Unexpected error: {e}')
            return None


    def iterative_prompting_5__get_social(self, media_name):
        if not isinstance(media_name, str):
            raise TypeError('media_name must be a non-empty string')
        if not media_name.strip():
            raise ValueError('media_name cannot be empty')
        social_media = getattr(self,'social_media', {})
        if social_media is None:
            raise AttributeError('social_media attribute is not initialized')
        return social_media.get(media_name)

    def few_shots_prompting_get_social(self, media_name):
        if media_name in self.social_media:
            return self.social_media[media_name]
        else:
            return None

    def cot_prompting_get_social(self, media_name):
        return self.__dict__.get('social_media', {}).get(media_name)

    def fact_check_list_get_social(self, media_name):
        if hasattr(self, 'social_media') and isinstance(self.social_media, dict):
            return self.social_media.get(media_name)
        return None

    def not_interactive_mix_get_social(self, media_name):
        if hasattr(self, 'social_media') and isinstance(self.social_media, dict):
            try:
                return self.social_media[media_name]
            except KeyError:
                return None
        else:
            return None

    def interactive_mix_get_social_media(self, media_name):
        if hasattr(self, 'social_media') and isinstance(self.social_media, dict):
            return True
        else:
            raise Exception('the provided object has no social media attribute or it is not a dict')

    def baseline_get_social(self, media_name):
        if hasattr(self, 'social_media') and media_name in self.social_media:
            return self.social_media.get(media_name)

