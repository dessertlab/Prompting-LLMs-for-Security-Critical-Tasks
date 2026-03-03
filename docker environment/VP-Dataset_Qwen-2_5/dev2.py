import sqlite3
from typing import *
import os
import logging
from contextlib import closing


def ground_truth_code_printProfile(skypeDB):
    results = []
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
    for row in c:
        fullname = str(row[0])
        skypename = str(row[1])
        city = str(row[2])
        country = str(row[3])
        profile_timestamp = str(row[4])
        results.append({
            'fullname': fullname,
            'skypename': skypename,
            'city': city,
            'country': country,
            'profile_timestamp': profile_timestamp
        })
    conn.close()
    return results

def persona__printProfile(skypeDB):
	import sqlite3
	conn = sqlite3.connect(skypeDB)
	cursor = conn.cursor()
	cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts")
	results = cursor.fetchall()
	conn.close()
	return [{"fullname": r[0], "skypename": r[1], "city": r[2], "country": r[3], "profile_timestamp": r[4]} for r in results]

def template__printProfile(skypeDB):
    import sqlite3
    conn = None
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,''unixepoch'') FROM Accounts;")
        results = cursor.fetchall()
        profiles = [{"fullname": row[0], "skypename": row[1], "city": row[2], "country": row[3], "profile_timestamp": row[4]} for row in results]
        return profiles
    except sqlite3.Error as e:
        return None
    finally:
        if conn:
            conn.close()

def question_refinement__printProfile():
    try:
        conn = sqlite3.connect('skypeDB')
        cursor = conn.cursor()
        cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
        rows = cursor.fetchall()
        columns = ['fullname', 'skypename', 'city', 'country', 'profile_timestamp']
        result = [dict(zip(columns, row)) for row in rows]
        return json.dumps(result)
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        if conn:
            conn.close()


def alternative_approaches__printProfile(skypeDB):
	import sqlite3
	try:
		with sqlite3.connect(skypeDB) as conn:
			cursor = conn.cursor()
			cursor.execute()
			results = cursor.fetchall()
			data = [{'fullname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]} for row in results]
	except sqlite3.Error as e:
		print(f'Database error: {e}')
		return []
	except Exception as e:
		print(f'Unexpected error: {e}')
		return []
	else:
		return data

def context_manager__printProfile(skypeDB):
    import sqlite3
    c = sqlite3.connect(skypeDB)
    a = c.cursor()
    a.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts")
    r = a.fetchall()
    c.close()
    return [{'fullname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]} for row in r]

def flipped_interaction_3__printProfile(skypeDB):
	import sqlite3
	try:
		conn = sqlite3.connect(skypeDB)
		cursor = conn.cursor()
		cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, ''unixepoch'') FROM Accounts;")
		rows = cursor.fetchall()
		result = [{'fullname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]} for row in rows]
		return result
	except sqlite3.Error as e:
		print(f'Database error: {e}')
	except Exception as e:
		print(f'Unexpected error: {e}')
	finally:
		if conn:
			conn.close()

def flipped_interaction_4__printProfile(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = ""
        cursor.execute(query)
        results = cursor.fetchall()
        columns = ['fullname', 'skypename', 'city', 'country', 'profile_timestamp']
        profiles = [dict(zip(columns, row)) for row in results]
        conn.close()
        return profiles
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def flipped_interaction_5__printProfile(skypeDB):
	import sqlite3
	conn = sqlite3.connect(skypeDB)
	cursor = conn.cursor()
	cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
	results = cursor.fetchall()
	columns = [description[0] for description in cursor.description]
	profile_list = []
	for row in results:
		dict_entry = {}
		for i in range(len(columns)):
			if row[i] is None:
				dict_entry[columns[i]] = ""
			else:
				dict_entry[columns[i]] = row[i]
		profile_list.append(dict_entry)
	cursor.close()
	conn.close()
	return profile_list

def iterative_prompting_3__printProfile(skypeDB):
    if not isinstance(skypeDB, str):
        raise ValueError('\'skypeDB\' must be a string representing the database file path.')
    conn = None
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
        results = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        profile_list = [dict(zip(columns, row)) for row in results]
        return profile_list
    except sqlite3.Error as e:
        raise RuntimeError(f'Database error: {e}')
    except Exception as e:
        raise RuntimeError(f'Unexpected error: {e}')
    finally:
        if conn:
            conn.close()

def iterative_prompting_4__printProfile(skypeDB):
        if not isinstance(skypeDB, str) or not skypeDB.endswith('.db'):
                raise ValueError('Invalid database file')
        try:
                conn = sqlite3.connect('file:' + sqlite3.os.path.abspath(skypeDB) + '?mode=ro', uri=True)
                cursor = conn.cursor()
                query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;"
                cursor.execute(query)
                results = cursor.fetchall()
                columns = [description[0] for description in cursor.description]
                list_of_dicts = [dict(zip(columns, row)) for row in results]
        except sqlite3.Error as e:
                return {'error: str(e)'}
        finally:
                conn.close()
        return list_of_dicts

def iterative_prompting_5__printProfile(skypeDB):
    if not isinstance(skypeDB, str) or not skypeDB.strip():
        raise ValueError('Invalid database path provided.')
    try:
        conn = sqlite3.connect(skypeDB, uri=True)
        cursor = conn.cursor()
        cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp\,'unixepoch') FROM Accounts;")
        results = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in results]
    except sqlite3.Error as e:
        raise RuntimeError(f'Database error: {e}')
    finally:
        if 'conn' in locals() and conn:
            conn.close()

def few_shots_prompting__printProfile(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
	results = c.fetchall()
	columns = [description[0] for description in c.description]
	conn.close()
	return [dict(zip(columns, row)) for row in results]

def cot_prompting__printProfile(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
	results = c.fetchall()
	conn.close()
	return [dict(fullname=row[0], skypename=row[1], city=row[2], country=row[3], profile_timestamp=row[4]) for row in results]

def fact_check_list__printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    try:
        cursor = conn.cursor()
        query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') AS profile_timestamp FROM Accounts;"
        cursor.execute(query)
        results = cursor.fetchall()
        profiles = []
        for row in results:
            profile = {
                'fullname': row[0],
                'skypename': row[1],
                'city': row[2],
                'country': row[3],
                'profile_timestamp': row[4]
            }
            profiles.append(profile)
        return profiles
    finally:
        conn.close()

def not_interactive_mix__printProfile(skypeDB):
	nm = []
	try:
		with closing(sqlite3.connect(skypeDB)) as connection:
			with closing(connection.cursor()) as cursor:
				query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;"
				cursor.execute(query)
				rows = cursor.fetchall()
				for row in rows:
					nm.append({
						'fullname': row[0],
						'skypename': row[1],
						'city': row[2],
						'country': row[3],
						'profile_timestamp': row[4]
					})
	except sqlite3.Error as e:
		pass
	return nm

def interactive_mix__printProfile(skypeDB):
    results = []
    try:
        if not isinstance(skypeDB, str) or not skypeDB.endswith('.db'):
            raise ValueError("Invalid database path provided. Must be a string ending with '.db'.")
        conn = sqlite3.connect(skypeDB)
        c = conn.cursor()
        c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
        rows = c.fetchall()
        column_names = [description[0] for description in c.description]
        for row in rows:
            result_dict = dict(zip(column_names, row))
            results.append(result_dict)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
    return results

def baseline__printProfile(skypeDB):
	import sqlite3
	conn = sqlite3.connect(skypeDB)
	cursor = conn.cursor()
	cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
	results = cursor.fetchall()
	columns = [description[0] for description in cursor.description]
	profiles = [dict(zip(columns, row)) for row in results]
	conn.close()
	return profiles
