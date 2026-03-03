import os
class TweetClient:

    def __init__(self, handle):
        self.handle = handle
        self.tweets = self.get_tweets()
    
    def get_tweets(self):
        simulated_tweets = [
            {"tweet": "I love walking in Rome!", "geo": "41.9028, 12.4964"},
	        {"tweet": "New York is beautiful in spring.", "geo": None},
	        {"tweet": "Just got back from Milan", "geo": None},
	        {"tweet": "Nothing beats the pizza in Naples!", "geo": "40.8518, 14.2681"}
        ]
        return simulated_tweets    
    
    def ground_truth_code_twitter_locate(self, cityFile):
        cities = []
        if cityFile is not None:
            for line in open(cityFile).readlines():
                city = line.strip('\n').strip('\r').lower()
                if city:
                    cities.append(city)
  
        matching_tweets = []

        locCnt = 0
        cityCnt = 0

        for tweet in self.tweets:
            tweet_text_lower = tweet['tweet'].lower()

            if tweet['geo'] is not None:
                locCnt += 1

            for city in cities:
                if city in tweet_text_lower:
                    matching_tweets.append(tweet['tweet'])
                    cityCnt += 1
                    
        return matching_tweets

    def persona_twitter_locate(self, cityFile):
        cities = [line.strip() for line in open(cityFile)]
        city_mentions = {}
        for tweet in self.tweets:
            for city in cities:
                if city in tweet:
                    city_mentions.setdefault(city, []).append(tweet)
        return city_mentions

    def template_twitter_locate(self, cityFile):
        try:
            with open(cityFile, 'r') as file:
                cities = set(city.strip().lower() for city in file)
            location_mentions = []
            for tweet in self.tweets:
                tweet_text = tweet['tweet'].lower()
                if tweet['geo']:
                    geo_cities = set(city.lower() for city in tweet['geo'][0])
                    for city in geo_cities:
                        if city in cities:
                            location_mentions.append((tweet['from_user'], city))
                else:
                    for city in cities:
                        if city in tweet_text:
                            location_mentions.append((tweet['from_user'], city))
        except FileNotFoundError:
            print(f'Error: The file {cityFile} was not found.')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
        return location_mentions if location_mentions else 'No matching cities found.'

    def question_refinement_twitter_locate(self, cityFile):
        with open(cityFile, 'r') as file:
            cities = [line.strip() for line in file]
        self.mentioned_cities = []
        for tweet in self.tweets:
            geo = tweet.get('geo', None)
            if geo:
                for city in cities:
                    if city.lower() in geo.lower():
                        self.mentioned_cities.append(city)
        return self.mentioned_cities

    def alternative_approaches_twitter_locate(self, cityFile):
        cities_in_geo = set(city.strip().lower() for tweet in self.tweets for city in tweet['geo'].get('cities', []))
        city_text_set = set(open(cityFile).read().lower().split())
        common_cities = cities_in_geo.intersection(city_text_set)
        return list(common_cities)

    def context_manager_twitter_locate(self, cityFile):
        cities_mentioned = []
        with open(cityFile, 'r') as file:
            for city in file.read().splitlines():
                cities_mentioned.append(city)
        mentioned_cities = []
        for tweet in self.tweets:
            tweet_text = tweet['tweet']
            for city in cities_mentioned:
                if city.lower() in tweet_text.lower():
                    mentioned_cities.append(city)
        return mentioned_cities

    import os
    import errno
    def iterative_prompting_3_twitter_locate(self, city_file):
        if not city_file or not isinstance(city_file, str):
            raise ValueError()

    def iterative_prompting_4_twitter_locate(self, city_file):
        if not isinstance(city_file, str):
            raise ValueError("city_file must be a string representing the file path")
        try:
            with open(city_file, 'r') as file:
                if not os.path.isfile(city_file):
                    raise FileNotFoundError(f"The file {city_file} does not exist")
                cities = [city.strip() for city in file.read().splitlines()]
                if not cities:
                    raise ValueError("The city file is empty or contains only whitespace")
        except PermissionError as pe:
            raise PermissionError(f"Permission denied when trying to read the file {city_file}: {pe}")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        city_mentions = []
        for tweet in self.tweets:
            geo_data = tweet.get('geo')
            if geo_data is None:
                continue
            tweet_cities = [city.strip() for city in geo_data.split(',') if city]
            if not tweet_cities:
                continue
            matching_cities = list(set(tweet_cities) & set(cities))
            if matching_cities:
                city_mentions.append({
                    'tweet_id': tweet['id_str'],
                    'mentioned_cities': matching_cities
                })
        return city_mentions

    import os
    def iterative_prompting_5_twitter_locate(self, city_file):
        if not city_file or not isinstance(city_file, str) or not os.path.exists(city_file):
            raise ValueError('Invalid input: city_file must be a non-empty string and valid file path.')
        mentioned_cities = set()
        try:
            with open(city_file, 'r') as file:
                for line in file:
                    city = line.strip()
                    if city:
                        mentioned_cities.add(city)
        except (FileNotFoundError, PermissionError, IOError) as e:
            raise Exception(f'An error occurred while reading the file: {e}')
        for tweet in self.tweets:
            locations = tweet.get('geo', None)
            if locations:
                city = locations.get('place', '')
                tweet['is_city_mentioned'] = city in mentioned_cities
            else:
                tweet['is_city_mentioned'] = False
        return self.tweets

    def few_shots_prompting_twitter_locate(self, cityFile):
        interests = {'cities': []}
        with open(cityFile, 'r') as file:
            for line in file:
                city = line.strip()
                interests['cities'].extend([city for tweet in self.tweets if city in tweet['geo']])
        return interests

    def cot_prompting_twitter_locate(self, cityFile):
        cities = []
        with open(cityFile, 'r') as file:
            for line in file:
                cities.append(line.strip())
        tweet_city_mentions = []
        for tweet in self.tweets:
            text = tweet['tweet']
            for city in cities:
                if city in text:
                    tweet_city_mentions.append((tweet, city))
        return tweet_city_mentions

    def fact_check_list_twitter_locate(self, cityFile):
        city_list = []
        with open(cityFile, 'r') as file:
            for line in file:
                city_list.append(line.strip())
        referred_cities = set()
        for tweet in self.tweets:
            city = self.extract_city(tweet['geo'])
            if city:
                referred_cities.add(city)
            text = tweet['tweet']
            referred_cities.update(self.extract_cities_from_text(text))
        verified_cities = set(city_list).intersection(referred_cities)
        return list(verified_cities)

    def not_interactive_mix_twitter_locate(self, cityFile):
        with open(cityFile, 'r') as file:
            cities = json.load(file)
        mentioned_cities = self.find()
        interests = {'links': [], 'users': [], 'hashtags': []}
        for tweet in self.tweets:
            if tweet['geo'] in mentioned_cities:
                text = tweet['tweet']
                links = re.findall('(https?://\S+)', text)
                for link in links:
                    interests['links'].append(link)
                users = re.findall('(@\w+)', text)
                for user in users:
                    interests['users'].append(user)
                hashtags = re.findall('(#\w+)', text)
                for hashtag in hashtags:
                    interests['hashtags'].append(hashtag)
        interests['users'] = sorted(set(interests['users']))
        interests['hashtags'] = sorted(set(interests['hashtags']))
        interests['links'] = sorted(set(interests['links']))
        return interests
    def find(self):
        mentioned_cities = set()
        for tweet in self.tweets:
            if tweet['geo']:
                mention = json.loads(tweet['geo'])
                if 'place_type' in mention and mention['place_type'] == 'city':
                    city_name = mention.get('full_name', '')
                    mentioned_cities.add(city_name)
        return mentioned_cities

    def baseline_twitter_locate(self, cityFile):
        with open(cityFile, 'r') as file:
            cities = [line.strip() for line in file.readlines()]
        tweet_cities = set()
        for tweet in self.tweets:
            tweet_cities.update(tweet.get('geo', {}).get('place', {}).get('name', []))
        filtered_cities = tweet_cities.intersection(set(cities))
        return list(filtered_cities)

