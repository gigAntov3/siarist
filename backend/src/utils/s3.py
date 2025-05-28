import boto3
from botocore.client import Config

from core import config

def create_s3_session():
    return boto3.client(
        service_name='s3',
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        endpoint_url=config.AWS_ENDPOINT_URL,
        region_name=config.AWS_REGION,
        config=Config(signature_version='s3v4')
    )