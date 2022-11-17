from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
# Upload resume file if needed
RESUME = 'ADD RESUME FILE'
# Setting up working Selenium for Mac OSX on Chrome 96.4554.55
ser = Service("FILE PATH TO CHROME DRIVER")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get('https://www.linkedin.com/')
# Logging in
username = driver.find_element(By.NAME, 'session_key')
username.send_keys('***')
password = driver.find_element(By.NAME, 'session_password')
password.send_keys('***')
sign_in = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button')
sign_in.click()
# Going to jobs
jobs_link = driver.find_element(By.ID, 'ember22')
jobs_link.click()
# wait cuz internet could be slow
time.sleep(2)
# Search for your job preference
job_search_field = driver.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')
job_search_field.send_keys('Python')
job_search_click = driver.find_element(By.CLASS_NAME, 'jobs-search-box__submit-button')
job_search_click.click()
# Get job cards in list to apply to
time.sleep(2)
filter_click = driver.find_element(By.CSS_SELECTOR, '.search-reusables__filter-binary-toggle button')
filter_click.click()
time.sleep(3)
jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container--clickable')
for job in jobs:
    job.click()
    try:
        time.sleep(1)
        apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
        button_text = apply_button.get_attribute('data-control-name')
        if button_text != 'jobdetails_topcard_inapply':
            print('Not Easy Application')
            continue
        else:
            time.sleep(1)
            apply_button.click()
            time.sleep(5)
            try:
                save_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn')
                print('yes i found the save bar footer')
            except NoSuchElementException:
                print('No Save Button This Time')
            next_button = driver.find_element(By.CLASS_NAME, 'artdeco-button')
            next_button.click()
            break
    except NoSuchElementException:
        print('No button found')
        continue