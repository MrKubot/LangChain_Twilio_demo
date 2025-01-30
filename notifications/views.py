from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .services import send_sms
from employees.models import Employee
from .models import SMSLog

# Create your views here.


def send_notification(request, employee_id, message_body):
    employee = get_object_or_404(Employee, id=employee_id)
    result = send_sms(employee.phone_number, message_body)

    SMSLog.objects.create(
        employee=employee,
        message=message_body,
        status=result['status'],
        twilio_sid=result.get('sid'),
        error_message=result.get('error')
    )

    return JsonResponse(result)

