import boto3
import requests
from time import sleep
from random import random, seed

client = boto3.client('dynamodb')

x=100

while (x<=201):
    y = random()
    #print('Sleeping: ', round(y,2))
    sleep(round(y,2))

    response = client.get_item(
        Key={
            'item_number': { "N": str(x)}
        },
        TableName='items',
    )
    print(response)
    x+=1