import time

from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

ele=driver.find_element(By.ID,"email")
ele.send_keys("hello12344@gmail.com")



driver.find_element(By.ID,"email").send_keys("hello1234@gmail.com")
driver.find_element(By.ID,"pass").send_keys("welcome123")

# #click on login
driver.find_element(By.NAME,"login").click()

time.sleep(5)

driver.quit()


