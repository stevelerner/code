from flask import Flask, make_response, request
from random import random, seed, randint, uniform
from time import sleep
import json
import boto3

client = boto3.client('dynamodb')

app = Flask(__name__)
seed(1)

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    x=randint(1,99)
    response = client.get_item(
        Key={
            'item_sku': { 'S': str(x) },
            'item_name': { 'S': str(x) },
            },
            TableName='items',
        )
    log_dict = {
        'inventory': str(response["Item"]["item_desc"]["S"])
        }

    y = uniform(0,.1)
    sleep(y)
    return(log_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4997)