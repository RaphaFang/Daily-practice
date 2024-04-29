STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

import requests
from twilio.rest import Client
import os
import datetime

CURRENT_DAY = datetime.datetime.now()
print(CURRENT_DAY.strftime("%Y-%m-%d"))

stock_api ="G9Z2GMSVFNVM3B7M" #os.environ.get("stock_api")
news_api ="4a9ec963962745a2b3b96ab9e60d336d"   #os.environ.get("news_api")
print(stock_api)

stock_para = {
    "function":"TIME_SERIES_INTRADAY",
    "symbol":STOCK_NAME,
    "interval":"60min",
    "apikey":stock_api
}
response = requests.get(STOCK_ENDPOINT, params=stock_para)
response.raise_for_status()
data = response.json()['Time Series (60min)']  # 如果不加上json() ，會得出 <Response [200]>

data = [value for (key, value) in data.items()]

yesterday_closing_price = data[0]['4. close']
yyesterday_closing_price = data[16]['4. close']
diff = abs(float(yesterday_closing_price)-float(yyesterday_closing_price))
diff_percent = (diff/float(yesterday_closing_price))*100
# 可以多細部的漲跌 emoji設定，並且成現在下方的f""中
# 323.  6:20
if diff_percent>1:
    news_para = {
        "q" :STOCK_NAME,
        "apiKey":news_api
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_para)
    articles = news_response.json()['articles']
    articles = articles[:3]
    # print(articles)

    formatted_articles = [f"Headline: {articles["title"]}. \nBrief: {articles["description"]}" for n  in  articles]

# 設定 Twilio 323. 3:20