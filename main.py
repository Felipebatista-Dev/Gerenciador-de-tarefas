from modules import tasks,listtasks,status
from time import sleep

num = -1

while num != 0:

  print('Hello, choose an option below using your number')

  num = int(input('1-add task, \n2-remove task, \n3-update task, \n4-show task status, \nlist all tasks \n5-list \n6-completed tasks, \n7-list tasks in progress, \n8-list tasks not started \n0-close program \n'))

  print('loading...')
  sleep(2)

  if num == 0:
     break
  elif num == 1:
     var1 = input('Enter the task you want to add ').lower().strip()
     tasks.add_tasks(var1)
  elif num == 2:
     var2 = input('Enter the task you want to remove').lower().strip()
     tasks.remove_tasks(var2)

   