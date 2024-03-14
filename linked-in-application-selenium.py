from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3789879230&f_AL=true&geoId=102257491&keywords=economics&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

PASSWORD = OWN_PASSWORD
EMAIL = OWN_EMAIL

sign_up = driver.find_element(By.XPATH, value="/html/body/div[3]/header/nav/div/a[2]")
sign_up.click()
time.sleep(5)

username = driver.find_element(By.ID, value="username")
username.send_keys(EMAIL, Keys.ENTER)
password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD, Keys.ENTER)

time.sleep(7)
save_job = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
save_job.click()
