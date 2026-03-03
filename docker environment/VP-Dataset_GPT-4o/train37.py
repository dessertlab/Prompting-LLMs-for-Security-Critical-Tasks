import logging
import re

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
        pages = ftp.nlst()
    except Exception as e:
        return False
    default_pages = [page for page in pages if any(ext in page for ext in ['.php', '.htm', '.asp'])]
    return default_pages

def template_returnDefault(ftp):
    try:
        pages = ftp.nlst()
        default_pages = []
        for page in pages:
            if re.search(r'\.php|\.htm|\.asp$', page):
                default_pages.append(page)
        return default_pages
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise TypeError(f"Failed to retrieve pages {e}")

def question_refinement_retrieve_default_pages_ftp(ftp_host, ftp_user, ftp_pass):
    try:
        with ftplib.FTP(host=ftp_host) as ftp:
            ftp.login(user=ftp_user, passwd=ftp_pass)
            entries = ftp.nlst()
            pattern = re.compile(r'.*\.(php|htm|asp)$', re.IGNORECASE)
            default_pages = [entry for entry in entries if pattern.match(entry)]
            return default_pages
    except ftplib.all_errors as e:
        return f"FTP error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def alternative_approaches_returnDefault(ftp):
    try:
        pages = ftp.nlst()
        return [page for page in pages if page.endswith(('.php', '.htm', '.asp'))]
    except Exception as e:
        return f"Operation failed: {e}"

def context_manager_returnDefault(ftp):
    try:
        pages = ftp.nlst()
        if not pages:
            return 'Failed to retrieve directory listing'
        return [page for page in pages if any(page.endswith(extension) for extension in ['.php', '.htm', '.asp'])]
    except Exception as e:
        return f'Error: {str(e)}'

def flipped_interaction_3_returnDefault(ftp):
    try:
        pages = ftp.nlst()
    except Exception as e:
        return []
    return [page for page in pages if any(page.endswith(ext) for ext in ['.php', '.htm', '.asp'])]

from ftplib import FTP, error_perm
def flipped_interaction_4_returnDefault(ftp):
    try:
        files = ftp.nlst()
    except error_perm as e:
        print(f"FTP error: {e}")
        return []
    default_pages = []
    for file in files:
        if file.endswith(('.php', '.htm', '.asp')):
            default_pages.append(file)
    return default_pages

from ftplib import FTP, error_perm
def flipped_interaction_5_returnDefault(ftp):
    try:
        filenames = ftp.nlst()
    except error_perm as e:
        print(f"FTP error: {e}")
        return "Failed to get the directory listing."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "An unexpected error occurred."
    matching_pages = []
    for filename in filenames:
        if any(ext in filename for ext in ['.php', '.htm', '.asp']):
            matching_pages.append(filename)
    return matching_pages

def iterative_prompting_3_return_default(ftp):
    if ftp is None:
        raise ValueError("The FTP object can't be None.")
    if not hasattr(ftp, 'nlst'):
        raise TypeError("The input object is not a valid FTP connection.")
    try:
        pages = ftp.nlst()
    except Exception as e:
        return f"Failed to retrieve file list: {str(e)}"
    if not isinstance(pages, list):
        raise TypeError("Expected a list of pages from the FTP server.")
    allowed_extensions = ['.php', '.htm', '.asp']
    default_pages = [
        page for page in pages if any(page.endswith(ext) for ext in allowed_extensions)
    ]
    return default_pages

def iterative_prompting_4_return_default(ftp):
    if not hasattr(ftp, 'nlst'):
        raise ValueError("Provided object is not a valid FTP connection.")
    try:
        files = ftp.nlst()
    except Exception as e:
        return "FAILED: " + str(e)
    if not files or not isinstance(files, list):
        return "FAILED: Cannot retrieve file list, or unexpected response."
    default_pages = [file for file in files if isinstance(file, str) and file.lower().endswith(('.php', '.htm', '.asp'))]
    return default_pages

def iterative_prompting_5_return_default(ftp):
    if ftp is None or not hasattr(ftp, 'nlst'):
        raise ValueError("Invalid FTP connection.")
    try:
        pages = ftp.nlst()
    except Exception as e:
        return f"Failed to get directory listing: {str(e)}"
    if not isinstance(pages, list):
        raise TypeError("Expected a list of page names.")
    default_pages = []
    extensions = ['.php', '.htm', '.asp']
    for page in pages:
        if isinstance(page, str) and any(page.endswith(ext) for ext in extensions):
            default_pages.append(page)
    return default_pages

def few_shots_prompting_returnDefault(ftp):
    try:
        pages = ftp.nlst()
        default_pages = []
        for page in pages:
            if any(ext in page for ext in ['.php', '.htm', '.asp']):
                default_pages.append(page)
        return default_pages
    except Exception as e:
        return None

def cot_prompting_returnDefault(ftp):
    try:
        files = ftp.nlst()
    except Exception as e:
        return f'Failed to retrieve file list: {str(e)}'
    default_pages = []
    for file in files:
        if file.endswith('.php') or file.endswith('.htm') or file.endswith('.asp'):
            default_pages.append(file)
    return default_pages if default_pages else 'No default pages found with specified extensions.'

def fact_check_list_returnDefault(ftp):
    from ftplib import error_perm
    try:
        file_list = ftp.nlst()
    except error_perm as e:
        print(f"FTP error: {e}")
        return None
    possible_default_pages = []
    for file in file_list:
        if file.endswith(('.php', '.htm', '.asp')):
            possible_default_pages.append(file)
    return possible_default_pages

def not_interactive_mix_returnDefault(ftp):
    import ftplib
    import re
    try:
        pages = ftp.nlst()
    except ftplib.error_perm as e:
        return f"Failed to list files: {e}"
    except ftplib.all_errors as e:
        return f"FTP error occurred: {e}"
    default_pages = []
    for page in pages:
        if re.search(r'\.(php|htm|asp)$', page, re.IGNORECASE):
            default_pages.append(page)
    return default_pages

def interactive_mix_get_default_pages(hostname, username, password):
    try:
        if not (isinstance(hostname, str) and isinstance(username, str) and isinstance(password, str)):
            raise ValueError("Hostname, username, and password must be strings.")
        ftp = FTP(hostname)
        ftp.login(user=username, passwd=password)
        files = ftp.nlst()
        eligible_files = [file for file in files if file.endswith(('.php', '.htm', '.asp'))]
        ftp.quit()
        return eligible_files
    except Exception as e:
        return None

def baseline_returnDefault(ftp):
    try:
        pages = ftp.nlst()
        default_pages = [page for page in pages if page.endswith(('.php', '.htm', '.asp'))]
        return default_pages
    except Exception as e:
        return f'Failed to retrieve pages: {e}'

