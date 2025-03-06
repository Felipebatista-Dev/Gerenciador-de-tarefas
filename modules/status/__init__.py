import json


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
