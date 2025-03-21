import os
import boto3

# Define bucket name and local folder
BUCKET_NAME = "s3automationbucket"
LOCAL_FOLDER = "/home/arnoldmbuthia/Downloads/"

# Initialize S3 client
s3 = boto3.client("s3")

def upload_files():
    """
    Uploads all files from LOCAL_FOLDER to the specified S3 bucket.
    """
    for root, _, files in os.walk(LOCAL_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = os.path.relpath(file_path, LOCAL_FOLDER)  # Keep the folder structure

            try:
                print(f"Uploading {file_path} to {BUCKET_NAME}/{s3_key}...")
                s3.upload_file(file_path, BUCKET_NAME, s3_key)
                print(f"✅ Successfully uploaded {file}")
            except Exception as e:
                print(f"❌ Failed to upload {file}: {e}")

if __name__ == "__main__":
    upload_files()

import os
import boto3

BUCKET_NAME = "s3automationbucket"
LOCAL_FOLDER = "/home/arnoldmbuthia/Downloads/"
UPLOAD_LIMIT = 2  # Set a limit on the number of files uploaded per run

s3 = boto3.client("s3")

def upload_files():
    count = 0
    for root, _, files in os.walk(LOCAL_FOLDER):
        for file in files:
            if count >= UPLOAD_LIMIT:
                print("Upload limit reached. Stopping...")
                return  # Stop execution once limit is reached
            
            file_path = os.path.join(root, file)
            s3_key = os.path.relpath(file_path, LOCAL_FOLDER)

            try:
                print(f"Uploading {file_path} to {BUCKET_NAME}/{s3_key}...")
                s3.upload_file(file_path, BUCKET_NAME, s3_key)
                print(f"✅ Successfully uploaded {file}")
                count += 1  # Increment count after a successful upload
            except Exception as e:
                print(f"❌ Failed to upload {file}: {e}")

if __name__ == "__main__":
    upload_files()
