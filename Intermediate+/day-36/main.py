import requests
import os
from dotenv import load_dotenv
import datetime as dt
from send_email import GmailSender


# Load environment variables from .env file
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")


def get_stock_days():
    today_date = dt.date.today()
    stock_days = {
        0: (3, 4),  # Monday:       (day1=-3 days -> Friday,    day2=-4 days -> Thursday)
        1: (1, 4),  # Tuesday:      (day1=-1 days -> Monday,    day2=-4 days -> Friday)
        2: (1, 2),  # Wednesday:    (day1=-1 days -> Tuesday,   day2=-2 days -> Monday)
        3: (1, 2),  # Thursday:     (day1=-1 days -> Wednesday, day2=-2 days -> Tuesday)
        4: (1, 2),  # Friday:       (day1=-1 days -> Thursday,  day2=-2 days -> Wednesday)
        5: (1, 2),  # Saturday:     (day1=-1 days -> Friday,    day2=-2 days -> Thursday)
        6: (2, 3)   # Sunday:       (day1=-2 days -> Friday,    day2=-3 days -> Thursday)
    }

    day1, day2 = stock_days[today_date.weekday()]
    yesterday = str(today_date - dt.timedelta(days=day1))
    day_before_yesterday = str(today_date - dt.timedelta(days=day2))

    return yesterday, day_before_yesterday


def get_stock_difference(data):
    yesterday_closing = float(data[yesterday]["4. close"])
    before_yesterday_closing = float(data[day_before_yesterday]["4. close"])
    percentage_difference = round(((yesterday_closing - before_yesterday_closing) / before_yesterday_closing) * 100, 2)

    return percentage_difference


def get_stock_data():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }

    stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
    stock_response.raise_for_status()
    return stock_response.json()["Time Series (Daily)"]


def get_stock_news():
    news_params = {
        "apikey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title,description",
        "from": yesterday,
        "to": yesterday,
        "sortBy": "relevancy",
        "pageSize": 20,
        "page": 1
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    stock_news = news_response.json()["articles"]

    news = []
    titles = []
    for index in range(len(stock_news)):
        # getting rid of repeated titles
        if stock_news[index]["title"] not in titles:
            titles.append(stock_news[index]["title"])

            new_dict = {"title": stock_news[index]["title"],
                        "description": stock_news[index]["description"]}
            news.append(new_dict)

    # return the first 3 articles
    return news[0:3]


# --------------------- MAIN ---------------------------

yesterday, day_before_yesterday = get_stock_days()

stock_data = get_stock_data()
stock_difference = get_stock_difference(stock_data)

if abs(stock_difference) > 5.0:
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
