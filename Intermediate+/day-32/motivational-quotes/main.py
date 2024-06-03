import datetime as dt
import random

import os.path
import base64
from email.message import EmailMessage
from dotenv import load_dotenv  # Library to load ENV VARS from a '.env' file

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

# Load environment variables from .env file
load_dotenv()


def get_credentials():
    """Get the user's credentials, or prompt them to log in if not available/valid."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def send_email(creds, quote):
    """Create and send an email message."""
    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content(quote)

        # Using ENV VARS from .env file
        message["To"] = os.environ.get("EMAIL_TO")
        message["From"] = os.environ.get("EMAIL_FROM")
        message["Subject"] = "Motivational Quote of the Day"

        # Encode the message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}

        # Send the message
        send_message = service.users().messages().send(userId="me", body=create_message).execute()
        print(f'Message Id: {send_message["id"]}')

        # Return the result of the send operation
        return send_message

    except HttpError as error:
        print(f"An error occurred: {error}")

        # Return None to indicate an error
        return None


def get_random_quote():
    with open("quotes.txt") as file:
        quotes = file.readlines()

    return random.choice(quotes)


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:    # 0 is Monday --- 6 is Sunday
    quote_of_the_day = get_random_quote()
    credential = get_credentials()
    result = send_email(credential, quote_of_the_day)

    # Optionally, do something with the result
    if result:
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
