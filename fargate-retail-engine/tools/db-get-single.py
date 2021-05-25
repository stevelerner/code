import boto3
import pprint

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('items')
client = boto3.client('dynamodb')

# response = table.get_item(
#     Key={
#         'item_sku': '1',
#         'item_name': '1'
#     }
# )

# print(response)

response2 = client.get_item(
    Key={
        'item_sku': { 'S': '1' },
        'item_name': { 'S': '1' },
        },
        TableName='items',
    )

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(response2["Item"]["item_desc"]["S"])
print(response2["Item"]["item_desc"]["S"])