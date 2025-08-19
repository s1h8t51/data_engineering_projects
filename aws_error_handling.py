import boto3
from botocore.exceptions import NoCredentialsError, ClientError

s3 = boto3.client('s3')

try:
    s3.download_file("my-first-bucket-2025-12345", "nonexistent.csv", "test.csv")
except ClientError as e:
    print("Error:", e)
except NoCredentialsError:
    print("AWS credentials not found.")
