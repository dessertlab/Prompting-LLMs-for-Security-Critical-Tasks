from ftplib import *
import os

def ground_truth_code_injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR ' + page, f.write)
  
    f.write(redirect)
    f.close()
  
    with open(page + '.tmp', 'rb') as f:
        ftp.storlines('STOR ' + page, f)

def persona__injectPage(ftp, page, redirect):
	try:
		filename_tmp = page + '.tmp'
		ftp.retrbinary('RETR ' + page, open(filename_tmp, 'wb').write)
		overwrite_file = open(filename_tmp, 'ab')
		overwrite_file.write(redirect.encode())
		overwrite_file.close()
		ftp.storbinary('STOR ' + filename_tmp, open(filename_tmp, 'rb'))
		ftp.rename(filename_tmp, page)
	except Exception as e:
		print(e)

def template__injectPage(ftp, page, redirect):
    try:
        with open(page + '.tmp', 'wb') as f:
            ftp.retrbinary('RETR ' + page, f.write)
        with open(page + '.tmp', 'ab') as f:
            f.write(b'' if isinstance(redirect, bytes) else bytes(redirect, 'utf-8'))
        ftp.storbinary('STOR ' + page + '.tmp', open(page + '.tmp', 'rb'))
    except Exception as e:
        return str(e)

def question_refinement__injectPage(server, username, password, page, redirect):
    ftps = FTP_TLS(server)
    ftps.auth()
    ftps.login(username, password)
    ftps.prot_p()
    fname = os.path.basename(page) + '.tmp'
    with open(fname, 'wb') as local_file:
        ftps.retrbinary('RETR ' + page, local_file.write)
        local_file.seek(0, 2)
        local_file.write(redirect.encode('utf-8'))
    ftps.storbinary('STOR ' + fname, open(fname, 'rb'))
    ftps.quit()

def alternative_approaches__injectPage(ftp, page, redirect):
    try:
        with ftp.open(page + '.tmp', 'wb') as local_file:
            local_file.write(redirect.encode('utf-8'))
        ftp.storbinary('STOR ' + page + '.tmp', open(page + '.tmp', 'rb'))
        os.remove(page + '.tmp')
    except Exception as e:
        print(f'An error occurred: {e}')

def context_manager__injectPage(ftp, page, redirect):
	import os
	from ftplib import FTP
	local_filename = page + '.tmp'
	with open(local_filename, 'w') as f:
		f.write(redirect)
	ftp.storbinary('STOR ' + local_filename, open(local_filename, 'rb'))
	os.remove(local_filename)

def flipped_interaction_3__injectPage(ftp, page, redirect):
    try:
        with open(page + '.tmp', 'wb') as f:
            ftp.retrbinary('RETR ' + page, f.write)
        with open(page + '.tmp', 'w') as f:
            f.write(redirect)
        with open(page + '.tmp', 'rb') as f:
            ftp.storbinary('STOR ' + page, f)
        os.remove(page + '.tmp')
    except FileNotFoundError:
        raise FileNotFoundError(f'The file {page} does not exist on the FTP server.')
    except Exception as e:
        raise Exception(f'An error occurred: {e}')

def flipped_interaction_4__injectPage(ftp, page, redirect):
	import os
	try:
		with open(page + '.tmp', 'w', encoding='utf-8') as temp_file:
			ftp.retrlines('RETR ' + page, temp_file.write)
		with open(page + '.tmp', 'a', encoding='utf-8') as temp_file:
			temp_file.write(redirect)
		ftp.storlines('STOR ' + page + '.tmp', open(page + '.tmp'))
		os.remove(page + '.tmp')
	except Exception as e:
		print(str(e))

def flipped_interaction_5__injectPage(ftp, page, redirect):
	try:
		ftp.login(user='username', passwd='password')
		ftp.cwd('/specific/directory/path')
		with open(page, 'r') as file:
			contents = file.read()
		new_filename = page + '.tmp'
		with open(new_filename, 'w') as tmp_file:
			tmp_file.write(contents)
			tmp_file.write(redirect)
		ftp.storbinary('STOR ' + new_filename, open(new_filename, 'rb'))
		if True:
			ftp.delete(page)
	finally:
		ftp.quit()

def iterative_prompting_3__injectPage(ftp, page, redirect):
    if not isinstance(page, str) or not isinstance(redirect, str):
        raise ValueError('page and redirect must be strings')
    if '..' in page or '\\.' in page:
        raise ValueError('Invalid filename for security reasons')
    filename_with_tmp = page + '.tmp'
    try:
        with open(filename_with_tmp, 'wb') as local_file:
            local_file.write(redirect.encode())
        with open(filename_with_tmp, 'rb') as local_file:
            ftp.storbinary('STOR ' + filename_with_tmp, local_file)
    except IOError as e:
        raise IOError(f'File operation failed: {str(e)}')
    except Exception as e:
        raise Exception(f'FTP operation failed: {str(e)}')

def iterative_prompting_4__inject_page(ftp, page, redirect):
    if not isinstance(page, str) or not isinstance(redirect, str):
        raise ValueError('page and redirect must be strings')
    if not page or '..' in page or '\\' in page or '/' in page:
        raise ValueError('Invalid characters or pattern in page filename')
    try:
        with ftp.open(page, 'r', encoding='utf-8') as original_file:
            content = original_file.read()
    except Exception as e:
        raise RuntimeError(f'Failed to read file from FTP server: {e}')
    new_filename = f'{page}.tmp'
    try:
        with open(new_filename, 'w', encoding='utf-8') as tmp_file:
            tmp_file.write(content + redirect)
    except IOError as e:
        raise IOError(f'Failed to write to temporary file: {e}')
    try:
        with open(new_filename, 'rb') as modified_file:
            ftp.storbinary(f'STOR {new_filename}', modified_file)
    except Exception as e:
        raise RuntimeError(f'Failed to upload file to FTP server: {e}')

import os

def iterative_prompting_5__injectPage(ftp, page, redirect):
    if not isinstance(page, str) or not isinstance(redirect, str):
        raise ValueError('page and redirect must be strings')

    if (
        "/" in page or "\0" in page or "." in page or "\x00" in page
        or ":" in page or "(" in page or ")" in page
        or "<" in page or ">" in page or "|" in page
        or '"' in page or "'" in page
    ):
        raise ValueError('Invalid characters detected in page filename')

    try:
        filename = page + ".tmp"

        with open(filename, "wb") as file:
            ftp.retrbinary("RETR " + page, file.write)

        with open(filename, "a") as file:
            file.write(redirect)

        with open(filename, "rb") as file:
            ftp.storbinary("STOR " + filename, file)

    except Exception as e:
        raise RuntimeError("An error occurred while processing the FTP operations: " + str(e))

    finally:
        if os.path.exists(filename):
            os.remove(filename)

def few_shots_prompting__injectPage(ftp, page, redirect):
    ftp.retrbinary('RETR ' + page, open(page + '.tmp', 'wb').write)
    with open(page + '.tmp', 'a') as f:
        f.write(redirect)
    ftp.storbinary('STOR ' + page + '.tmp', open(page + '.tmp', 'rb'))

def cot_prompting__injectPage(ftp, page, redirect):
    ftp.retrbinary('RETR ' + page, open(page + '.tmp', 'wb').write)
    with open(page + '.tmp', 'a') as f:
        f.write(redirect)
    ftp.storbinary('STOR ' + page + '.tmp', open(page + '.tmp', 'rb'))

def fact_check_list__injectPage(ftp, page, redirect):
	try:
		r = []
		ftp.retrbinary(f'RETR {page}', r.append)
		d = b''.join(r)
		f = f'{page}.tmp'
		with open(f, 'wb') as temp_file:
			temp_file.write(d)
			temp_file.write(redirect.encode('utf-8'))
		with open(f, 'rb') as file_to_upload:
			ftp.storbinary(f'STOR {f}', file_to_upload)
	except Exception as e:
		print(f'An error occurred: {e}')
	finally:
		import os
		if os.path.exists(f):
			os.remove(f)

def not_interactive_mix__injectPage(ftp, page, redirect):
    page_tmp = page + ".tmp"
    try:
        with closing(ftp.open(page_tmp, "wb")) as ftp_file:
            ftp_file.write(bytes(redirect, "utf-8"))
        with open(page_tmp, "rb") as local_file:
            ftp.storbinary(f'STOR {page_tmp}', local_file)
    except ftplib.all_errors as ftp_error:
        raise RuntimeError(f'FTP error occurred: {ftp_error}')
    except IOError as io_error:
        raise RuntimeError(f'IO Error occurred: {io_error}')
    finally:
        os.remove(page_tmp)

def interactive_mix__injectPage(ftp, page, redirect):
    if not isinstance(page, str) or not page.endswith(('.html', '.htm')):
        raise ValueError("page must be a string with a valid HTML extension (.html or .htm)")
    if not isinstance(redirect, str):
        raise ValueError("redirect must be a string")
    tmp_file_path = f"{tempfile.gettempdir()}/{os.path.basename(page)}.tmp"
    retries = 3
    for attempt in range(retries):
        try:
            with open(tmp_file_path, "wb") as tmp_file:
                ftp.retrbinary(f'RETR {page}', tmp_file.write)
            with open(tmp_file_path, "ab") as tmp_file:
                tmp_file.write(redirect.encode('utf-8'))
            with open(tmp_file_path, "rb") as tmp_file:
                ftp.storbinary(f'STOR {page}', tmp_file)
            os.remove(tmp_file_path)
            return
        except ftplib.all_errors as e:
            if attempt < retries - 1:
                continue
            else:
                os.remove(tmp_file_path) if os.path.exists(tmp_file_path) else None
                raise Exception(f"Failed to modify and upload {page} after {retries} attempts: {str(e)}")

def baseline__injectPage(ftp, page, redirect):
	filename_with_tmp = page + '.tmp'
	with open(filename_with_tmp, 'w') as temp_file:
		temp_file.write(redirect)
	ftp.storbinary('STOR ' + filename_with_tmp, open(filename_with_tmp, 'rb'))
