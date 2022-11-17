from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path=r"C:\Users\ygohe\Desktop\Yash\Code\Development_Random\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://python.org")

dates=driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
names=driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')
events={}

for n in range(len(dates)):
    events[n]={
        "date":dates[n].text,
        "name":names[n].text
    }

print(events)

driver.quit()