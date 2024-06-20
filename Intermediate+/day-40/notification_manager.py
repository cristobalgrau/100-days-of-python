import os
from dotenv import load_dotenv
from twilio.rest import Client

import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_phone = os.environ.get('TWILIO_PHONE_NUM')
    receiver_phone = os.environ.get('RECEIVER_PHONE_NUM')

    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

    def __init__(self) -> None:
        self.client = Client(self.account_sid, self.auth_token)
        self.credentials = self.get_credentials()
        self.service = build("gmail", "v1", credentials=self.credentials)
        self.email_from = os.environ.get("EMAIL_FROM")
    
    def send_sms(self, message_body):
        message = self.client.messages.create(body=message_body, from_=self.twilio_phone,  to=self.receiver_phone)
        print(message.status)

    def get_credentials(self):
        """Get the user's credentials, or prompt them to log in if not available/valid."""
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        return creds

    def send_email(self, email_to, subject, text):
        """Create and send an email message."""
        try:
            message = EmailMessage()
            message.set_content(text)

            # Using ENV VARS from .env file
            message["To"] = email_to
            message["From"] = self.email_from
            message["Subject"] = subject

            # Encode the message
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            create_message = {"raw": encoded_message}

            # Send the message
            send_message = self.service.users().messages().send(userId="me", body=create_message).execute()

            # Return the result of the send operation
            # return send_message

        except HttpError as error:
            print(f"An error occurred: {error}")
            # Return None to indicate an error
            return None

    def send_offers_email(self, email_list, subject, text):
        for user in email_list:
            user_email = user["whatIsYourEmail?"]
            self.send_email(user_email, subject, text)

