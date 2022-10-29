from main.models import *
from django.forms import ModelForm
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class MarkForm(ModelForm):
    class Meta:
        model = Mark
        fields = ['points', 'created', 'discipline', 'teacher', 'student']

        widgets = {
            'created': DateInput()
        }