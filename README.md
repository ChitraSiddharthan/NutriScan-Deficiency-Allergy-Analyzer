# 🧬 NutriScan: Allergy & Deficiency Analyzer

NutriScan is a cloud-based web application designed to help users analyze their symptoms and identify potential nutritional deficiencies and allergies. Built using Django and integrated with multiple AWS services, NutriScan bridges the gap between early symptom awareness and professional diagnosis by offering personalized insights and recommendations.

---

## 📖 Description

In many parts of the world, access to affordable healthcare is a challenge. NutriScan aims to provide an initial layer of health awareness by allowing users to input symptoms and receive meaningful insights about possible causes — such as allergies or deficiencies — and what steps to take next.

This project is deployed using **AWS Elastic Beanstalk** and integrates six major AWS services: **Lambda**, **SNS**, **SQS**, **DynamoDB**, **S3**, and **CloudWatch**.

Key highlights:
- Analyze symptoms with a custom-built Python library
- Cloud-native infrastructure for scalability and availability
- Real-time notifications and message queuing
- Dashboard UI for symptom entry, history tracking, and AWS service visualization

---

## 🚀 Features

1. User authentication and profile management  
2. Symptom-based analysis with dietary/medical recommendations  
3. Cloud-based database and storage (DynamoDB, S3)  
4. Notification alerts via AWS SNS  
5. Asynchronous processing using AWS SQS  
6. CI/CD pipeline with GitHub Actions  
7. Static code analysis with pylint  
8. Custom Python library for symptom analysis  

---

## 🛠️ Technologies Used

**Backend**  
- Django (Python)

**Frontend**  
- HTML, CSS

**Cloud Services (AWS)**  
- Elastic Beanstalk  
- Lambda  
- SNS  
- SQS  
- DynamoDB  
- S3  
- CloudWatch  

**CI/CD**  
- GitHub Actions

**Static Code Analysis**  
- Pylint

---

## 🧠 Custom Python Library

A dedicated library for analyzing user symptoms:

📦 `lambda_package/symptom_analysis/`  
- `data.py`: Contains symptom-to-condition mapping and recommendations  
- `analyzer.py`: Logic for processing symptom inputs and generating results  

🔗 Published on PyPI:  
[https://pypi.org/project/symptom-analysis/1.0.2/](https://pypi.org/project/symptom-analysis/1.0.2/)

---

## 🌐 Deployment

Deployed on **AWS Elastic Beanstalk**:  
🔗 [Live Application](http://allergyanalyzersystem-env.eba-eyus5yb4.us-east-1.elasticbeanstalk.com/)

---

## 📦 AWS Services Explained

### 1. Elastic Beanstalk
Simplifies deployment, scaling, and monitoring of the web app.
- Easy to deploy and manage
- Built-in monitoring and logging

### 2. SNS (Simple Notification Service)
Used for sending real-time alerts to users via email/SMS.

### 3. SQS (Simple Queue Service)
Ensures reliable, asynchronous message processing for symptom analysis requests.

### 4. DynamoDB
NoSQL database to store user data, symptom history, and recommendations.

### 5. S3 (Simple Storage Service)
Stores files generated from the analysis and UI interactions.

### 6. CloudWatch
Monitors logs and application performance metrics.

---

## ⚙️ Setup Instructions

### Prerequisites:
- Python 3.x
- AWS CLI & credentials set up (for AWS services)
- Cloud9 or local environment

### Local Development

```bash
# Clone the repository
git clone https://github.com/Yashashwini0310/cpp_project.git
cd allergy-analyzer

# Create virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start the server
python manage.py runserver 8080
