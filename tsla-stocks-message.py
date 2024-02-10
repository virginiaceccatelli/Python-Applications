import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
ACCOUNT_SID = Own Account 
AUTH_TOKEN = Authentication Token 

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_API = Stock API 
NEWS_API = News API

PHONE_NUMBER_A = Own Number
PHONE_NUMBER_B = Own Number b

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API
}

r = requests.get(STOCK_ENDPOINT, stock_params)
data = r.json()

time_series_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in time_series_data.items()]
yesterday_data = data_list[0]
yesterday_closing = float(yesterday_data["4. close"])


two_days_ago_data = data_list[1]
two_days_ago_closing = float(two_days_ago_data["4. close"])

positive_difference = abs(yesterday_closing - two_days_ago_closing)
average = (yesterday_closing + two_days_ago_closing) / 2
percentage_change = positive_difference / average * 100

news_params = {
    "apiKey": NEWS_API,
    "q": COMPANY_NAME,
    "searchIn": "title",
    "sortBy": "popularity"
}
r = requests.get(NEWS_ENDPOINT, news_params)
data = r.json()
articles = data["articles"]
first_three_articles = articles[:3]

news_list = [f"Headline: {article['title']}. \nDescription: {article['description']}" for article in first_three_articles]

if percentage_change >= 5:
    if yesterday_closing > two_days_ago_closing:
        for article in news_list:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            message = client.messages.create(
                from_= PHONE_NUMBER_A,
                to = PHONE_NUMBER_B,
                body=f"TSLA: 🔺5%\n {article}"
            )
    elif two_days_ago_closing > yesterday_closing:
        for article in news_list:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            message = client.messages.create(
                from_= PHONE_NUMBER_A,
                to = PHONE_NUMBER_B,
                body=f"TSLA: 🔻5%\n {article}"
            )
else:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_= PHONE_NUMBER_A,
        to= PHONE_NUMBER_B,
        body="The Tesla stock has not significantly increased or decreased today"
    )
