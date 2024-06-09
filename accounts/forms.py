from attr import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.contrib.auth import get_user_model

class UserForm(forms.ModelForm):
  class Meta:
    model = get_user_model()
    fields = ['username', 'first_name', 'last_name', 'email', 'is_faculty']

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = get_user_model()
    fields = ['username', 'first_name', 'last_name', 'email', 'is_faculty']
    
  # Validate if the email ends with @du.ac.bd
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if (not email.endswith('@du.ac.bd')) and (not email.endswith('@rme.du.ac.bd')):
      raise forms.ValidationError('Email must be a DU email [@du.ac.bd or @rme.du.ac.bd]')
    return email

class FacultyProfileForm(forms.ModelForm):
  class Meta:
    model = get_user_model()
    fields = ['first_name', 'last_name','department', 'designation', 'university', 'education', 'experience', 'research_activities', 'membership', 'publication', 'award', 'contact', 'scholar_link', 'image', 'github_link', 'linkedin_link']
    
class StudentProfileForm(forms.ModelForm):
  class Meta:
    model = get_user_model()
    fields = ['first_name', 'last_name','department', 'university', 'education', 'experience', 'research_activities', 'membership', 'publication', 'award', 'contact', 'scholar_link', 'image', 'github_link', 'linkedin_link']