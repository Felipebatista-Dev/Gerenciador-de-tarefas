import json

with open("tasklist.json",encoding='utf-8') as my__json:
     data = json.load(my__json)

# essa função tem como objetivo mostrar o status de determinada função

def show_status(statusparameter):
        status = ''
        for k,v in data.items():
            if k == statusparameter:
               status  = v
        return v
#ela nao precisa de salvar nada no arquivo ao contrario das outras
