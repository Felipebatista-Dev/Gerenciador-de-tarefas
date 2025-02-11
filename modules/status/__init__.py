import json
import os
import sys

def get_base_path():
    return getattr(sys, '_MEIPASS', os.path.abspath("."))

caminho_json = os.path.join(get_base_path(), "tasklist.json")

with open(caminho_json, "r", encoding="utf-8") as f:
    data = f.read()

with open("tasklist.json",encoding='utf-8') as my__json:
     data = json.load(my__json)


# this function aims to show the status of a given function

def show_status(statusparameter):
    status = ''
    for k,v in data.items():
        if k == statusparameter:
           status = v
    if not status:
       return'This task is not present in the list'
    else:
       return status
#it doesn't need to save anything in the file unlike the others
