import re

def detailed_comparison(data1, data2):
    # Controllo se i due tipi di dati sono uguali
    if type(data1) == type(data2):
        if isinstance(data1, (list, tuple)):
            # Se sono liste o tuple, confronto gli elementi considerando l'ordine
            if len(data1) != len(data2):
                return False
            for i in range(len(data1)):
                if not detailed_comparison(data1[i], data2[i]):
                    return False
            return True
        
        elif isinstance(data1, dict):
            # Se sono dizionari, confronto le chiavi e i valori senza considerare l'ordine delle chiavi
            if set(data1.keys()) != set(data2.keys()):
                return False
            for key in data1.keys():
                if not detailed_comparison(data1[key], data2[key]):
                    return False
            return True
        
        elif isinstance(data1, set):
            # Se sono insiemi, confronto gli elementi senza considerare l'ordine
            return set(data1) == set(data2)
        
        # Se sono altri tipi di dati confrontabili, uso l'operatore di confronto ==
        return data1 == data2
    
    # Se i tipi di dati sono diversi ma confrontabili come valori
    if isinstance(data1, (list, tuple)) and isinstance(data2, (list, tuple)):
        return set(data1) == set(data2)
    
    if isinstance(data1, (list, tuple)) and isinstance(data2, set):
        return set(data1) == data2
    
    if isinstance(data2, (list, tuple)) and isinstance(data1, set):
        return data1 == set(data2)
    
    if isinstance(data1, dict) and isinstance(data2, (list, tuple)):
        return set(data1.values()) == set(data2)

    if isinstance(data2, dict) and isinstance(data1, (list, tuple)):
        return set(data2.values()) == set(data1)
    
    return False



def compare_function_outputs(func1_result, func2_result):
    if func1_result is None and func2_result is None:
        return True
    if type(func1_result) == type(func2_result):
        if isinstance(func1_result, (list, tuple, dict, set)):
            return detailed_comparison(func1_result, func2_result)
        else:
            return func1_result == func2_result
    return detailed_comparison(func1_result, func2_result)


# Funzione per estrarre il nome della funzione da una stringa
def extract_function_name(function_string):
    match = re.search(r'def\s+(\w+)\s*\(', function_string)
    if match:
        return match.group(1)
    return None

def test_functions(func1, func2, *args, **kwargs):
    result1 = func1(*args, **kwargs)
    result2 = func2(*args, **kwargs)
    
    if compare_function_outputs(result1, result2):
        print(f"I risultati delle due funzioni {func1.__name__} e {func2.__name__} sono identici.")
    else:
        print(f"I risultati delle due funzioni {func1.__name__} e {func2.__name__} sono diversi.")


# Definizione delle funzioni come stringhe
function1 = """
def function1_list():
    return [1, 2, 3, 4]
"""

function2 = """
def function2_list():
    return [1, 2, 3, 4]
"""

# Estrai il nome delle funzioni
func1_name = extract_function_name(function1)
func2_name = extract_function_name(function2)

# Esegui il codice delle stringhe per definire le funzi   oni
exec(function1)
exec(function2)

# Ottieni le funzioni definite dinamicamente
func1 = locals()[func1_name]
func2 = locals()[func2_name]

# Esegui il test sulle funzioni estratte
test_functions(func1, func2)

# Esempi di funzioni con parametri definite come stringhe
function1_with_params = """
def function1_with_params(a, b):
    return a + b
"""

function2_with_params = """
def function2_with_params(a, b):
    return a + b
"""

# Estrai il nome delle funzioni
func3_name = extract_function_name(function1_with_params)
func4_name = extract_function_name(function2_with_params)

# Esegui il codice delle stringhe per definire le funzioni
exec(function1_with_params)
exec(function2_with_params)

# Ottieni le funzioni definite dinamicamente
func3 = locals()[func3_name]
func4 = locals()[func4_name]

# Esegui il test sulle funzioni estratte con parametri
test_functions(func3, func4, 2, 3)  # Passa i parametri 2 e 3 alle funzioni

#Funzioni di test con stesse strutture dati
"""
def function1_list():
    return [1, 2, 3, 4]
def function2_list():
    return [1, 2, 3, 4]
test_functions(function1_list, function2_list)
def function1_list_no_order():
    return [1, 2, 4, 3]
def function2_list_no_order():
    return [1, 2, 3, 4]
test_functions(function1_list_no_order, function2_list_no_order)
def function1_tuple():
    return (1, 2, 3, 4)
def function2_tuple():
    return (1, 2, 3, 4)
test_functions(function1_tuple, function2_tuple)
def function1_tuple_no_order():
    return (1, 2, 4, 3)
def function2_tuple_no_order():
    return (1, 2, 3, 4)
test_functions(function1_tuple_no_order, function2_tuple_no_order)
def function1_set():
    return {1, 2, 3, 4}
def function2_set():
    return {1, 2, 3, 4}
test_functions(function1_set, function2_set)
# Funzioni di test con diverse strutture dati
def function1_list_tuple():
    return [1, 2, 3, 4]
def function2_list_tuple():
    return (1, 2, 4, 3)
test_functions(function1_list_tuple, function2_list_tuple)
def function1_dict():
    return {'a': 1, 'b': 2, 'c': 3}
def function2_dict():
    return {'c': 3, 'b': 2, 'a': 1}
test_functions(function1_dict, function2_dict)
def function1_list_of_dicts():
    return [{'a': 1}, {'b': 2}]
def function2_list_of_dicts():
    return [{'b': 2}, {'a': 1}]
test_functions(function1_list_of_dicts, function2_list_of_dicts)
def function1_nested():
    return [1, [2, 3], {'a': [4, 5]}]
def function2_nested():
    return [1, (2, 3), {'a': (4, 5)}]
test_functions(function1_nested, function2_nested)
def function1_set_list():
    return {1, 2, 3, 4}
def function2_set_list():
    return [4, 3, 2, 1]
test_functions(function1_set_list, function2_set_list)
def function1_tuple_of_dicts():
    return ({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
def function2_tuple_of_dicts():
    return ({'c': 3, 'd': 4}, {'a': 1, 'b': 2})
test_functions(function1_tuple_of_dicts, function2_tuple_of_dicts)
def function1_sets():
    return {1, 2, 3, 4}
def function2_sets():
    return {4, 3, 2, 1}
test_functions(function1_sets, function2_sets)
def function1_tuple_of_lists():
    return ([1, 2], [3, 4])
def function2_tuple_of_lists():
    return ([1, 2], [4, 3])
test_functions(function1_tuple_of_lists, function2_tuple_of_lists)
def function1_void():
    pass  # Non fa niente e non restituisce niente
def function2_void():
    return  # Esplicitamente restituisce None
test_functions(function1_void, function2_void)
"""


#CASE TEST TRAIN-23
"""
class Person:
    def __init__(self, first_name, last_name, job='', social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media
    def assign_attributes(self, first_name, last_name, job, social_media):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media
# Funzione per creare un oggetto Person usando __init__
def create_person_with_init():
    return Person("John", "Doe", "Engineer", {"LinkedIn": "johndoe"})
# Funzione per creare un oggetto Person e assegnare attributi usando assign_attributes
def create_person_with_assign():
    person = Person("Jane", "Smith")
    person.assign_attributes("John", "Doe", "Engineer", {"LinkedIn": "johndoe"})
    return person
# Esempio di utilizzo
test_functions(create_person_with_init, create_person_with_assign)
"""