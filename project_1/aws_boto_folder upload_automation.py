import os
import boto3
from pprint import pprint


# Create a boto3 session
aws_management_console = boto3.session.Session(profile_name ="default") 
s3 = aws_management_console.client('s3') 

def upload_folder(local_dir, bucket, prefix=""):
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            print('sahi')
            local_path = os.path.join(root, file)
            s3_path = os.path.join(prefix, file) # <--- Still problematic here
            s3.upload_file(local_path, bucket, s3_path) # <--- This is where the resource call happens
            print(f"Uploaded {local_path} → s3://{bucket}/{s3_path}")


upload_folder("/Users/sahitya_gantala/Desktop/projects/sem1/seeds (1)", "my-first-bucket-2025-12345", "data")
