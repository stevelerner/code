import boto3
import pprint

client = boto3.client('dynamodb')
response = client.list_tables(
    Limit=10
)  

pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(response)