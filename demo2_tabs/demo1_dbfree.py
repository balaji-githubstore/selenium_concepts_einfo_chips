import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.db4free.net/")

#click on phpMyAdmin
driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()

#switch to second tab
driver.switch_to.window(driver.window_handles[1])

#enter username
driver.find_element(By.ID,"input_username").send_keys("bala")
#enter password as welcome123
#click on login

# driver.find_element(By.ID,"bill-date-long").send_keys("14/04/2022")

time.sleep(5)
driver.quit()

# Please use the link in chat to take python post assessment
#
# Duration: 12:15PM to 12:35 PM IST
#
# Link will be active till 12:35 PM only so please submit on or before 12:35 PM IST