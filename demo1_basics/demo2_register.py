import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.facebook.com/")  # wait for page load to complete

# click on create new account
driver.find_element(By.LINK_TEXT, "Create new account").click()

# enter firstname as john
driver.find_element(By.NAME, "firstname").send_keys("bala")

# enter lastname as dina
driver.find_element(By.NAME, "lastname").send_keys("dina")

# enter password as welcome123
driver.find_element(By.ID, "password_step_input").send_keys("welcom123")

# click on custom radio button
driver.find_element(By.XPATH, "//input[@name='sex']").click()

# click on signup
driver.find_element(By.NAME, "websubmit").click()
time.sleep(5)
