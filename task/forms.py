from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Task


class TaskForm(forms.ModelForm):
    status = forms.ChoiceField(
        label='Status', choices=[('Normal', 'Normal'), ('Important', 'Important')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    work_hour = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Task
        fields = ['work_hour', 'status', 'title', 'memo']
        widgets = {
            # 'user_id': forms.Select(attrs={'class': 'form-control'}),
            # 'work_hour': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'task': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'memo': forms.Textarea(attrs={'class': 'form-control'}),
        }
