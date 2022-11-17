from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# for enabling timer features

import time
timeout=time.time()+5
five_min=time.time() + 60*5

# initializing driver

chrome_driver_path=r"C:\Users\ygohe\Desktop\Yash\Code\Development_Random\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie=driver.find_element(By.ID,"cookie")

# getting ids of each element

all_i=driver.find_elements(By.CSS_SELECTOR,"#store div")
items_i=[i.get_attribute("id") for i in all_i]

while True:
    cookie.click()

# checking for 5 second rule

    if time.time()>timeout:

        print("tick")

# getting prices of each and converting them to numbers

        all_p=driver.find_elements(By.CSS_SELECTOR,"#store b")
        items_p=[]
        for p in all_p:
            price_text=p.text
            price=''.join(filter(str.isdigit,price_text))
            items_p.append(price)

#Create dictionary of store items and prices

        cookie_ups={}
        for n in range(len(items_p)):
            cookie_ups[items_p[n]]=items_i[n]

#Get current cookie count

        money=driver.find_element(By.ID,"money").text
        money=''.join(filter(str.isdigit,money))

#Find upgrades that we can currently afford

        affordable_ups={}
        for p,i in cookie_ups.items():
            if money>p:
                affordable_ups[p]=i

#Purchase the most expensive affordable upgrade

        highest=max(affordable_ups)
        print(highest)
        purchase_id=affordable_ups[highest]
        driver.find_element(By.ID,purchase_id).click()

# adding 5 seconds to timer

        timeout=time.time()+5

# After 5 minutes stop the bot and check the cookies per second count.
    if time.time()>five_min:
        cookie_per_s=driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break