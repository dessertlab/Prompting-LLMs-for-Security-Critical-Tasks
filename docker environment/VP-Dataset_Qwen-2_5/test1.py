import sqlite3
import os

def ground_truth_code_printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
    results = c.fetchall()
    return results

def persona__printContacts(skypeDB):
	import sqlite3
	import json
	conn = sqlite3.connect(skypeDB)
	cursor = conn.cursor()
	try:
		cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
		results = cursor.fetchall()
		contacts = [{'displayname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'phone_mobile': row[4], 'birthday': row[5]} for row in results]
		return json.dumps(contacts)
	except sqlite3.Error as e:
		return json.dumps({'error': str(e)})
	finally:
		if conn:
			conn.close()

def template__printContacts(skypeDB):
    import sqlite3
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        results = cursor.fetchall()
        return results
    finally:
        conn.close()

def question_refinement__fetch_contacts():
    import sqlite3
    conn = None
    try:
        conn = sqlite3.connect('skypeDB')
        cursor = conn.cursor()
        query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        if conn:
            conn.close()
        return str(e)

def alternative_approaches__printContacts(skypeDB):
    import sqlite3
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f'Database error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')
    finally:
        if conn:
            conn.close()
    return rows

def context_manager__printContacts(skypeDB):
    connection = sqlite3.connect(skypeDB)
    cursor = connection.cursor()
    query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

def flipped_interaction_3__printContacts(skypeDB):
	import sqlite3
	conn = sqlite3.connect(skypeDB)
	cursor = conn.cursor()
	cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
	results = cursor.fetchall()
	conn.close()
	return results

def flipped_interaction_4__printContacts(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def flipped_interaction_5__printContacts(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        results = cursor.fetchall()
        columns = ['displayname', 'skypename', 'city', 'country', 'phone_mobile', 'birthday']
        contacts_list = [dict(zip(columns, row)) for row in results]
        return contacts_list
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def iterative_prompting_3__printContacts(skypeDB):
	if not isinstance(skypeDB, str) or not skypeDB.strip():
		raise ValueError('Invalid database path provided.')
	try:
		conn = sqlite3.connect(skypeDB)
		cursor = conn.cursor()
		cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
		results = cursor.fetchall()
	except sqlite3.Error as e:
		raise Exception(f'Database error: {e}')
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()
	return results

def iterative_prompting_4__printContacts(skypeDB):
    if not skypeDB:
        raise ValueError('Database connection object is not provided.')
    try:
        cursor = skypeDB.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        results = cursor.fetchall()
    except Exception as e:
        raise RuntimeError(f'Error executing query: {str(e)}')
    finally:
        if cursor:
            cursor.close()
    if results:
        for result in results:
            print(result)

def iterative_prompting_5__printContacts(skypeDB):
	if not isinstance(skypeDB, str):
		raise ValueError('Database path must be a string')
	if not os.path.isfile(skypeDB):
		raise FileNotFoundError(f'Database file not found at {{skypeDB}}')
	conn = None
	cursor = None
	try:
		conn = sqlite3.connect(skypeDB, uri=True)
		cursor = conn.cursor()
		query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
		cursor.execute(query)
		results = cursor.fetchall()
	except sqlite3.Error as e:
		raise RuntimeError(f'Database error: {{e}}')
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()
	return results

def few_shots_prompting__printContacts(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
	results = c.fetchall()
	conn.close()
	return results

def cot_prompting__printContacts(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
	results = c.fetchall()
	for row in results:
		print(row)
	conn.close()
	return row

def fact_check_list__printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        contacts = cursor.fetchall()
        for contact in contacts:
            displayname, skypename, city, country, phone_mobile, birthday = contact
            print(f'Display Name: {displayname}, Skype Name: {skypename}, City: {city}, Country: {country}, Mobile Phone: {phone_mobile}, Birthday: {birthday}')
    finally:
        conn.close()
    return contacts

def not_interactive_mix__printContacts(skypeDB):
    if not isinstance(skypeDB, str):
        raise ValueError('Database path must be a string')
    import sqlite3
    conn = None
    cursor = None
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def interactive_mix__fetch_skype_contacts(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except sqlite3.Error as e:
        logging.error(f'Database error: {e}')
        return []
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return []

def baseline__printContacts(skypeDB):
	cursor = skypeDB.cursor()
	cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
	results = cursor.fetchall()
	return [{'displayname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'phone_mobile': row[4], 'birthday': row[5]} for row in results]
