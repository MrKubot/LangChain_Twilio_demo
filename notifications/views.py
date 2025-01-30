from django.shortcuts import get_object_or_404, render, redirect
from .services import send_sms
from .forms import NotificationForm
from .models import SMSLog

# Create your views here.


def send_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            recipients = form.cleaned_data['recipients']
            message_body = form.cleaned_data['message']

            for employee in recipients:
                result = send_sms(employee.phone_number, message_body)
                SMSLog.objects.create(
                    employee=employee,
                    message=message_body,
                    status=result['status'],
                    twilio_sid=result.get('sid'),
                    error_message=result.get('error')
                )
            
            return redirect('send_notifications')
    else:
        form = NotificationForm()
    
    return render(request, 'notifications/send_form.html', {'form': form})

