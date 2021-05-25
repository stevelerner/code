from flask import Flask, make_response, request
import json
import boto3
from random import random, seed, randint

client = boto3.client('dynamodb')

seed(1)
app = Flask(__name__)
   
@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
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
    return(log_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)