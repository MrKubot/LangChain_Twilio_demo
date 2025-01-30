from django.conf import settings
from twilio.rest import Client

def get_twilio_client():
    return Client(
        settings.TWILIO['ACCOUNT_SID'],
        settings.TWILIO['AUTH_TOKEN']
    )