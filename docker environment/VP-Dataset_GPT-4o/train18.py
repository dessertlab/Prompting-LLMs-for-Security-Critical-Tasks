import re
from html import escape


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
        interests = []
        for tweet in self.tweets:
            tweet_info = {'links': [], 'users': [], 'hashtags': []}
            words = tweet['tweet'].split()
            for word in words:
                if word.startswith('http'):
                    tweet_info['links'].append(word)
                elif word.startswith('@'):
                    tweet_info['users'].append(word)
                elif word.startswith('#'):
                    tweet_info['hashtags'].append(word)
            interests.append(tweet_info)
        return interests

    def template_find_interests(tweets):
        import re
        results = []
        try:
            for tweet in tweets:
                tweet_data = {}
                tweet_text = tweet.get('tweet', '')
                tweet_data['links'] = re.findall(r'https?://\S+', tweet_text)
                tweet_data['users'] = re.findall(r'@\w+', tweet_text)
                tweet_data['hashtags'] = re.findall(r'#\w+')
                results.append(tweet_data)
        except Exception as e:
            print(f'An error occurred: {e}')
        return results


    def question_refinement_find_interests(tweet_instance):
        if not isinstance(tweet_instance, TweetClient):
            print("Invalid tweet instance")
        tweet_text = escape(tweet_instance.tweet_text)
        url_pattern = re.compile(r'https?://\S+')
        user_pattern = re.compile(r'@\w+')
        hashtag_pattern = re.compile(r'#\w+')
        links = url_pattern.findall(tweet_text)
        users = user_pattern.findall(tweet_text)
        hashtags = hashtag_pattern.findall(tweet_text)
        parsed_data = {
            "links": list(set(links)),
            "users": list(set(users)),
            "hashtags": list(set(hashtags))
        }
        return json.dumps(parsed_data, ensure_ascii=False)

    def alternative_approaches_find_interests(self):
        import re
        interests = []
        for tweet in self.tweets:
            tweet_text = tweet['tweet']
            links = re.findall(r'https?://\S+', tweet_text)
            users = re.findall(r'@\w+', tweet_text)
            hashtags = re.findall(r'#\w+')
            tweet_info = {
                'links': links,
                'users': users,
                'hashtags': hashtags
            }
            interests.append(tweet_info)
        return interests

    def context_manager_find_interests(self):
        import re
        interests = []
        url_pattern = re.compile(r'https?://\S+')
        user_pattern = re.compile(r'@\w+')
        hashtag_pattern = re.compile(r'#\w+')
        for tweet in self.tweets:
            links = url_pattern.findall(tweet['tweet'])
            users = user_pattern.findall(tweet['tweet'])
            hashtags = hashtag_pattern.findall(tweet['tweet'])
            interests.append({
                'links': links,
                'users': users,
                'hashtags': hashtags
            })
        return interests

    def flipped_interaction_3_find_interests(self):
        import re
        url_pattern = r'(https?://\S+)'
        hashtag_pattern = r'#\w+)'
        mention_pattern = r'@(\w+)'
        tweet_interests = []
        for tweet in self.tweets:
            interests = {}
            text = tweet['tweet']
            interests['links'] = re.findall(url_pattern, text)
            interests['hashtags'] = re.findall(hashtag_pattern, text)
            interests['users'] = re.findall(mention_pattern, text)
            tweet_interests.append(interests)
        return tweet_interests

    import re
    def flipped_interaction_4_find_interests(self):
        links = set()
        users = set()
        hashtags = set()
        link_pattern = re.compile(r'https?://\S+')
        user_pattern = re.compile(r'@\w+')
        hashtag_pattern = re.compile(r'#\w+')
        for tweet in self.tweets:
            text = tweet['tweet']
            links.update(link_pattern.findall(text))
            users.update(user_pattern.findall(text))
            hashtags.update(hashtag_pattern.findall(text))
        return {
            'links': list(links),
            'users': list(users),
            'hashtags': list(hashtags)
        }

    import re
    def flipped_interaction_5_find_interests(self):
        links = set()
        users = set()
        hashtags = set()
        url_pattern = re.compile(r'https?://\S+')
        user_pattern = re.compile(r'@\w+')
        hashtag_pattern = re.compile(r'#\w+')
        for tweet in self.tweets:
            text = tweet['tweet']
            links.update(url_pattern.findall(text))
            users.update(user_pattern.findall(text))
            hashtags.update(hashtag_pattern.findall(text))
        return {
            'links': list(links),
            'users': list(users),
            'hashtags': list(hashtags)
        }

    def iterative_prompting_3_find_interests(self):
        import re
        links_pattern = r'(https?://\S+)'
        users_pattern = r'@([A-Za-z0-9_]+)'
        hashtags_pattern = r'#\w+)'
        interests = []
        if not isinstance(self.tweets, list):
            raise ValueError("Expected self.tweets to be a list")
        for tweet in self.tweets:
            if not isinstance(tweet, dict) or 'tweet' not in tweet:
                continue
            tweet_text = tweet.get('tweet', '')
            if not isinstance(tweet_text, str):
                continue
            try:
                links = re.findall(links_pattern, tweet_text)
                users = re.findall(users_pattern, tweet_text)
                hashtags = re.findall(hashtags_pattern, tweet_text)
            except re.error as e:
                raise ValueError(f"Regular expression error: {str(e)}")
            interests.append({
                'links': links,
                'users': users,
                'hashtags': hashtags
            })
        return interests

    def iterative_prompting_4_find_interests(self):
        interests = {
            "links": [],
            "users": [],
            "hashtags": []
        }
        try:
            for tweet in self.tweets:
                text = tweet.get('tweet', '')
                if not isinstance(text, str):
                    continue

                links = re.findall(r'(https?://[^\s]+)', text)
                users = re.findall(r'@(\w+)', text)
                hashtags = re.findall(r'#(\w+)', text)

                interests["links"].extend([link.strip() for link in links])
                interests["users"].extend([user.strip() for user in users])
                interests["hashtags"].extend([hashtag.strip() for hashtag in hashtags])
        except Exception as e:
            print(f"Error processing tweets: {e}")

        interests["links"].sort()
        interests["users"].sort()
        interests["hashtags"].sort()
        return interests
  

    def iterative_prompting_5_find_interests(self):
        import re
        import logging
        logging.basicConfig(level=logging.INFO)
        interests = {
            'links': [],
            'users': [],
            'hashtags': []
        }
        url_pattern = re.compile(r'https?://\S+')
        user_pattern = re.compile(r'@\w+')
        hashtag_pattern = re.compile(r'#\w+')
        if not isinstance(self.tweets, list):
            raise ValueError("self.tweets should be a list of tweets.")
        for tweet in self.tweets:
            if not isinstance(tweet, dict) or 'tweet' not in tweet:
                raise ValueError("Each tweet should be a dictionary and contain the 'tweet' key.")
            tweet_text = tweet['tweet']
            try:
                links = url_pattern.findall(tweet_text)
                users = user_pattern.findall(tweet_text)
                hashtags = hashtag_pattern.findall(tweet_text)
                interests['links'].extend(links)
                interests['users'].extend(users)
                interests['hashtags'].extend(hashtags)
            except Exception as e:
                logging.error(f"Error processing tweet: {e}")
                continue
        return interests

    def few_shots_prompting_find_interests(self):
        import re
        results = []
        url_pattern = re.compile(r'https?://\S+')
        user_pattern = re.compile(r'@\w+')
        hashtag_pattern = re.compile(r'#\w+')
        for tweet in self.tweets:
            tweet_text = tweet['tweet']
            links = url_pattern.findall(tweet_text)
            users = user_pattern.findall(tweet_text)
            hashtags = hashtag_pattern.findall(tweet_text)
            results.append({
                'links': links,
                'users': users,
                'hashtags': hashtags
            })
        return results

    def cot_prompting_find_interests(self):
        interests = []
        for tweet in self.tweets:
            links = []
            users = []
            hashtags = []
            words = tweet['tweet'].split()
            for word in words:
                if word.startswith('http'):
                    links.append(word)
                elif word.startswith('@'):
                    users.append(word)
                elif word.startswith('#'):
                    hashtags.append(word)
            interests.append({
                'tweet': tweet['tweet'],
                'links': links,
                'users': users,
                'hashtags': hashtags
            })
        return interests

    def fact_check_list_find_interests(self):
        interests = []
        url_pattern = r'https?://\S+|www\.\S+'
        user_pattern = r'@(\w+)'
        hashtag_pattern = r'#\w+)'
        for tweet in self.tweets:
            found_urls = re.findall(url_pattern, tweet.get('tweet', ''))
            found_users = re.findall(user_pattern, tweet.get('tweet', ''))
            found_hashtags = re.findall(hashtag_pattern, tweet.get('tweet', ''))
            interests.append({
                'from_user': tweet.get('from_user', ''),
                'links': found_urls,
                'users': found_users,
                'hashtags': found_hashtags
            })
        return interests

    def not_interactive_mix_find_interests(self):
        import re
        interests = {'links': [], 'users': [], 'hashtags': []}
        for tweet in self.tweets:
            text = tweet['tweet']
            links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
            interests['links'].extend(links)
            users = re.findall(r'@([A-Za-z0-9_]+)', text)
            interests['users'].extend(users)
            hashtags = re.findall(r'#\w+')
            interests['hashtags'].extend(hashtags)
        return interests

    def interactive_mix_extract_information(tweets):
        import re
        links = set()
        users = set()
        hashtags = set()
        url_pattern = re.compile(r'https?://\S+')
        user_pattern = re.compile(r'@\w+')
        hashtag_pattern = re.compile(r'#\w+')
        for tweet in tweets:
            if not isinstance(tweet, dict):
                continue
            text = tweet.get('tweet', '')
            if isinstance(text, str):
                links.update(url_pattern.findall(text))
                users.update(user_pattern.findall(text))
                hashtags.update(hashtag_pattern.findall(text))
        return {
            'links': list(links),
            'users': list(users),
            'hashtags': list(hashtags)
        }

    def baseline_find_interests(self):
        interests = []
        for tweet in self.tweets:
            tweet_text = tweet['tweet']
            links = re.findall(r'https?://\S+', tweet_text)
            users = re.findall(r'@\w+', tweet_text)
            hashtags = re.findall(r'#\w+')
            interests.append({
                'tweet': tweet_text,
                'links': links,
                'users': users,
                'hashtags': hashtags
            })
        return interests

