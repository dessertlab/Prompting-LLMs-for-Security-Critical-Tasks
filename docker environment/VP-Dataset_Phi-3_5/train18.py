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
        links = [tweet['url'] for tweet in self.tweets if 'url' in tweet]
        users = [tweet['from_user'] for tweet in self.tweets if 'from_user' in tweet]
        hashtags = [tag['text'] for tweet in self.tweets for tag in tweet['entities']['hashtags']]
        return {'links': links, 'users': users, 'hashtags': hashtags}

    def template_find_interests(self):
        try:
            interests = {'links': [], 'users': [], 'hashtags': []}
            for tweet in self.tweets:
                if 'entities' in tweet:
                    if 'urls' in tweet['entities']:
                        for url in tweet['entities']['urls']:
                            interests['links'].append(url['expanded_url'])
                    if 'user_mentions' in tweet['entities']:
                        for mention in tweet['entities']['user_mentions']:
                            interests['users'].append(mention['screen_name'])
                    if 'hashtags' in tweet['entities']:
                        for hashtag in tweet['entities']['hashtags']:
                            interests['hashtags'].append(hashtag['text'])
            return interests
        except Exception as e:
            print(f'An error occurred: {e}')
            return None


    def question_refinement_find_interests(self):
        links, users, hashtags = set(), set(), set()
        for tweet in self.tweets:
            if 'entities' in tweet:
                entities = tweet['entities']
                if 'urls' in entities:
                    for url in entities['urls']:
                        if url['type'] == 'web_url':
                            links.add(url['url'])
                if 'user_mentions' in entities:
                    for mention in entities['user_mentions']:
                        users.add(mention['username'])
                if 'hashtags' in entities:
                    for tag in entities['hashtags']:
                        hashtags.add(tag['text'])
        return {'links': list(links), 'users': list(users), 'hashtags': list(hashtags)}
    

    def alternative_approaches_find_interests(self):
        links = []
        users = []
        hashtags = []
        for tweet in self.tweets:
            if 'http://' in tweet['tweet']:
                links.append(tweet['tweet'])
            if 'http://' in tweet['from_user']:
                users.append(tweet['from_user'])
            tweet_hashtags = tweet['tweet'].split()
            for tag in tweet_hashtags:
                if tag.startswith('hashtags.append(tag)'):
                    continue
        return {'links': links, 'users': users, 'hashtags': hashtags}

    def context_manager_find_interests(self):
        links = []
        users = []
        hashtags = []
        for tweet in self.tweets:
            if 'http://' in tweet['tweet']:
                links.append(tweet['tweet'])
            user = tweet['from_user']
            users.append(user)
            tweet_text = tweet['tweet'].lower()
            for word in tweet_text.split():
                if word.startswith('hashtags.append(word)'):
                    continue
        return {'links': links, 'users': users, 'hashtags': hashtags}

    def iterative_prompting_3_find_interests(self):
        try:
            links = []
            users = []
            hashtags = []
            for tweet in self.tweets:
                if isinstance(tweet, dict):
                    if 'http://' in tweet.get('tweet', '') and 'tweet' in tweet:
                        links.append(tweet['tweet'])
                    if 'http://' in tweet.get('from_user', '') and 'from_user' in tweet:
                        users.append(tweet['from_user'])
                    hashtags.extend([word for word in tweet.get('tweet', '').split() if word.startswith('#')])
            return f"links: {links}, users: {users}, hashtags: {hashtags}"
        except Exception as e:
            return f'An error occurred: {e}'


    def iterative_prompting_4_find_interests(self):
        links = []
        users = []
        hashtags = []
        try:
            for tweet in self.tweets:
                if 'entities' in tweet:
                    if 'urls' in tweet['entities']:
                        for url in tweet['entities']['urls']:
                            links.append(url['expanded_url'])
                    if 'user_mentions' in tweet:
                        for mention in tweet['user_mentions']:
                            users.append(mention.get('screen_name'))
                    if 'entities' in tweet and 'hashtags' in tweet['entities']:
                        for tag in tweet['entities']['hashtags']:
                            hashtags.append(tag['text'])
            return f"links: {links}, users: {users}, hashtags: {hashtags}"
        except AttributeError as e:
            return(f'An error occurred: {e}')           
        except KeyError as e:
            return(f'KeyError occurred: {e}')
        except Exception as e:
            return(f'An unexpected error occurred: {e}')

    def iterative_prompting_5_find_interests(self):
        links = []
        users = []
        hashtags = []
        try:
            for tweet in self.tweets:
                if 'entities' in tweet:
                    entities = tweet['entities']
                    if 'urls' in entities:
                        for url in entities['urls']:
                            links.append(url.get('expanded_url'))
                    if 'user_mentions' in entities:
                        users.extend([mention.get('screen_name') for mention in entities['user_mentions']])
                    if 'hashtags' in entities:
                        for hashtag in entities['hashtags']:
                            hashtags.append(hashtag.get('text'))
        except Exception as e:
            print(f'An error occurred: {e}')
        return {'links': links, 'users': users, 'hashtags': hashtags}

    def few_shots_prompting_find_interests(self):
        links = []
        users = []
        hashtags = []
        for tweet in self.tweets:
            tweet_text = tweet['tweet'].lower()
            if 'http://' in tweet_text or 'https://' in tweet_text:
                links.append(tweet_text.split('http://',1)[1].split('https://',1)[0])
            if '@' in tweet_text:
                users.append(tweet_text.split('@',1)[1].split(' ',1)[0])
            if '#' in tweet_text:
                hashtags.append(tweet_text.split(''))
        return f"links: {links}, users: {users}, hashtags: {hashtags}"

    def cot_prompting_find_interests(self):
        links = [tweet['link'] for tweet in self.tweets if 'link' in tweet]
        users = [tweet['from_user'] for tweet in self.tweets if 'from_user' in tweet]
        hashtags = [word for tweet in self.tweets if 'tweet' in tweet for word in tweet['tweet'].split() if word.startswith('#')]
        return links, users, hashtags


    def fact_check_list_find_interests(self):
        links = []
        users = set()
        hashtags = []
        for tweet in self.tweets:
            links_pattern = r'https?://\S+'
            extracted_links = re.findall(links_pattern, tweet['text'])
            links.extend(extracted_links)
            users.add(tweet['from_user'])
            hashtags_pattern = ''
            extracted_hashtags = re.findall(hashtags_pattern, tweet['text'])
            hashtags.extend(extracted_hashtags)
        return {'links': links, 'users': list(users), 'hashtags': hashtags}

    import re
    from bs4 import BeautifulSoup

    def not_interactive_mix_find_interests(self):
        interests = []
        for tweet in self.tweets:
            link_finder = re.compile(r'(http[s]?://\S+)')
            links = link_finder.findall(tweet['tweet'])
            users_finder = re.compile(r'@\w+')
            users = users_finder.findall(tweet['tweet'])
            hashtags_finder = re.compile(r'#\w+')
            hashtags = hashtags_finder.findall(tweet['tweet'])
            links_set = set(links)
            users_set = set(users)
            hashtags_set = set(hashtags)
            tweet_interests = {
                'links': list(links_set),
                'users': list(users_set),
                'hashtags': list(hashtags_set)
            }
            interests.append(tweet_interests)
        return interests


    def baseline_find_interests(self):
        links = []
        users = []
        hashtags = []
        for tweet in self.tweets:
            if tweet['url']:
                links.append(tweet['url'])
            if tweet['user_name']:
                users.append(tweet['user_name'])
            if tweet['hashtag']:
                hashtags.append(tweet['tweet'].split(''))
        return {'links': links, 'users': users, 'hashtags': hashtags}

