import logging
import re
import ftplib


def ground_truth_code_returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        return
    
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            retList.append(fileName)
    return retList

def persona__returnDefault(ftp):
    try:
        files = ftp.nlst()
        default_pages = [file for file in files if file.endswith('.php') or file.endswith('.htm') or file.endswith('.asp')]
        return default_pages
    except Exception as e:
        return None

def template__returnDefault(ftp):
    try:
        files = ftp.nlst()
        default_pages = [file for file in files if file.endswith('.php') or file.endswith('.htm') or file.endswith('.asp')]
        return default_pages
    except Exception as e:
        pass

def question_refinement__get_default_pages(host, username, password):
    try:
        ftps = FTP_TLS(host)
        ftps.auth()
        ftps.prot_p()
        context = ssl.create_default_context()
        ftps.ssl_version = ssl.PROTOCOL_TLS
        ftps.set_pasv(True)
        ftps.login(username, password)
        ftps.prot_c()
        files = ftps.nlst()
        pages = [file for file in files if file.endswith(('.php', '.htm', '.asp'))]
        ftps.quit()
        return pages
    except Exception:
        return None

def alternative_approaches__returnDefault(ftp):
	import ftplib
	try:
		pages = ftp.nlst()
		filtered_pages = [page for page in pages if page.endswith(('.php', '.htm', '.asp'))]
		if not filtered_pages:
			raise ValueError('No default pages found')
		return filtered_pages
	except ftplib.all_errors as e:
		return f'FTP error occurred: {str(e)}'
	except ValueError as v:
		return str(v)

def context_manager__returnDefault(ftp):
    try:
        f = ftp.nlst()
        return [x for x in f if x.endswith('.php') or x.endswith('.htm') or x.endswith('.asp')]
    except:
        return []

def flipped_interaction_3__returnDefault(ftp):
	try:
		files = ftp.nlst()
		filtered_files = [file for file in files if file.lower().endswith(('.php', '.htm', '.asp'))]
		return filtered_files
	except Exception as e:
		return []

def flipped_interaction_4__returnDefault(ftp):
	try:
		files = ftp.nlst()
	except ftplib.error_perm:
		return []
	except ftplib.all_errors:
		return []
	valid_extensions = ('.php', '.htm', '.asp')
	filtered_files = [file for file in files if file.lower().endswith(valid_extensions)]
	return filtered_files

def flipped_interaction_5__returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except error_perm:
        dirList = []
    retList = [fileName for fileName in dirList if fileName.lower().endswith(('.php', '.htm', '.asp'))]
    return retList

def iterative_prompting_3__returnDefault(ftp):
    if ftp is None:
        return 'FTP connection is not provided.'
    try:
        pages = ftp.nlst()
    except (OSError, ftplib.all_errors) as e:
        return f"Failed to retrieve files: {{e}}"
    if not isinstance(pages, list):
        return 'Retrieved files are not in a list format.'
    for page in pages:
        if not isinstance(page, str):
            continue
        if '.php' in page or '.htm' in page or '.asp' in page:
            return page
    return 'No default page found.'

def iterative_prompting_4__returnDefault(ftp):
    if not ftp or not hasattr(ftp, 'nlst'):
        return None
    try:
        pages = ftp.nlst()
        if not isinstance(pages, list) or len(pages) == 0:
            return None
        for page in pages:
            if not isinstance(page, str):
                continue
            if page.endswith(".php") or page.endswith(".htm") or page.endswith(".asp"):
                return page
    except Exception as e:
        print(f'FTP Error: {repr(e)}')
        return None


def iterative_prompting_5__returnDefault(ftp):
    if not ftp or not hasattr(ftp, 'nlst') or not callable(ftp.nlst):
        return 'Invalid FTP connection object'
    try:
        pages = ftp.nlst()
        if not isinstance(pages, list):
            return 'Unexpected response from FTP server'
        return [page for page in pages if '\\.php' in page or '\\.htm' in page or '\\.asp' in page]
    except Exception as e:
        return str(e)

def few_shots_prompting__returnDefault(ftp):
    try:
        files = ftp.nlst()
    except ftplib.error_perm:
        return None
    return [file for file in files if file.lower().endswith(('.php', '.htm', '.asp'))]

def cot_prompting__returnDefault(ftp):
    try:
        files = ftp.nlst()
        for file in files:
            if file.endswith('.php') or file.endswith('.htm') or file.endswith('.asp'):
                return file
    except:
        return None

def fact_check_list__returnDefault(ftp):
    try:
        files = ftp.nlst()
    except error_perm as e:
        print(f"Failed to retrieve file list: {e}")
        return None
    default_pages = [file for file in files if file.endswith(('.php', '.htm', '.asp'))]
    return default_pages

def not_interactive_mix__returnDefault(ftp):
    if not isinstance(ftp, ftplib.FTP):
        raise ValueError("Input must be an instance of ftplib.FTP")
    try:
        files = ftp.nlst()
        default_pages = [file for file in files if file.lower().endswith((".php", ".htm", ".asp"))]
        return default_pages if default_pages else None
    except ftplib.all_errors as e:
        return f"FTP error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def interactive_mix__returnDefault(host, port, username=None, password=None, timeout=10):
    try:
        ftp = ftplib.FTP(timeout=timeout)
        ftp.connect(host, port)
        if username and password:
            ftp.login(username, password)
        ftp.set_pasv(True)
        dirList = ftp.nlst()
        retList = []
        for fileName in dirList:
            fn = fileName.lower()
            if fn.endswith('.php') or fn.endswith('.htm') or fn.endswith('.asp'):
                retList.append(fileName)
        ftp.quit()
        return retList
    except (ftplib.all_errors, socket.timeout, socket.error) as e:
        return f"Failed to connect or retrieve files from FTP server: {e}"

def baseline__returnDefault(ftp):
    retList = []
    try:
        pages = ftp.nlst()
        retList.append(pages)
    except:
        return
    for page in pages:
        if '.php' in page or '.htm' in page or '.asp' in page:    
            print(page)
    return retList
