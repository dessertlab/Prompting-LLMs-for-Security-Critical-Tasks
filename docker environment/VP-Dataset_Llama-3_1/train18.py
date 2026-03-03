import re
import urllib
from urllib.parse import urlparse
import logging

class TweetClient:

    def __init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()

    def get_tweets(self):
        simulated_tweets = [
            {'geo': None, 'tweet': 'Visitando Roma oggi! Che bella città! #Roma #Viaggi http://visitroma.it'},
            {'geo': 'Milano', 'tweet': 'La moda a Milano è incredibile. @fashionista #Milano #Moda https://example.com'},
            {'geo': None, 'tweet': 'Buongiorno a tutti da Napoli. @napoli_fan #Napoli https://example.org/'},
            {'geo': None, 'tweet': 'Giornata di sole a Firenze. #Firenze #Sole https://jsonplaceholder.typicode.com'},
            {'geo': 'Venezia', 'tweet': 'Passeggiando per i canali di Venezia. #Venezia https://designer.mocky.io/'},
        ]
        return simulated_tweets

    def ground_truth_code_find_interests(self):
        interests = {
            'links': [],
            'users': [],
            'hashtags': []
        }

        for tweet in self.tweets:
            text = tweet['tweet']
            links = re.compile('(http.*?)\Z|(http.*?) ').findall(text)

            for link in links:
                if link[0]:
                    link = link[0]
                elif link[1]:
                    link = link[1]
                else:
                    continue
            interests['links'].append(link)

            #try:
            #	response = urllib.request.urlopen(link)
            #	full_link = response.url
            #	interests['links'].append(full_link)
            #except:
            #	pass

            interests['users'] += re.compile('(@\w+)').findall(text)
            interests['hashtags'] += re.compile('(#\w+)').findall(text)

        interests['users'].sort()
        interests['hashtags'].sort()
        interests['links'].sort()
        return interests
    
    

    def persona_find_interests(self):
        users = []
        hashtags = []
        links = []
        for tweet in self.tweets:
            words = tweet['tweet'].split()
            for word in words:
                if word.startswith('@') and word not in users:
                    users.append(word[1:])
                if word.startswith('#') and word not in hashtags:
                    hashtags.append(word[1:])
                if word.startswith('http') and word not in links:
                    links.append(word)
        return {'users': users, 'hashtags': hashtags, 'links': links}



    def template_find_interests(self):
        try:
            interests = []
            for tweet in self.tweets:
                tweet_interests = {}
                tweet_interests['users'] = []
                tweet_interests['hashtags'] = []
                tweet_interests['links'] = []
                for word in tweet['tweet'].split():
                    if word.startswith('@'):
                        tweet_interests['users'].append(word[1:])
                    elif word.startswith('#'):
                        tweet_interests['hashtags'].append(word[1:])
                    elif word.startswith('http'):
                        tweet_interests['links'].append(word)
                interests.append(tweet_interests)
            return {'interests': interests}
        except AttributeError as e:
            print(f"An AttributeError occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")



    def question_refinement_find_interests(self, tweet):
        extracted_data = []
        try:
            links = [word for word in tweet.split() if word.startswith('http')]
            info = {}
            info['links'] = links
            users = [word for word in tweet.split() if word.startswith('@')]
            info['users'] = users
            hashtags = [word for word in tweet.split() if word.startswith('#')]
            info['hashtags'] = hashtags
            info['tweet'] = tweet
            extracted_data.append(info)
        except Exception as e:
            extracted_data.append({'error': str(e), 'tweet': tweet})
        return extracted_data



    def alternative_approaches_find_interests(self):
        tweet_results = {}
        for index, tweet in enumerate(self.tweets):
            tweet_results[index] = {'links': [], 'users': [], 'hashtags': []}
            for word in tweet['tweet'].split():
                if word.startswith('http'):
                    tweet_results[index]['links'].append(word)
                elif word.startswith('@'):
                    user = word[1:]
                    tweet_results[index]['users'].append(user)
                elif word.startswith('#'):
                    hashtag = word[1:]
                    tweet_results[index]['hashtags'].append(hashtag)
        return tweet_results


    def context_manager_find_interests(self):
        def get_hashtags(tweet):
            return [word for word in tweet.split() if word.startswith('#')]

        def get_users(tweet):
            return [word for word in tweet.split() if word.startswith('@')]

        def get_links(tweet):
            return [word for word in tweet.split() if word.startswith('http')]

        result = {}
        for i, tweet in enumerate(self.tweets):
            result[i] = {
                'links': get_links(tweet['tweet']),
                'users': get_users(tweet['tweet']),
                'hashtags': get_hashtags(tweet['tweet'])
            }
        return result


    def flipped_interaction_3__find_interests(self):
        links = []
        users = []
        hashtags = []
        for tweet in self.tweets:
            text = tweet['tweet']
            import urllib.parse
            import requests
            for word in text.split():
                if word.startswith('http'):
                    try:
                        link = requests.head(word, allow_redirects=True).url
                        links.append(urllib.parse.urlparse(link).netloc)
                    except Exception as e:
                        pass
            for word in text.split():
                if word.startswith('@'):
                    users.append(word[1:])
            for word in text.split():
                if word.startswith('#'):
                    hashtags.append(word[1:])
            return {'links': sorted(list(set(links))), 'users': sorted(list(set(users))),
                    'hashtags': sorted(list(set(hashtags)))}


    def flipped_interaction_4__find_interests(self):
        links = set()
        users = set()
        hashtags = set()
        for tweet in self.tweets:
            tweet_text = tweet['tweet'].lower()
            links.update([url for url in tweet_text.split() if url.startswith('http')])
            users.update([user[1:] for user in tweet_text.split() if user.startswith('@')])
            hashtags.update([hashtag[1:] for hashtag in tweet_text.split() if hashtag.startswith('#')])
        return {'links': sorted(list(links)), 'users': sorted(list(users)), 'hashtags': sorted(list(hashtags))}




    def flipped_interaction_5__find_interests(self):
        link_pattern = re.compile(r'https?://\S+')
        user_pattern = re.compile(r'@\w+')
        hashtag_pattern = re.compile(r'#\w+')
        interests = []
        for tweet in self.tweets:
            links = []
            users = []
            hashtags = []
            links.extend(link_pattern.findall(tweet['tweet']))
            users.extend(user_pattern.findall(tweet['tweet']))
            hashtags.extend(hashtag_pattern.findall(tweet['tweet']))
            interests.append({'tweet': tweet['tweet'], 'links': links, 'users': users, 'hashtags': hashtags})
        return interests


    def iterative_prompting_3__find_interests(self):
        if not hasattr(self, 'tweets') or not self.tweets:
            raise AttributeError('Tweets not found')
        links = []
        users = []
        hashtags = []
        for tweet in self.tweets:
            if not isinstance(tweet, dict) or 'tweet' not in tweet:
                raise ValueError('Invalid tweet format')
            text = tweet['tweet']
            if not isinstance(text, str):
                raise ValueError('Tweet text must be a string')
            words = text.split()
            for word in words:
                if word.startswith('http'):
                    if urllib.parse.urlparse(word).scheme in ['http', 'https']:
                        links.append(word)
                elif word.startswith('@'):
                    if len(word) > 1 and word[1:].isalnum():
                        users.append(word[1:])
                elif word.startswith('#'):
                    if len(word) > 1 and word[1:].isalnum():
                        hashtags.append(word[1:])
        return {'links': links, 'users': users, 'hashtags': hashtags}

    def iterative_prompting_4__find_interests(self):
        if not hasattr(self, 'tweets') or not self.tweets:
            raise ValueError('No tweets available')
        for tweet in self.tweets:
            if 'tweet' not in tweet:
                raise KeyError('Invalid tweet format')
            link_list = []
            user_list = []
            hashtag_list = []
            words = tweet['tweet'].split()
            for word in words:
                if word.startswith('http'):
                    try:
                        result = urlparse(word)
                        if all([result.scheme, result.netloc]):
                            link_list.append(word.strip('\x00'))
                    except (ValueError, TypeError):
                        return("Error: link couldn't be properly formatted")
                elif word.startswith('@'):
                    try:
                        if len(word) > 1 and word[1:].isalnum():
                            user_list.append(word.strip('\x00'))
                    except TypeError:
                        return("Error: user couldn't be properly formatted")
                elif word.startswith('#'):
                    try:
                        if len(word) > 1 and word[1:].isalnum():
                            hashtag_list.append(word.strip('\x00'))
                    except TypeError:
                        return("Error: hashtag couldn't be properly formatted")
            if link_list or user_list or hashtag_list:
                return {'links': link_list, 'users': user_list, 'hashtags': hashtag_list}


    def iterative_prompting_5__find_interests(self):
        if not hasattr(self, 'tweets') or not self.tweets:
            raise ValueError('No tweets found.')
        for tweet in self.tweets:
            if 'tweet' not in tweet:
                raise ValueError('Invalid tweet format.')
            links = []
            users = []
            hashtags = []
            try:
                words = tweet['tweet'].split()
                for word in words:
                    if urllib.parse.urlparse(word).scheme:
                        links.append(word)
                    elif word.startswith('@'):
                        users.append(word.lstrip('@'))
                    elif word.startswith('#'):
                        hashtags.append(word.lstrip('#'))
                print('Links:', links)
                print('Users:', users)
                print('Hashtags:', hashtags)
                return {'links': links, 'users': users, 'hashtags': hashtags}
            except urllib.error.URLError as e:
                return('URLError occurred: %s', e)
            except Exception as e:
                return('An error occurred: %s', e)
            else:
                return('Tweet processed successfully.')

    def few_shots_prompting_find_interests(self):
        for tweet in self.tweets:
            links = re.findall(r'https?://\S+', tweet['tweet'])
            users = re.findall(r'@[\w]+', tweet['tweet'])
            hashtags = re.findall(r'#[\w]+', tweet['tweet'])
        return {'links': links, 'users': users, 'hashtags': hashtags}

    def cot_prompting_find_interests(self):
        for tweet in self.tweets:
            links = [word for word in tweet['tweet'].split() if word.startswith('http')]
            users = [word for word in tweet['tweet'].split() if word.startswith('@')]
            hashtags = [word for word in tweet['tweet'].split() if word.startswith('#')]
        return {'links': links, 'users': users, 'hashtags': hashtags}


    def fact_check_list_find_interests(self):
        interests = []
        for tweet in self.tweets:
            tweet_interests = {
                'tweet': tweet['tweet'],
                'links': self.extract_links(tweet['tweet']),
                'users': self.extract_users(tweet['tweet']),
                'hashtags': self.extract_hashtags(tweet['tweet'])
            }
            interests.append(tweet_interests)
        return interests

    def not_interactive_mix_find_interests(self):
        interests = []
        for tweet in self.tweets:
            tweet_interests = {}
            try:
                links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                tweet['tweet'])
                users = re.findall('@([a-zA-Z0-9_]+)', tweet['tweet'])
                hashtags = re.findall('#([a-zA-Z0-9_]+)', tweet['tweet'])
                tweet_interests['links'] = links
                tweet_interests['users'] = users
                tweet_interests['hashtags'] = hashtags
            except Exception as e:
                return(f'Error processing tweet: {e}')
            interests.append(tweet_interests)
        return interests

    def interactive_mix_find_interests(tweets):
        interests = {"links": [], "users": [], "hashtags": [], "tweets": []}
        for tweet in tweets:
            tweet_interests = {"text": tweet, "links": [], "users": [], "hashtags": []}
            for link in re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                tweet):
                parsed_url = urlparse(link)
                tweet_interests["links"].append(f"{parsed_url.scheme}://{parsed_url.netloc}")
                if f"{parsed_url.scheme}://{parsed_url.netloc}" not in interests["links"]:
                    interests["links"].append(f"{parsed_url.scheme}://{parsed_url.netloc}")
            users = re.findall(r'@\w+', tweet)
            for user in users:
                if user not in interests["users"]:
                    interests["users"].append(user)
            tweet_interests["users"] = users
            hashtags = re.findall(r'#\w+', tweet)  # Aggiunto il pattern per gli hashtag
            for hashtag in hashtags:
                if hashtag not in interests["hashtags"]:
                    interests["hashtags"].append(hashtag)
            tweet_interests["hashtags"] = hashtags
            interests["tweets"].append(tweet_interests)
        return interests

    def baseline_find_interests(self):
        tweets_data = []
        for tweet in self.tweets:
            data = {}
            data['tweet'] = tweet['tweet']
            data['links'] = [word for word in tweet['tweet'].split() if word.startswith('http')]
            data['users'] = [word for word in tweet['tweet'].split() if word.startswith('@')]
            data['hashtags'] = [word for word in tweet['tweet'].split() if word.startswith('#')]
            tweets_data.append(data)
        return tweets_data

