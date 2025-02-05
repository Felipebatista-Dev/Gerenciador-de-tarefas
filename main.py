from modules import tasks,listtasks,status

obj = listtasks.list_all_tasks()
print(obj)
tasks.add_tasks("lavar cabeça")
obj = listtasks.list_all_tasks()
print(obj)
