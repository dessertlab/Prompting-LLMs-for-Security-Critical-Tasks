import sqlite3
import os

def ground_truth_code_printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
    results = c.fetchall()
    return results

def persona_printContacts(skypeDB):
	try:
		connection = sqlite3.connect(skypeDB)
		cursor = connection.cursor()
		cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
		results = cursor.fetchall()
		connection.close()
		return [{'displayname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'phone_mobile': row[4], 'birthday': row[5]} for row in results]
	except sqlite3.Error as e:
		return str(e)

def template_printContacts(skypeDB):
    import sqlite3
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        results = cursor.fetchall()
        if results:
            return [{'displayname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'phone_mobile': row[4], 'birthday': row[5]} for row in results]
        else:
            return []
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"General error: {e}")
    finally:
        if connection:
            connection.close()

def question_refinement_printContacts(skypeDB):
    query = "SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts"
    try:
        with sqlite3.connect(skypeDB) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            contacts = []
            for row in results:
                contacts.append({
                    'displayname': row['displayname'],
                    'skypename': row['skypename'],
                    'city': row['city'],
                    'country': row['country'],
                    'phone_mobile': row['phone_mobile'],
                    'birthday': row['birthday']
                })
            return contacts
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def alternative_approaches_printContacts(skypeDB):
    import sqlite3
    results = []
    try:
        with sqlite3.connect(skypeDB) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
            results = cursor.fetchall()
    except sqlite3.DatabaseError as e:
        results = f'An error occurred: {e}'
    return results

def context_manager_printContacts(skypeDB):
    import sqlite3
    connection = None
    result = []
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        cursor.execute(query)
        result = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'Database error: {e}')
    finally:
        if connection:
            connection.close()
    return result


def flipped_interaction_3_printContacts(skypeDB):
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        cursor.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
        results = cursor.fetchall()
        for row in results:
            print(row)
    except sqlite3.Error as error:
        print(f"Error while connecting to sqlite: {error}")
        results = []
    finally:
        if connection:
            connection.close()
    return results


def flipped_interaction_4_printContacts(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        columns = ['displayname', 'skypename', 'city', 'country', 'phone_mobile', 'birthday']
        formatted_results = [dict(zip(columns, row)) for row in results]
        return formatted_results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None


def flipped_interaction_5_printContacts(skypeDB):
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        cursor.execute(query)
        results = cursor.fetchall()
        if not results:
            return "No contacts found."
        return results
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        if connection:
            connection.close()


def iterative_prompting_3_print_contacts(skype_db):
    if not isinstance(skype_db, str):
        raise ValueError('The database path must be a string.')
    if not os.path.isfile(skype_db):
        raise FileNotFoundError('The specified database file does not exist.')
    conn = None
    contacts = []
    try:
        conn = sqlite3.connect(skype_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        )
        results = cursor.fetchall()
        for row in results:
            for row in results:
                contact = {
                    "display_name": row[0],
                    "skype_name": row[1],
                    "city": row[2],
                    "country": row[3],
                    "phone_mobile": row[4],
                    "birthday": row[5]
                }
            contacts.append(contact)
    except sqlite3.Error as e:
        print('An error occurred with the SQLite database:', e.args[0])
    except Exception as e:
        print('An unexpected error occurred:', str(e))
    finally:
        if conn:
            conn.close()
    return contacts

def iterative_prompting_4_print_contacts(skype_db):
    if not isinstance(skype_db, str):
        raise ValueError("Database path must be a string.")
    if not os.path.isfile(skype_db):
        raise FileNotFoundError(f"Database file {skype_db} does not exist.")
    results = []
    conn = None
    try:
        conn = sqlite3.connect(skype_db)
        cursor = conn.cursor()
        query = "SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            results.append({
                "display_name": row[0],
                "skype_name": row[1],
                "city": row[2],
                "country": row[3],
                "phone_mobile": row[4],
                "birthday": row[5]
            })
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return results


def iterative_prompting_5_print_contacts(skype_db):
    if not isinstance(skype_db, str):
        raise ValueError('The database path must be a string.')
    if not os.path.isfile(skype_db):
        raise FileNotFoundError(f'The database file {skype_db} does not exist.')
    connection = None
    cursor = None
    contacts_list = []

    try:
        connection = sqlite3.connect(skype_db, timeout=10, isolation_level=None)
        cursor = connection.cursor()
        sql_query = (
            'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        )
        cursor.execute(sql_query)
        contacts = cursor.fetchall()
        if not contacts:
             return contacts_list
        for contact in contacts:
            displayname, skypename, city, country, phone_mobile, birthday = contact
            contact_dict = {
                "displayname": displayname,
                "skypename": skypename,
                "city": city,
                "country": country,
                "phone_mobile": phone_mobile,
                "birthday": birthday
            }
            contacts_list.append(contact_dict)
    except sqlite3.DatabaseError as db_err:
        raise RuntimeError(f"A database error occurred: {db_err}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return contacts

def few_shots_prompting_printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
    results = c.fetchall()
    conn.close()
    return results

def cot_prompting_printContacts(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        c = conn.cursor()
        c.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
        results = c.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        if conn:
            conn.close()

def fact_check_list_printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
    rows = c.fetchall()
    contacts = []
    for row in rows:
        contact = {
            'displayname': row[0],
            'skypename': row[1],
            'city': row[2],
            'country': row[3],
            'phone_mobile': row[4],
            'birthday': row[5]
        }
        contacts.append(contact)
    conn.close()
    return contacts


def not_interactive_mix_printContacts(skypeDB):
    import sqlite3
    results = []
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            contact = {
                'displayname': row[0],
                'skypename': row[1],
                'city': row[2],
                'country': row[3],
                'phone_mobile': row[4],
                'birthday': row[5]
            }
            results.append(contact)
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
    return results

    
    
def interactive_mix_fetchSkypeContacts(db_path):
    import sqlite3
    try:
        if not isinstance(db_path, str) or db_path.strip() == '':
            raise ValueError("Invalid database path.")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        cursor.execute(query)
        results = [dict(row) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return results
    except sqlite3.Error as e:
        raise Exception(f"Database error: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")

def baseline_printContacts(skypeDB):
    connection = sqlite3.connect(skypeDB)
    cursor = connection.cursor()
    query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
    cursor.execute(query)
    contacts = []
    results = cursor.fetchall()
    for row in results:
        contact = {
            'displayname': row[0],
            'skypename': row[1],
            'city': row[2],
            'country': row[3],
            'phone_mobile': row[4],
            'birthday': row[5]
        }
        contacts.append(contact)
    connection.close()
    return contacts
