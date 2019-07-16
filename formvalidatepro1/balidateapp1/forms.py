from django import forms
from balidateapp1.models import Employee



class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"