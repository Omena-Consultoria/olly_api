from boto3 import resource
import os

dynamodb = resource("dynamodb",
                    aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                    aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
                    region_name=os.environ['AWS_REGION_NAME'],
                    )

tables = [
    {
        "TableName": "olly-database",
        "KeySchema": [
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'created_at',
                'KeyType': 'RANGE'
            },

        ],
        "AttributeDefinitions": [
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'created_at',
                'AttributeType': 'S'
            }
        ],
    },
]


def create_tables():
    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:
        print(e)