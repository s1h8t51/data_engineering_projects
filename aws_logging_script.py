import boto3, logging

#way to setup rootlogger only setup at start whihc tells to make sure to save all file 
# into s3_ops.log file  and INFO will save all the information 

logging.basicConfig(filename="s3_ops.log", level=logging.INFO)
s3 = boto3.client('s3')

def safe_upload(local_file, bucket, key):
    try:
        s3.upload_file(local_file, bucket, key)
        logging.info(f"Uploaded {local_file} → s3://{bucket}/{key}")
    except Exception as e:
        logging.error(f"Failed to upload {local_file}: {e}")

safe_upload("local.csv", "my-first-bucket-2025-12345", "logged_upload.csv")


#logs are saved to your local dir or parent one to check the logs 

#to check the loggin file 
responce = s3.list_objects_v2(Bucket="my-first-bucket-2025-12345")
#pprint(responce)
for i in responce.get("Contents",[]):
    print(i["Key"])