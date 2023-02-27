import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.db4free.net/")


#switch to second tab
driver.switch_to.new_window("tab")
driver.get("http://goole.com")
token=driver.title

driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()

print(driver.window_handles)

for window in driver.window_handles:
    print(window)
    driver.switch_to.window(window)
    print(driver.title)
    if "phpMy" in driver.title:
        break
    print("-------")


#driver will point to tab with title phpMyAdmin
driver.find_element(By.ID,"input_username").send_keys("bala")

time.sleep(5)

driver.quit()