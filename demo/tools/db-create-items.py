import boto3
from time import sleep
from random import random, seed, randint


# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('items')

x=1
while (x<101):

    random_number = randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number = hex_number[2:]
    
    table.put_item(
    Item={
        'item_sku': str(x),
        'item_name': str(x),
        'item_desc': hex_number,
    } )
    
    y=round(random(),1)+.25
    sleep(y)
    x+=1