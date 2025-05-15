""" 
pre-assigned url allow you to grant temporary access 
to private S3 objects without sharing our AWS credentials to users.
"""
import logging
from django.conf import settings
import boto3
#this is to make sure that the authenticated user gets the report, due to less IAM credentials
logger = logging.getLogger(__name__)
def generate_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a pre-signed URL to share an S3 object."""
    s3_client = boto3.client('s3', region_name=settings.AWS_REGION)
    try:
        response = s3_client.generate_presigned_url(
            'get_object', # The operation to generate a URL for (downloading an object)
            Params={
                'Bucket': bucket_name, #s3 buckets name
                'Key': object_name #the name of s3 object
            },
            ExpiresIn=expiration) #url's expiration time is set
        logger.info(f"Generated pre-signed URL for {object_name}") #logs success url generation
    except Exception as e:
        logger.error("Error generating pre-signed URL: %s",e)#else error logs
        return None
    return response
