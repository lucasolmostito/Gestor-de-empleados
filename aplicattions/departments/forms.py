from django import forms
from django.forms.fields import EmailField

class AddDepartmentForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    adress = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=75)
    number = forms.CharField(max_length=12)
    image = forms.ImageField()
    department = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)
    
    