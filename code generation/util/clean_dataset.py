import pandas as pd
import ast
import re

def extract_imports_from_code(code):
    """Estrae tutte le istruzioni di import da una stringa di codice Python."""
    imports = set()
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(f"import {alias.name}")
            elif isinstance(node, ast.ImportFrom):
                module = node.module if node.module else ''
                for alias in node.names:
                    imports.add(f"from {module} import {alias.name}")
    except SyntaxError:
        pass  # Ignora errori di sintassi nel codice
    return imports

def remove_blank_lines_comments_and_example_calls(input_string):
    """Rimuove linee vuote, commenti e chiamate a funzioni definite."""
    if not isinstance(input_string, str):
        return ""
    
    # Divide la stringa in linee
    lines = input_string.split('\n')
    
    # Filtra le linee vuote e i commenti
    non_blank_non_comment_lines = [
        line for line in lines if line.strip() != '' and not line.strip().startswith('#')
    ]
    
    # Unisci le linee in una stringa temporanea per identificare i pattern
    cleaned_string = '\n'.join(non_blank_non_comment_lines)
    
    # Identifica tutte le funzioni definite nella stringa
    function_definitions = re.findall(r'\bdef (\w+)\(', cleaned_string)
    
    # Rimuove le righe che sono chiamate alle funzioni trovate
    final_lines = []
    for line in cleaned_string.split('\n'):
        if not any(line.strip().startswith(func + '(') for func in function_definitions):
            final_lines.append(line)
    
    # Unisci le linee rimanenti in una singola stringa
    result = '\n'.join(final_lines)
    return result

def main():
    # Leggi il file Excel
    file_name = 'C:\\Users\\alber\\OneDrive\\Desktop\\tesi magistrale\\tesi-magistrale-main\\code generation\\util\\Prompt Engineering Code - Dataset (v2).xlsx'  # Modifica con il nome del tuo file se è diverso
    sheet_name = 'VP Functions'
    
    # Carica il file Excel
    df = pd.read_excel(file_name, sheet_name=sheet_name, engine='openpyxl')
    
    # Estrai il codice delle funzioni e applica la funzione di pulizia
    for col in df.columns[3:]:  # A partire dalla colonna D
        for idx, code in df[col].iteritems():
            if idx > 0 and pd.notna(code):  # Ignora la prima riga e celle vuote
                cleaned_code = remove_blank_lines_comments_and_example_calls(code)
                df.at[idx, col] = cleaned_code  # Sovrascrive il contenuto della cella
    
    # Scrivi di nuovo il DataFrame modificato nel foglio Excel
    with pd.ExcelWriter(file_name, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)

if __name__ == "__main__":
    main()
