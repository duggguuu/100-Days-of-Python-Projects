import requests
from datetime import datetime

TODAY=datetime.now()
DATE=TODAY.strftime("%Y%m%d")
USERNAME="yashgohel"
TOKEN="qwertyuiop"
ID="graph1"

headers={
    "X-USER-TOKEN":TOKEN
}

#creating user

pixela_endpoint="https://pixe.la/v1/users"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response=requests.post(url=pixela_endpoint,json=user_params)

#creating graph

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
graph_response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)

#reating pixels

pixel_endpoint=f"{graph_endpoint}/{ID}"
pixel_config={
    "date":DATE,
    "quantity":"35",
}
pixel_response=requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)

update_endpoint=f"{pixel_endpoint}/{DATE}"
update_config={
    "quantity":"56"
}
update_response=requests.put(url=update_endpoint,json=update_config,headers=headers)
print(update_response.text)