from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name_arabic', 'full_name_english', 'phone_number', 'email', 'university', 'department', 'city', 'region', 'agree_to_terms']
