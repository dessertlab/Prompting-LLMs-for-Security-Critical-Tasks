
import re 
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

from geopy.geocoders import Nominatim

def get_city_from_coordinates(lat, lon):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.reverse((lat, lon), exactly_one=True)
    if location and 'city' in location.raw['address']:
        return location.raw['address']['city']
    return None

def persona_twitter_locate(tweets, cities):
    mentioned_cities = set()
    for tweet in tweets:
        if 'geo' in tweet and tweet['geo'] and tweet['geo']['coordinates'] and tweet['geo']['type'] == 'Point':
            city = get_city_from_coordinates(tweet['geo']['coordinates'][0], tweet['geo']['coordinates'][1])
            if city:
                mentioned_cities.add(city)
    cities_from_text = set()
    for city in cities:
        for tweet in tweets:
            if city.lower() in tweet['tweet'].lower():
                cities_from_text.add(city)
                break
    return list(mentioned_cities.union(cities_from_text))

def template_twitter_locate(tweets, cities):
    try:
        located_cities = set()
        for tweet in tweets:
            if isinstance(tweet, dict):
                if 'geo' in tweet and tweet['geo']:
                    located_cities.add(tweet['geo']['place']['name'])
                if 'tweet' in tweet:
                    for city in cities:
                        if city.lower() in tweet['tweet'].lower():
                            located_cities.add(city)
            else:
                raise ValueError("Invalid tweet format")
        return list(located_cities)
    except Exception as e:
        return(f"Error occurred: {str(e)}")
    
def question_refinement_twitter_locate(tweets, cities):
	try:
		if not isinstance(tweets, list) or not isinstance(cities, list):
			raise ValueError('Input must be a list.')
		geo_cities = set(city.strip().lower() for tweet in tweets for city in tweet.get('geo', '').split(',') if city.strip())
		text_cities = set(city.strip().lower() for city in cities for tweet in tweets if city.strip().lower() in tweet.get('text', '').lower())
		return list(geo_cities.union(text_cities))
	except ValueError as e:
		return(f'Error: {e}')
	except Exception as e:
		return(f'An error occurred: {e}')
     
def alternative_approaches_twitter_locate(tweets, cities):
	cities_in_tweets = set()
	cities_in_geo = set()
	for tweet in tweets:
		if 'geo' in tweet and tweet['geo'] is not None:
			if isinstance(tweet['geo'], dict) and 'coordinates' in tweet['geo']:
				city_name =''.join([str(coord) for coord in tweet['geo']['coordinates']])
				cities_in_geo.add(city_name)
		elif isinstance(tweet['geo'], str):
			cities_in_geo.add(tweet['geo'])
		for city in cities:
			if city.lower() in tweet['tweet'].lower():
				cities_in_tweets.add(city)
	return {'cities_in_tweets': list(cities_in_tweets.union(cities_in_geo))}

def context_manager_twitter_locate(tweets, cities):
    geo_cities = [tweet['geo']['coordinates'][1] if tweet['geo'] is not None else None for tweet in tweets]
    geo_cities = [city for city in geo_cities if city is not None]; cities_in_tweets = []
    for city in cities:
        for tweet in tweets:
            if city in tweet['tweet']:
                cities_in_tweets.append(city)
                break
    cities_in_tweets = list(set(cities_in_tweets))
    return list(set([city for city in geo_cities + cities_in_tweets]))

def flipped_interaction_3__twitter_locate(tweets, cities):
    city_set = set(cities)
    cities_from_geo = set()
    cities_from_text = set()
    for tweet in tweets:
        if 'geo' in tweet and isinstance(tweet['geo'], dict):
            city = tweet['geo'].get('city', '').strip()
            if city and city in city_set:
                cities_from_geo.add(city)
        for city in city_set:
            if city.strip().lower() in tweet['tweet'].lower():
                cities_from_text.add(city)
    return list(cities_from_geo.union(cities_from_text))

def flipped_interaction_4__twitter_locate(tweets, cities):
    locations = []
    for tweet in tweets:
        if 'geo' in tweet and tweet['geo'] is not None:
            locations.append(tweet['geo'])
        tweet_text = tweet['tweet'].lower()
        for city in [c.lower() for c in cities]:
            if city in tweet_text and city not in [loc.lower() for loc in locations]:
                locations.append(city)
    return locations

def flipped_interaction_5__twitter_locate(tweets, cities):
    found_cities = set()
    for tweet in tweets:
        if 'geo' in tweet and tweet['geo'] is not None and isinstance(tweet['geo'], str):
            found_cities.add(tweet['geo'])
    for city in cities:
        city = city.lower()
        for tweet in tweets:
            if city in tweet['tweet'].lower():
                found_cities.add(city)
                break
    return list(found_cities)

def iterative_prompting_3__twitter_locate(tweets, cities):
    if not isinstance(tweets, list) or not isinstance(cities, list):
        raise TypeError("Both 'tweets' and 'cities' must be lists")
    if not all(isinstance(tweet, dict) for tweet in tweets):
        raise ValueError("All elements in 'tweets' must be dictionaries")
    if not all(isinstance(city, str) for city in cities):
        raise ValueError("All elements in 'cities' must be strings")
    cities_from_geo = set()
    cities_from_text = set()
    for tweet in tweets:
        try:
            geo_data = tweet.get('geo', {})
            if 'coordinates' in geo_data and geo_data['coordinates'] not in [[None, None]]:
                for city in cities:
                    if city.lower() in str(geo_data['coordinates'][0]).lower():
                        cities_from_geo.add(city)
            place_data = geo_data.get('place', {})
            if place_data and 'name' in place_data:
                for city in cities:
                    if city.lower() in place_data['name'].lower():
                        cities_from_geo.add(city)
            tweet_text = tweet.get('tweet', '')
            for city in cities:
                if city.lower() in tweet_text.lower():
                    cities_from_text.add(city)
        except KeyError as e:
            return(f"Warning: Missing key in tweet. Key: {e}")
    return list(cities_from_geo.union(cities_from_text))

from geopy.geocoders import Nominatim

def reverse_geocode(coordinates):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.reverse(coordinates, exactly_one=True)
    if location:
        # Restituisce il nome della città, se disponibile
        address = location.raw.get('address', {})
        city = address.get('city') or address.get('town') or address.get('village')
        return city
    return None

def iterative_prompting_4__twitter_locate(tweets, cities):
    if not isinstance(tweets, list) or not all(isinstance(tweet, dict) for tweet in tweets):
        raise ValueError('Invalid input: tweets must be a list of dictionaries')
    if not isinstance(cities, list) or not all(isinstance(city, str) for city in cities):
        raise ValueError('Invalid input: cities must be a list of strings')
    geo_cities = []
    for tweet in tweets:
        try:
            if tweet.get('geo') and tweet['geo'].get('coordinates'):
                city = reverse_geocode(tweet['geo']['coordinates'])
                if city and city.lower() in [c.lower() for c in cities]:
                    geo_cities.append(city)
        except KeyError as e:
            print(f'Error parsing tweet data as JSON: {e}')
            try:
                print(f'Raw tweet data: {tweet}\n')
            except Exception as e:
                print(f'Error printing raw tweet data: {e}')
    text_cities = []
    for tweet in tweets:
        try:
            text = tweet.get('text', '').lower()
            for city in cities:
                if city.lower() in text:
                    text_cities.append(city)
                    break
        except Exception as e:
            print(f'Error parsing tweet data or text of the tweet: {e}')
    try:
        return list(set(geo_cities + text_cities))
    except Exception as e:
        return(f'Error: {e}. Please check your inputs. Returning None. ')
                                                
def iterative_prompting_5__twitter_locate(tweets, cities):
    if not isinstance(tweets, list) or not isinstance(cities, list):
        raise ValueError("'tweets' and 'cities' must be lists")
    if not all(isinstance(tweet, dict) for tweet in tweets):
        raise ValueError("All elements in 'tweets' must be dictionaries")
    if not all(isinstance(city, str) for city in cities):
        raise ValueError("All elements in 'cities' must be strings")
    cities_found = set()
    for idx, tweet in enumerate(tweets):
        try:
            if 'geo' in tweet and isinstance(tweet['geo'], dict):
                city_in_geo = tweet['geo'].get('place', {}).get('full_name')
                if city_in_geo and isinstance(city_in_geo, str):
                    city = city_in_geo.split(', ')[0].strip().casefold()
                    if city in (city.casefold() for city in cities):
                        cities_found.add(city)
            text = tweet.get('tweet', '')
            if text:
                text = str(text).casefold()
                for city in cities:
                    if city.casefold() in text and city not in cities_found:
                        cities_found.add(city)
        except Exception as e:
            return(f"Error processing tweet {idx}: {str(e)}")
    return list(cities_found)

def few_shots_prompting_twitter_locate(tweets, cities):
    cities_lower = [city.lower() for city in cities]
    cities_from_geo = []
    for tweet in tweets:
        if tweet['geo'] is not None:
            if 'coordinates' in tweet['geo'] and tweet['geo']['coordinates'] is not None:
                cities_from_geo.extend([city for city in cities_lower if city in tweet['geo']['coordinates']])
            elif 'place' in tweet['geo'] and tweet['geo']['place'] is not None:
                cities_from_geo.append(tweet['geo']['place']['name'].lower())
    cities_from_text = []
    for tweet in tweets:
        tweet_text = tweet['tweet'].lower()
        for city in cities_lower:
            if city in tweet_text and city not in cities_from_text:
                cities_from_text.append(city)
    cities_from_geo.extend([city for city in cities_from_text if city not in cities_from_geo])
    return list(set(cities_from_geo))

def cot_prompting_twitter_locate(tweets, cities):
    cities_from_geo = [tweet['geo'] for tweet in tweets if tweet['geo']]
    cities_from_text = []
    for city in cities:
        for tweet in tweets:
            if city.lower() in tweet['tweet'].lower() and city not in cities_from_text:
                cities_from_text.append(city)
    return list(set(cities_from_geo + cities_from_text))

def fact_check_list_twitter_locate(tweets, cities):
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        if 'geo' in tweet and tweet['geo']:
            geo_cities.add(tweet['geo'])
        text = tweet['tweet'].lower()
        for city in cities:
            city = city.lower()
            if re.search(r'\b' + re.escape(city) + r'\b', text):
                text_cities.add(city)
    return list(set(list(geo_cities) + list(text_cities)))

def not_interactive_mix_twitter_locate(tweets, cities):
	cities_found_geo = set()
	cities_found_text = set()
	try:
		for tweet in tweets:
			if 'geo' in tweet and tweet['geo']:
				if isinstance(tweet['geo'], str):
					cities_found_geo.add(tweet['geo'])
		for city in cities:
			for tweet in tweets:
				if 'tweet' in tweet:
					if isinstance(tweet['tweet'], str) and city in tweet['tweet']:
						cities_found_text.add(city)
	except Exception as e:
		return(f"An error occurred: {e}")
	return list(cities_found_geo.union(cities_found_text))

import re
def interactive_mix_twitter_locate(tweets, cities):
    citiesInGeo = set()
    citiesInText = set()
    citiesLower = [city.lower() for city in cities]
    for tweet in tweets:
        if 'from_user' in tweet and 'geo' in tweet:
            if 'full_name' in tweet['geo']:
                geoCityName = tweet['geo']['full_name'].strip().lower()
                if geoCityName in citiesLower:
                    citiesInGeo.add(geoCityName)
        for city in citiesLower:
            if re.search(r'\b' + re.escape(city) + r'\b', tweet['tweet'].lower(), re.IGNORECASE):
                citiesInText.add(city)
    return list(set(citiesInGeo).union(set(citiesInText)))

def baseline_twitter_locate(tweets, cities):
    geo_cities = [city for tweet in tweets for place in tweet['geo']['place'] if 'full_name' in place for city in [place['full_name']] if city]
    text_cities = []
    for city in cities:
        for tweet in tweets:
            if city.lower() in tweet['tweet'].lower():
                text_cities.append(city)
    return list(set(geo_cities + text_cities))
