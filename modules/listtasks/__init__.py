import json
import os
import sys

def get_base_path():
    return getattr(sys, '_MEIPASS', os.path.abspath("."))

caminho_json = os.path.join(get_base_path(), "tasklist.json")

with open(caminho_json, "r", encoding="utf-8") as f:
    data = f.read()


with open("tasklist.json",encoding='utf-8') as my__json:
     data = json.load(my__json)



# this function returns the tasks dictionary
def list_all_tasks():
    if not data: 
     return 'the list is empty'
    else:
     return data
    
# this function lists completed tasks
def list_completed_tasks():
    comp = []
    for k,v in data.items():
        if v == 'completed': 
           comp.append(k)
    if not comp:
       return'the list has no completed tasks'
    else:
       return comp

# this function lists in progress tasks
def list_inprogress_tasks():
    prog = []
    for k,v in data.items():
        if v == 'inprogress':
          prog.append(k)
    if not prog:
       return'the list has no tasks in progress'
    else: 
       return prog

# this function lists not started tasks
def list_notstarted_tasks():
    nots = []
    for k,v in data.items():
        if v == 'notstarted':
           nots.append(k)
    if not nots:
        return'the list has no unstarted tasks'  
    else:  
        return nots