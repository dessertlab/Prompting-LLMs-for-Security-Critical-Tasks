import os
from utils.execute_script_case import *

param = os.getenv("TEST_PARAM", "1")
functions_dir = os.path.join(os.getcwd(), "functions")

output_path = os.path.join(os.getcwd(), "output")
os.makedirs(output_path, exist_ok=True)

#Estrazione degli script
py_files = [os.path.splitext(f)[0] for f in os.listdir(functions_dir)
            if f.endswith('.py') and f != 'anonBrowser.py']				        

#Raccolta dei risultati di tutte le versioni di una funzione
def add_result(aggregated_results, func_name, inputs_str, output):
    if func_name not in aggregated_results:
        aggregated_results[func_name] = {"Inputs": [], "Outputs": []}
    aggregated_results[func_name]["Inputs"].append(inputs_str)
    aggregated_results[func_name]["Outputs"].append(output)
    
def format_list_as_string(lst):
    return "[" + "; ".join(f"({x})" for x in lst) + "]"

for py_file in py_files:
    file_path = os.path.join(functions_dir, f"{py_file}.py")
    i = 0
        
    aggregated_results = {}  
    test_cases = load_test_cases_from_toml(py_file)
    
    for case in test_cases:
        if py_file in ["dev5", "train55","test4"]:
            test_args = create_pkt(py_file, case)
            inputs_str = f"pkt{i+1}"
            i = i + 1
        
        elif isinstance(case, dict):
            test_args = list(case.values())
            inputs_str = ", ".join(str(v) for v in case.values())
        else:
            test_args = [case]
            inputs_str = str(case)
    
        class_name = get_class_name(py_file)
        
        if class_name:      
            results = test_functions_with_class(py_file, file_path, test_args, class_name, case, param)
        else:
            results = test_functions(py_file, file_path, test_args, case, param)
        
        for res in results:
            add_result(aggregated_results, res.get("Function", "Unknown"), inputs_str, res.get("Output", ""))

        
    excel_rows = []
    for func, data in aggregated_results.items():
        formatted_inputs = format_list_as_string(data["Inputs"])
        formatted_outputs = format_list_as_string(data["Outputs"])

        excel_rows.append({
            "Function": func,
            "Inputs": formatted_inputs,
            "Outputs": formatted_outputs,
        })


    #Risultati salvati in un excel
    save_results(excel_rows, py_file, output_path)
