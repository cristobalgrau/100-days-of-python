# Day 32 - Send Email (smtplib) & Manage Dates (datetime)

This day we made 2 projects, the first one to Send Motivational Quotes on a specific day of the week by email, and the second one to automate a Birthday wisher to send emails on your friend's birthday.

To perform the option that Python sends emails, in my case with Gmail, Google made some updates on its User Account GUI. They discontinued the option to create the App Password.
Now you have to use the OAuth 2.0 version instead.

OAuth 2.0 is a more secure, modern authorization protocol that replaces the need for application passwords. 
Allow apps to access your Gmail data with your explicit consent, without having to share your password.

You can follow the steps according to their [Python quickstart documentation](https://developers.google.com/gmail/api/quickstart/python?hl=en)

After you follow the procedure you will download a `.json` file with the Gmail credentials, you have to rename it as `credentials.json` and store it in the root of your project folder.

## Project #1: Send Motivational Quotes on a weekday via Email

The Motivational Quotes app is designed to send a random motivational quote via email every Monday. This application uses Google APIs to send emails and `dotenv` to manage environment variables securely.

### Key Features:

- **Random Quote Selection**: Reads and selects a random quote from a text file.
- **Automated Email Sending**: Sends the selected quote via email using Gmail API.
- **Credential Management**: Handles user credentials securely for accessing Gmail API.
- **Scheduled Execution**: Runs the quote-sending function every Monday.

### Libraries:

- `datetime`: Used to get the current date and time to determine the day of the week.
- `random`: Utilized to randomly select a quote from a list.
- `os.path`: Used for manipulating and working with file paths, in this case, to verify if `token.json` exists.
- `base64`: Encodes email messages in base64 format for sending through Gmail API.
- `dotenv`: Loads environment variables from a `.env` file.
- `google.auth`: Manages authentication and authorization.
- `google.auth.transport.requests`: Provides the Request class for refreshing credentials.
- `google.oauth2.credentials`: Manages OAuth 2.0 credentials.
- `google_auth_oauthlib.flow`: Handles the OAuth 2.0 flow.
- `googleapiclient.discovery`: Builds and interacts with Google APIs.
- `googleapiclient.errors`: Handles errors related to Google API interactions.

### Implementation:

The Motivational Quotes app is implemented using the following functions and structure:

**Getting Credentials**:

The `get_credentials` function manages user credentials for accessing Gmail API. It checks for existing credentials, refreshes them if expired or prompts the user to log in if no valid credentials are found. The credentials are saved in `token.json` file.

**Sending Email**:

The `send_email` function composes and sends an email using the Gmail API. It uses environment variables (ENV VARS) for the sender and recipient email addresses, in this way you don't have to hard code the emails. To use the ENV VARS you need to create the file `.env` and inside the file write down your ENV VARS, and to call them inside the code you have to import the library `dotenv` and use the code `os.environ.get()` to get the ENV VARS values.

```python
message["To"] = os.environ.get("EMAIL_TO")
message["From"] = os.environ.get("EMAIL_FROM")
```

**Selecting a Random Quote**:

The `get_random_quote` function reads quotes from a text file, stores them in the variable as a list using the method `readlines()`, and selects one randomly using the random method `choice()`.

**Main execution**:

The main part of the script checks if the current day is Monday and, if so, it will call the respective functions and send the motivational quote email.

### Result: 

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/37acaf3c-023a-4c0b-bfae-5a8e13ac4654)



## Project # 2: Automated Birthday Wisher

The Automated Birthday Wisher is an application designed to send personalized birthday wishes via email to individuals whose birthdays match the current date. 

### Key Features:

- **Birthday Checking**: Reads a CSV file to find individuals whose birthdays match the current date.
- **Personalized Email Sending**: Sends personalized birthday wishes using randomly selected template letters.
- **Credential Management**: Handles user credentials securely for accessing Gmail API.
- **Environment Variable Management**: Utilizes `dotenv` to securely manage environment variables.

### Libraries:

- `datetime`: Used to get the current date.
- `csv`: Utilized for reading birthday data from a CSV file.
- `random`: Used to randomly select a template letter.
- `os`: Used for manipulating and working with file paths, in this case, to verify if `token.json` exists.
- `base64`: Encodes email messages in base64 format for sending through Gmail API.
- `dotenv`: Loads environment variables from a .env file.
- `google.auth`: Manages authentication and authorization.
- `google.auth.transport.requests`: Provides the Request class for refreshing credentials.
- `google.oauth2.credentials`: Manages OAuth 2.0 credentials.
- `google_auth_oauthlib.flow`: Handles the OAuth 2.0 flow.
- `googleapiclient.discovery`: Builds and interacts with Google APIs.
- `googleapiclient.errors`: Handles errors related to Google API interactions.

### Implementation:

The Automated Birthday Wisher is implemented using the following functions and structure:

**Getting Credentials**:

The `get_credentials` function manages user credentials for accessing Gmail API. It checks for existing credentials, refreshes them if expired or prompts the user to log in if no valid credentials are found. The credentials are saved in `token.json` file.

**Sending Email**:

The `send_email` function composes and sends an email using the Gmail API. It uses environment variables (ENV VARS) for the sender email addresses, in this way you don't have to hard code the emails. And for the recipient email it will be received as a function parameter from the information obtained from the CSV file. 

To use the ENV VARS you need to create the file `.env` and inside the file write down your ENV VARS, and to call them inside the code you have to import the library `dotenv` and use the code `os.environ.get()` to get the ENV VARS values.

```python
message["From"] = os.environ.get("EMAIL_FROM")
```

**Checking Birthdays**:

The `check_birthdays` function reads the `birthdays.csv` file to find individuals whose birthdays match the current date. It returns a dictionary of names and email addresses for today's birthdays.

**Picking a Birthday Template**:

The `pick_birthday_template` function randomly selects a template letter from the `letter_templates` directory and personalizes it with the recipient's name.

**Main Execution**:

The main part of the script checks if there are any birthdays today, picks a personalized template for each birthday person, and sends the emails.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/129a73cb-b06a-4dc8-a5d7-c95cf8e30b52)

