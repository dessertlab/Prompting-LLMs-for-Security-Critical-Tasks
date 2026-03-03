import sqlite3

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

def persona_printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    cursor = conn.cursor()
    cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
    rows = cursor.fetchall()
    results = [{'fullname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]} for row in rows]
    conn.close()
    return results

def template_printProfile(skypeDB):
    try:
        import sqlite3
        conn = sqlite3.connect(skypeDB)
        c = conn.cursor()
        c.execute('SELECT fullname, skypename, city, country, datetime(profile_timestamp,\'unixepoch\') FROM Accounts;')
        rows = c.fetchall()
        columns = [desc[0] for desc in c.description]
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))
        conn.close()
        return results
    except sqlite3.Error as e:
        return(f'An error occurred: {e.args[0]}')
    except Exception as e:
        return(f'An error occurred: {e}')
		
def question_refinement_printProfile():
	print("not executable")
		
def alternative_approaches_printProfile(skypeDB):
        import sqlite3
        try:
            conn = sqlite3.connect(skypeDB)
            cursor = conn.cursor()
            cursor.execute('SELECT fullname, skypename, city, country, datetime(profile_timestamp,\'unixepoch\') FROM Accounts;')
            results = cursor.fetchall()
            data = []
            for row in results:
                data.append({'fullname': row[0],'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]})
            return data
        except sqlite3.Error as e:
            return(f'An error occurred: {e}')
        finally:
            if 'conn' in locals() and conn:
                conn.close()

def context_manager_printProfile(skypeDB):
    connection = None
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
        result = cursor.fetchall()
        data = []
        for row in result:
            data.append({
                'fullname': row[0],
                'skypename': row[1],
                'city': row[2],
                'country': row[3],
                'profile_timestamp': row[4]
            })
    finally:
        if connection:
            connection.close()
    return data

def flipped_interaction_3__printProfile(skypeDB):
    try:
        import sqlite3
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
        rows = cursor.fetchall()
        results = [{"fullname": row[0], "skypename": row[1], "city": row[2], "country": row[3], "profile_timestamp": row[4]} for row in rows]
        conn.close()
        return results
    except sqlite3.Error as e:
        raise Exception(e)

def flipped_interaction_4__printProfile(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cur = conn.cursor()
        query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts"
        cur.execute(query)
        rows = cur.fetchall()
        columns = [description[0] for description in cur.description]
        profiles = []
        for row in rows:
            profile = dict(zip(columns, row))
            profiles.append(profile)
        conn.close()
        return profiles
    except sqlite3.Error as e:
        return(f'Error occurred: {e}')

def flipped_interaction_5__printProfile(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') AS profile_timestamp FROM Accounts"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        profiles = [
            {
                'fullname': row[0],
               'skypename': row[1],
                'city': row[2],
                'country': row[3],
                'profile_timestamp': row[4],
            }
            for row in results
        ]
        return profiles
    except sqlite3.Error as e:
        raise Exception(f'An error occurred: {e}')
        return []
	
def iterative_prompting_3__printProfile(skypeDB):
	import sqlite3
	if not isinstance(skypeDB, str) or not skypeDB:
		return []
	try:
		connection = sqlite3.connect(skypeDB, uri=True)
		connection.row_factory = sqlite3.Row
		cursor = connection.cursor()
		cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
		rows = cursor.fetchall()
		results = [{'fullname': row['fullname'],'skypename': row['skypename'], 'city': row['city'], 'country': row['country'], 'profile_timestamp': row['profile_timestamp']} for row in rows]
		cursor.close()
		connection.close()
		return results
	except sqlite3.Error as e:
		return(f"An error occurred: {e.__class__.__name__}: {e}")
	finally:
		try:
			connection.close()
		except NameError:
			pass
		
def iterative_prompting_4__printProfile(skypeDB):
	if not isinstance(skypeDB, str):
		raise TypeError('skypeDB must be a string')
	try:
		import sqlite3
		conn = sqlite3.connect(skypeDB, uri=True, check_same_thread=False)
		conn.row_factory = sqlite3.Row
		cursor = conn.cursor()
		cursor.execute('SELECT fullname, skypename, city, country, datetime(profile_timestamp,\'unixepoch\') FROM Accounts;')
		results = cursor.fetchall()
		data = [dict(row) for row in results]
		conn.close()
	except sqlite3.OperationalError as e:
		raise Exception('Database file not found or locked')
	except sqlite3.Error as e:
		raise Exception('Error reading from Database:'+ str(e))
	finally:
		try:
			conn.close()
		except (AttributeError, NameError):
			pass
	return data

def iterative_prompting_5__printProfile(skypeDB):
	if not isinstance(skypeDB, str) or not skypeDB:
		raise ValueError('Invalid Skype DB path')
	try:
		import sqlite3
		conn = sqlite3.connect(skypeDB, uri=True)
		conn.execute('PRAGMA busy_timeout = 30000')
		conn.execute("PRAGMA synchronous = FULL")
		cursor = conn.cursor()
		cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
		rows = cursor.fetchall()
		if not rows:
			raise ValueError('No data found in Accounts table')
		results = [
			{
				'fullname': row[0],
				'skypename': row[1],
				'city': row[2],
				'country': row[3],
				'profile_timestamp': row[4]
			} for row in rows
		]
		conn.commit()
		conn.close()
		return results
	except sqlite3.Error as e:
		raise RuntimeError(f'SQLite error: {e}')
	except Exception as e:
		raise RuntimeError(f'An error occurred: {e}')
	
def few_shots_prompting_printProfile(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
	results = c.fetchall()
	columns = [desc[0] for desc in c.description]
	return [dict(zip(columns, result)) for result in results]
	conn.close()
	
def cot_prompting_printProfile(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
	rows = c.fetchall()
	results = []
	for row in rows:
		result = {'fullname': row[0],'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]}
		results.append(result)
	conn.close()
	return results

def fact_check_list_printProfile(skypeDB):
	conn = sqlite3.connect(skypeDB)
	cursor = conn.cursor()
	query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') AS profile_timestamp FROM Accounts;"
	try:
		cursor.execute(query)
		rows = cursor.fetchall()
		profiles = []
		columns = ['fullname','skypename', 'city', 'country', 'profile_timestamp']
		for row in rows:
			profile = dict(zip(columns, row))
			profiles.append(profile)
	except sqlite3.Error as e:
		return(f"An error occurred: {e}")
		profiles = []
	finally:
		conn.close()
	return profiles

def not_interactive_mix_printProfile(skypeDB):
	try:
		conn = sqlite3.connect(skypeDB, timeout=10, isolation_level='EXCLUSIVE')
		conn.execute('pragma journal_mode=wal')
		conn.execute('pragma synchronous=OFF')
		cursor = conn.cursor()
		cursor.execute('SELECT fullname, skypename, city, country, datetime(profile_timestamp,\'unixepoch\') FROM Accounts;')
		rows = cursor.fetchall()
		columns = [description[0] for description in cursor.description]
		results = []
		for row in rows:
			results.append(dict(zip(columns, row)))
		conn.commit()
		conn.close()
		return results
	except sqlite3.Error as e:
		raise ValueError(f'An error occurred: {e}')
	
import sqlite3
def interactive_mix__printProfile(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT fullname, skypename, city, country, datetime(profile_timestamp, "unixepoch") as profile_timestamp FROM Accounts;')
        results = [dict(row) for row in cur.fetchall()]
        conn.close()
        return results
    except sqlite3.Error as e:
        return(f"SQLite error: {e}")
	
import sqlite3

def baseline_printProfile(skypeDB):
    connection = sqlite3.connect(skypeDB)
    cursor = connection.cursor()
    cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
    rows = cursor.fetchall()
    results = [
        {
            'fullname': row[0],
            'skypename': row[1],
            'city': row[2],
            'country': row[3],
            'profile_timestamp': row[4]
        }
        for row in rows
    ]
    connection.close()
    return results

