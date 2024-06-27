from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['work_hour', 'task', 'status', 'title', 'memo']
        widgets = {
            # 'user_id': forms.Select(attrs={'class': 'form-control'}),
            'work_hour': forms.NumberInput(attrs={'class': 'form-control'}),
            'task': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'memo': forms.Textarea(attrs={'class': 'form-control'}),
        }