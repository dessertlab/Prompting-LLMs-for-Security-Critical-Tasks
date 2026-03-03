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
            links = re.compile(r'(http.*?)\Z|(http.*?) ').findall(text)

            for link in links:
                if link[0]:
                    link = link[0]
                elif link[1]:
                    link = link[1]
                else:
                    continue
                interests['links'].append(link)

            # try:
            #     response = urllib.request.urlopen(link)
            #     full_link = response.url
            #     interests['links'].append(full_link)
            # except:
            #     pass

            interests['users'] += re.compile(r'(@\w+)').findall(text)
            interests['hashtags'] += re.compile(r'(#\w+)').findall(text)

        interests['users'].sort()
        interests['hashtags'].sort()
        interests['links'].sort()
        return interests

    def persona__find_interests(self):
        import re
        interests = {}
        interests["links"] = []
        interests["users"] = []
        interests["hashtags"] = []
        for tweet in self.tweets:
            tweet_text = tweet["tweet"]
            links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet_text)
            users = re.findall(r'@([a-zA-Z0-9_]+)', tweet_text)
            hashtags = re.findall(r'#([A-Za-z0-9_]+)', tweet_text)
            interests["links"].extend(links)
            interests["users"].extend(users)
            interests["hashtags"].extend(hashtags)
        interests["links"] = list(set(interests["links"]))
        interests["users"] = list(set(interests["users"]))
        interests["hashtags"] = list(set(interests["hashtags"]))
        return interests

    def template__find_interests(self):
        try:
            links = set()
            users = set()
            hashtags = set()
            for tweet in self.tweets:
                tweet_text = tweet['tweet']
            return {'links': links, 'users': users, 'hashtags': hashtags}
        except Exception:
            pass


    def question_refinement__find_interests(tweet):
        tweet_data = {'links': [], 'users': [], 'hashtags': []}
        import re
        for link in re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet):
            tweet_data['links'].append(link)
        for user in re.findall(r'@([a-zA-Z0-9_]{1,15})', tweet):
            tweet_data['users'].append(user)
        for hashtag in re.findall(r'#([A-Za-z0-9_]+)', tweet):
            tweet_data['hashtags'].append(hashtag)
        return tweet_data

    def alternative_approaches__find_interests(self):
        import re
        interests = {"links": [], "users": [], "hashtags": []}
        for tweet in self.tweets:
            tweet_text = tweet['tweet']
            interests['links'].extend(
                re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet_text)
            )
            interests['users'].extend(
                re.findall(r'@([a-zA-Z0-9_]{1,15})', tweet_text)
            )
            interests['hashtags'].extend(
                re.findall(r'#([A-Za-z0-9_]+)', tweet_text)
            )
        return interests

    def context_manager__find_interests(self):
        import re
        links = []
        users = set()
        hashtags = set()
        for tweet in self.tweets:
            urls = re.findall(
                r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                tweet['tweet']
            )
            links.extend(urls)
            mentioned_users = re.findall(r'@([a-zA-Z0-9_]+)', tweet['tweet'])
            users.update(mentioned_users)
            found_hashtags = re.findall(r'#([A-Za-z0-9_]+)', tweet['tweet'])
            hashtags.update(found_hashtags)
        return {'links': links, 'users': list(users), 'hashtags': list(hashtags)}

    def flipped_interaction_3__find_interests(self):
        links = set()
        users = set()
        hashtags = set()
        for tweet in self.tweets:
            tweet_text = tweet['tweet']
            link_pattern = re.compile(
                r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            )
            tweet_links = link_pattern.findall(tweet_text)
            links.update(tweet_links)
            user_pattern = re.compile(r'@(\w+)')
            tweet_users = user_pattern.findall(tweet_text)
            users.update(tweet_users)
            hashtag_pattern = re.compile(r'#(\w+)')
            tweet_hashtags = hashtag_pattern.findall(tweet_text)
            hashtags.update(tweet_hashtags)
        return {
            'links': list(links),
            'users': list(users),
            'hashtags': list(hashtags)
        }

    def flipped_interaction_4__find_interests(self):
        links_set = set()
        users_set = set()
        hashtags_set = set()
        link_pattern = re.compile(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        )
        user_pattern = re.compile(r'@([A-Za-z0-9_]{1,15})')
        hashtag_pattern = re.compile(r'#([A-Za-z0-9_]+)')
        for tweet in self.tweets:
            tweet_text = tweet['tweet']
            links = link_pattern.findall(tweet_text)
            links_set.update(links)
            users = user_pattern.findall(tweet_text)
            users_set.update(users)
            hashtags = hashtag_pattern.findall(tweet_text)
            hashtags_set.update(hashtags)
        return {
            'links': sorted(links_set),
            'users': sorted(users_set),
            'hashtags': sorted(hashtags_set)
        }

    def flipped_interaction_5__find_interests(self):
        links = []
        users = []
        hashtags = []
        link_pattern = re.compile(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        )
        user_pattern = re.compile(r'@(\w+)')
        hashtag_pattern = re.compile(r'#(\w+)')
        for tweet in self.tweets:
            tweet_text = tweet['tweet']
            links.extend(link_pattern.findall(tweet_text))
            users.extend(user_pattern.findall(tweet_text))
            hashtags.extend(hashtag_pattern.findall(tweet_text))
        return {'links': list(set(links)), 'users': list(set(users)), 'hashtags': list(set(hashtags))}

    def iterative_prompting_3__find_interests(self):
        import re
        links = []
        users = []
        hashtags = []
        for tweet in self.tweets:
            try:
                tweet_text = tweet['tweet']
                links.extend(re.findall(r'https?://[^\s]+', tweet_text))
                users.extend(re.findall(r'@\w+', tweet_text))
                hashtags.extend(re.findall(r'#\w+', tweet_text))
            except TypeError:
                continue
            except KeyError:
                continue
        return {'links': links, 'users': users, 'hashtags': hashtags}

    def iterative_prompting_4__find_interests(self):
        links = []
        users = []
        hashtags = []
        if not isinstance(self.tweets, list):
            raise ValueError('self.tweets must be a list')
        for tweet in self.tweets:
            if not isinstance(tweet, dict) or 'tweet' not in tweet:
                continue
            try:
                tweet_text = tweet['tweet']
                links.extend(
                    re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet_text)
                )
                users.extend(re.findall(r'@[a-zA-Z0-9_]+', tweet_text))
                hashtags.extend(re.findall(r'#\w+', tweet_text))
            except re.error as e:
                print(f'Regex error processing tweet: {e}')
            except Exception as e:
                print(f'Unexpected error processing tweet: {e}')
        return {'links': list(set(links)), 'users': list(set(users)), 'hashtags': list(set(hashtags))}

    def iterative_prompting_5__find_interests(self):
        links = set()
        users = set()
        hashtags = set()
        if not isinstance(self.tweets, list):
            return {'links': [], 'users': [], 'hashtags': []}
        for tweet in self.tweets:
            try:
                tweet_text = tweet['tweet']
                if not isinstance(tweet_text, str):
                    continue
                links.update(re.findall(r'(https?://\S+)', tweet_text))
                users.update(re.findall(r'@\w+', tweet_text))
                hashtags.update(re.findall(r'#\w+', tweet_text))
            except (TypeError, KeyError):
                continue
        valid_links = [link for link in links if re.match(r'https?://\w+', link)]
        valid_users = [user for user in users if re.match(r'@\w{1,15}', user)]
        valid_hashtags = [hashtag for hashtag in hashtags if re.match(r'#\w+', hashtag)]
        return {'links': valid_links, 'users': valid_users, 'hashtags': valid_hashtags}

    def few_shots_prompting__find_interests(self):
        links = []
        users = set()
        hashtags = set()
        for tweet in self.tweets:
            text = tweet['tweet']
            links.extend(
                re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
            )
            users.update(re.findall(r'@([a-zA-Z0-9_]+)', text))
            hashtags.update(re.findall(r'#([A-Za-z0-9_]+)', text))
        return {'links': links, 'users': list(users), 'hashtags': list(hashtags)}

    def cot_prompting__find_interests(self):
        links = []
        users = []
        hashtags = []
        import re
        for tweet in self.tweets:
            links.extend(
                re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet['tweet'])
            )
            users.extend(
                re.findall(r'(?<=^|[^a-zA-Z0-9-_\.])@([A-Za-z]+[A-Za-z0-9-_]+)', tweet['tweet'])
            )
            hashtags.extend(re.findall(r'#\w+', tweet['tweet']))
        return {'links': links, 'users': users, 'hashtags': hashtags}

    def fact_check_list__find_interests(self):
        links = set()
        users = set()
        hashtags = set()
        for tweet in self.tweets:
            link_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            found_links = re.findall(link_pattern, tweet['tweet'])
            links.update(found_links)
            user_pattern = r'@[\w-]+'
            found_users = re.findall(user_pattern, tweet['tweet'])
            users.update(found_users)
            hashtag_pattern = r'#\w+'
            found_hashtags = re.findall(hashtag_pattern, tweet['tweet'])
            hashtags.update(found_hashtags)
        return {
            'links': list(links),
            'users': list(users),
            'hashtags': list(hashtags)
        }

    def not_interactive_mix__find_interests(self):
        interests = {'links': set(), 'users': set(), 'hashtags': set()}
        for tweet in self.tweets:
            text = tweet['tweet']
            links = re.findall(r'https?://[^-\s]+', text)
            for link in links:
                interests['links'].add(link)
            users = re.findall(r'@([\w-]+)', text)
            for user in users:
                interests['users'].add(user)
            hashtags = re.findall(r'#\w+', text)
            for hashtag in hashtags:
                interests['hashtags'].add(hashtag)
        return {
            'links': list(interests['links']),
            'users': list(interests['users']),
            'hashtags': list(interests['hashtags'])
        }

    def interactive_mix__find_interests(self):
        interests = {
            'links': [],
            'users': set(),
            'hashtags': set()
        }
        url_pattern = re.compile(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        )
        user_pattern = re.compile(r'@(\w+)')
        hashtag_pattern = re.compile(r'#(\w+)')
        for tweet in self.tweets:
            text = tweet['tweet']
            links = url_pattern.findall(text)
            for link in links:
                try:
                    # requests non è importato in questo file: lascio la chiamata com’è
                    response = requests.head(link, allow_redirects=True, timeout=5)  # noqa: F821
                    interests['links'].append(response.url)
                except Exception:
                    interests['links'].append('BROKEN_LINK')
            users = user_pattern.findall(text)
            for user in users:
                interests['users'].add(user)
            hashtags = hashtag_pattern.findall(text)
            for hashtag in hashtags:
                interests['hashtags'].add(hashtag)
        interests['links'].sort()
        interests['users'] = sorted(interests['users'])
        interests['hashtags'] = sorted(interests['hashtags'])
        return interests

    def baseline__find_interests(self):
        links = []
        users = []
        hashtags = []
        for tweet in self.tweets:
            links.extend(
                re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet['tweet'])
            )
            users.extend(re.findall(r'@[a-zA-Z0-9_]+', tweet['tweet']))
            hashtags.extend(re.findall(r'#\w+', tweet['tweet']))
        return {'links': list(set(links)), 'users': list(set(users)), 'hashtags': list(set(hashtags))}

