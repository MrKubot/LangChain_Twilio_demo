from django.shortcuts import get_object_or_404, render, redirect
from .services import send_sms
from .forms import NotificationForm
from .models import SMSLog
from employees.models import Employee
from LLMs.services import analyze_message

# Create your views here.


def send_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            message_body = form.cleaned_data['message']

            recipients_roles = analyze_message(message_body)
            recipients = Employee.objects.filter(role__in=recipients_roles)

            if not recipients.exists():
                recipients = Employee.objects.filter(role='MNGR')

            for employee in recipients:
                result = send_sms(employee.phone_number, message_body)
                SMSLog.objects.create(
                    employee=employee,
                    message=message_body,
                    status=result['status'],
                    twilio_sid=result.get('sid'),
                    error_message=result.get('error')
                )
            
            return render(request, 'notifications/send_result.html', {
                'message': message_body,
                'recipients': recipients,
                'roles': recipients_roles,
            })
    else:
        form = NotificationForm()
    
    return render(request, 'notifications/send_form.html', {'form': form})

