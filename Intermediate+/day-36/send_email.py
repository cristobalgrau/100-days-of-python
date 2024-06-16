import os
import base64
from email.message import EmailMessage
from dotenv import load_dotenv  # Library to load ENV VARS from a '.env' file

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GmailSender:
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        self.credentials = self.get_credentials()
        self.service = build("gmail", "v1", credentials=self.get_credentials())
        self.email_from = os.environ.get("EMAIL_FROM")

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
            return send_message

        except HttpError as error:
            print(f"An error occurred: {error}")
            # Return None to indicate an error
            return None
