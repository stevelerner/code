import requests
from time import sleep
from random import random, seed
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

seed(1)
url = 'http://localhost:4997/inventory'

def pythonrequests():
    payload = {'key': 'value'}
    try:
        r=requests.post(url, params=payload)
        log_dict = {
            'reponse': r.content
            }
        inv = json.loads(r.content)
        print(inv["Inventory"])

    except requests.exceptions.RequestException as err:
        log_dict = {'error': str(err),   
            }
        print(log_dict)

while True:
    pythonrequests()
    y = random()
    #print('Sleeping: ', round(y,2))
    sleep(round(y,2))