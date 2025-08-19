import boto3
from boto3.s3.transfer import TransferConfig
from pprint import pprint

#initiating the console 
s3 = boto3.client('s3')

#to make big file a parallel upload we use this
#greater than the mentioned threshold then the file will parallely divided to 
#different files and then load 


config = TransferConfig(multipart_threshold=5*1024*1024) 

s3.upload_file("multipart_zip_file.zip", "my-first-bucket-2025-12345", "multipart_zip_file.zip", Config=config)
print("Multipart upload successful!")

#we need to check the upload then go to aws_scripts_upload file 

responce = s3.list_objects_v2(Bucket="my-first-bucket-2025-12345")
#pprint(responce)
for i in responce.get("Contents",[]):
    print(i["Key"])