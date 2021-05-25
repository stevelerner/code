from flask import Flask, make_response, request
from random import random, seed, randint, uniform
from time import sleep
import requests
import json
import boto3

client = boto3.client('dynamodb')
invservice = 'http://localhost:4997/inventory'

app = Flask(__name__)
seed(1)
   
@app.route('/catalog', methods=['GET', 'POST'])
def catalog():

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

    x=randint(1,99)
    response = client.get_item(
        Key={
            'item_sku': { 'S': str(x) },
            'item_name': { 'S': str(x) },
            },
            TableName='items',
        )
    log_dict = {
            'catalog': str(response["Item"]["item_desc"]["S"])
            }

    y = uniform(0,.1)
    sleep(y)

    return(log_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)