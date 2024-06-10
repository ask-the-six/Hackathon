import os
import boto3
import s3fs
import pandas as pd

# Set your AWS credentials
os.environ['AWS_ACCESS_KEY_ID'] = 'your_access_key'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your_secret_key'

# Create an S3 filesystem object
s3 = s3fs.S3FileSystem(anon=False)

# Specify the bucket and file path of the CSV file
bucket_name = 'your_bucket_name'
csv_file_path = 'path/to/csv/file.csv'

# Read the CSV file using pandas
with s3.open(f'{bucket_name}/{csv_file_path}', 'rb') as file:
  df = pd.read_csv(file)

# Print the contents of the CSV file
print(df)
