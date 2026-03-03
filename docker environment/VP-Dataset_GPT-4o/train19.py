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
        cities_in_geo = set()
        for tweet in self.tweets:
            geo = tweet['geo']
            if geo:
                cities_in_geo.add(geo)
        with open(cityFile, 'r', encoding='utf-8') as file:
            city_list = [line.strip() for line in file.readlines()]
        cities_mentioned_in_text = set()
        for tweet in self.tweets:
            tweet_text = tweet['tweet']
            for city in city_list:
                if city.lower() in tweet_text.lower():
                    cities_mentioned_in_text.add(city)
        combined_cities = cities_in_geo.union(cities_mentioned_in_text)
        return list(combined_cities)

    def template_twitter_locate(self, cityFile):
        cities_in_geo = set()
        cities_in_text = set()
        try:
            with open(cityFile, 'r') as f:
                all_cities = set(map(str.strip, f.readlines()))
        except FileNotFoundError:
            raise Exception('City file not found. Please check the file path.')
        for tweet in self.tweets:
            if tweet['geo']:
                geo_data = tweet.get('geo') or {}
                if 'city' in geo_data:
                    cities_in_geo.add(geo_data['city'])
            tweet_text = tweet.get('tweet', '').lower()
            for city in all_cities:
                if city.lower() in tweet_text:
                    cities_in_text.add(city)
        return list(cities_in_geo.intersection(cities_in_text))

    def question_refinement_twitter_locate():
            basicConfig(level=ERROR)
            logger = getLogger(__name__)
            city_mentions = {}
            try:
                response = requests.get(city_file_url, timeout=10)
                response.raise_for_status()
                city_list = set(json.loads(gzip.decompress(response.content).decode('utf-8')))
            except (RequestException, json.JSONDecodeError, OSError) as e:
                logger.error("Failed to retrieve or parse the city file: %s", e)
                return city_mentions
            for tweet in data:
                tweet_text = tweet.get('text', '').lower()
                city_from_geo = tweet.get('geo', {}).get('city', '').lower()
                if city_from_geo and city_from_geo in city_list:
                    city_name = city_from_geo.title()
                    city_mentions[city_name] = city_mentions.get(city_name, 0) + 1
                for city in city_list:
                    city_lower = city.lower()
                    if city_lower in tweet_text:
                        city_title = city.title()
                        city_mentions[city_title] = city_mentions.get(city_title, 0) + 1
            return city_mentions

    def alternative_approaches_twitter_locate(self, cityFile):
        try:
            with open(cityFile, 'r', encoding='utf-8') as f:
                cities_list = f.read().splitlines()
            geo_cities = [tweet['geo'] for tweet in self.tweets if tweet['geo'] is not None]
            text_cities = set()
            for tweet in self.tweets:
                tweet_text_lower = tweet['tweet'].lower()
                for city in cities_list:
                    if city.lower() in tweet_text_lower:
                        text_cities.add(city)
            return {
                "geo_cities": list(set(geo_cities) & text_cities),
                "text_cities_only": list(text_cities - set(geo_cities))
            }
        except Exception as e:
            return {"error": str(e)}

    def context_manager_twitter_locate(self, cityFile):
        cities_in_geo = set()
        for tweet in self.tweets:
            if tweet['geo'] is not None:
                cities_in_geo.update(tweet['geo'].get('cities', []))
        with open(cityFile, encoding='utf-8') as file:
            file_cities = set(line.strip() for line in file)
        cities_in_text = set()
        for tweet in self.tweets:
            for city in file_cities:
                if city.lower() in tweet['tweet'].lower():
                    cities_in_text.add(city)
        return list(cities_in_geo.intersection(cities_in_text))

    def flipped_interaction_3_twitter_locate(self, cityFile):
        cities_from_geo = {tweet['geo'] for tweet in self.tweets if tweet['geo']}
        matching_cities = set()
        with open(cityFile, 'r', encoding='utf-8') as file:
            city_names = {line.strip().lower() for line in file}
        for tweet in self.tweets:
            tweet_text = tweet['tweet'].lower()
            for city in city_names:
                if city in tweet_text:
                    matching_cities.add(city)
        all_cities = cities_from_geo.union(matching_cities)
        return all_cities

    def flipped_interaction_4_twitter_locate(self, cityFile):
        import re
        import json
        with open(cityFile, 'r') as file:
            city_names = set(line.strip().lower() for line in file)
        mentioned_cities = set()
        for tweet in self.tweets:
            if tweet['geo'] and isinstance(tweet['geo'], str):
                city_geo = tweet['geo'].lower()
                if city_geo in city_names:
                    mentioned_cities.add(city_geo)
            tweet_text = tweet['tweet'].lower()
            for city in city_names:
                if re.search(r'\b' + re.escape(city) + r'\b', tweet_text):
                    mentioned_cities.add(city)
        return list(mentioned_cities)

    def flipped_interaction_5_twitter_locate(self, cityFile):
        with open(cityFile, 'r') as file:
            city_list = [line.strip().lower() for line in file]
        matched_cities = []
        for tweet in self.tweets:
            tweet_text = tweet['tweet'].lower()
            for city in city_list:
                if city in tweet_text:
                    matched_cities.append(city)
        return matched_cities

    def iterative_prompting_3_twitter_locate(self, city_file):
        if not isinstance(city_file, str) or not city_file.strip():
            raise ValueError("Provided city_file must be a non-empty string.")
        geo_cities = set()
        for tweet in self.tweets:
            geo_info = tweet.get('geo')
            if geo_info and isinstance(geo_info, dict) and 'city' in geo_info:
                city_name = geo_info.get('city', '')
                if isinstance(city_name, str):
                    geo_cities.add(city_name.lower())
        city_file_cities = set()
        try:
            with open(city_file, 'r', encoding='utf-8') as file:
                for line in file:
                    stripped_line = line.strip().lower()
                    if stripped_line:
                        city_file_cities.add(stripped_line)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {city_file}")
        except Exception as e:
            raise RuntimeError(f"An error occurred reading the city file: {e}")
        text_mentioned_cities = set()
        tweet_texts = ' '.join(tweet.get('tweet', '').lower() for tweet in self.tweets if isinstance(tweet.get('tweet'), str))
        for city in city_file_cities:
            if city in tweet_texts:
                text_mentioned_cities.add(city)
        intersection_cities = geo_cities.intersection(text_mentioned_cities)
        return {
            'geo_cities': list(geo_cities),
            'text_mentioned_cities': list(text_mentioned_cities),
            'intersection_cities': list(intersection_cities)
        }

    def iterative_prompting_4_twitter_locate(self, city_file):
        if city_file is not None and not isinstance(city_file, str):
            raise ValueError("city_file must be a string path to a file.")
        geo_cities = set()
        text_cities = set()

        try:
            for tweet in self.tweets:
                if 'geo' in tweet and tweet['geo']:
                    city = tweet['geo'].strip().lower()
                    geo_cities.add(city)

            cities = []
            if city_file and os.path.isfile(city_file):
                with open(city_file, "r", encoding="utf-8") as f:
                    cities = [line.strip().lower() for line in f if line.strip()]

            tweet_texts = " ".join(tweet['tweet'].lower() for tweet in self.tweets if 'tweet' in tweet)

            for city in cities:
                if city in tweet_texts:
                    text_cities.add(city)
        except Exception as e:
            print(f"Error processing tweets or city file: {e}")

        return list(geo_cities.union(text_cities))

        
    def iterative_prompting_5_twitter_locate(self, city_file):
   
        if city_file is not None and not isinstance(city_file, str):
            raise ValueError("city_file must be a string path to a file.")
        geo_cities = set()
        text_cities = set()

        try:
            for tweet in self.tweets:
                if 'geo' in tweet and tweet['geo']:
                    city = tweet['geo'].strip().lower()
                    geo_cities.add(city)

            cities = []
            if city_file and os.path.isfile(city_file):
                with open(city_file, "r", encoding="utf-8") as f:
                    cities = [line.strip().lower() for line in f if line.strip()]

            tweet_texts = " ".join(tweet['tweet'].lower() for tweet in self.tweets if 'tweet' in tweet)

            for city in cities:
                if city in tweet_texts:
                    text_cities.add(city)
        except Exception:
            pass

        return list(geo_cities.union(text_cities))
    

    def few_shots_prompting_twitter_locate(self, cityFile):
        geo_cities = set()
        for tweet in self.tweets:
            geo = tweet['geo']
            if geo is not None and 'city' in geo:
                geo_cities.add(geo['city'].lower())
        with open(cityFile, 'r') as f:
            city_list = [line.strip().lower() for line in f]
        mentioned_cities = set()
        for tweet in self.tweets:
            text = tweet['tweet'].lower()
            for city in city_list:
                if city in text:
                    mentioned_cities.add(city)
        return list(geo_cities.union(mentioned_cities))

    def cot_prompting_twitter_locate(self, cityFile):
        cities_from_geo = {tweet['geo'] for tweet in self.tweets if tweet['geo']}
        cities_in_text = set()
        with open(cityFile, 'r') as file:
            known_cities = {line.strip().lower() for line in file}
        for tweet in self.tweets:
            tweet_text = tweet['tweet'].lower()
            for city in known_cities:
                if city in tweet_text:
                    cities_in_text.add(city)
        all_identified_cities = cities_from_geo.union(cities_in_text)
        return all_identified_cities

    def fact_check_list_twitter_locate(self, cityFile):
        city_locations = set()
        cities_in_text = set()
        with open(cityFile, 'r') as f:
            cities = {line.strip().lower() for line in f}
        for tweet in self.tweets:
            geo_info = tweet.get('geo')
            if geo_info and isinstance(geo_info, str) and geo_info.lower() in cities:
                city_locations.add(geo_info.lower())
        for tweet in self.tweets:
            tweet_text = tweet['tweet'].lower()
            for city in cities:
                if city in tweet_text:
                    cities_in_text.add(city)
        return {
            'geo': list(city_locations),
            'text': list(cities_in_text)
        }

    def not_interactive_mix_twitter_locate(self, cityFile):
        import re
        import json
        try:
            with open(cityFile, 'r') as f:
                city_names = set(line.strip() for line in f if line.strip())
        except FileNotFoundError:
            return "City file not found."
        except Exception as e:
            return f"An error occurred: {str(e)}"
        cities_in_geo = set()
        for tweet in self.tweets:
            geo_info = tweet.get('geo')
            if geo_info:
                if isinstance(geo_info, str):
                    geo_cities = map(str.strip, geo_info.split(','))
                    cities_in_geo.update(filter(lambda city: city in city_names, geo_cities))
        cities_in_tweets = set()
        for tweet in self.tweets:
            tweet_text = tweet.get('tweet', '')
            for city in city_names:
                if re.search(r'\b' + re.escape(city) + r'\b', tweet_text, re.IGNORECASE):
                    cities_in_tweets.add(city)
        combined_cities = cities_in_geo.union(cities_in_tweets)
        return list(combined_cities)

    def interactive_mix_process_tweet_cities(tweets, city_file):
        import csv
        def load_cities(file_path):
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                return {row[0].strip().lower() for row in reader}
        cities_in_geos = []
        cities_in_texts = []
        city_set = load_cities(city_file)
        for tweet in tweets:
            geo_cities = tweet.get('geo', '').lower().split()
            tweet_text = tweet.get('tweet', '').lower().split()
            for city in geo_cities:
                if city in city_set:
                    cities_in_geos.append(city)
            for word in tweet_text:
                if word in city_set:
                    cities_in_texts.append(word)
        return cities_in_geos, cities_in_texts

    def baseline_twitter_locate(self, cityFile):
        city_geo_set = set()
        for tweet in self.tweets:
            if tweet['geo']:
                city_geo_set.add(tweet['geo'])
        city_text_set = set()
        with open(cityFile, 'r') as f:
            city_list = f.read().splitlines()
            for tweet in self.tweets:
                text = tweet['tweet']
                for city in city_list:
                    if city.lower() in text.lower():
                        city_text_set.add(city)
        cities_mentioned = city_geo_set.union(city_text_set)
        return list(cities_mentioned)

