import json

# crei um objeto que tem o conteudo do arquivo json

# o arquivo json foi lido como uma lista
with open("tasklist.json",encoding='utf-8') as my__json:
     data = json.load(my__json)

# essa função é capaz de adcionar novas tarefas a minha lista

# sempre que o codigo é executado ele so adciona a tarefa se ela nao ja estiver presente na lista, para nao duplicar tarefas

# def reset():
#     res = input('digite r para resetar')

def add_tasks(tasksparameter1):
    if tasksparameter1 not in data: 
        data[tasksparameter1] = 'naoiniciada'
        with open("tasklist.json", 'w', encoding='utf-8') as my_json:
          json.dump(data, my_json)

# essa função é capaz de de remover tarefas da minha lista json, isso é feito atraves da chave

def remove_tasks(tasksparameter2):
    if tasksparameter2 in data:
        data.pop(tasksparameter2)
        with open("tasklist.json", 'w', encoding='utf-8') as my_json:
          json.dump(data, my_json)

# essa função permite ao usuario atualizar o status da tarefa com 3 opções disponiveis

def update_tasks(tasksparameter3,taskparameter4):
    if tasksparameter3 in data:
     data[tasksparameter3] = taskparameter4
     with open("tasklist.json", 'w', encoding='utf-8') as my_json:
       json.dump(data, my_json)
   




# def remover_tasks(parameter2):
#     if parameter2 in data:
#      data.remove(parameter2)
#      with open("tasklist.json", 'w', encoding='utf-8') as my_json:
#         json.dump(data, my_json)
