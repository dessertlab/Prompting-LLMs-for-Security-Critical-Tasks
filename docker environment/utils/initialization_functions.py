import os
import shutil

def clean_all():
    # Cartelle che iniziano con questi prefissi
    prefix_targets = ("coverage", "output")
    
    # Cartelle specifiche da eliminare/ricreare
    explicit_targets = ["known_hosts", os.path.join("resources", "data")]
    
    all_entries = os.listdir(".")
    matched_dirs = [
        d for d in all_entries
        if os.path.isdir(d) and d.startswith(prefix_targets)
    ]
    
    matched_dirs.extend(explicit_targets)

    for dir_path in matched_dirs:
        if os.path.exists(dir_path):
            try:
                shutil.rmtree(dir_path)
                print(f"[✓] Eliminata la cartella: {dir_path}")
            except Exception as e:
                print(f"[!] Errore nell'eliminazione di {dir_path}: {e}")
        else:
            print(f"[i] Cartella non trovata: {dir_path}")
        
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"[✓] Creata la cartella vuota: {dir_path}")
        except Exception as e:
            print(f"[!] Errore nella creazione di {dir_path}: {e}")
