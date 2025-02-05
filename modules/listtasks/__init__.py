import json

with open("tasklist.json",encoding='utf-8') as my__json:
     data = json.load(my__json)

def list_all_tasks():
    return data
