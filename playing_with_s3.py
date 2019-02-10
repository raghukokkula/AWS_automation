#These following command is used to list all the buckets in S3
import boto3
import os
s3 = boto3.resource('s3')


#Upload a file into all the buckets in our account.
for bucket in s3.buckets.all():
    bucket_name = bucket.name
    cwd = os.getcwd()
    s3.Bucket(bucket_name).upload_file(str(cwd)+'/ufck.txt', "ufck.txt")
    print(bucket_name)


