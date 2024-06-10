import os
import boto3
import s3fs

# Set your AWS credentials
os.environ['AWS_ACCESS_KEY_ID'] = 'your_access_key'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your_secret_key'

# Create an S3 filesystem object
s3 = s3fs.S3FileSystem(anon=False)

# List all files in a bucket
bucket_name = 'your_bucket_name'
files = s3.ls(bucket_name)

# Upload a file to S3
local_file_path = 'path/to/local/file.txt'
s3_file_path = 'path/to/s3/file.txt'
s3.put(local_file_path, s3_file_path)

# Download a file from S3
s3.get(s3_file_path, local_file_path)

# Delete a file from S3
s3.rm(s3_file_path)
