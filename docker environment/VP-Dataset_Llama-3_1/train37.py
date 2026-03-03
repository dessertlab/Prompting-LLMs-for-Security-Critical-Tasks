from ftplib import FTP, error_perm
import ftplib
import logging

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

def persona_returnDefault(ftp):
    try:
        default_pages = ftp.nlst()
        php_pages   = [page for page in default_pages if '.php' in page.lower()]
        htm_pages   = [page for page in default_pages if '.htm' in page.lower()]
        asp_pages   = [page for page in default_pages if '.asp' in page.lower()]
        return php_pages + htm_pages + asp_pages
    except Exception as e:
        return(f"Failed to retrieve default pages: {str(e)}")
	
def template_returnDefault(ftp):
	try:
		files = ftp.nlst()
		pages = []
		for file in files:
			if '.php' in file or '.htm' in file or '.asp' in file:
				pages.append(file)
		return pages
	except Exception as e:
		return(f'Failed to get default pages: {e}')

	
def question_refinement_returnDefault():
    try:
        from ftplib import FTP
        import re
        ftp = FTP('ftp.dlptest.com')
        ftp.login(user='dlpuser@dlptest.com', passwd='eUj8GEwKvY%5')
        pages = ftp.nlst()
        pages = [page for page in pages if re.search(r'\.(php|htm|asp)$', page)]
        ftp.quit()
        return pages
    except ImportError:
        return ['Error: ftplib or re library missing']
    except Exception as e:
        return [f'Error: {str(e)}']
	
def alternative_approaches_returnDefault(ftp):
    try:
        files = ftp.nlst()
    except Exception as e:
        return('Failed to retrieve the list of files:'+ str(e))
    default_pages = []
    for file in files:
        if file.lower().endswith(('.php', '.htm', '.asp')):
            default_pages.append(file)
    return default_pages

def context_manager_returnDefault(ftp):
    try:
        pages = ftp.nlst()
        defaults = [page for page in pages if page.endswith(('.php', '.htm', '.asp'))]
        return defaults
    except Exception as e:
        return ['Failed', str(e)]

def flipped_interaction_3__returnDefault(ftp):
	try:
		pages = ftp.nlst()
	except Exception as e:
		pages = []
	return [page for page in pages if page.lower().endswith(('.php', '.htm', '.asp'))]

def flipped_interaction_4__returnDefault(ftp):
    try:
        files = ftp.nlst()
        return [file for file in files if file.lower().endswith(('.php', '.htm', '.asp'))]
    except Exception:
        return []
	
def flipped_interaction_5__returnDefault(ftp):
    try:
        files = ftp.nlst()
    except Exception:
        return []
    default_pages = [file for file in files if file.lower().endswith(('php', '.htm', '.asp'))]
    return default_pages

def iterative_prompting_3__returnDefault(ftp):
	if not isinstance(ftp, object):
		raise TypeError('ftp must be an object')
	if not hasattr(ftp, 'nlst'):
		raise AttributeError('ftp must have nlst method')
	try:
		files = ftp.nlst()
		if not isinstance(files, list):
			raise TypeError('ftp.nlst() must return a list')
		default_pages = [file for file in files if isinstance(file, str) and len(file) > 0 and file.lower().endswith(('.php', '.htm', '.asp'))]
		return default_pages
	except Exception as e:
		return(f'An error occurred: {e}')

	
def iterative_prompting_4__returnDefault(ftp):
	if not isinstance(ftp, type(None)) and isinstance(ftp, (ftplib.FTP, ftplib.FTP_TLS)):
		try:
			if hasattr(ftp, 'nlst') and callable(ftp.nlst):
				pages = ftp.nlst()
				if isinstance(pages, list):
					default_pages = [page for page in pages if isinstance(page, str) and (page.lower().endswith('.php') or page.lower().endswith('.htm') or page.lower().endswith('.asp'))]
				if default_pages:
					return default_pages
				else:
					return []
			else:
				return []
		except ftplib.all_errors as e:
			return(f'FTP error occurred: {e}')
		except Exception as e:
			return(f'An error occurred: {e}')
	else:
		return('Input must be an instance of FTP or FTP_TLS')
	
def iterative_prompting_5__returnDefault(ftp):
    if not isinstance(ftp, object): 
        print('Invalid FTP object')
        return
    try:
        if hasattr(ftp, 'sock') and ftp.sock is not None: 
            ftp.sock.settimeout(10.0)
        pages = ftp.nlst()
    except AttributeError: 
        return('Invalid FTP object: nlst() method not found')
    except TimeoutError as e: 
        return(f'FTP connection timed out: {e}')
    except Exception as e: 
        return(f'Failed to get pages: {e} (type: {type(e).__name__})')

    pages = pages if isinstance(pages, list) else []
    for page in pages: 
        if isinstance(page, str) and any(extension in page.casefold() for extension in ['.php', '.html', '.htm', '.asp', '.aspx', '.jsp', '.jspx']):
            print(page)

	
    
def few_shots_prompting_returnDefault(ftp):
    try:
        files = ftp.nlst()
    except Exception as e:
        return(f"Error retrieving files: {e}")
    
    for file in files:
        if '.php' in file.lower() or '.htm' in file.lower() or '.asp' in file.lower():
            return file

   
def cot_prompting__returnDefault(ftp):
	try:
		files = ftp.nlst()
		default_pages = []
		for file in files:
			if ".php" in file.lower() or ".htm" in file.lower() or ".asp" in file.lower():
				default_pages.append(file)
		return default_pages
	except Exception as e:
		return("Failed to retrieve default pages: ", str(e))
      
def fact_check_list_returnDefault(ftp):
	try:
		files = ftp.nlst()
		default_pages = [file for file in files if file.lower().endswith(('.php', '.htm', '.asp'))]
		return default_pages
	except Exception as e:
		return(f"An error occurred: {e}")
      
def not_interactive_mix_returnDefault(ftp):
    try:
        files = ftp.nlst()
        dflt_pages = ['index' + file for file in ['.php', '.htm', '.asp'] if file.lower() in ' '.join(files)]
        default_pages = [file for file in files if file.lower().endswith(('.php', '.htm', '.asp'))]
        return dflt_pages + default_pages
    except Exception as e:
        return 'Failed to retrieve default pages: ' + str(e)

class FTPDefaultPagesException(Exception):
    """Custom exception to handle errors related to default FTP pages."""
    pass
    
def interactive_returnDefault(ftp):
    try:
        pages = ftp.nlst()
        defaultPages = [page for page in pages if any(extension in page.lower() for extension in ['.php', '.htm', '.asp'])]
        return defaultPages
    except Exception as e:
        raise FTPDefaultPagesException(f"Failed to retrieve default pages: {e}")
    
def baseline_returnDefault(ftp):
	try:
		files = ftp.nlst()
	except Exception as e:
		return str(e)
	default_pages = []
	for file in files:
		if '.php' in file or '.htm' in file or '.asp' in file:
			default_pages.append(file)
	return default_pages
