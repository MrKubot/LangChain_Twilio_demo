from django import forms
from employees.models import Employee


class NotificationForm(forms.Form):
    recipients = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Odbiorcy',
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4
        }),
        label='Treść wiadomości',
        max_length=500,
    )