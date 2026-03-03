import ast

def get_function_signature(function_code):
    """
    Estrae la firma di una funzione Python data come stringa.
    
    Args:
    function_code (str): Il codice sorgente della funzione.

    Returns:
    str: La firma della funzione.
    """
    try:
        # Analizza il codice sorgente in un albero di sintassi
        tree = ast.parse(function_code)
        # Trova la definizione della funzione
        function_def = next(node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
        # Ricostruisce la firma della funzione
        function_name = function_def.name
        args = [arg.arg for arg in function_def.args.args]
        signature = f"def {function_name}({', '.join(args)}):"
        return signature
    except Exception as e:
        return str(e)

# Esempio di utilizzo
if __name__ == "__main__":
    function_code = """
def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
"""
    signature = get_function_signature(function_code)
    print(signature)
    print("ciao")
