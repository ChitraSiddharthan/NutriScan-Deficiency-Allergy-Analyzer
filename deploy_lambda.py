"""
File to deploy the lambda code to aws programatically
"""
import boto3
LAMBDA_NAME = "SymptomAnalysisLambda"
ROLE_ARN = "arn:aws:iam::091200948475:role/LabRole"
lambda_client = boto3.client("lambda", region_name="us-east-1")
def deploy_lambda():
    """deploys lambda zip file to aws """
    # Read the ZIP file
    with open("lambda_function.zip", "rb") as f:
        zip_content = f.read()
    try:
        # Attempt to update the function code
        response = lambda_client.update_function_code(
            FunctionName=LAMBDA_NAME,
            ZipFile=zip_content,
            Publish=True  # Publish a new version.
        )
        print(f"Lambda {LAMBDA_NAME} code updated successfully!")
        print(response)
        # Update the configuration.
        response = lambda_client.update_function_configuration(
            FunctionName=LAMBDA_NAME,
            Role=ROLE_ARN,
            Handler="lambda_function.lambda_handler",
            Runtime="python3.9",
            Timeout=10,
            MemorySize=128,
        )
        print(f"Lambda {LAMBDA_NAME} configuration updated successfully!")
        print(response)
    except lambda_client.exceptions.ResourceNotFoundException:
        print(f"Lambda function '{LAMBDA_NAME}' does not exist. Creating...")
        # Create the Lambda function
        response = lambda_client.create_function(
            FunctionName=LAMBDA_NAME,
            Runtime="python3.9",
            Role=ROLE_ARN,
            Handler="lambda_function.lambda_handler",
            Code={"ZipFile": zip_content},
            Timeout=10,
            MemorySize=128,
        )
        print(f"Lambda {LAMBDA_NAME} created successfully!")
        print(response)

    except Exception as e:
        print(f"Error deploying Lambda function: {e}")
if __name__ == "__main__":
    deploy_lambda()