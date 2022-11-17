#importing classes

import requests
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

#environment variables

ACCOUNT_SID=os.getenv("ACCOUNT_SID")
AUTH_TOKEN=os.getenv("AUTH_TOKEN")
APIKEY=os.getenv("APIKEY")

#setting up impt variables and api response

# current_weather="current.json"
forecast_weather="forecast.json"
# search_weather="search.json"
# history_weather="history.json"
# future_weather="future.json"
# time_zone="timezone.json"
# sports="sports.json"
# astronomy="astronomy.json"
# ip_lookup="ip.json"

LAT=22
LON=86
CITY="Jamshedpur"
FORECAST_DAYS=14

FORECAST_URL=f"http://api.weatherapi.com/v1/{forecast_weather}"

forecast_p={
    "key":APIKEY,
    "q":CITY,
    "days":FORECAST_DAYS
}

response=requests.get(FORECAST_URL,forecast_p)
response.raise_for_status()
data=response.json()
all_days_data=data["forecast"]["forecastday"]
current_hour=int(data["current"]["last_updated"].split(" ")[1].split(":")[0])
go_to_hour=int(current_hour+12)

#checking if it'll rain

for each_day in all_days_data:
    all_hours=each_day["hour"]
    for each_hour in all_hours:
        checking_hour=int(each_hour["time"].split(" ")[1].split(":")[0])
        if checking_hour==go_to_hour:
            if each_hour["will_it_rain"]==1:
                client = Client(ACCOUNT_SID,AUTH_TOKEN) #sending SMS
                message = client.messages \
                                .create(
                                    body="It's going to rain today!!!!",
                                    from_='+14054490775',
                                    to='+928618624209'
                                )
                print(message.sid)