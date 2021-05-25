from random import seed, uniform
from time import sleep
import requests
import json

seed(1)
url = 'http://localhost:4999/shopengine'

def pythonrequests():
    payload = {'key': 'value'}
    try:
        r=requests.post(url, params=payload)
        log_dict = {'httpMETHOD': "post",
            'httpURL': str(r.url),
            'httpSTATUS': str(r.status_code),
            'httpCONTENT': str(r.content)
            }
        print(json.dumps(log_dict,indent=2,separators=(',', ':')))
    except requests.exceptions.RequestException as err:
        log_dict = {'error': str(err),   
            }
        print(json.dumps(log_dict,indent=2,separators=(',', ':')))

while True:
    pythonrequests()
    y = uniform(0,.25)
    sleep(y)