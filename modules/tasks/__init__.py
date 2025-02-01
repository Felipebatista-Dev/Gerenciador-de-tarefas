import json

# crei um objeto que tem o conteudo do arquivo json

# o arquivo json foi lido como uma lista
with open("tasklist.json",encoding='utf-8') as my__json:
     data = json.load(my__json)

# essa função é capaz de adcionar novas tarefas a minha lista

def add_tasks(parameter):
    data.append(parameter)
