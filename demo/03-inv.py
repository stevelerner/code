from flask import Flask, make_response, request
import json
import boto3
from random import random, seed, randint
from time import sleep

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('items')
client = boto3.client('dynamodb')

seed(1)
app = Flask(__name__)

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
        'Inventory': str(response["Item"]["item_desc"]["S"])
        }
    y=round(random(),1)+.25
    sleep(y)

    return(log_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4997)