import os
import pandas as pd

def coverage_report(report_dir, output_file):
    import os
    import pandas as pd

    # Lista dei report da analizzare
    report_files = [f for f in os.listdir(report_dir) if f.startswith("report_") and f.endswith(".txt")]

    results = []

    for report_file in report_files:
        full_path = os.path.join(report_dir, report_file)
        with open(full_path, "r") as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            #print("DEBUG LINE:", line)
            if line.startswith("functions/") and "anonBrowser.py" not in line:
                parts = line.split()
                if len(parts) >= 4:
                    full_name = parts[0]
                    #print(f"\n{full_name}\n")
                    script_name = os.path.splitext(os.path.basename(full_name))[0]
                    results.append({
                        "Name": script_name,  
                        "Stmts": int(parts[1]),
                        "Miss": int(parts[2]),
                        "Cover": parts[3]
                    })
                    
    df = pd.DataFrame(results)
    with pd.ExcelWriter(f"{output_file}", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="Coverage", index=False)

    print(f"✅ Copertura filtrata salvata in: {output_file}")

    
for i in range (1,5):
    if i == 1:
        report_dir = "./../docker environment/coverage_GPT-4o"  
        output_file = "VP Dataset GPT-4o.xlsx"
    elif i == 2:
        report_dir = "./../docker environment/coverage_Llama-3_1"  
        output_file = "VP Dataset Llama.xlsx"
    elif i == 3:
        report_dir = "./../docker environment/coverage_Phi-3_5"  
        output_file = "VP Dataset Phi-3_5.xlsx"
    elif i == 4:
        report_dir = "./../docker environment/coverage_Qwen-2_5"  
        output_file = "VP Dataset_Qwen-2_5.xlsx"
        
    coverage_report(report_dir, output_file)
    
    
    
