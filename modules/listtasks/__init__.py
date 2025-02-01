import json

with open("tasklist.json",encoding='utf-8') as my__json:
     dados = json.load(my__json)

def list_all_tasks():
    return dados