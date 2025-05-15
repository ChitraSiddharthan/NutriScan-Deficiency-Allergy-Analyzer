"""SQS handler file to log errors and send the messages to the user through webpage"""
import json
import logging
import boto3
logger = logging.getLogger(__name__)
AWS_REGION = "us-east-1"
SQS_QUEUE_NAME = "SymptomAlertsQueue"
#
sqs_client = boto3.client("sqs", region_name=AWS_REGION)
#
def get_sqs_queue_url():
    """Fetch the SQS queue URL with error handling."""
    try:
        response = sqs_client.get_queue_url(QueueName=SQS_QUEUE_NAME)
        return response["QueueUrl"]
    except Exception as e:
        logger.error("Error fetching SQS queue URL: %s", e) # Log the error
        return None
#
def send_message_to_sqs(message_body):
    """Sends a message to the SQS queue, handling queue URL errors."""
    queue_url = get_sqs_queue_url()
    if not queue_url: # Check if queue_url is None (error occurred in get_sqs_queue_url)
        logger.error("Cannot send message to SQS because queue URL is None.")
        return False # Indicate failure to send message
    try:
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message_body)
        )
        print(f"Message sent to SQS: {response['MessageId']}")
        return True # Indicate successful message sending
    except Exception as e:
        logger.error("Error sending message to SQS: %s", e)
        return False # Indicate failure to send message
#
def receive_sqs_messages():
    """Retrieve messages from SQS with error handling."""
    messages_list = [] # Initialize list to return even if errors occur
    try:
        queue_url = get_sqs_queue_url() # Get queue URL
        if not queue_url: # Checks if get_sqs_queue_url returned None (error)
            logger.error("SQS queue URL is None, cannot proceed to receive messages.")
            # Returns user-friendly error
            return ["Error: Could not retrieve system messages. Queue URL not found."]
        response = sqs_client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=5,
            WaitTimeSeconds=10
        )
        # Safely accessess in case 'Messages' key was missing
        messages_data = response.get("Messages", [])
        for msg_data in messages_data:
            #Inner try-except for processing each message
            #to prevent one bad message from stopping all
            try:
                message_body = msg_data['Body'] # Extract message body
                parsed_body = json.loads(message_body)  # Parsing JSON here
                messages_list.append(parsed_body) # Addding to list
                print(f"Received and Processed SQS Message: {parsed_body}") # Log processing
            # Delete the message after successful processing
                sqs_client.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=msg_data["ReceiptHandle"]
                )
                # Log deletion
                print(f"Deleted SQS Message with ReceiptHandle: {msg_data['ReceiptHandle']}")
            except json.JSONDecodeError:
                logger.error(f"Error decoding, ReceiptHandle: {msg_data.get('ReceiptHandle', 'N/A')}", exc_info=True)
                messages_list.append({"error": "Invalid JSON message received."})
            except Exception as processing_error:
                # Log error for individual message processing
                logger.error(f"Error processing SQS message: {processing_error}, ReceiptHandle: {msg_data.get('ReceiptHandle', 'N/A')}", exc_info=True)
                messages_list.append({"error": "Error processing message."})
    except Exception as e:
        logger.error("Error retrieving or processing SQS messages: %s", e) # Log detailed error
        # User-friendly error message to display on dashboard
        messages_list = ["Error retrieving system messages. Please check logs."]
# Return the list of messages (could be empty or contain error message in case of failure)
    return messages_list
if __name__ == "__main__":
    receive_sqs_messages()
