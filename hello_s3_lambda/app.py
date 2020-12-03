import boto3
import os
import uuid
from datetime import datetime

s3 = boto3.client('s3')


def lambda_handler(event, context):
    bucket = os.environ['OUTPUT_BUCKET_NAME']
    random_id = str(uuid.uuid1())
    time = str(datetime.now())
    upload_text = f'Hello S3, the time is now {time}'
    upload_bytes = bytes(upload_text.encode('UTF-8'))
    s3.put_object(Bucket=bucket, Key=random_id, Body=upload_bytes)
    print('Put Complete')
