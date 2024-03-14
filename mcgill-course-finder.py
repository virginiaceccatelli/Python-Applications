from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

COURSE = input("Name of your Academic Course (official title): \n")
LEVEL = input("Level of studies (Major, Minor, etc): \n")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.mcgill.ca/undergraduate-admissions/programs")
time.sleep(2)

course_find = driver.find_element(By.XPATH, value='//*[@id="edit-query"]')
course_find.send_keys(COURSE, Keys.ENTER)
time.sleep(2)

cname = driver.find_element(By.XPATH, value=f"// a[contains(text(),'{COURSE}')]")
cname.click()

learn_more = driver.find_element(By.CSS_SELECTOR, value="div.bl-tpl a.button--outline")
learn_more.click()

heading_level = driver.find_elements(By.XPATH, value=f"// a[contains(text(),'{LEVEL}')]")
table_of_content = driver.find_element(By.CSS_SELECTOR, value="div.table-of-contents")
for h in heading_level:
    h.click()


all_courses = driver.find_element(By.LINK_TEXT, value=f"http://www.mcgill.ca/{COURSE.lower()}/undergraduates/courses/")
all_courses.click()

time.sleep(20)
driver.quit()
