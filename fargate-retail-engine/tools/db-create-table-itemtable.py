import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='items',
    KeySchema=[
        {
            'AttributeName': 'item_sku',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'item_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'item_sku',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'item_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='items')

# Print out some data about the table.
print(table.item_count)