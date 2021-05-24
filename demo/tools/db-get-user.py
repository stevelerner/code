import boto3
import requests
from time import sleep
from random import random, seed

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

while True:
    y = random()
    #print('Sleeping: ', round(y,2))
    sleep(round(y,2))
    response = table.get_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        }
    )
    item = response['Item']
    print(item)