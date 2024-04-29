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
    "appid" : "a44068740825277d74e1b162dd339228",
    "interval":"60min",
    "apikey":stock_api
}
response = requests.get(STOCK_ENDPOINT, params=stock_para)
response.raise_for_status()
data = response.json()  # 如果不加上json() ，會得出 <Response [200]>


yesterday_closing_price = data['Time Series (60min)']['2024-04-26 19:00:00']['4. close']
yyesterday_closing_price = data['Time Series (60min)']['2024-04-26 19:00:00']['4. close']
# news_para = {
#     "q" :STOCK_NAME,
#     "lon" :121.41909206086044,
#     "appid" : "a44068740825277d74e1b162dd339228",
#     "cnt":4
# }
# response = requests.get(endpoint, params=weather_para)
# response.raise_for_status()
# data = response.json()  # 如果不加上json() ，會得出 <Response [200]>
# will_rain = False
# for n in data["list"]:
#     if n["weather"][0]["id"] < 700:
#         will_rain = True
# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#     body = "rain alert",
#     from_='+12513095591',
#     to='+8860908296150')
#     print(message.status)


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

