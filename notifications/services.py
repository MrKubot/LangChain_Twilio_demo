from .twilio_clients import get_twilio_client
from django.conf import settings


def send_sms(to_number, message_body):
    client = get_twilio_client()

    try:
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO['PHONE_NUMBER'],
            to=to_number
        )
        return {
            'status': 'success',
            'sid': message.sid,
            'error': None
        }
    except Exception as e:
        return{
            'status': 'error',
            'sid': None,
            'error': str(e)
        }

