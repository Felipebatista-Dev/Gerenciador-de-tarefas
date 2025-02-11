import json
import os
import sys

def get_base_path():
    return getattr(sys, '_MEIPASS', os.path.abspath("."))

caminho_json = os.path.join(get_base_path(), "tasklist.json")

# Carrega o conteúdo do arquivo JSON
try:
    with open(caminho_json, "r", encoding='utf-8') as my_json:
        data = json.load(my_json)
        if not isinstance(data, dict):
            raise ValueError("O conteúdo do arquivo JSON deve ser um dicionário.")
except Exception as e:
    print(f"Erro ao carregar o arquivo JSON: {e}")
    data = {}

# I created an object that has the content of the json file

# the json file was read as a list


# this function is able to add new tasks to my list

# whenever the code is executed it only adds the task if it is not already present in the list, so as not to duplicate tasks

# def reset():
# res = input('type r to reset')

def add_tasks(tasksparameter1,taskparameter1b):
    if tasksparameter1 not in data:
        data[tasksparameter1] = taskparameter1b
    with open("tasklist.json", 'w', encoding='utf-8') as my_json:
      json.dump(data, my_json)

# this function is able to remove tasks from my json list, this is done through the key

def remove_tasks(tasksparameter2):
    if tasksparameter2 in data:
         data.pop(tasksparameter2)
    with open("tasklist.json", 'w', encoding='utf-8') as my_json:
        json.dump(data, my_json)

# this function allows the user to update the task status with 3 available options

def update_tasks(tasksparameter3,taskparameter4):
    if tasksparameter3 in data:
         data[tasksparameter3] = taskparameter4
    with open("tasklist.json", 'w', encoding='utf-8') as my_json:
      json.dump(data, my_json)