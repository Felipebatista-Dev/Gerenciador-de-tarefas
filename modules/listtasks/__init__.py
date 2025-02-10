import json

with open("tasklist.json",encoding='utf-8') as my__json:
     data = json.load(my__json)

# essa função retorna o dicioanrio de tarefas
def list_all_tasks():
    return data

# essa função lista as tarefas concluidas
def list_completed_tasks():
    comp = []
    for k,v in data.items():
        if v == 'completed':
           comp.append(k)
    return comp

# essa função lista as tarefas em andamento
def list_inprogress_tasks():
    prog = []
    for k,v in data.items():
        if v == 'inprogress':
           prog.append(k)
    return prog

# essa função lista lista as tarefas nao inciadas
def list_notstarted_tasks():
    nots = []
    for k,v in data.items(): 
        if v == 'notstarted':
           nots.append(k)
    return nots   