from django import forms
from employees.models import Employee


class NotificationForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4
        }),
        label='Treść wiadomości',
        max_length=500,
    )