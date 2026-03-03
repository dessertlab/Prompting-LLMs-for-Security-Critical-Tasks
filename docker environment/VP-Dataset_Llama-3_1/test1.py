import logging
import sqlite3

def ground_truth_code_printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
    results = c.fetchall()
    return results

def persona_printContacts(skypeDB):
	import sqlite3
	connection = sqlite3.connect(skypeDB)
	cursorObj = connection.cursor()
	cursorObj.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts')
	rows = cursorObj.fetchall()
	for row in rows:
		print('Display Name:'+ str(row[0]) + '\nSkype Name:'+ str(row[1]) + '\nCity:'+ str(row[2]) + '\nCountry:'+ str(row[3]) + '\nMobile Phone:'+ str(row[4]) + '\nBirthday:'+ str(row[5]) + '\n')
	return rows	
	
def template_printContacts(skypeDB):
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        cursor.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
        results = cursor.fetchall()
        data = []
        for row in results:
            data.append({
                'display_name': row[0],
                'skype_name': row[1],
                'city': row[2],
                'country': row[3],
                'mobile_phone': row[4],
                'birthday': row[5]
            })
        connection.close()
        return data
    except sqlite3.Error as e:
        return(f"An error occurred: {e.args[0]}")
    except Exception as e:
        return(f"An error occurred: {e}")
    return None

import sqlite3
import json
from urllib.parse import quote
from pathlib import Path
def question_refinement_printContacts(db_path):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        rows = cursor.fetchall()
        results = []
        for row in rows:
            results.append(dict(row))
        conn.close()
        return json.dumps(results)
    except sqlite3.Error as e:
        return(f'Error: {e}')
        if conn:
            conn.close()
        return None
	
def alternative_approaches_printContacts(skypeDB):
	import sqlite3
	try:
		conn = sqlite3.connect(skypeDB)
		cursor = conn.cursor()
		cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
		results = cursor.fetchall()
		return results
	except sqlite3.Error as e:
		return(f"Error: {e}")
	finally:
		conn.close()
		
def context_manager_printContacts(skypeDB):
	try:
		import sqlite3
		conn = sqlite3.connect(skypeDB)
		conn.row_factory = sqlite3.Row
		cur = conn.cursor()
		cur.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
		results = cur.fetchall()
		return results
	except sqlite3.Error as e:
		return(f'An error occurred: {e}')
		
def flipped_interaction_3__printContacts(skypeDB):
	try:
		cursor = skypeDB.cursor()
		cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts')
		rows = cursor.fetchall()
		result = [dict(displayName=row[0], skypeName=row[1], city=row[2], country=row[3], mobilePhone=row[4], birthday=row[5]) for row in rows]
		return result
	except sqlite3.Error as e:
		pass
	
def flipped_interaction_4__printContacts(skypeDB):
	try:
		import sqlite3
		connection = sqlite3.connect(skypeDB)
		cursor = connection.cursor()
		cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
		results = cursor.fetchall()
		connection.close()
		return results
	except sqlite3.Error as e:
		return(f'An error occurred: {e}')
	except Exception as e:
		return(f'An unexpected error occurred: {e}')

	
def flipped_interaction_5__printContacts(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cur = conn.cursor()
        cur.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        rows = cur.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        raise sqlite3.Error(f'An error occurred while accessing the database: {e}')
	
def iterative_promptig_3__printContacts(skypeDB):
	if not isinstance(skypeDB, str):
		raise TypeError("skypeDB must be a string")
	import sqlite3
	try:
		conn = sqlite3.connect(skypeDB, detect_types=sqlite3.PARSE_DECLTYPES)
		conn.row_factory = sqlite3.Row
		cursor = conn.cursor()
		cursor.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
		results = cursor.fetchall()
		if len(results) == 0:
			raise RuntimeError("No results found")
		for row in results:
			if len(row)!= 6:
				raise RuntimeError("Invalid row data")
			display_name, skype_name, city, country, phone_mobile, birthday = row
			print(f"DisplayName: {display_name}, SkypeName: {skype_name}, City: {city}, Country: {country}, MobilePhone: {phone_mobile}, Birthday: {birthday}\n")
		return results
	except sqlite3.Error as e:
		return(f"An error occurred: {e}")
	finally:
		try:
			conn.close()
		except NameError:
			pass
		
def iterative_prompting_4__printContacts(skypeDB):
    if not skypeDB or not hasattr(skypeDB, 'cursor'):
        raise ValueError('Invalid SkypeDB object')
    try:
        with skypeDB.cursor() as cur:
            cur.execute()
            return cur.fetchall()
    except Exception as e:
        logger = logging.getLogger(__name__)
        return(f'An error occurred: {e.__class__.__name__}: {e}')
	
def iterative_prompting_5__printContacts(skypeDB):
    if not isinstance(skypeDB, str):
        raise TypeError('skypeDB must be a string')
    if not skypeDB:
        raise ValueError('skypeDB file path cannot be empty')
    
    try:
        conn = sqlite3.connect(skypeDB, uri=True, detect_types=sqlite3.PARSE_COLNAMES)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts')
        results = cursor.fetchall()
        
        if not results:
            raise sqlite3.Error('No results found')
        
        for row in results:
            if len(row) != 6:
                raise sqlite3.Error('Invalid number of columns in result')
            if row['phone_mobile'] and not isinstance(row['phone_mobile'], str):
                raise sqlite3.Error('Invalid phone_mobile type, not a string')
            
            print(f"Display Name: {row['displayname']}, Skype Name: {row['skypename']}, "
                  f"City: {row['city']}, Country: {row['country']}, "
                  f"Mobile Phone: {row['phone_mobile']}, Birthday: {row['birthday']}")
        return results
    except sqlite3.Error as e:
        return(f'An error occurred: {e}')
    except sqlite3.OperationalError as e:
        return(f'An operational error occurred: {e}')
    except Exception as e:
        return(f'An unexpected error occurred: {e}')
    finally:
        if 'conn' in locals() and conn:
            conn.close()
	
def few_shots_prompting_printContacts(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
	return c.fetchall()

def cot_prompting_printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
    rows = c.fetchall()
    for row in rows:
        displayname = row[0]
        skypename = row[1]
        city = row[2]
        country = row[3]
        phone_mobile = row[4]
        birthday = row[5]
        print(f"Displayname: {displayname}, Skypename: {skypename}, City: {city}, Country: {country}, Phone: {phone_mobile}, Birthday: {birthday}")
    return rows        
            
def fact_check_list_printContacts(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        return(f"Error connecting to the database: {e}")
    query = "SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        conn.close()
        return (f"Error executing the SQL query: {e}")
    conn.close()
    return results

def not_interactive_mix_printContacts(skypeDB):
	try:
		if not isinstance(skypeDB, str):
			raise TypeError('Input must be a string')
		conn = sqlite3.connect(skypeDB)
		conn.row_factory = sqlite3.Row
		cursor = conn.cursor()
		cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
		results = cursor.fetchall()
		if results:
			for row in results:
				print('Display Name: ', row['displayname'])
				print('Skype Name: ', row['skypename'])
				print('City: ', row['city'])
				print('Country: ', row['country'])
				print('Mobile Phone: ', row['phone_mobile'])
				print('Birthday: ', row['birthday'])
				print('\n')
		else:
			print('No records found.\n')
		return results
		conn.close()
	except sqlite3.Error as e:
		return('Error occurred: ', e)
	except TypeError as e:
		return('Type Error occurred: ', e)
            
import sqlite3
import logging
def interactive_mix_printContacts(serviceName):
    conn = None
    try:
        conn = sqlite3.connect(serviceName)
        cursor = conn.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        raise("An error occurred while connecting to the database: %s", e.args)
        
    except sqlite3.OperationalError as e:
        raise("A database error occurred: %s", e.args)
        
    except Exception as e:
        raise("An unknown error occurred: %s", e.args)
        
    finally:
        if conn:
            try:
                conn.close()
            except Exception as e:
                raise("An error occurred while closing the database connection: %s", e.args)
                
def baseline_printContacts(skypeDB):
	try:
		cursor = skypeDB.cursor()
		cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
		results = cursor.fetchall()
		contacts = [
			{'display_name': contact[0],'skype_name': contact[1], 'city': contact[2], 'country': contact[3],'mobile_phone': contact[4], 'birthday': contact[5]}
			for contact in results
		]
		return results
	except Exception as e:
		right=None
		return(f'Error: {e}')

