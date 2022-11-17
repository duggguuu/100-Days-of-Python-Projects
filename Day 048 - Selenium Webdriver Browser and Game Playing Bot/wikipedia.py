from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path=r"C:\Users\ygohe\Desktop\Yash\Code\Development_Random\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count=driver.find_element(By.ID,"articlecount")
articlecount=count.text
articlecount=''.join(filter(str.isdigit,articlecount))
print(articlecount)

driver.quit() 