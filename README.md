# CPP_PROJECT : ALLERGY AND DEFICIENCY ANALYZER
This is a web-based application called "Allergy and Deficiency Analyzer".

# Description:
Motivation for this project - There are several disease accross the world, and many cannot afford large fees for their diagnosed medical issues.
This projects aims to build a gap between initial symptoms and professional diagnosis where patients/users can know beforehand what are their symptoms and why is it occuring, what are the recommendations.
This cloud-based application helps users to analyze their symptoms and provides possible conditions based upon their inputs.
This project is integrated using 6 AWS services, they are AWS Lambda, SNS, SQS, DynamoDB, S3 and Cloudwatch.
The Dashboard also displays the SQS queue message on the application to display users/developers how the SQS handles the message queue.
The UI of the Dashboard displays Home, Allergies, Deficiencies, Logout.
Home button provides dashboard for users to analyse their symptoms. 
Allergies and Deficiencies on the dashboard provides users to add, delete, update, read their added allergies and deficiencies on their profile.

# Features of this Project:
1. Authenticates user and manages the profile.<br />
2. Symtom-based analysis with recommendations<br />
3. Cloud based database and file storage using AWS.<br />
4. Notification alerts via AWS SNS.<br />
5. Secure message processing using AWS SQS.<br />
6. CI/CD pipeline with GitHub actions.<br />
7. Static Code Analysis using pylint.<br />
8. Custom Python library for Symptom analysis. <br />

# Technologies used are:
For Backend: <br />
    --Django, python <br />
For Cloud Services: <br />
    --AWS Cloudwatch, S3, DynamoDB, SNS, SQS, Lambda <br />
For CI/CD: <br />
    --GitHub Actions <br />
For Static Code Analysis: <br />
    --Pylint <br />
For Frontend: <br />
    --HTML, CSS <br />
Custom Library:
    I have created a custom library to handle the data for analysis when a user provides the symptoms on the dashboard. <br />
    In the Directory named lambda_package/symptom_analysis  - <br /> 
    a. data.py : This file has limited data to map the symptoms, conditions and recommedations to the user  <br />
    b. analyzer.py: This file has the logic behind analysing the symptom and medical history from the dashboard <br />
    Published in pypi: <br />
    https://pypi.org/project/symptom-analysis/1.0.2/  <br />

# This Project is Deployed in AWS using Elastic Beanstalk:
    http://allergyanalyzersystem-env.eba-eyus5yb4.us-east-1.elasticbeanstalk.com/

# About AWS services used in this project and reason for them:
# 1. AWS Elastic Beanstalk:
purpose:<br />
Elastic beanstalk simplifies the scaling, management and deployment of web applications.<br />
Why was it used: <br />
a. Easy deployment <br />
b. Built-in Monitoring facility.

# 2. AWS Simple Notification Service (SNS):

purpose:<br />
SNS is a messaging service providing facility to alert users via email/SMS.<br />
<br />
why was this used:<br />
It provides easy subscription.<br />
Messages are reliable.<br />
Real-time Alerts to users.<br />
<br />
# 3. AWS Simple Queue Service (SQS)

purpose:<br />
SQS is a queuing system used to handle the processing of messages.<br />
<br />
why was this used:<br />
Ensures asynchronous processing like when users enter symptoms the analysis requests are queued.<br />
Preventing overloading of messages.<br />
Reliable delivery of message processing.<br />

# 4. AWS DynamoDB<br />

purpose:<br />
DynamoDB is a NoSQL database for storing user data and their symptom history.<br />
<br />
why was this used:<br />
a. Scalability - Scales automatically based on the loads.<br />
b. High availability as data is being replicated across many AWS regions.<br />
c. No need for the database management<br />

# 5. S3 (Simple Storage Service)

purpose:<br />
S3 provides storage facilities in AWS for files generated from the analysis on the dashboard.<br />

# Setup Instructions: (Cloud9 is used for this project)

# 1. Clone the repository:

git clone https://github.com/Yashashwini0310/cpp_project.git<br />
cd allergy-analyzer<br />

# 2. Create a virtual environment and install the dependencies:

python -m venv env<br />
source env/bin/activate (linux based project)<br />
pip install -r requirements.txt<br />
<br />
# 3. If using Learners lab, check if these AWS are accessible and setup AWS credentials using boto3 accordingly
<br />
# 4. Run the application locally first:
<br />
python manage.py migrate<br />
python manage.py runserver 8080<br />
<br />
# 5. Lastly, Deploy to Elastic Beantalk:
<br />
(deactivate the virtual environment and then perform below steps)
a. install awsebcli : pip install awsebcli<br />
<br />
b. Helps in initializing the eb from terminal, you can provide any name of your choice, as this creates the function on AWS<br />
eb init -p python-<version> <function_name> <br />
<for example: eb init -p python-3.9 AllergyAnalyzer><br />
<br />
c. Helps in deploying the environment created<br />
eb deploy or use eb deploy AllergyAnalyzer-env<br />
<br />
d. you can open your deployed AWS domain of your project using below command<br />
eb open<br />
<br />
# For testing
Run tests Locally:<br />
python3 manage.py test <br />
<br />
Run Pylint for Static Code Analysis locally<br />
if your root folder is Allergy_Analyzer:<br />
pylint Allergy_Analyzer<br />
if you want to run for each folder use: <br />
pylint user_management/ <br />
<br />
# How to use: 
1. Register/login the application<br />
2. Enter Symtoms (example: Fever, headache, fatigue, chest pain, cough) <br />
   Enter your Medical history if available (eg. diabetes, Heart Disease, Hypertension, Asthma) <br />
   Get your report on possible results (deficiencies/allergy)<br />
3. Subscribe to SNS alerts for notifications.<br />
4. Accept the request on your mail. <br />
5. You will be notified everytime your symptoms are entered<br />
6. you can also view SQS queue in the application.<br />
<br />
# Please Note 
This project has manual datasets provided for the analysis. Hence the medical history is limited, you can provide above example medical history for testing.<br />
<br />
# Known Issues and future Enhancements:
--Expand medical history database for better recommendations.<br />
--Enhance UI for more user experience<br />
--Add more AWS security measures.<br />
--Enhance the analyzer by adding robust API for more accurate results.<br />
<br />
<br />
# Author : Yashashwini
# linkedIn : https://www.linkedin.com/in/yashashwini-s-485283190/ 

# Home Page, Login Page, Subscribe, allergy and deficieny ribbon. 
![image](https://github.com/user-attachments/assets/88c72963-1ab7-468f-9816-c0f5df7a9e5f)

![image](https://github.com/user-attachments/assets/8e4254fd-6888-4db4-9684-55c2b780d248)

# Dashboard before and after entering symptoms
![image](https://github.com/user-attachments/assets/0a23fd74-6e99-4bff-a09a-13d8ff2ebc17)

![image](https://github.com/user-attachments/assets/8a384812-4b0d-4493-8b0c-1e43e72e22e9)

# Subscribe to news page
![image](https://github.com/user-attachments/assets/308df69b-e7c6-4d5f-8e1c-440c09b8843e)

# Deficiency and Allergy Page
![image](https://github.com/user-attachments/assets/f84e303d-7012-402e-aebe-dee476726bf8)

![image](https://github.com/user-attachments/assets/831da49b-9b2a-42b1-9161-a5d397c4dc6b)





