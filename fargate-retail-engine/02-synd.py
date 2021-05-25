from flask import Flask, make_response, request
from random import random, seed, randint, uniform
from time import sleep
import requests
import json
import boto3

app = Flask(__name__)
seed(1)

catalogurl = 'http://localhost:5000/catalog'
invservice = 'http://localhost:4997/inventory'

@app.route('/shopengine', methods=['GET', 'POST'])
def shopengine():
    # inventory service
    payload = {'key': 'value'}
    try:
        r=requests.post(invservice, params=payload)
        log_dict = {
            'reponse': r.content
            }
        inv = json.loads(r.content)
    except requests.exceptions.RequestException as err:
        log_dict = {'error': str(err),   
            }
        print(json.dumps(log_dict))
        
    # catalog service
    payload = {'key': inv}
    try:
        r=requests.post(catalogurl, params=payload)
        log_dict = {'httpMETHOD': "post",
            'httpURL': str(r.url),
            'httpSTATUS': str(r.status_code),
            'httpCONTENT': str(r.content)
            }
        print(json.dumps(log_dict))
    except requests.exceptions.RequestException as err:
        log_dict = {'error': str(err),   
            }
        print(json.dumps(log_dict))

    y = uniform(0,.1)
    sleep(y)

    return(inv)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4999)