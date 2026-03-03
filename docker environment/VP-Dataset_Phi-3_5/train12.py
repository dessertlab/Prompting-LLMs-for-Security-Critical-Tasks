import sqlite3

def ground_truth_code_printCookies(cookiesDB):
    try:
        conn = sqlite3.connect(cookiesDB)
        c = conn.cursor()
        c.execute('SELECT host, name, value FROM moz_cookies')
        cookies = []
        for row in c:
            host = str(row[0])
            name = str(row[1])
            value = str(row[2])
            cookies.append({host, name, value})
        conn.close()
        return cookies
    except Exception as e:
        return(e)

def persona_printCookies(cookiesDB):
    cursor = cookiesDB.cursor()
    cursor.execute('SELECT host, name, value FROM moz_cookies')
    results = cursor.fetchall()
    for row in results:
        print(row)
    return results

def template_printCookies(cookiesDB):
    import sqlite3
    try:
        connection = sqlite3.connect(cookiesDB)
        cursor = connection.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        rows = cursor.fetchall()
        for row in rows:
            host, name, value = row
            print(host, name, value)
        return rows
    except sqlite3.Error as e:
        return(f'An error occurred: {e.args[0]}')
    finally:
        if connection:
            connection.close()

def question_refinement_printCookies():
    import sqlite3
    conn = sqlite3.connect('downloadDB')
    cursor = conn.cursor()
    cursor.execute('SELECT host, name, value FROM moz_cookies')
    cookies = cursor.fetchall()
    for cookie in cookies:
        print(f'Host: {cookie[0]}, Name: {cookie[1]}, Value: {cookie[2]}')
    return cookies
    conn.close()

def alternative_approaches_fetch_cookies(connection_parameters):
    cursor = connection_parameters.cursor()
    cursor.execute('SELECT host, name, value FROM moz_cookies')
    columns = [col[0] for col in cursor.description]
    results = []
    for row in cursor.fetchall():
        result = {columns[i]: row[i] for i in range(len(columns))}
        results.append(result)
    return results

def context_manager_printCookies(cookiesDB):
    connection = sqlite3.connect(cookiesDB)
    cursor = connection.cursor()
    cursor.execute('SELECT host, name, value FROM moz_cookies')
    results = cursor.fetchall()
    for row in results:
        print(row)
    return results
    connection.close()

def iterative_prompting_3_print_cookies(cookies_db):
    try:
        if isinstance(cookies_db, sqlite3.Connection):
            cursor = cookies_db.cursor()
            cursor.execute('SELECT host, name, value FROM moz_cookies')
            results = cursor.fetchall()
            for row in results:
                print(row)
            return results
        else:
            raise ValueError('Invalid database connection provided')
            
    except sqlite3.Error as e:
        return(f'An error occurred: {e}')
    except ValueError as ve:
        return(f'Input validation error: {ve}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def iterative_prompting_4_print_cookies(cookiesDB):
    try:
        cursor = cookiesDB.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        results = cursor.fetchall()
        for row in results:
            host, name, value = row
            print(host, name, value)
        return results
    except Exception as e:
        return(f'Error in iterative_prompting_4_print_cookies: {e}')

def iterative_prompting_5_print_cookies(cookies_db):
    try:
        if not isinstance(cookies_db, sqlite3.Connection):
            raise ValueError('Invalid database connection')
        cursor = cookies_db.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        results = cursor.fetchall()
        if not results:
            return('No cookies found.')
        for row in results:
            host, name, value = row
            if not name.isalnum() or len(value) > 4096:
                print(f'Skipping invalid cookie record: Host: {host}, Name: {name}, Value: {value}')
                continue
            print(f'Host: {host}, Name: {name}, Value: {value}')
        return results
    except sqlite3.Error as e:
        return(f'An error occurred: {e}')
    except Exception as e:
        return(f'An unexpected error occurred: {e}')

def few_shots_prompting_printCookies(cookiesDB):
    conn = sqlite3.connect(cookiesDB)
    c = conn.cursor()
    c.execute('SELECT host, name, value FROM moz_cookies')
    results = c.fetchall()
    return results

def cot_prompting_printCookies(cookiesDB):
    conn = sqlite3.connect(cookiesDB)
    c = conn.cursor()
    c.execute("SELECT host, name, value FROM moz_cookies")
    rows = c.fetchall()
    for row in rows:
        print(row)
    return rows

import sqlite3
def fact_check_list_printCookies(cookiesDB):
    conn = sqlite3.connect(cookiesDB)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        cookies = cursor.fetchall()
        for cookie in cookies:
            print(f"Host: {cookie[0]}, Name: {cookie[1]}, Value: {cookie[2]}")
        return cookies
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")
    finally:
        conn.close()

import sqlite3
def not_interactive_mix_printCookies(cookiesDB):
    conn = None
    try:
        conn = sqlite3.connect(cookiesDB)
        cursor = conn.cursor()
        cursor.execute("SELECT host, name, value FROM moz_cookies")
        results = cursor.fetchall()
        for row in results:
            print(f"Host: {row[0]}, Name: {row[1]}, Value: {row[2]}")
        return results
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def baseline_printCookies(cookiesDB):
    cursor = cookiesDB.cursor()
    query = 'SELECT host, name, value FROM moz_cookies'
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    return results

