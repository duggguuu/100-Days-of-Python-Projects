#importing classes

import requests
import datetime as dt
from twilio.rest import Client
import sys

#extracting today's date

todays_date=str(dt.datetime.now()).split(" ")[0]

#creating variables for stock data

check_symbol="TSLA"
check_stock="tesla"
STOCK_DATA_API="YP8JJ4ZG1E7HQEGR"
STOCK_DATA_URL="https://www.alphavantage.co/query"
params_s={
    "function":"TIME_SERIES_DAILY",
    "symbol":check_symbol,
    "apikey":STOCK_DATA_API
}

#creating variables for news data

NEWS_DATA_API="7e78bbd5cc674f248d30a2a38bf09445"
NEWS_EVERY_URL="https://newsapi.org/v2/everything"
NEWS_TOP_URL="https://newsapi.org/v2/top-headlines"

params_n={
    "q":check_stock,
    "from":todays_date,
    "to":todays_date,
    "sortBy":"popularity",
    "apiKey":NEWS_DATA_API
}

#creating variables for sending SMS via Twilio

ACCOUNT_SID="AC0f815f9341390410b158041de655cfb6"
AUTH_TOKEN="3822b21c0727aeb9f0666b4b7844e1f0"
SENDER="+14054490775"
SENDING="+918618624209"

#calling stock API

stock_response=requests.get(STOCK_DATA_URL,params_s)
stock_response.raise_for_status()

last_refreshed=stock_response.json()["Meta Data"]["3. Last Refreshed"] #checking if market was open on that day
if last_refreshed!=todays_date:
    sys.exit()

stock_data=stock_response.json()["Time Series (Daily)"]
today_data=stock_data[todays_date]

#extracting move percentage

move=float(today_data["1. open"])-float(today_data["4. close"])
move_abs=abs(move)
move_p=float(move_abs)/float(today_data["1. open"])*100
move_p=float("{:.2f}".format(move_p))

print(move_p)

#defining alert function

def send_sms():
    news_response=requests.get(NEWS_EVERY_URL,params_n)
    news_response.raise_for_status()
    news_data=news_response.json()["articles"][0]

    if move<0:
        tosend_headline=f"{check_symbol} is down by {move_p}%"
    elif move>0:
        tosend_headline=f"{check_symbol} is up by {move_p}%"
    
#extracting news and forming a message

    tosend_title=news_data["title"]
    tosend_titletext=f"Headline: {tosend_title}"

    tosend_news=news_data["description"]
    tosend_newstext=f"Brief: {tosend_news}"

    tosend_source=news_data["source"]["name"]
    tosend_sourcetext=f"-source: {tosend_source}"

    full_message=f"{tosend_headline}\n{tosend_titletext}\n{tosend_newstext}\n{tosend_sourcetext}"

#calling twilio api to send sms

    client = Client(ACCOUNT_SID,AUTH_TOKEN) #sending SMS
    message = client.messages \
                    .create(
                        body=full_message,
                        from_='+14054490775',
                        to='+918618624209'
                    )
    print(message.sid)


# if stock data diff of close and open > 3% then major move, send sms

if move_p>3:
    send_sms()