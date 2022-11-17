import requests
from bs4 import BeautifulSoup

url="https://www.amazon.in/Logitech-Advanced-Illuminated-Bluetooth-Responsive/dp/B08196YFMK"
header={
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
}
response=requests.get(url,headers=header)
soup=BeautifulSoup(response.content,"lxml")

price=soup.find(class_="a-price-whole").getText()
price=''.join(filter(str.isdigit,price))
print(price)

if price<=12000:
    print("hit")
