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
    city_mentions_geo = []
    city_mentions_text = []
    for tweet in tweets:
        mentioned_cities_geo = set(tweet['geo']).intersection(set(cities))
        mentioned_cities_text = set(re.findall(r'\b(' + '|'.join(cities) + ')', tweet['tweet'], re.I)).difference(city_mentions_geo)
        city_mentions_geo.update(mentioned_cities_geo)
        city_mentions_text.update(mentioned_cities_text)
    return list(city_mentions_geo.union(city_mentions_text))

def template_twitter_locate(tweets, cities):
    from collections import defaultdict
    city_mentions_geo = []
    city_mentions_text = defaultdict(int)
    for tweet in tweets:
        geo = tweet.get('geo')
        if geo:
            cities_in_geo = set(geo.get('place_type', []))
            city_mentions_geo.extend(cities_in_geo & set(cities))
        text = tweet.get('tweet', '').lower()
        if text:
            for city in cities:
                if city.lower() in text:
                    city_mentions_text[city] += 1
    mentioned_cities = set(city_mentions_geo)
    textually_mentioned_cities = {city for city, count in city_mentions_text.items() if count > 0}
    final_mentioned_cities = mentioned_cities.union(textually_mentioned_cities)
    return list(final_mentioned_cities)

def question_refinement_find_cities_in_tweets(tweets, cities):
    mentioned_cities = set()
    for tweet in tweets:
        if 'geo' in tweet and tweet['geo']:
            tweet_cities = set(tweet['geo'].get('place', {}).get('full_name', '').lower().split())
            mentioned_cities.update(tweet_cities.intersection(cities))
    return list(mentioned_cities)

def alternative_approaches_twitter_locate(tweets, cities):
    geo_cities = {geo['place_id'] for tweet in tweets if 'geo' in tweet and tweet['geo']}
    text_cities = {city for tweet in tweets for city in tweet['text'].split() if city in cities}
    return list(set(geo_cities.union(text_cities)))

def context_manager_twitter_locate(tweets, cities):
    mentioned_in_geo = set()
    mentioned_in_text = set(cities)
    city_mentions = set()
    for tweet in tweets:
        if tweet['geo']:
            for city in cities:
                if city in tweet['geo']:
                    mentioned_in_geo.add(city)
        if tweet['tweet']:
            for city in cities:
                if city in tweet['tweet']:
                    mentioned_in_text.add(city)
    city_mentions = mentioned_in_geo.union(mentioned_in_text)
    return list(city_mentions)

def iterative_prompting_3_twitter_locate(tweets, cities):
    if not isinstance(tweets, list) or not all(isinstance(tweet, dict) for tweet in tweets):
        raise ValueError("Input must be a list of dictionaries representing tweets.")
    geo_cities = set()
    text_cities = set()
    for tweet in tweets:
        if not tweet.get('geo'):
            continue
        geo = tweet['geo']
        if geo.get('type') != 'Point':
            continue
        latitude = geo['coordinates'][1]
        longitude = geo['coordinates'][0]
        city = find_city(latitude, longitude)
        if city:
            geo_cities.add(city)
        text = tweet['tweet'].lower()
        words = text.split()
        for word in words:
            if word in cities:
                text_cities.add(word)
    return list(geo_cities.union(text_cities))

import logging
import re
def iterative_prompting_4_twitter_locate(tweets, cities):
    if not isinstance(tweets, list):
        raise TypeError('tweets must be a list')
    if not all(isinstance(city, str) for city in cities):
        raise TypeError('all items in cities must be strings')
    geo_cities = set()
    text_cities = set(cities)
    for tweet in tweets:
        if not isinstance(tweet, dict):
            logging.warning('Skipping invalid tweet: %s', tweet)
            continue
        geo = tweet.get('geo', {})
        if isinstance(geo, dict):
            coords = geo.get('coordinates')
            if isinstance(coords, list) and all(isinstance(coord, (list, tuple)) for coord in coords):
                geo_cities.update(coords)
            else:
                logging.warning('Invalid geo coordinates: %s', geo)
        else:
            logging.warning('Skipping tweet without valid geo data: %s', tweet)
        text = tweet.get('tweet', '')
        if isinstance(text, str):
            text_cities.update(re.findall(r'\b(' + '|'.join(map(re.escape, cities)) + ')\b', text))
        else:
            logging.warning('Skipping tweet without text: %s', tweet)
    return list(geo_cities.union(text_cities))

def iterative_prompting_5_twitter_locate(tweets, cities):
    if not isinstance(tweets, list) or not all(isinstance(tweet, dict) for tweet in tweets):
        raise ValueError('The tweets parameter must be a list of dictionaries.')
    if not isinstance(cities, list) or not all(isinstance(city, str) for city in cities):
        raise ValueError('The cities parameter must be a list of strings.')
    geo_cities = \
        {tweet['geo']['place_id'] for tweet in tweets if 'geo' in tweet and \
        isinstance(tweet['geo'], dict) and 'place_id' in tweet['geo']}
    mentioned_cities = set(cities) & geo_cities
    text_cities = \
        {city for tweet in tweets for city in tweet['tweet'].split() if city in cities}
    all_cities = list(set().union(mentioned_cities, text_cities))
    return all_cities

def few_shots_prompting_twitter_locate(tweets, cities):
    mentioned_cities_geo = []
    mentioned_cities_text = []
    for tweet in tweets:
        tweet_text = tweet['tweet']
        tweet_geo = tweet['geo']
        if tweet_geo:
            for city in cities:
                if city in tweet_geo.get('place', ''):
                    mentioned_cities_geo.append(city)
        if tweet_text:
            for city in cities:
                if city in tweet_text:
                    mentioned_cities_text.append(city)
    return list(set(mentioned_cities_geo + mentioned_cities_text))

def cot_prompting_twitter_locate(tweets, cities):
    city_mentions = set()
    text_city_mentions = set(cities)
    for tweet in tweets:
        geo = tweet['geo']
        if geo:
            for city in geo.split(','):
                city_name = city.split(' ')[-1]
                city_mentions.add(city_name)
    return list(city_mentions.union(text_city_mentions))

import json
import urllib.parse
from collections import Counter
def fact_check_list_twitter_locate(tweets, cities):
    mentioned_cities_geo = set()
    for tweet in tweets:
        geo = tweet.get('geo', None)
        if geo and 'place_id' in geo:
            place_name = json.loads(geo)['place']['name']
            if place_name in cities:
                mentioned_cities_geo.add(place_name)
    mentioned_cities_text = set()
    tweet_texts = [tweet['tweet'] for tweet in tweets if 'tweet' in tweet]
    for text in tweet_texts:
        for city in cities:
            if city.lower() in text.lower():
                mentioned_cities_text.add(city)
    combined_cities = sorted([city for city in mentioned_cities_geo.union(mentioned_cities_text)])
    return combined_cities

def not_interactive_mix_twitter_locate(tweets, cities):
    found_cities = set()
    geo_cities = set()
    for tweet in tweets:
        geo = tweet['geo']
        if geo:
            try:
                lat, lon = map(float, geo['coordinates'].split(','))
                found_cities.add(geo['place_id'])
                geo_cities.add(geo['place_id'])
            except ValueError:
                pass
    for city in cities:
        city_lower = city.lower()
        for tweet in tweets:
            text = tweet['tweet'].lower()
            if city_lower in text:
                found_cities.add(city)
    combined_cities = found_cities.union(geo_cities, cities)
    return list(combined_cities)

def baseline_twitter_locate(tweets, cities):
    geo_mentions = set()
    text_mentions = set(cities)
    for tweet in tweets:
        if tweet.get('geo'):
            geo_coords = tweet['geo'].get('coordinates')
            if geo_coords:
                city = geo_coords[0]
                geo_mentions.add(city)
        text = tweet.get('tweet', '')
        text_mentions &= set(re.findall(r'\b(' + '|'.join(cities) + r')\b', text, re.IGNORECASE))
    return list(geo_mentions | text_mentions)

