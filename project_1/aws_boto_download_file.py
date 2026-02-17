
import boto3
from pprint import pprint

# Create a boto3 session
aws_management_console = boto3.session.Session(profile_name ="default") 

# Get an IAM resource object from the session
#iam_console = aws_management_console.client('iam') 
#ec2_console = aws_management_console.client('ec2')

# Get an s3 resource object from the session
s3 = aws_management_console.client('s3')
 

# downloading a and listing objects
s3.download_file("my-first-bucket-2025-12345","uploaded.csv","downloaded.csv")

#list objects >> list_objects_v2 latest one 
responce = s3.list_objects_v2(Bucket="my-first-bucket-2025-12345")
#pprint(responce)
for i in responce.get("Contents",[]):
    print(i["Key"])
