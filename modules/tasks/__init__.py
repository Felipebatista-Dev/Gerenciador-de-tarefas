import json

# Carrega o conteúdo do arquivo JSON

with open("tasklist.json", encoding='utf-8') as my_json:
    data = json.load(my_json)
      

# I created an object that has the content of the json file

# the json file was read as a list


# this function is able to add new tasks to my list

# whenever the code is executed it only adds the task if it is not already present in the list, so as not to duplicate tasks

# def reset():
# res = input('type r to reset')

def add_tasks(tasksparameter1,taskparameter1b):
    if tasksparameter1 not in data:
       var = taskparameter1b
       if var == 1:
          data[tasksparameter1] = 'notstarted'
       elif var == 2:
          data[tasksparameter1] = 'inprogress'
       elif var == 3:
          data[tasksparameter1] = 'completed'
       else:
          print('Incorrect number')
    else:
        print('This task already exists')
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