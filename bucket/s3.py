import boto3
import os

def load_olly_data_from_s3():
    access_key = os.environ['AWS_ACCESS_KEY']
    secret_key = os.environ['AWS_SECRET_KEY']

    client = boto3.client(
            's3',
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key
    )

    excel_object = client.get_object(Bucket=os.environ['S3_BUCKET_NAME'], Key=os.environ['S3_ARCHIVE_NAME'])
    olly_data = excel_object['Body'].read()

    return olly_data