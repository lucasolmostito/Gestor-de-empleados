from django import forms
from django.db.models.enums import Choices
from django.forms.fields import EmailField
from .models import Employees


class EmployeesForm(forms.ModelForm):
    """Form definition for Employees."""

    class Meta:
        """Meta definition for Employeesform."""

        model = Employees
        fields = (
            'name',
            'surname',
            'adress',
            'number',
            'email',
            'job',
            'department',
            'image',
            'skills',
        )
        
        widgets = {
            'skills': forms.CheckboxSelectMultiple()
        }

    