from django import forms
from .models import Student

class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'admitted_class', 'section', 'contact']