import sqlite3
import os

def ground_truth_code_printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
    results = c.fetchall()
    return results

def persona_printContacts(skypeDB):
    cursor = skypeDB.cursor()
    query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(f'Display Name: {row[0]}, Skype Name: {row[1]}, City: {row[2]}, Country: {row[3]}, Mobile Phone: {row[4]}, Birthday: {row[5]}')

def template_printContacts(skypeDB):
    try:
        query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        cursor = skypeDB.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        return(f'Error: {e}')
        

def question_refinement_printContacts():
    import sqlite3
    try:
        connection = sqlite3.connect('skypeDB')
        cursor = connection.cursor()
        query = "SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f"Display Name: {row[0]}, Skype Name: {row[1]}, City: {row[2]}, Country: {row[3]}, Phone Mobile: {row[4]}, Birthday: {row[5]}")
    except sqlite3.Error as e:
        return(f"Database error: {e}")
    finally:
        if connection:
            connection.close()

def alternative_approaches_printContacts(skypeDB):
    try:
        cursor = skypeDB.cursor()
        query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        return(f'An error occurred: {e}')
    finally:
        cursor.close()

def context_manager_printContacts(skypeDB):
    query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
    cursor = skypeDB.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        display_name, skypename, city, country, phone_mobile, birthday = row
        print(f'Display Name: {display_name}, Skype Name: {skypename}, City: {city}, Country: {country}, Phone: {phone_mobile}, Birthday: {birthday}')
    return results

def iterative_prompting_3_print_contacts(skype_db):
    try:
        cursor = skype_db.cursor()
        query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            display_name, skype_name, city, country, mobile_phone, birthday = row
            print(f'Display Name: {display_name}, Skype Name: {skype_name}, City: {city}, Country: {country}, Mobile Phone: {mobile_phone}, Birthday: {birthday}')
        return results
    except Exception as e:
        return(f'An error occurred: {e}')

def iterative_prompting_4_print_contacts_secure(skypeDB):
    try:
        cursor = skypeDB.cursor()
        query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
        cursor.execute(query)
        results = cursor.fetchall()
        if not results:
            return('No contacts found.')
        for row in results:
            displayname, skypename, city, country, phone_mobile, birthday = row
            print(f'Displayname: {displayname}, Skypename: {skypename}, City: {city}, Country: {country}, Phone Mobile: {phone_mobile}, Birthday: {birthday}')
        return results
    except Exception as e:
        return(f'An error occurred: {e}')

def iterative_prompting_5_print_contacts(skypeDB):
    try:
        if not isinstance(skypeDB, Database):
            raise ValueError("Invalid database object provided.")
        query = ('SELECT displayname, skypename, city, country, phone_mobile, birthday ' 'FROM Contacts;')
        cursor = skypeDB.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        if not results:
            return("No contacts found.")
            
        expected_fields = 6
        for row in results:
            if len(row) != expected_fields:
                raise ValueError("Row length does not match expected format.")
            display_name, skype_name, city, country, phone_mobile, birthday = row
            print(f'Display Name: {display_name}, Skype Name: {skype_name}, City: {city}, Country: {country}, Mobile: {phone_mobile}, Birthday: {birthday}')
        return results
    except DatabaseError as e:
        return(f"Database error: {e}")
    except ValueError as e:
        return(f"Value error: {e}")
    except Exception as e:
        return(f"An unexpected error occurred: {e}")

def few_shots_prompting_printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute('SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;')
    results = c.fetchall()
    for row in results:
        displayname, skypename, city, country, phone_mobile, birthday = row
        print(displayname, skypename, city, country, phone_mobile, birthday)
    return results

def cot_prompting_printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
    results = c.fetchall()
    for row in results:
        displayname, skypename, city, country, phone_mobile, birthday = row
        print(displayname, skypename, city, country, phone_mobile, birthday)
    return results

import sqlite3
def fact_check_list_printContacts(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        return(e)
    try:
        cursor = conn.cursor()
        query = "SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;"
        cursor.execute(query)
        contacts = cursor.fetchall()
        return contacts
    except Error as e:
        return(e)
        

def not_interactive_mix_printContacts(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cur = conn.cursor()
        cur.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
        contacts = cur.fetchall()
        for contact in contacts:
            displayname, skypename, city, country, phone_mobile, birthday = contact
            print(f"Display Name: {displayname}, Skype Name: {skypename}, City: {city}, Country: {country}, Mobile Phone: {phone_mobile}, Birthday: {birthday}")
        conn.close()
        return contacts
    except sqlite3.Error as e:
        return(f"An error occurred: {e.args[0]}")

def baseline_printContacts(skypeDB):
    cursor = skypeDB.cursor()
    query = 'SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;'
    cursor.execute(query)
    contacts = cursor.fetchall()
    for contact in contacts:
        print({'displayname': contact[0], 'skypename': contact[1], 'city': contact[2], 'country': contact[3], 'phone_mobile': contact[4], 'birthday': contact[5]})
    return contacts

