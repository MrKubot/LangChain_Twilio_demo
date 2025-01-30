from django.urls import path
from . import views

urlpatterns = [
    path('send/<int:employee_id>/<str:message_body>', views.send_notification, name='send_sms'),
]