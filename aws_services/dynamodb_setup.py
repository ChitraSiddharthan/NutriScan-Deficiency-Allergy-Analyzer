import logging
import boto3
"""dynamodb_setup file code below created dynamodb table programatically
helps in storing report files from the user dashboard"""
logger = logging.getLogger(__name__)
AWS_REGION = "us-east-1"
TABLE_NAME = "AllergyAnalysisHistory"
def create_dynamodb_table():
    """Create DynamoDB table for storing analysis history."""
    dynamodb = boto3.client("dynamodb", region_name=AWS_REGION) #create a dynamodb client
    #
    try: #get a list of existing table name
        existing_tables = dynamodb.list_tables()["TableNames"]
        if TABLE_NAME in existing_tables:
            logger.info(f"Table '{TABLE_NAME}' already exists.") #logs if the table exists
            return 
        response = dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{"AttributeName": "username", "KeyType": "HASH"}, #partition key (username)
                       {"AttributeName": "timestamp", "KeyType": "RANGE"}], #sort key (timestamp)
            AttributeDefinitions=[{"AttributeName": "username", "AttributeType": "S"},
                                  {"AttributeName": "timestamp", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5} 
        )
        #
        logger.info(f"Table '{TABLE_NAME}' creation in progress: {response}") #logs table creation
    except Exception as e:
        logger.error(f"Error creating table: {e}") #logs if any error occured
        #
if __name__ == "__main__":
    create_dynamodb_table() # Call the function to create the table if the script is run directly.
