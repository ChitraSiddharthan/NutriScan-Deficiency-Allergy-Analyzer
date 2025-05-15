"""
Form for user registration
"""
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Allergy, Deficiency
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    symptoms = forms.CharField(widget=forms.Textarea(), required=False)
    medical_history = forms.CharField(widget=forms.Textarea(), required=False)
    class Meta:
        model = User #uses the built-in user model
        fields = ['username', 'email', 'password'] #fields for the project
    def save(self, commit=True):
        """
        This is a custom save method to handle password hashing and userprofile creation
        """
        user = super().save(commit=False) #creates user instance but doesn't save it yet
        user.set_password(self.cleaned_data['password']) #hashes the password
        if commit:
            user.save() #here it saves the user instance
            # UserProfile is created or updated with the symptoms later in views.py
            UserProfile.objects.create( #creates userprofile instance
                user=user,
                symptoms=self.cleaned_data['symptoms'],
                medical_history=self.cleaned_data['medical_history']  # Saves medical history
            )
        return user
class UserLoginForm(forms.Form):
    """
    form for user login
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput()) #masks the password field
class UserProfileForm(forms.ModelForm):
    """
    form for updating user profile (symptoms and medical history)
    """
    class Meta:
        model = UserProfile
        fields = ['symptoms', 'medical_history'] #fields in userprofile form
class AllergyForm(forms.ModelForm):
    """
    form for creating/updating allergy info
    """
    class Meta:
        model = Allergy
        fields = ['name', 'description'] #fields in allergy form
class DeficiencyForm(forms.ModelForm):
    """
    form for creating/updating deficiency info
    """
    class Meta:
        model = Deficiency
        fields = ['name', 'description']#fields in deficiency form
