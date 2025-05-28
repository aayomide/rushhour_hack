import boto3
from config import access_key, secret_key, region_name


def aws_session():
    """
    setting up aws boto3 session credentials
    """
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region_name,
    )
    return session