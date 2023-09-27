from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'importance', ]
        widgets = { 
            'title': forms.TextInput(attrs={ 
            'class': 'form-control',
            'placeholder':'Write a task title' }),
            'description': forms.Textarea(attrs={ 
            'class': 'form-control',
            'placeholder':'Write a task description' }),
            'importance': forms.CheckboxInput(attrs={ 
            'class': 'form-check-input m-auto'}),
        }
