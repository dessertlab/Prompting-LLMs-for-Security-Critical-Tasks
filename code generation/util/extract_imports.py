import pandas as pd
import ast

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

def main():
    # Leggi il file Excel
    file_path = 'C:\\Users\\alber\\OneDrive\\Desktop\\tesi magistrale\\tesi-magistrale-main\\code generation\\util\\Prompt Engineering Code - Dataset (v2).xlsx'  # Modifica con il percorso del tuo file
    sheet_name = 'VP Functions'
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

    # Estrai il codice delle funzioni
    codes = []
    for col in df.columns[3:]:  # A partire dalla colonna D
        for code in df[col][1:]:  # A partire dalla seconda riga
            if pd.notna(code):
                codes.append(code)
    
    # Estrai tutte le istruzioni di import
    all_imports = set()
    for code in codes:
        all_imports.update(extract_imports_from_code(code))
    
    # Stampa le istruzioni di import uniche
    for imp in sorted(all_imports):
        print(imp)

if __name__ == "__main__":
    main()