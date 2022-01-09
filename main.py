import requests
# import datetime
# import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY="GS584GA7ELHWUOHP"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY="601321545201438da465f6f4c922eb78"

account_sid="AC5701e23f74dab3f9266b6ed97ba899ff"
auth_token="528d8ee56554e055f34ba5eb18711421"

parameters={
    "function":"TIME_SERIES_DAILY",
     "symbol":STOCK,
      "apikey":STOCK_API_KEY,

}
# now=datetime.datetime.now()
# yesterday_date=now.day-1
# day_before_yesterday=yesterday_date-1
# month=now.month
#
# if month<9:
#     month=f"0{month}"
# else:
#     month=now.month
# year=now.year
#

response=requests.get(STOCK_ENDPOINT,params=parameters)
print(response.status_code)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_=data_list[0]
yesterday_close=yesterday_["4. close"]
print(yesterday_close)

day_before_yesterday_close=data_list[1]["4. close"]
print(day_before_yesterday_close)

difference=float(yesterday_close)-float(day_before_yesterday_close)

diff_percent=round((difference/float(yesterday_close))*100)
print(diff_percent)
up_down="🔺📈"


if abs(diff_percent)>0:
    up_down="🔺📈"
else:
    up_down="🔻📉🚩"

news_parameters = {
        "qIntitle": COMPANY_NAME,
        "apikey": NEWS_API_KEY,

    }
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()
articles = news_data["articles"]
three_articles = articles[:3]
    # print(f'Headline: {news_data["articles"][0]["title"]}')
    # print(f'Brief: {news_data["articles"][0]["description"]}')
ls = [f"{STOCK} :{up_down}{diff_percent}% \nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
print(ls)
for article in ls:
        # proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        # client = Client(account_sid, auth_token, http_client=proxy_client)
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=article,
            from_='+14023076766',
            to='+91 98846 63770'
        )# print(message.status)

# yesterday_stock=data["Time Series (Daily)"][f"{year}-{month}-{yesterday_date}"]["4. close"]
# day_before_yesterday_stock=data["Time Series (Daily)"][f"{year}-{month}-{day_before_yesterday}"]["4. close"]
# difference=float(yesterday_stock)-float(day_before_yesterday_stock)
# print(difference)
# if difference<0:
#     print(-1*(difference))