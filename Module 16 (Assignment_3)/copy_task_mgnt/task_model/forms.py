from django import forms
from .models import Task
from django.forms.widgets import NumberInput

class TaskForm(forms.ModelForm):
    assign_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Task
        fields = '__all__'