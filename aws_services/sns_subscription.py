import boto3
import logging

AWS_REGION = "us-east-1"
SNS_TOPIC_NAME = "SymptomAlertsTopic"

sns_client = boto3.client("sns", region_name=AWS_REGION)
logger = logging.getLogger(__name__)

def get_sns_topic_arn():
    """Retrieve SNS topic ARN."""
    try:
        response = sns_client.list_topics()
        for topic in response.get("Topics", []):
            if SNS_TOPIC_NAME in topic["TopicArn"]:
                return topic["TopicArn"]
    except Exception as e:
        logger.error(f"Error fetching SNS Topic ARN: {e}")
    return None

def subscribe_user(email=None, phone=None):
    """Subscribe a user to the SNS topic via email and/or phone."""
    topic_arn = get_sns_topic_arn()
    if not topic_arn:
        logger.error("SNS Topic not found!")
        return False

    if email:
        try:
            sns_client.subscribe(
                TopicArn=topic_arn,
                Protocol="email",
                Endpoint=email  # User's Email
            )
            logger.info(f"Subscription request sent to {email}. Check your email to confirm!")
        except Exception as e:
            logger.error(f"Error subscribing email: {email}, Error: {e}")

    if phone:
        try:
            sns_client.subscribe(
                TopicArn=topic_arn,
                Protocol="sms",
                Endpoint=phone  # User's Phone Number
            )
            logger.info(f"SMS Subscription request sent to {phone}.")
        except Exception as e:
            logger.error(f"Error subscribing phone: {phone}, Error: {e}")

    return True
