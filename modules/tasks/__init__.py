import json

# crei um objeto que tem o conteudo do arquivo json

# o arquivo json foi lido como uma lista
with open("tasklist.json",encoding='utf-8') as my__json:
     data = json.load(my__json)

# essa função é capaz de adcionar novas tarefas a minha lista

# sempre que o codigo é executado ele so adciona a tarefa se ela nao ja estiver presente na lista, para nao duplicar tarefas

def reset():
    res = input('digite r para resetar')

def add_tasks(parameter1):
    for k,v in data:
     if parameter1 not in k:
       data = [parameter1]  
       data[parameter1] = 'naoiniciada'
       with open("tasklist.json", 'w', encoding='utf-8') as my_json:
        json.dump(data, my_json)

# essa função é capaz de de remover tarefas da minha lsita json

def remove_tasks(parameter2):
    if parameter2 in data:
       for i in data:
           if i == parameter2:
              data.remove(i)
       with open("tasklist.json", 'w', encoding='utf-8') as my_json:
        json.dump(data, my_json)



# def remover_tasks(parameter2):
#     if parameter2 in data:
#      data.remove(parameter2)
#      with open("tasklist.json", 'w', encoding='utf-8') as my_json:
#         json.dump(data, my_json)
