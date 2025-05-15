"""Test file to test if the dashboard is retrieving the data and analysing the condition,
also by sending sqs and sns
"""
import django
import os
from django.test import TestCase, Client
from django.contrib.auth.models import User
from unittest.mock import patch
from user_management.models import UserProfile
os.environ['DJANGO_SETTINGS_MODULE'] = 'allergy_analyzer.settings'
django.setup()
class DashboardViewTest(TestCase):
    """runs tests by creating a testuser, sending sns, analyzing symptom"""
    def setUp(self):
        """testuser client is created for testing"""
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.user_profile = UserProfile.objects.create(user=self.user)
    def test_dashboard_get_request(self):
        """Test if dashboard loads correctly with GET request"""
        response = self.client.get("/api/dashboard/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_management/dashboard.html")

    @patch("user_management.views.invoke_lambda")
    def test_dashboard_post_request(self, mock_invoke_lambda):
        """Test dashboard POST request with symptom input"""
        mock_invoke_lambda.return_value = {
            "conditions": ["Allergy"],
            "severity": "Moderate",
            "recommendation": ["Take antihistamines"]
        }
        response = self.client.post("/api/dashboard/", {
            "symptoms": "sneezing, cough",
            "medical_history": "asthma"
        })
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        mock_invoke_lambda.assert_called_once()  # Check if the Lambda function was called
        self.assertContains(response, "Allergy")  # Check if the response contains the expec cond