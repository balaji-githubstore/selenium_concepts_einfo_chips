import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

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

#20 Dec 2000
select_day=Select(driver.find_element(By.ID,"day"))
select_day.select_by_visible_text("20")

select_month=Select(driver.find_element(By.XPATH,"//select[@title='Month']"))
select_month.select_by_visible_text("Dec")

#select year as 2000
select_year=Select(driver.find_element(By.ID,"year"))
select_year.select_by_visible_text("2000")


# click on signup
driver.find_element(By.NAME, "websubmit").click()
time.sleep(5)

driver.quit()