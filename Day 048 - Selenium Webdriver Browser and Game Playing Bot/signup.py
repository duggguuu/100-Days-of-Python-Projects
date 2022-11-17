from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

chrome_driver_path=r"C:\Users\ygohe\Desktop\Yash\Code\Development_Random\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname=driver.find_element(By.NAME,'fName')
fname.send_keys("Yash")
lname=driver.find_element(By.NAME,'lName')
lname.send_keys("Gohel")
email=driver.find_element(By.NAME,'email')
email.send_keys("ygohel30@gmail.com")
submit=driver.find_element(By.CSS_SELECTOR,'form button')
submit.click()

while(True):
    pass