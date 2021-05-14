import os
import boto3


TARGET_BUCKET_NAME = os.environ.get("TARGET_BUCKET_NAME")


def lambda_handler(event, context):
    print("hello lambda")
    return None
