import os
import re

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

    def persona__twitter_locate(self, cityFile):
        with open(cityFile, 'r') as file:
            citySet = set(line.strip().lower() for line in file)
        geoCities = set()
        textCities = set()
        for tweet in self.tweets:
            if tweet['geo'] and 'city' in tweet['geo']:
                geoCities.add(tweet['geo']['city'].strip().lower())
            textCities.update(city.lower() for city in re.split(r'[ ,.;!?]', tweet['tweet']) if city.lower() in citySet)
        return {'geo_cities': list(geoCities), 'text_cities': list(textCities)}

    def template__twitter_locate(self, cityFile):
        try:
            with open(cityFile, 'r') as file:
                cities = set(city.strip().lower() for city in file)
        except Exception as e:
            return {'error': str(e)}
        mentioned_cities_in_geo = set()
        mentioned_cities_in_text = set()
        for tweet in self.tweets:
            if tweet['geo'] is not None and 'city' in tweet['geo']:
                mentioned_cities_in_geo.add(tweet['geo']['city'].strip().lower())
            tweet_text = tweet['tweet'].strip().lower()
            mentioned_cities_in_text.update(city for city in cities if city in tweet_text)
        return {'geo_cities': list(mentioned_cities_in_geo), 'text_cities': list(mentioned_cities_in_text)}

    def question_refinement__retrieve_cities_from_tweets_and_file(tweets, cityFile):
        import json
        import re
        try:
            cities_from_geo = set()
            for tweet in tweets:
                if isinstance(tweet, dict) and 'geo' in tweet and isinstance(tweet['geo'], dict) and 'city' in tweet['geo']:
                    cities_from_geo.add(tweet['geo']['city'])
            with open(cityFile, 'r') as file:
                city_data = json.load(file)
            cities_in_file = set(city_data.get('cities', [])) if isinstance(city_data, dict) else set()
            pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, cities_in_file)) + r')\b', re.IGNORECASE)
            cities_in_tweets_text = set()
            for tweet in tweets:
                if isinstance(tweet, dict) and 'text' in tweet:
                    found_cities = pattern.findall(tweet['text'])
                    cities_in_tweets_text.update([city.lower() for city in found_cities])
            return list(cities_from_geo.union(cities_in_tweets_text))
        except (json.JSONDecodeError, TypeError, FileNotFoundError, KeyError) as e:
            return str(e)

    def alternative_approaches__twitter_locate(self, cityFile):
        if not os.path.isfile(cityFile):
            print('File does not exist.')
            return {}
        try:
            with open(cityFile, 'r', encoding='utf-8') as file:
                cities = set(city.strip().lower() for city in file.readlines())
        except Exception as e:
            print('Error reading file: {}'.format(e))
            return {}
        foundCitiesInGeo = set()
        foundCitiesInText = set()
        for tweet in self.tweets:
            geo_info = tweet['geo']
            if geo_info and geo_info['type'] == 'Point':
                lat, lon = geo_info['coordinates']
            tweetTextWords = set(tweet['tweet'].lower().split())
            foundCitiesInText.update(tweetTextWords.intersection(cities))
        allCities = foundCitiesInGeo.union(foundCitiesInText)
        return {k: list(v) for k, v in {'geo_cities': foundCitiesInGeo, 'text_cities': foundCitiesInText, 'all_cities': allCities}.items()}

    def context_manager__twitter_locate(self, cityFile):
        cities_in_geo = set()
        cities_in_text = set()
        for tweet in self.tweets:
            if tweet['geo'] and isinstance(tweet['geo'], dict) and 'coordinates' in tweet['geo'] and 'place' in tweet['geo']:
                if tweet['geo']['place']:
                    cities_in_geo.add(tweet['geo']['place']['name'])
            cities_in_tweet.update(re.findall(r'\w+\b', tweet['tweet']))
        with open(cityFile, 'r') as f:
            valid_cities = set(f.read().splitlines())
        cities_in_text.intersection_update(valid_cities)
        return {'geo_cities': list(cities_in_geo), 'text_cities': list(cities_in_text)}

    def flipped_interaction_3__twitter_locate(self, cityFile):
        with open(cityFile, 'r') as file:
            city_list = {line.strip().lower() for line in file}
        cities_in_geo = set()
        cities_in_text = set()
        for tweet in self.tweets:
            if tweet['geo']:
                city_name = tweet['geo'].lower()
                if city_name in city_list:
                    cities_in_geo.add(city_name)
            text = tweet['tweet'].lower()
            words_in_text = re.findall(r'\b\w+\b', text)
            for word in words_in_text:
                if word in city_list:
                    cities_in_text.add(word)
        all_cities = cities_in_geo.union(cities_in_text)
        return sorted(list(all_cities))

    def flipped_interaction_4__twitter_locate(self, cityFile):
        cities_set = set()
        if cityFile:
            try:
                with open(cityFile, 'r') as file:
                    for line in file:
                        city = line.strip().lower()
                        cities_set.add(city)
            except FileNotFoundError:
                return []
            except Exception as e:
                return []
        unique_cities = set()
        for tweet in self.tweets:
            if tweet['geo']:
                if isinstance(tweet['geo'], dict) and 'place_url' in tweet['geo']:
                    place_info_url = tweet['geo']['place_url']
                    try:
                        place_response = urllib.request.urlopen(place_info_url)
                        place_json = json.load(place_response)
                        if 'place' in place_json and 'name' in place_json['place']:
                            geo_city = place_json['place']['name'].strip().lower()
                            unique_cities.add(geo_city)
                    except (urllib.error.URLError, ValueError) as e:
                        pass
                else:
                    geo_city = str(tweet['geo']).strip().lower()
                    unique_cities.add(geo_city)
            text = tweet['tweet']
            cleaned_text = re.sub(r'[^-\w\s\'-]', '', text).lower()
            words = cleaned_text.split()
            for word in words:
                if word in cities_set:
                    unique_cities.add(word)
        return sorted(list(unique_cities))

    def flipped_interaction_5__twitter_locate(self, cityFile):
        with open(cityFile, 'r') as file:
            city_names = set(line.strip().lower() for line in file)
        located_cities = set()
        for tweet in self.tweets:
            geo = tweet['geo']
            if geo and 'coordinates' in geo:
                lat, lon = geo['coordinates']['coordinates']
                city_name_from_geo = self.get_city_name_from_coordinates(lat, lon)
                if city_name_from_geo.lower() in city_names:
                    located_cities.add(city_name_from_geo.lower())
            tweet_text = tweet['tweet'].lower()
            words_in_tweet = set(tweet_text.split())
            matched_cities = words_in_tweet.intersection(city_names)
            located_cities.update(matched_cities)
        return list(located_cities)

    def iterative_prompting_3__twitter_locate(self, city_file):
        if not isinstance(city_file, str):
            raise ValueError('city_file must be a string representing the file path.')
        try:
            with open(city_file, 'r', encoding='utf-8') as file:
                city_set = {line.strip().lower() for line in file if line.strip()}
        except FileNotFoundError:
            raise FileNotFoundError(f'The file {city_file} was not found.')
        except IOError:
            raise IOError(f'An error occurred while reading the file {city_file}.')
        geo_cities = set()
        text_cities = set()
        if not isinstance(self.tweets, list):
            raise TypeError('self.tweets must be a list of tweets.')
        for tweet in self.tweets:
            if not isinstance(tweet, dict) or 'geo' not in tweet or 'text' not in tweet:
                raise ValueError('Each tweet must be a dictionary containing at least \u2018geo\u2019 and \u2018text\u2019 keys.')
            if tweet['geo'] and isinstance(tweet['geo'], dict) and 'coordinates' in tweet['geo']:
                city_from_geo = self.get_city_from_coordinates(tweet['geo']['coordinates'])
                if city_from_geo:
                    geo_cities.add(city_from_geo.lower())
            for city in city_set:
                if city in tweet['text'].lower():
                    text_cities.add(city)
        return geo_cities, text_cities

    def iterative_prompting_4__twitter_locate(self, city_file):
        if not isinstance(city_file, str):
            raise ValueError('city_file must be a string representing a file path.')
        cities_in_geo = set()
        for tweet in self.tweets:
            geo = tweet.get('geo')
            if geo and isinstance(geo, dict) and 'city' in geo:
                city = geo['city']
                if isinstance(city, str) and city:
                    cities_in_geo.add(city)
        try:
            with open(city_file, 'r', encoding='utf-8') as f:
                all_cities = f.read().splitlines()
        except FileNotFoundError:
            raise FileNotFoundError(f'The file {city_file} was not found.')
        except IOError as e:
            raise IOError(f'An error occurred while reading the file {city_file}: {e.strerror}')
        cities_mentioned_in_tweets = set()
        for tweet in self.tweets:
            tweet_text = tweet.get('tweet', '')
            if isinstance(tweet_text, str):
                tweet_text = tweet_text.lower()
                for city in all_cities:
                    if isinstance(city, str) and city.lower() in tweet_text:
                        cities_mentioned_in_tweets.add(city)
        return {'cities_in_geo': list(cities_in_geo), 'cities_mentioned_in_tweets': list(cities_mentioned_in_tweets)}

    def iterative_prompting_5__twitter_locate(self, cityFile):
        if not isinstance(cityFile, str):
            raise ValueError('cityFile must be a string representing the file path.')
        cities_in_geo = set()
        try:
            for tweet in self.tweets:
                geo = tweet.get('geo', {})
                if isinstance(geo, dict) and geo.get('type') == 'Point':
                    city_info = geo.get('place', {}).get('name')
                    if isinstance(city_info, str):
                        cities_in_geo.add(city_info)
        except Exception as e:
            print(f'An unexpected error occurred while processing tweets: {e}')
        try:
            with open(cityFile, 'r', encoding='utf-8') as file:
                all_cities = set(line.strip().lower() for line in file if line.strip())
        except FileNotFoundError:
            raise FileNotFoundError(f'The file {cityFile} was not found.')
        except IOError as e:
            raise IOError(f'An I/O error occurred while reading the file: {e}')
        cities_in_text = set()
        try:
            for tweet in self.tweets:
                text = tweet.get('tweet', '').lower()
                if isinstance(text, str):
                    for city in all_cities:
                        if city in text:
                            cities_in_text.add(city)
        except Exception as e:
            print(f'An unexpected error occurred while searching for cities in tweet text: {e}')
        return cities_in_geo.union(cities_in_text)

    def few_shots_prompting__twitter_locate(self, cityFile):
        cities_from_geo = set()
        cities_from_text = set()
        with open(cityFile, 'r') as file:
            cities_set = set(file.read().splitlines())
        for tweet in self.tweets:
            if tweet['geo'] and 'city' in tweet['geo']:
                cities_from_geo.add(tweet['geo']['city'])
            for word in tweet['tweet'].split():
                if word.lower() in cities_set:
                    cities_from_text.add(word.lower())
        return cities_from_geo, cities_from_text

    def cot_prompting__twitter_locate(self, cityFile):
        cities_from_geo = set()
        cities_from_text = set()
        for tweet in self.tweets:
            if tweet['geo']:
                city = tweet['geo'].get('city', '')
                if city:
                    cities_from_geo.add(city.lower())
            cities_from_text.update(re.findall(r',\s*(\w+)', tweet['tweet'].lower()))
        with open(cityFile, 'r') as file:
            valid_cities = set(file.read().splitlines())
        matched_cities_geo = cities_from_geo.intersection(valid_cities)
        matched_cities_text = cities_from_text.intersection(valid_cities)
        return matched_cities_geo, matched_cities_text

    def fact_check_list__twitter_locate(self, cityFile):
        with open(cityFile, 'r') as f:
            city_set = set(city.strip().lower() for city in f.readlines())
        geo_cities = [tweet['geo'].lower() for tweet in self.tweets if tweet['geo']]
        tweet_text_cities = []
        city_pattern = re.compile(r'\b(?:' + '|'.join(re.escape(city) for city in city_set) + r')\b', re.IGNORECASE)
        for tweet in self.tweets:
            text = tweet['tweet']
            found_cities = city_pattern.findall(text)
            tweet_text_cities.extend(found_city.lower() for found_city in found_cities)
        common_cities = set(geo_cities).intersection(set(tweet_text_cities))
        return {
            'geo_cities': geo_cities,
            'tweet_text_cities': tweet_text_cities,
            'common_cities': list(common_cities)
        }

    def not_interactive_mix__twitter_locate(self, cityFile):
        cities_from_geo = set()
        cities_from_text = set()
        if not os.path.exists(cityFile):
            raise FileNotFoundError("The city file does not exist")
        try:
            with open(cityFile, 'r') as f:
                known_cities = set(f.read().splitlines())
        except IOError as e:
            raise IOError(f"Failed to open city file: {e.strerror}")
        for tweet in self.tweets:
            geo = tweet['geo']
            text = tweet['text']
            if geo is not None and 'city' in geo:
                city = geo['city'].strip().lower()
                if city in known_cities:
                    cities_from_geo.add(city)
            city_mentions = re.compile(r'\b(?:' + '|'.join(map(re.escape, known_cities)) + r')\b', re.IGNORECASE).findall(text)
            for city in city_mentions:
                cities_from_text.add(city)
        return {'cities_from_geo': list(cities_from_geo), 'cities_from_text': list(cities_from_text)}

    def interactive_mix__twitter_locate(tweets, cityFile):
        import re
        with open(cityFile, 'r') as f:
            city_names = set(line.strip().lower() for line in f)
        found_cities = set()
        city_pattern = re.compile(r'\b(?:' + '|'.join(re.escape(city) for city in city_names) + r')\b', re.IGNORECASE)
        for tweet in tweets:
            tweet_text = tweet.get('tweet', '').lower()
            geo_city = tweet.get('geo', {}).get('coordinates', {}).get('city', '').lower()
            if geo_city and geo_city in city_names:
                found_cities.add(geo_city)
            matches = city_pattern.findall(tweet_text)
            for match in matches:
                original_city = [city for city in city_names if city_pattern.search(city).group() == match][0]
                found_cities.add(original_city)
        return list(found_cities)

    def baseline__twitter_locate(self, cityFile):
        cities_set = set(city for city in open(cityFile, 'r').read().splitlines())
        cities_in_geo = set()
        cities_in_tweet = set()
        for tweet in self.tweets:
            if tweet['geo'] and 'coordinates' in tweet['geo']:
                city = cityFromCoordinates(tweet['geo']['coordinates'])
                if city in cities_set:
                    cities_in_geo.add(city)
            tweet_text = tweet['text'].lower()
            cities_in_tweet.update(set(city.lower() for city in cities_set if city.lower() in tweet_text))
        return {'cities_in_geo': list(cities_in_geo), 'cities_in_tweet': list(cities_in_tweet)}

