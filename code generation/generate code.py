import os
from dotenv import load_dotenv
import subprocess
import openpyxl

# Carica le variabili d'ambiente dal file .env
load_dotenv()

def run_scripts_in_folder(folder_path):
    # Ottiene tutti i file nella cartella specificata
    for filename in os.listdir(folder_path):
        # Controlla se il file ha estensione .py
        if filename.endswith(".py"):
            # Costruisce il percorso completo del file
            file_path = os.path.join(folder_path, filename)
            # Stampa prima di eseguire lo script
            print(f"\nESEGUO SCRIPT {filename}...\n")
            try:
                # Esegue il file usando il modulo subprocess
                result = subprocess.run(["python3", file_path], capture_output=True, text=True)
                print(f"SCRIPT {filename} ESEGUITO CON SUCCESSO")
                
                if result.stdout:
                    print(f"Output di {filename}:\n{result.stdout}")
                # Stampa gli errori, se ce ne sono
                if result.stderr:
                    print(f"Errori in {filename}:\n{result.stderr}")
            except Exception as e:
                print(f"Errore nell'esecuzione di {filename}: {e}")


def check_excel_for_empty_cells(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    
    # Controlla le colonne dalla D in poi, esclusa la prima riga
    for row in sheet.iter_rows(min_row=2, min_col=4, values_only=True):
        for cell in row:
            if cell is None:
                return True
    return False

if __name__ == "__main__":
    # Definisce il percorso della cartella "patterns"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    patterns_folder = os.path.join(current_directory, "patterns_4o")
    
    # Percorso del file Excel
    excel_file = "VP Code - Dataset.xlsx"
    
    # Nome del foglio da controllare
    sheet_name = "VP Functions"

    iteration = 0
    # Continua a eseguire finché ci sono celle vuote
    while check_excel_for_empty_cells(excel_file, sheet_name):
        iteration += 1
        print(f"\n--- Iterazione {iteration} ---\n")
        run_scripts_in_folder(patterns_folder)
    
    print("Tutte le celle sono popolate. Esecuzione terminata.")
