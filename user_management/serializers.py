"""Serializers to convert the data to JSON"""
from rest_framework import serializers
from .models import UserProfile, Allergy, Deficiency
#This serializer is used to convert UserProfile model instances into JSON
class UserProfileSerializer(serializers.ModelSerializer):
    """This serializer is used to convert UserProfile model instances into JSON """
    class Meta:
        model = UserProfile
        fields = ['user', 'symptoms', 'medical_history']
#This serializer is used to convert Allergy model instances into JSON
class AllergySerializer(serializers.ModelSerializer):
    """This serializer is used to convert Allergy model instances into JSON"""
    class Meta:
        model = Allergy
        fields = '__all__'
#This serializer is used to convert Deficiency model instances into JSON
class DeficiencySerializer(serializers.ModelSerializer):
    """This serializer is used to convert Deficiency model instances into JSON"""
    class Meta:
        model = Deficiency
        fields = '__all__'
