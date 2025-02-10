from modules import tasks,listtasks,status
from time import sleep

num = -1

while num != 0:

  print('Hello, choose an option below using your number')

  num = int(input('1-add task, \n2-remove task, \n3-update task, \n4-show task status, \n5-list all tasks \n6-completed tasks, \n7-list tasks in progress, \n8-list tasks not started \n0-close program \n'))

  print('loading...')
  sleep(2)

  if num == 0:
     print('program closed')
     break
  elif num == 1:
     var1 = input('Enter the task you want to add  ').lower().strip()
     tasks.add_tasks(var1)
  elif num == 2:
     var2 = input('Enter the task you want to remove ').lower().strip()
     tasks.remove_tasks(var2)
  elif num == 3:
     var3 = input('Enter the task that you want to update status ').lower().strip()
     var3_5 = input('now enter status \n1- not started \n2- in progress \n3- completed \n').lower().strip()
   # #   if var3_5 != 'notstarted' or var3_5!= 'inprogress' or var3_5 != 'completed':
   # #      print('incorect values')
   #   else:
     tasks.update_tasks(var3,var3_5) 
  elif num == 4:
     var4 = input('Enter the task you want to show the status ').lower().upper()
     statustask = status.show_status(var4)
     print(statustask)
  elif num == 5:
     dictonarie = listtasks.list_all_tasks()
     print(dictonarie)

   