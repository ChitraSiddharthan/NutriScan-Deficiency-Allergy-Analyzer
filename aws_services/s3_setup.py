"""s3 setup file helps in creating s3 bucket in AWS programatically """
import logging
import boto3
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logging level at Info
# AWS Configuration
AWS_REGION = "us-east-1"
BUCKET_NAME = "allergy-analyzer-reports"
def create_s3_bucket():
    """Create an S3 bucket if it doesn't exist."""
    s3_client = boto3.client("s3", region_name=AWS_REGION) #create s3 client
    try:
        s3_client.create_bucket(Bucket=BUCKET_NAME)  #create s3 bucket
        logger.info(f"S3 bucket '{BUCKET_NAME}' created successfully.") #logs if success
    except s3_client.exceptions.BucketAlreadyOwnedByYou:
        logger.info(f"S3 bucket '{BUCKET_NAME}' already exists.") #logs if bucket already exists
    except Exception as e:
        logger.error(f"Error creating S3 bucket: {e}") #logs error if any
#
if __name__ == "__main__":
    create_s3_bucket()
