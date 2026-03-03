import json
import re
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
        cities = set()
        for tweet in self.tweets:
            if tweet['geo'] and 'coordinates' in tweet['geo']:
                city = tweet['geo']['coordinates']
                cities.add(city)
        with open(cityFile, 'r') as f:
            city_list = [line.strip().lower() for line in f]
        city_mentions = []
        for tweet in self.tweets:
            for city in city_list:
                if city in tweet['tweet'].lower():
                    city_mentions.append(city)
        return list(cities), city_mentions
    
    def template_twitter_locate(self, cityFile):
        citiesLocation = {}
        citiesMentioned = {}
        locations = set()
        try:
            with open(cityFile, 'r') as f:
                cityFileContent = f.read()
            cityFileContent = cityFileContent.split("\n")
            for city in cityFileContent:
                if city.strip() != "" and city.lower() not in locations:
                    locations.add(city.lower())
            for tweet in self.tweets:
                city = tweet.get('geo', None)
                if city is not None:
                    if city not in citiesLocation:
                        citiesLocation[city] = 0
                    citiesLocation[city] += 1
                    for location in locations:
                        if location in city:
                            if location not in citiesMentioned:
                                citiesMentioned[location] = 0
                            citiesMentioned[location] += 1
                text = tweet['tweet'].lower()
                for location in locations:
                    if location in text:
                        if location not in citiesMentioned:
                            citiesMentioned[location] = 0
                        citiesMentioned[location] += 1
        except Exception as e:
            return('An error occurred: ' + str(e))
        
        return {"cities Mentioned in geo location": citiesLocation, "cities Mentioned in text": citiesMentioned}

        

    def question_refinement_twitter_locate(self, cityFile, tweets):
        import json
        from nltk.tokenize import word_tokenize
        import nltk
        nltk.download('punkt')
        cityMentions = {}
        
        data = ''
        with open(cityFile) as f:
            for line in f:
                data += line
        listCities = json.loads(data)
        
        for city in listCities:
            cityLower = city.lower()
            for tweet in tweets:
                if 'geo' in tweet and tweet['geo'] is not None:
                    geoLocation = str(tweet['geo']).lower()
                    if cityLower in geoLocation:
                        cityMentions[city] = cityMentions.get(city, []) + [tweet['id']]
                if 'text' in tweet:
                    textTokens = word_tokenize(tweet['text'].lower())
                    if cityLower in textTokens:
                        cityMentions[city] = cityMentions.get(city, []) + [tweet['id']]
                        
        return cityMentions
    
    def alternative_approaches_twitter_locate(self, cityFile):
            cityList = []
            with open(cityFile, 'r') as file:
                cityList = file.readlines()
            cityList = [city.rstrip() for city in cityList]
            city_in_tweet_text = []
            city_in_geo_attr = []
            for tweet in self.tweets:
                if tweet['geo']:
                    for city in cityList:
                        if city in tweet['geo']:
                            city_in_geo_attr.append((city, tweet['geo']))
                for city in cityList:
                    if city in tweet['tweet']:
                        city_in_tweet_text.append((city, tweet['tweet']))
            results = {'cities_in_geo_attribute': city_in_geo_attr, 'cities_in_tweet_text': city_in_tweet_text}
            return json.dumps(results, indent=4)
    
    def context_manager_twitter_locate(self, cityFile):
        geo_cities = [tweet['geo'] for tweet in self.tweets if tweet['geo']]
        city_list = open(cityFile).read().splitlines()
        geo_cities.extend([city for tweet in self.tweets for city in city_list if city in tweet['tweet'].lower() and city not in geo_cities])
        return geo_cities
    
    def flipped_interaction_3__twitter_locate(self, cityFile):
            cities_in_tweets = {}
            cities_in_text = {}
            for tweet in self.tweets:
                geo = tweet['geo']
                if geo and 'coordinates' in geo:
                    city = geo['place']['name']
                    cities_in_tweets[city.lower()] = cities_in_tweets.get(city.lower(), 0) + 1
                for line in open(cityFile, 'r').readlines():
                    city_to_search = line.strip().lower()
                    if city_to_search in tweet['tweet'].lower():
                        cities_in_text[city_to_search] = cities_in_text.get(city_to_search, 0) + 1
            cities = cities_in_tweets.copy()
            cities.update(cities_in_text)
            city_list = list(cities.keys())
            city_list.sort()
            return city_list
    
    def flipped_interaction_4__twitter_locate(self, cityFile):
        city_names = [line.strip().lower() for line in open(cityFile, 'r')]
        locations = {}
        for tweet in self.tweets:
            if tweet['geo'] and tweet['geo']['coordinates']:
                city_name = tweet['geo']['place']['name'].lower()
                if city_name in city_names:
                    locations[city_name] = tweet['geo']['coordinates']
            if tweet['tweet'].lower() in [city for city in city_names if city not in locations.keys()]:
                location_keys = [key for key in locations.keys() if key in tweet['tweet'].lower()]
                for key in location_keys: del locations[key]
                locations[tweet['tweet'].lower()] = None
            for city in city_names:
                if city in tweet['tweet'].lower() and city not in locations.keys():
                    locations[city] = None
        result = []
        for city in locations:
            if locations[city] is not None:
                result.append([city, locations[city]])
            else:
                result.append(city)
        return result
    
    def flipped_interaction_5__twitter_locate(self, cityFile):
        locations = set()
        city_names = {}
        with open(cityFile, 'r') as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) < 3:
                    continue
                geo = "{} {}".format(parts[0], parts[1])
                names = parts[2:]
                for name in names:
                    city_names[name.strip().lower()] = geo
        for tweet in self.tweets:
            text = tweet['tweet'].lower()
            for name in city_names:
                if name in text and city_names[name]:
                    locations.add(city_names[name])
            if tweet['geo']:
                locations.add(tweet['geo'])
        return list(locations)
    
    def iterative_prompting_3__twitter_locate(self, cityFile):
        if not isinstance(cityFile, str):
            raise TypeError('cityFile must be a string')
        if not cityFile:
            raise ValueError('cityFile cannot be empty')
        try:
            import os
            if not os.path.isfile(cityFile):
                raise FileNotFoundError('cityFile not found')
            cities = {}
            if not self.tweets:
                return cities
            for tweet in self.tweets:
                if 'geo' in tweet and 'coordinates' in tweet['geo'] and len(tweet['geo']['coordinates']) == 2:
                    lat = tweet['geo']['coordinates'][0]
                    long = tweet['geo']['coordinates'][1]
                    cities[str(lat) + ',' + str(long)] = tweet['tweet']
            with open(cityFile, 'r', encoding='utf-8', errors='ignore') as file:
                cities_in_file = [line.strip().lower() for line in file]
            for tweet in self.tweets:
                for city in cities_in_file:
                    if city and isinstance(tweet['tweet'], str) and city in tweet['tweet'].lower():
                        cities[city] = tweet['tweet']
            return cities
        except Exception as e:
            raise Exception('An error occurred:'+ str(e))
        
    def iterative_prompting_4__twitter_locate(self, cityFile):
        try:
            if not isinstance(cityFile, str) or not cityFile: raise ValueError('Invalid cityFile')
            if not cityFile.endswith('.txt'): raise ValueError('Invalid cityFile extension')
            if len(cityFile) > 255: raise ValueError('cityFile path too long')
            with open(cityFile, 'r', encoding='utf-8', errors='ignore') as file: cityText = file.read()
            if not cityText: raise ValueError('Empty cityFile')
        except (OSError, ValueError) as e: return {'error': str(e)}, {}
        if not hasattr(self, 'tweets') or not self.tweets: return {}, {}
        if not isinstance(self.tweets, list): return {'error': 'Invalid tweets type'}, {}
        if not all(isinstance(tweet, dict) for tweet in self.tweets): return {'error': 'Invalid tweets type'}, {}
        cityList = {}
        for tweet in self.tweets:
            try:
                if 'geo' not in tweet: continue
                if not tweet['geo']: continue
                city = tweet['geo'].get('place', {}).get('name')
                if not city: continue
                cityList[city] = cityList.get(city, 0) + 1
            except Exception as e:
                import logging
                logging.error(e)
                continue
        cityInText = {}
        cityList_in_text = {}
        for line in cityText.split('\n'):
            try:
                city_name = line.strip()
                if not city_name: continue
                if len(city_name) > 255: continue
                for tweet in self.tweets:
                    try:
                        text = tweet['tweet']
                        if len(text) > 280: continue
                        if len(city_name) > 1 and city_name.lower() in text.lower():
                            cityInText[city_name] = cityInText.get(city_name, 0) + 1
                    except Exception as e:
                        import logging
                        logging.error(e)
                        continue
            except Exception as e:
                import logging
                logging.error(e)
                return {'error': str(e)}, {}
        try:
            cityList_in_text = {city: cityInText[city] for city in cityList if city in cityInText}
            cityInText.update(cityList_in_text)
        except Exception as e:
            import logging
            logging.error(e)
            return {'error': str(e)}, {}
        return cityList, cityInText

    
    def iterative_prompting_5__twitter_locate(self, cityFile):
        if not isinstance(cityFile, str) or not cityFile.strip():
            raise ValueError('Invalid cityFile path')
        if not os.path.isfile(cityFile):
            raise ValueError(f'File {cityFile} not found')
        cities = {}
        try:
            with open(cityFile, 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    city = line.strip().lower()
                    if city:
                        cities[city] = 1
        except Exception as e:
            raise ValueError(f'Failed to read file {cityFile}: {str(e)}')
        if not hasattr(self, 'tweets') or not isinstance(self.tweets, list):
            raise ValueError('Invalid self.tweets')
        for tweet in self.tweets:
            if not isinstance(tweet, dict):
                raise ValueError('Invalid tweet format')
        cities_in_geo = {}
        for tweet in self.tweets:
            if 'geo' in tweet and tweet['geo'] and isinstance(tweet['geo'], dict):
                if 'coordinates' in tweet['geo'] and len(tweet['geo']['coordinates']) == 2:
                    lon = str(tweet['geo']['coordinates'][0])
                    lat = str(tweet['geo']['coordinates'][1])
                    for city in cities:
                        if lon in city or lat in city:
                            cities_in_geo[city] = cities_in_geo.get(city, 0) + 1
        cities_in_tweets = {}
        for tweet in self.tweets:
            if 'tweet' in tweet and isinstance(tweet['tweet'], str):
                text = tweet['tweet'].lower()
                for city in cities:
                    if city in text:
                        cities_in_tweets[city] = cities_in_tweets.get(city, 0) + 1
        common_cities = set(cities_in_geo) & set(cities_in_tweets)
        return common_cities
    
    def few_shots_prompting_twitter_locate(self, cityFile):
        cities = set()
        for tweet in self.tweets:
            if tweet['geo']:
                try:
                    cities.add(tweet['geo']['place']['full_name'])
                except:
                    pass
        with open(cityFile, 'r') as f:
            city_data = f.read()
        for tweet in self.tweets:
            text = tweet['tweet'].lower()
            for city in cities:
                if city.lower() in text and city.lower() not in city_data.lower():
                    print("City: %s, Tweet: %s" % (city, tweet['tweet']))
                    
    def cot_prompting_twitter_locate(self, cityFile):
        print("not executable")
        '''
        cities = TransportationTools.load_city_file(cityFile)
        all_cities = []
        located_cities = []
        for tweet in self.tweets:
            if tweet['geo'] is not None:
                for city in cities.keys():
                    if TransportationTools.match_city_to_area(tweet['geo'], cities[city]):
                        all_cities.append(city)
        for tweet in self.tweets:
            for city in cities.keys():
                if TransportationTools.match_city(tweet['tweet'], cities[city]):
                    located_cities.append(city)
        return all_cities, located_cities
        '''
    
    def fact_check_list_twitter_locate(self, cityFile):
        location_results = {'tweets_with_cities': [], 'cities_mentioned': []}
        with open(cityFile, 'r') as city_file:
            cities = [city.strip().lower() for city in city_file.readlines()]
        geo_cities = []
        for tweet in self.tweets:
            if tweet['geo'] and 'coordinates' in tweet['geo']:
                city = str(tweet['geo']['coordinates'])
                geo_cities.append(city)
            elif tweet['geo'] and 'city' in tweet['geo']:
                city = tweet['geo']['city'].lower()
                geo_cities.append(city)
        for tweet in self.tweets:
            text = tweet['tweet'].lower()
            for city in cities:
                if city in text:
                    location_results['cities_mentioned'].append(city)
                    location_results['tweets_with_cities'].append(tweet)
                    break
        location_results['tweets_with_cities'] = list({tweet['from_user'] + tweet['tweet']: tweet for tweet in location_results['tweets_with_cities']}.values())
        location_results['tweets_with_cities'].sort(key=lambda x: (x['from_user'], x['tweet']))
        location_results['cities_mentioned'] = list(set(location_results['cities_mentioned']))
        return location_results
    
    def not_interactive_mix_twitter_locate(self, cityFile):
        with open(cityFile, 'r') as f:
            cityFileContent = f.read()
        cities = set(cityFileContent.strip().lower().splitlines())
        city_mentions = set()
        geo_cities = set()
        for tweet in self.tweets:
            if tweet['geo']:
                geo_cities.add(tweet['geo'].lower())
            text = tweet['tweet'].lower()
            for city in cities:
                if city in text:
                    city_mentions.add(city)
        return geo_cities, city_mentions
    
    def interactive_mix_twitter_locate(tweets, cityFile):
        with open(cityFile, 'r') as file:
            cities = [city.strip().lower() for city in file.readlines()]
        cities_from_geo = set()
        cities_from_text = set()
        for tweet in tweets:
            if 'geo' in tweet and tweet['geo'] is not None:
                for city in cities:
                    if city in tweet['geo'].lower():
                        cities_from_geo.add(city)
            if 'tweet' in tweet:
                text = tweet['tweet']
            elif 'text' in tweet:
                text = tweet['text']
            else: continue
            for city in cities:
                if city in text.lower():
                    cities_from_text.add(city)
        return list(cities_from_geo.union(cities_from_text))

    
    def baseline_twitter_locate(self, cityFile):
        print("not executable")
