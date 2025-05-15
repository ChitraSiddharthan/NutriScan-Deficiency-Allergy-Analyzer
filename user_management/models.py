""" Models file for userprofile, allergy and deficiency"""
from django.contrib.auth.models import User
from django.db import models
class UserProfile(models.Model):
    """
    extends the built-in User model with additional user specific information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE) #one to one relationship
    symptoms = models.TextField(blank=True, null=True)  # Store symptoms can be blank or null
    severity_level = models.IntegerField(blank=True, null=True) # Store severity can be blank/null
    medical_history = models.TextField(blank=True, null=True)  # Store medical history
    report_url = models.CharField(max_length=255, blank=True, null=True) #for s3 url
    def __str__(self):
        return self.user.username #returns the username for string representation
class Allergy(models.Model):
    """
    model representing allergies
    """
    name = models.CharField(max_length=100, unique=True) #allergy name is set to unique
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
class Deficiency(models.Model):
    """
    model representing deficiency
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
