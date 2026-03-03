from typing import *
import re
from collections import deque

def ground_truth_code_twitter_locate(tweets, cities):
    locations = []
    locCnt = 0
    cityCnt = 0
    tweetsText = ""

    for tweet in tweets:
        tweet_text = tweet['tweet'].lower()
        geo = tweet['geo']

        for city in cities:
            if city.lower() in tweet_text:
                cityCnt += 1
                # Se ha geo, associala alla città
                if geo is not None:
                    locations.append({city: geo})
                    locCnt += 1
                else:
                    locations.append({city: None})

        tweetsText += tweet_text

    return locations

def persona__twitter_locate(tweets, cities):
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        if tweet['geo'] and 'coordinates' in tweet['geo']:
            geo_cities.add(tweet['geo']['coordinates'])
        for city in cities:
            if city.lower() in tweet['tweet'].lower():
                text_cities.add(city)
    return list(geo_cities.union(text_cities))

def template__twitter_locate(tweets, cities):
	try:
		cities_from_geo = {city.get('geo', {}).get('city') for tweet in tweets if city.get('geo', {}).get('city')}
		mention_cities = {city for city in cities if any(city.lower() in tweet['tweet'].lower() for tweet in tweets)}
		return list(cities_from_geo.union(mention_cities))
	except Exception as e:
		return []

def question_refinement__twitter_locate(tweets, cities):
    import re
    seen_cities = set()
    geo_cities = [tweet.get('geo', {}).get('city').lower() for tweet in tweets if tweet.get('geo') and tweet.get('geo', {}).get('city')]
    for city in set(geo_cities):
        seen_cities.add(city)
    city_pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, [city.lower() for city in cities])) + r')\b', re.IGNORECASE)
    for tweet in tweets:
        matches = city_pattern.findall(tweet.get('tweet', ''))
        for match in matches:
            seen_cities.add(match)
    return list(seen_cities)

def alternative_approaches__twitter_locate(tweets, cities):
	geo_cities = {tweet['geo']['coordinates'] for tweet in tweets if tweet['geo']}
	text_cities = {city for tweet in tweets for city in cities if city.lower() in tweet['tweet'].lower()}
	return list(geo_cities.union(text_cities))

def context_manager__twitter_locate(tweets, cities):
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        if tweet['geo'] and tweet['geo']['coordinates']:
            geo_cities.add(tweet['geo']['coordinates'])
        text = tweet['tweet'].lower()
        for city in cities:
            if city.lower() in text:
                text_cities.add(city)
    return list(geo_cities.union(text_cities))

def flipped_interaction_3__twitter_locate(tweets, cities):
    city_set = set(city.lower() for city in cities)
    located_cities = set()
    for tweet in tweets:
        geo_city = tweet.get('geo')
        if geo_city and isinstance(geo_city, str) and geo_city.strip():
            located_cities.add(geo_city.lower())
        tweet_text = tweet['tweet'].lower()
        for city in city_set:
            if re.search(r'\b' + re.escape(city) + r'\b', tweet_text):
                located_cities.add(city)
    return sorted(located_cities)


def flipped_interaction_4__twitter_locate(tweets, cities):
    import re
    import requests
    def reverse_geocode(lat, lon):
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'address' in data:
                return data['address'].get('city') or data['address'].get('town') or data['address'].get('village')
        return None
    city_set = set()
    cities_lower = {city.lower() for city in cities}
    abbreviations = {
        'ny': 'new york',
        'la': 'los angeles',
        'sf': 'san francisco',
        'nyc': 'new york city'
    }
    for tweet in tweets:
        if tweet['geo'] and 'coordinates' in tweet['geo']:
            lat, lon = tweet['geo']['coordinates']
            city = reverse_geocode(lat, lon)
            if city:
                city_set.add(city.lower())
        text = tweet['tweet'].lower()
        text = re.sub(r'a-z0-9 ]', '', text)
        for city in cities_lower:
            if city in text:
                city_set.add(city)
        for abbr, full_city in abbreviations.items():
            if f'{abbr}\b' in text and full_city in cities_lower:
                city_set.add(full_city)
    return list(city_set)

def flipped_interaction_5__twitter_locate(tweets, cities):
    cities_lower = set(city.lower() for city in cities)
    cities_in_tweets = set()
    for tweet in tweets:
        text = tweet['tweet'].lower()
        words = text.split()
        for word in words:
            if word in cities_lower:
                cities_in_tweets.add(word)
    original_case_cities_in_tweets = {city for city in cities if city.lower() in cities_in_tweets}
    final_cities = set(original_case_cities_in_tweets).union(set(cities))
    return list(final_cities)


def iterative_prompting_3__twitter_locate(tweets, cities):
    if not isinstance(tweets, list):
        raise ValueError('tweets must be a list')
    if not isinstance(cities, list):
        raise ValueError('cities must be a list')
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        if not isinstance(tweet, dict):
            raise ValueError('each tweet must be a dictionary')
        geo_info = tweet.get('geo')
        if isinstance(geo_info, dict) and 'city' in geo_info:
            city = geo_info['city']
            if not isinstance(city, str):
                raise ValueError('city in geo attribute must be a string')
            geo_cities.add(city)
        if 'tweet' not in tweet or not isinstance(tweet['tweet'], str):
            raise ValueError('tweet text must be a string')
        for city in cities:
            if not isinstance(city, str):
                raise ValueError('each city in the cities list must be a string')
            if city.lower() in tweet['tweet'].lower():
                text_cities.add(city)
    return list(geo_cities.union(text_cities))

def iterative_prompting_4__twitter_locate(tweets, cities):
        if not isinstance(tweets, list):
                raise ValueError("tweets must be a list")
        if not isinstance(cities, list):
                raise ValueError("cities must be a list")
        if not all(isinstance(city, str) for city in cities):
                raise ValueError("All cities must be strings")
        geo_cities = set()
        mentioned_cities = set(city.lower() for city in cities)
        for tweet in tweets:
                if not isinstance(tweet, dict):
                        raise ValueError("Each tweet must be a dictionary")
                if 'geo' not in tweet:
                        raise KeyError("geo key is missing in tweet")
                if isinstance(tweet['geo'], dict) and 'coordinates' in tweet['geo']:
                    try:
                        city_name = tweet['geo']['coordinates']
                        if isinstance(city_name, (list, tuple)) and len(city_name) == 2:
                            pass
                    except Exception as e:
                        print(f"Errore nell'elaborazione delle coordinate: {e}")


def iterative_prompting_5__twitter_locate(tweets, cities):
    if not isinstance(tweets, list):
        raise TypeError('tweets must be a list')
    if not all(isinstance(tweet, dict) for tweet in tweets):
        raise ValueError('each tweet must be a dictionary')
    if not isinstance(cities, list):
        raise TypeError('cities must be a list')
    if not all(isinstance(city, str) for city in cities):
        raise ValueError('each city must be a string')
    geo_cities = set()
    for tweet in tweets:
        try:
            geo_info = tweet['geo']
            if geo_info and 'coordinates' in geo_info and 'type' in geo_info and geo_info['type'] == 'Point':
                if 'city' in geo_info:
                    geo_cities.add(geo_info['city'])
        except KeyError:
            continue
    mentioned_cities = set()
    for tweet in tweets:
        try:
            tweet_text = tweet['tweet'].lower()
        except KeyError:
            continue
        for city in cities:
            if city.lower() in tweet_text:
                mentioned_cities.add(city)
    return list(geo_cities.union(mentioned_cities))

def few_shots_prompting__twitter_locate(tweets, cities):
	geo_cities = [tweet['geo']['coordinates'] for tweet in tweets if tweet['geo']]
	text_cities = [city for city in cities if any(city.lower() in tweet['tweet'].lower() for tweet in tweets)]
	return list(set(geo_cities + text_cities))

def cot_prompting__twitter_locate(tweets, cities):
	geo_cities = set()
	for tweet in tweets:
		if tweet['geo'] and 'coordinates' in tweet['geo']:
			continue
		if tweet['geo'] and isinstance(tweet['geo'], dict):
			location = tweet['geo'].get('place')
			if location:
				name = location.get('name')
				if name in cities:
					geo_cities.add(name)
	tweet_cities = set(city for city in cities if any(city.lower() in tweet['tweet'].lower() for tweet in tweets))
	return list(geo_cities.union(tweet_cities))

def fact_check_list__twitter_locate(tweets, cities):
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        if tweet['geo'] and isinstance(tweet['geo'], dict) and 'city' in tweet['geo']:
            geo_cities.add(tweet['geo']['city'].lower())
        for city in cities:
            if city.lower() in tweet['tweet'].lower():
                text_cities.add(city.lower())
    located_cities = geo_cities.union(text_cities)
    return sorted(located_cities)

def not_interactive_mix__twitter_locate(tweets, cities):
    cities_in_geo = set()
    cities_queue = deque(cities)
    city_name_pattern = re.compile(
    r'(?:' + '|'.join(re.escape(city) for city in cities) + r')\b',
    re.IGNORECASE
)
    for tweet in tweets:
        geo_info = tweet.get('geo')
        if geo_info and isinstance(geo_info, dict):
            if geo_info.get('type') and geo_info.get('type').lower() == 'place':
                place_full_name = geo_info.get('full_name')
                if place_full_name and isinstance(place_full_name, str):
                    city_name, _ = place_full_name.split(',')
                    cities_in_geo.add(city_name.strip())
        text = tweet.get('tweet', '')
        if isinstance(text, str):
            matches = city_name_pattern.findall(text)
            for city in matches:
                cities_in_geo.add(city)
    return sorted(cities_in_geo)

def interactive_mix__twitter_locate(tweets, cities):
    import re
    locations = set()
    cities_set = {city.lower().strip() for city in cities}
    for tweet in tweets:
        if tweet.get('geo') is not None:
            locations.add(tweet['geo'].lower().strip())
        try:
            tweet_text = tweet['tweet'].lower().strip()
            for city in cities_set:
                if re.search(rf'\b{re.escape(city)}\b', tweet_text):
                    locations.add(city)
        except KeyError:
            continue
    return list(locations)

def baseline__twitter_locate(tweets, cities):
	cities_in_geo = {city for tweet in tweets if tweet['geo'] and tweet['geo']['coordinates'] for city in cities if city.lower() in tweet['tweet'].lower()}
	cities_in_text = {city for tweet in tweets for city in cities if city.lower() in tweet['tweet'].lower()}
	return list(cities_in_geo.union(cities_in_text))
