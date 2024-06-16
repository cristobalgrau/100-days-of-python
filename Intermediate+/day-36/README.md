# Day 36 - Stock Trading News Alert Project

## Project: Stock Trading News Alert

The Stock Trading News Alert project is designed to monitor significant stock price changes and send email notifications with relevant news articles. The application uses various APIs to fetch stock data and news and utilizes a Gmail API for sending emails. The notification system alerts users when the stock price of a specified company changes by more than a given threshold, ensuring they stay informed about important market events.

The original project had to use Twilio API to send SMS but by the time I finished the project, Twilio didn't approve my Toll-Free verification to send SMS yet. So it was converted the email functions from day-32 project to a OOP code, in that way you can create your Object and send emails.


### Key Features:

- **Stock Price Monitoring**: Tracks daily stock prices and calculates the percentage change.
- **News Fetching**: Retrieves the latest news articles related to the specified company.
- **Email Notifications**: Sends email alerts with stock price changes and relevant news headlines and descriptions.
- **Environment Variables**: Uses environment variables for sensitive data like API keys and email credentials.


### Libraries Used: 

- `requests`: For making HTTP requests to stock and news APIs.
- `os`: For accessing environment variables.
- `dotenv`: For loading environment variables from a .env file.
- `datetime`: For handling date and time operations.
- `base64`: For encoding email messages.
- `email.message`: For constructing email messages.
- `google.auth.transport.requests`: For handling OAuth2 credentials.
- `google.oauth2.credentials`: For managing OAuth2 credentials.
- `google_auth_oauthlib.flow`: For handling OAuth2 login flow.
- `googleapiclient.discovery`: For building the Gmail API service.
- `googleapiclient.errors`: For handling API errors.


### Implementation:

- **Main Script: `main.py`**

**Load Environment Variables:**
The script begins by importing necessary libraries and loading environment variables from a .env file using load_dotenv. This file contains sensitive information like API keys and email credentials.

**Determine Relevant Dates:**
The `get_stock_days` function calculates the two most recent trading days' dates based on the current day of the week. This is crucial for comparing stock prices between consecutive trading days. The function uses Python's `datetime` library to handle date operations, ensuring accurate and efficient date calculations.

**Fetch Stock Data:**

The `get_stock_data` function constructs the request parameters and sends a `GET` request to the Alpha Vantage API to retrieve daily stock prices. The response is parsed to extract the "Time Series (Daily)" data.

The `get_stock_difference` function calculates the percentage change in stock prices between the two most recent trading days using the closing prices. This percentage change determines whether a significant price movement has occurred.

**Fetch News Data:**

If the stock price change exceeds a specified threshold (e.g., 5%), the `get_stock_news` function sends a `GET` request to the News API, retrieving news articles related to the company. The function filters out duplicate titles to ensure unique news items are returned and selects the top three relevant articles based on relevancy.

**Send Email Alerts:**

The script then initializes a `GmailSender object`, which is responsible for sending email notifications. Depending on whether the stock price increased or decreased, the email's subject line is set to reflect the percentage change.

For each news article, the script constructs an email body containing the headline and a brief description. It then sends the email using the `send_email` method of the `GmailSender class` and prints the result of the send operation.


- **Email Sending Module: `send_email.py`**

**GmailSender Class:**

The GmailSender class encapsulates all the functionality related to sending emails using the Gmail API. It ensures that email sending is handled in a clean and reusable manner as an OOP.

**Initialize Credentials:**

In the `__init__` method, the class loads environment variables and initializes the Gmail API service using OAuth2 credentials. This involves calling the get_credentials method to manage authentication and authorization.

**Get Credentials:**

The `get_credentials` method checks if valid credentials exist in a local file (`token.json`). If not, it initiates the OAuth2 flow to prompt the user to log in and authorize the application. The credentials are then saved for future use. This method ensures secure and authenticated access to the Gmail API.

**Send Email Method:**

The `send_email` method constructs an email message using the `EmailMessage class`, setting the recipient, sender, and subject. The message content is encoded in base64 to meet Gmail's requirements.

The encoded message is then sent using the Gmail API service. The method handles any errors that occur during this process and returns the result, indicating whether the email was sent successfully.


### Result:

For testing purposes the evaluation threshold was set to `< 5` instead to `> 5`:

```python
if abs(stock_difference) < 5.0:
    news_data = get_stock_news()
    email = GmailSender()
    if stock_difference > 0:
        subject = f"{STOCK}: 🔺{stock_difference}%"
    else:
        subject = f"{STOCK}: 🔻{stock_difference}%"

    for index in range(len(news_data)):
        body_text = (f"Headline: \n{news_data[index]["title"]}\n\n"
                     f"Brief: \n{news_data[index]["description"]}")
        email_result = email.send_email(os.environ.get("EMAIL_TO"), subject, body_text)

        if email_result:
            print(f"News email #{index+1} sent successfully!")
        else:
            print(f"News email #{index+1} failed to send")
```

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/3c3a2d75-e888-44f8-893a-cfdcf4cc4757)
