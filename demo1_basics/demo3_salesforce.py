import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

# 2.	Enter first name as “John”
driver.find_element(By.NAME,"UserFirstName").send_keys("john")

# 4.	Enter work email as “john@gmail.com”
driver.find_element(By.NAME,"UserEmail").send_keys("john@gmail.com")

# 5.	Select Job title as “IT Manager”
select_title=Select(driver.find_element(By.NAME,"UserTitle"))
select_title.select_by_visible_text("IT Manager")

# 6.	Select Employees as “101-500 employees”
select_emp_count=Select(driver.find_element(By.NAME,"CompanyEmployees"))
select_emp_count.select_by_visible_text("101 - 500 employees")

# 9.	Click on check box
driver.find_element(By.XPATH,"//div[@class='checkbox-ui']").click()
# 10.	Click on start my free trial
driver.find_element(By.NAME,"start my free trial").click()

# actual_error=driver.find_element(By.XPATH,"//span[contains(@id,'UserPhone')]").text
actual_error=driver.find_element(By.XPATH,"//span[contains(text(),'valid phone')]").text

print(actual_error)

time.sleep(5)
driver.quit()