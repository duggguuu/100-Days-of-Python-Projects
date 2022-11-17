import requests
from datetime import datetime

now_today=datetime.now().strftime("%Y%m%d")
now_time=datetime.now().strftime("%X")

API_KEY="926e13d79622b6b248a11aa98cf7e35e"
APP_ID="2fd47b99"
NUTRITIONIX_ENDPOINT="https://trackapi.nutritionix.com//v2/natural/exercise"
GENDER="male"
WEIGHT_KG ="92"
HEIGHT_CM ="183"
AGE ="25"
exercise_i_did=input("What exercises you did today? ")

params_n={
    "query":exercise_i_did,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

headers_n={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}

response_n=requests.post(url=NUTRITIONIX_ENDPOINT,json=params_n,headers=headers_n)
response_n.raise_for_status()
result_n=response_n.json()

USERNAME="waigeee"
PASSWORD="Crazy1234."
AUTH="Basic d2FpZ2VlZTpDcmF6eTEyMzQu"
SHEETY_ENDPOINT="https://api.sheety.co/ab93cc79a0c56baa415ec193620a348b/yash'sWorkout/sheet1"

headers_s={
    "Authorization":AUTH
}

for exercise in result_n["exercises"]:

    params_s={
        "sheet1":{
            "date":now_today,
            "time":now_time,
            "exercise":exercise["name"],
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    response_s=requests.post(url=SHEETY_ENDPOINT,json=params_s,headers=headers_s)
    response_s.raise_for_status()
    result_s=response_s.json()
