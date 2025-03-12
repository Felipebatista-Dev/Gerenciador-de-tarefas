import sys
import os
import json
from modules import tasks, listtasks, status
from time import sleep

def get_base_path():
    return getattr(sys, '_MEIPASS', os.path.abspath("."))

# Caminho do JSON
caminho_json = os.path.join(get_base_path(), "tasklist.json")

# Verifica se o arquivo JSON existe
if not os.path.exists(caminho_json):
    print(f"Erro: O arquivo {caminho_json} não foi encontrado.")
    input("Pressione ENTER para sair...")  # Mantém a janela aberta para ver o erro
    sys.exit(1)

# Lê o JSON
with open(caminho_json, encoding="utf-8") as f:
    dados = json.load(f)

print("Arquivo JSON carregado com sucesso!")


num = -1

while num != 0:

  print('Hello, choose an option below using your number')
  try: 
   num = int(input('1-add task, \n2-remove task \n3-update task \n4-show task status \n5-list all tasks \n6-list completed tasks \n7-list tasks in progress \n8-list tasks not started \n0-close program \n'))
  except(TypeError,ValueError):
   print('incorrect value, try again')
  print('loading...')
  sleep(2)
  
  if num == 0:
     print('program closed')
     break
  elif num == 1:
     var1 = input('Enter the task you want to add  \n').lower().strip()
     var1b = int(input('now inform the status of the task \n1- not started \n2- in progress \n3- completed \n'))
     try:
       tasks.add_tasks(var1,var1b)
     except(TypeError):
       print('Incorrect values')
  elif num == 2:
     var2 = input('Enter the task you want to remove \n').lower().strip()
     try:
       tasks.remove_tasks(var2)
     except(TypeError):
       print('Incorrect values')
  elif num == 3:
     var3 = input('Enter the task that you want to update status ').lower().strip()
     var3_5 = input('now enter status \n1- not started \n2- in progress \n3- completed \n').lower().strip()
     try:
       tasks.update_tasks(var3,var3_5) 
     except(TypeError):
       print('Incorrect values')
  elif num == 4:
     var4 = input('Enter the task you want to show the status \n').lower().upper()
     statustask = status.show_status(var4)
     print(statustask)
  elif num == 5:
     dictonarie = listtasks.list_all_tasks()
     print(dictonarie)
  elif num == 6:
     dictonariec = listtasks.list_completed_tasks()
     print(dictonariec)
  elif num == 7:
     dictonariep = listtasks.list_inprogress_tasks()
     print(dictonariep)
  elif num == 8:
     dictonarien = listtasks.list_notstarted_tasks() 
     print(dictonarien)
 
    

   