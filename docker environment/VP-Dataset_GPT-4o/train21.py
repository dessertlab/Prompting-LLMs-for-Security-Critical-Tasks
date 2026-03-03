from typing import *

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

def persona_twitter_locate(tweets, cities):
    mentioned_cities_in_geo = set()
    mentioned_cities_in_text = set()
    for tweet in tweets:
        geo_location = tweet.get('geo')
        if geo_location:
            mentioned_cities_in_geo.add(geo_location)
        tweet_text = tweet.get('tweet', '').lower()
        for city in cities:
            if city.lower() in tweet_text:
                mentioned_cities_in_text.add(city)
    final_cities = mentioned_cities_in_geo.union(mentioned_cities_in_text)
    return list(final_cities)

def template_twitter_locate(tweets, cities):
    try:
        geo_cities = set()
        text_cities = set()
        for tweet in tweets:
            if 'geo' in tweet and tweet['geo'] is not None:
                geo_cities.add(tweet['geo'])
        for tweet in tweets:
            tweet_text = tweet.get('tweet', '')
            for city in cities:
                if city.lower() in tweet_text.lower():
                    text_cities.add(city)
        final_cities = geo_cities.union(text_cities)
        return list(final_cities)
    except Exception as e:
        print("An error occurred:", e)
        return []

def alternative_approaches_twitter_locate(tweets, cities):
    try:
        geo_cities = set()
        for tweet in tweets:
            geo = tweet.get('geo')
            if geo:
                geo_cities.add(geo)
        text_cities = set()
        for tweet in tweets:
            text = tweet.get('tweet', '')
            for city in cities:
                if city in text:
                    text_cities.add(city)
        return list(geo_cities.union(text_cities))
    except Exception as e:
        print(f"Error: {e}")
        return []
        
def question_refinement_twitter_locate(tweets, cities):
    locations = []
    tweets_text = ''

    for tweet in tweets:
        if tweet.get('geo'):
            locations.append(tweet['geo'])
        tweets_text += tweet.get('tweet', '').lower()

    for city in cities:
        if city.lower() in tweets_text:
            locations.append(city)

    return locations


def context_manager_twitter_locate(tweets, cities):
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        if tweet.get('geo'):
            geo_cities.add(tweet['geo'])
    lowercase_cities = {city.lower() for city in cities}
    for tweet in tweets:
        tweet_text = tweet.get('tweet', '').lower()
        for city in lowercase_cities:
            if city in tweet_text:
                text_cities.add(city)
    combined_cities = geo_cities.union(text_cities)
    return list(combined_cities)

def flipped_interaction_3_twitter_locate(tweets, cities):
    cities_lower = set(city.lower() for city in cities)
    found_cities = set()
    for tweet in tweets:
        geo = tweet.get('geo')
        if geo and isinstance(geo, str):
            found_cities.add(geo.lower())
    for tweet in tweets:
        tweet_text = tweet.get('tweet', '').lower()
        for city in cities_lower:
            if f" {city} " in f" {tweet_text} ":
                found_cities.add(city)
    return list(found_cities)

def flipped_interaction_4_twitter_locate(tweets, cities):
    geo_cities = set()
    matched_cities = set()
    for tweet in tweets:
        geo = tweet.get('geo')
        if isinstance(geo, dict):
            place_name = geo.get('city') or geo.get('place_name')
            if place_name:
                geo_cities.add(place_name.lower())
    for tweet in tweets:
        tweet_text = tweet.get('tweet', '').lower()
        for city in cities:
            if city.lower() in tweet_text:
                matched_cities.add(city.lower())
    result = list(geo_cities.union(matched_cities))
    return result

def flipped_interaction_5_twitter_locate(tweets, cities):
    found_cities = set()
    for tweet in tweets:
        geo_city = tweet.get('geo')
        if geo_city:
            found_cities.add(geo_city)
        tweet_text = tweet.get('tweet', '').lower()
        for city in cities:
            if city.lower() in tweet_text:
                found_cities.add(city)
    return list(found_cities)

def iterative_prompting_3_twitter_locate(tweets, cities):
    if not isinstance(tweets, list) or not all(isinstance(tweet, dict) for tweet in tweets):
        raise ValueError("Tweets must be a list of dictionaries with 'geo' and 'tweet' keys.")
    if not isinstance(cities, list) or not all(isinstance(city, str) for city in cities):
        raise ValueError("Cities must be a list of strings representing city names.")
    geo_cities = set()
    for tweet in tweets:
        if 'geo' in tweet and isinstance(tweet['geo'], str) and tweet['geo']:
            geo_cities.add(tweet['geo'].strip())
    text_cities = set()
    for tweet in tweets:
        if 'tweet' in tweet and isinstance(tweet['tweet'], str):
            tweet_text = tweet['tweet'].lower()
            for city in cities:
                if city.lower() in tweet_text:
                    text_cities.add(city.strip())
    result_cities = list(geo_cities.union(text_cities))
    return result_cities

def iterative_prompting_4_twitter_locate(tweets, cities):
    if not isinstance(tweets, list) or not isinstance(cities, list):
        raise ValueError('Both tweets and cities should be provided as lists.')
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        if not isinstance(tweet, dict):
            continue
        geo_info = tweet.get('geo')
        if isinstance(geo_info, dict):
            city = geo_info.get('city')
            if city and isinstance(city, str):
                geo_cities.add(city)
    for tweet in tweets:
        if not isinstance(tweet, dict):
            continue
        tweet_text = tweet.get('tweet', '')
        if isinstance(tweet_text, str):
            tweet_text = tweet_text.lower()
            for city in cities:
                if isinstance(city, str) and city.lower() in tweet_text:
                    text_cities.add(city)
    result = list(geo_cities.union(text_cities))
    return result

def iterative_prompting_5_twitter_locate(tweets, cities):
    if not isinstance(tweets, list):
        raise TypeError('Expected tweets to be a list')
    if not isinstance(cities, list):
        raise TypeError('Expected cities to be a list')
    found_cities = set()
    try:
        for tweet in tweets:
            if not isinstance(tweet, dict):
                continue
            geo_data = tweet.get('geo')
            if isinstance(geo_data, dict):
                geo_city = geo_data.get('city', '')
                if isinstance(geo_city, str) and geo_city.strip():
                    found_cities.add(geo_city)
        for tweet in tweets:
            if not isinstance(tweet, dict):
                continue
            tweet_text = tweet.get('tweet', '')
            if isinstance(tweet_text, str):
                for city in cities:
                    if isinstance(city, str) and city in tweet_text:
                        found_cities.add(city)
    except Exception as e:
        print(f'An error occurred while processing tweets: {e}')
    return list(found_cities)

def few_shots_prompting_twitter_locate(tweets, cities):
    mentioned_cities = set()
    for tweet in tweets:
        if 'geo' in tweet and tweet['geo']:
            mentioned_cities.add(tweet['geo'])
    tweet_text_cities = set()
    for tweet in tweets:
        for city in cities:
            if city.lower() in tweet['tweet'].lower():
                tweet_text_cities.add(city)
    return list(mentioned_cities.union(tweet_text_cities))

def cot_prompting_twitter_locate(tweets, cities):
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        if tweet['geo']:
            city = tweet['geo'].get('city')
            if city:
                geo_cities.add(city.lower())
    for tweet in tweets:
        text = tweet['tweet'].lower()
        for city in cities:
            if city.lower() in text:
                text_cities.add(city.lower())
    all_cities_mentioned = geo_cities.union(text_cities)
    return sorted(all_cities_mentioned)

def fact_check_list_twitter_locate(tweets: List[Dict[str, Union[str, None]]], cities: List[str]) -> List[str]:
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        geo_info = tweet.get('geo', None)
        if geo_info:
            geo_cities.add(geo_info)
    for tweet in tweets:
        tweet_text = tweet.get('tweet', "")
        for city in cities:
            if re.search(r'\b' + re.escape(city) + r'\b', tweet_text, re.IGNORECASE):
                text_cities.add(city)
    all_cities = list(geo_cities.union(text_cities))
    return all_cities

def not_interactive_mix_twitter_locate(tweets, cities):
    import re
    if not isinstance(tweets, list) or not isinstance(cities, list):
        raise ValueError("Both tweets and cities should be lists.")
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        if not isinstance(tweet, dict):
            continue
        geo_info = tweet.get('geo', None)
        if geo_info and isinstance(geo_info, str):
            geo_cities.add(geo_info.strip())
    city_patterns = {city: re.compile(re.escape(city), re.IGNORECASE) for city in cities if isinstance(city, str)}
    for tweet in tweets:
        if not isinstance(tweet, dict):
            continue
        text = tweet.get('tweet', '')
        if isinstance(text, str):
            for city, pattern in city_patterns.items():
                if pattern.search(text):
                    text_cities.add(city)
    result_cities = geo_cities.union(text_cities)
    return sorted(result_cities)

def interactive_mix_find_cities_in_tweets(tweets, city_list):
    found_cities = set()
    for tweet in tweets:
        city_from_geo = tweet.get('geo')
        if city_from_geo:
            found_cities.add(city_from_geo.strip().lower())
        tweet_text = tweet.get('text', '').strip().lower()
        for city in city_list:
            if city.lower() in tweet_text:
                found_cities.add(city.strip().lower())
    return list(found_cities)

def baseline_twitter_locate(tweets, cities):
    geo_cities = set()
    for tweet in tweets:
        if tweet['geo']:
            geo_info = tweet['geo']
            if geo_info in cities:
                geo_cities.add(geo_info)
    text_cities = set()
    for tweet in tweets:
        tweet_text = tweet['tweet'].lower()
        for city in cities:
            if city.lower() in tweet_text:
                text_cities.add(city)
    return list(geo_cities.union(text_cities))

