#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


import requests

KIWI_API="fm83ifJo7IKOShI2kG6K-A_Dw3rQkche"
KIWI_ENDPOINT="https://tequila-api.kiwi.com/v2/search?"
LOC_ENDPOINT="https://tequila-api.kiwi.com/locations/query?"
headers={
    "apikey":KIWI_API,
}

departure=input("Where do you want to start from? ")
res_dep=requests.get(url=f"{LOC_ENDPOINT}term={departure}&limit=1",headers=headers)
fly_from_data=res_dep.json()["locations"][0]
fly_from=fly_from_data["code"]
fly_from_city=fly_from_data["name"]

arrival=input("Where do you want to go? ")
res_arr=requests.get(url=f"{LOC_ENDPOINT}term={arrival}&limit=1",headers=headers)
fly_to_data=res_arr.json()["locations"][0]
fly_to=fly_to_data["code"]
fly_to_city=fly_to_data["name"]

date_from=input("From which date do you want to search? Type your preference in dd/mm/yyyy format. ")
date_to=input("Upto what date do you want to search? Type your preference in dd/mm/yyyy format. ")

search_params={
    "fly_from":fly_from,
    "fly_to":fly_to,
    "date_from":date_from,
    "date_to":date_to,
    "flight_type":"oneway",
    "one_for_city":1,
    "adults":1,
    "selected_cabins":"M",
    "only_working_days":"false",
    "only_weekends":"false",
    "partner_market":"in",
    "curr":"INR",
    "vehicle_type":"aircraft",
    "limit":10
}

flight_response=requests.get(url=KIWI_ENDPOINT,params=search_params,headers=headers)
flight_data=flight_response.json()["data"][0]
flight_price=flight_data["price"]
print(flight_price)