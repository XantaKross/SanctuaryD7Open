"""
Darwin's root. Where it contains all the classes and functions that make change or affect or have a relation when given the command to it's home PC.
"""

from . import _common

def time_func(time_):
    if int(time_[:2]) <= 12: return 'morning'
    
    elif int(time_[:2]) < (5+12): return 'afternoon'
    
    elif int(time_[:2]) < (8+12): return 'evening'
    
    elif int(time_[:2]) < 24: return 'night'



#is not working because of new filter.
def run_apps(query):
    address= r'C:\Users\Pranav\Desktop\Programs'
    programs = list(listdir(address))
    
    results = []
    for idx in range(len(programs)):
        results.append([_common.word_sim(query, programs[idx]), programs[idx], idx])
        #conf, fltrd_command, index
    
    best_result = max(results)
    app_name = programs[best_result[2]]
    
    u = f'{address}\\{app_name.lower()}'
    
    if len(best_result) != 0 or best_result[0] > 0.5:
        webb.open(u)
    
    return [best_result[0], app_name.replace('.lnk', '')]