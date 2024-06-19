import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_phone = os.environ.get('TWILIO_PHONE_NUM')
    receiver_phone = os.environ.get('RECEIVER_PHONE_NUM')

    def __init__(self) -> None:
        self.client = Client(self.account_sid, self.auth_token)
    
    def send_sms(self, message_body):
        message = self.client.messages.create(body=message_body, from_=self.twilio_phone,  to=self.receiver_phone)
        print(message.status)
