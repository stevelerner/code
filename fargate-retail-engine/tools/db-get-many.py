import boto3
import requests
from random import random, seed, randint
from time import sleep
import json

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('items')
client = boto3.client('dynamodb')

seed(1)

url = 'https://ptsv2.com/'

def pythonrequests():
    try:
        r=requests.get(url)
        log_dict = {'httpMETHOD': "post",
            'httpURL': str(r.url),
            'httpSTATUS': str(r.status_code),
            'httpCONTENT': str(r.content)
            }
        print(log_dict["httpURL"],log_dict["httpSTATUS"])
    except requests.exceptions.RequestException as err:
        log_dict = {'error': str(err),   
            }
        print(log_dict["httpURL"])

while True:
    x=randint(1,99)
    response = client.get_item(
        Key={
            'item_sku': { 'S': str(x) },
            'item_name': { 'S': str(x) },
            },
            TableName='items'
        )
    print(response["Item"]["item_desc"]["S"])

    response = table.get_item(
        Key={
            'item_sku': str(x),
            'item_name': str(x)
            }
        )
    print(response["Item"])

    response = client.list_tables(
        Limit=10
        )  
    print(response["TableNames"])

    pythonrequests()

    y=round(random(),1)+.25
    sleep(y)