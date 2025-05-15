"""Integrating s3 to store the files generated"""
import logging
import boto3
# from django.conf import settings
logger = logging.getLogger(__name__)
AWS_REGION = "us-east-1"
BUCKET_NAME = "allergy-analyzer-reports"
s3_client = boto3.client("s3", region_name=AWS_REGION) #creates an s3 client
def upload_to_s3(file_path, s3_filename):
    """Uploads a file to S3"""
    try:
        with open(file_path, 'rb') as data: #opens the file in binary read mode
            s3_client.upload_fileobj(data, BUCKET_NAME, s3_filename) #uploads file object to s3
        file_url = f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{s3_filename}"
        logger.info(f"File uploaded to S3: {file_url}") #logging success of upload
        return file_url #returns s3 file url
    except Exception as e:
        logger.error("Error uploading file to S3: %s",e) #logs upload error
        return None
#
def download_from_s3(s3_filename, local_path):
    """Downloads a file from S3 to a local directory."""
    try:
        s3_client.download_file(BUCKET_NAME, s3_filename, local_path) #download the file from s3
        logger.info(f"File downloaded from S3: {local_path}") #logs success of file download
        return local_path #returns the local file path
    except Exception as e:
        logger.error("Error downloading file from S3: %s",e) #logs if any error while downloading
        return None
