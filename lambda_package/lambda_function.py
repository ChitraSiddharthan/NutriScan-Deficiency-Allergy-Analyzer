"""This lambda function is used to handle it programatically
"""
import json
from symptom_analysis.analyzer import analyze_symptoms  # Import the function
def lambda_handler(event):
    """serverless lambda function handling symptom analysis"""
    try:
        body = json.loads(event.get("body", "{}"))
        symptoms = body.get("symptoms", [])
        medical_history = body.get("medical_history", [])

        if not symptoms:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No symptoms provided"})
            }

        result = analyze_symptoms(symptoms, medical_history)

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
