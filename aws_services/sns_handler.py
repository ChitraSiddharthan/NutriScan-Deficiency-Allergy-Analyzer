""" SNS handler to get and send messages to alert the user """
import boto3
import random

AWS_REGION = "us-east-1"
SNS_TOPIC_NAME = "SymptomAlertsTopic"
sns_client = boto3.client("sns", region_name=AWS_REGION) #create sns client
def get_sns_topic_arn():
    """Retrieve SNS topic ARN."""
    response = sns_client.list_topics() #list all sns topics
    for topic in response.get("Topics", []): #iterate through the list of topics
        if SNS_TOPIC_NAME in topic["TopicArn"]: #checks if the topic name is in the arn
            return topic["TopicArn"] #returns if found
    return None #returns none if not found

def send_sns_alert():
    """Send health news"""
    topic_arn = get_sns_topic_arn() #gets the topicarn
    if not topic_arn: #checks if arn was found
        print("SNS Topic not found!") #prints error if not found
        return

    health_tips = [
        "📰 Health Tip: Exercise for 30 minutes daily to improve heart health!",
        "📰 Nutrition Fact: Eating more fiber reduces cholesterol levels.",
        "📰 Wellness Tip: Get at least 7-8 hours of sleep for better mental health.",
        "📰 Fun Fact: Dark chocolate can help lower blood pressure!",
        "😁Regular Health checkup reduces the need to spend money later",
        "😒Go out for walk, to help your fitness journey",
        "👌4 liters of water can do many wonders to a human body. Try it today",
    ]
    
    news_message = random.choice(health_tips) #picks random message

    #publishes the message to the SNS topic
    response = sns_client.publish(TopicArn=topic_arn, Message=news_message)
    print(f"Sent SNS Alert: {news_message}") #prints message saying the allert was sent

if __name__ == "__main__":
    send_sns_alert()
