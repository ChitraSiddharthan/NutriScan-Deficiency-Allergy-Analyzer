"""dynamodb handler file is created to store the users input in a form of table """
import logging
import datetime
import boto3
from django.conf import settings
from user_management.utils import generate_presigned_url #import the generate_presigned_url func
logger = logging.getLogger(__name__)
AWS_REGION = "us-east-1"
TABLE_NAME = "AllergyAnalysisHistory"
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)
def store_analysis(username, symptoms, medical_history, result, s3_filename):
    """Store analysis data in DynamoDB."""
    timestamp = datetime.datetime.utcnow().isoformat()
    try:
        logger.info(f"Attempting to store data in DynamoDB for user: {username}")
        response = table.put_item(
            Item={
                "username": username,
                "timestamp": timestamp,
                "symptoms": symptoms,
                "medical_history": medical_history,
                "analysis_result": result,
                "s3_filename": s3_filename #storing s3_filename for later retrieval
            }
        )
        logger.info(f"Data stored in dynamodb: {response}")
        return response
    except Exception as e:
        logger.error(f"Error storing data in DynamoDB:{e}")
        return None
def retrieve_analysis_history(username):
    """Retrieve most recent analysis history for a user."""
    try:
        response = table.query( #Queries by username, sorts and retrieves
            KeyConditionExpression=boto3.dynamodb.conditions.Key("username").eq(username),
            ScanIndexForward=False,  # sorts in descending order of timestamp
            Limit=1,  # retrieve only the latest item
        )
        items = response.get("Items", []) #gets the returned item from response
        for item in items:  # Check if any items were returned
            if "s3_filename" in item:
                item["s3_report_url"] = generate_presigned_url(
                    settings.AWS_STORAGE_BUCKET_NAME, item["s3_filename"]
                )
            else:
                #log a warning if s3 file is missing
                logger.warning(f"Item for user {username} is missing s3_filename.")
                item["s3_report_url"] = None #if no s3 file name is located it sets to none
        return items
    except Exception as e:
        logger.error("Error retrieving data from DynamoDB: %s", e)
        return []
