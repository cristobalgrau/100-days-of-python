import datetime as dt
import csv
import random
import os

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


def send_email(creds, text, email_to):
    """Create and send an email message."""
    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content(text)

        # Using ENV VARS from .env file
        message["To"] = email_to
        message["From"] = os.environ.get("EMAIL_FROM")
        message["Subject"] = "Happy Birthday"

        # Encode the message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}

        # Send the message
        send_message = service.users().messages().send(userId="me", body=create_message).execute()
        # print(f'Message Id: {send_message["id"]}')

        # Return the result of the send operation
        return send_message

    except HttpError as error:
        print(f"An error occurred: {error}")

        # Return None to indicate an error
        return None


def check_birthdays():
    with open("birthdays.csv", newline='') as birthdays:
        data = csv.DictReader(birthdays)
        birthdays_data = {}
        for row in data:
            if int(row["month"]) == month and int(row["day"]) == day:
                birthdays_data[row["name"]] = row["email"]

    return birthdays_data


def pick_birthday_template(name_for_template):
    # List all files in the folder
    files = os.listdir("./letter_templates")

    # Randomly select one of the text files
    random_file = random.choice(files)
    selected_file_path = f"./letter_templates/{random_file}"

    with open(selected_file_path, "r") as file:
        template_letter = file.read()
    birthday_letter = template_letter.replace("[NAME]", name_for_template)

    return birthday_letter


today = dt.datetime.now()
month = today.month
day = today.day

print(f"Looking for birthdays for: {month}/{day}")

today_birthdays = check_birthdays()
if today_birthdays:
    for name, email in today_birthdays.items():
        letter = pick_birthday_template(name)
        credential = get_credentials()
        result = send_email(credential, letter, email)

        # Optionally, do something with the result
        if result:
            print(f"Email sent successfully to {name} -> {email}!")
        else:
            print(f"Failed to send email to {name}.")

else:
    print("There is no Birthdays for today")
