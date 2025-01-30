from django.db import models
from employees.models import Employee

# Create your models here.

class SMSLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField()
    twilio_sid = models.CharField(max_length=34, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'SMS to {self.employee} - {self.status}'