# from selenium import webdriverfrom
#
# selenium.webdriver.common.by
# import By
# import time
# from selenium.webdriver.support.select
# import Selectdriver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("http://demo.openemr.io/b/openemr/")
# driver.find_element(By.ID, "authUser").send_keys("admin")
# driver.find_element(By.ID, "clearPass").send_keys(
#     "pass")  # Using XPath Directly#
# driver.find_element(By.XPATH, "//option[contains(@value,'18')]").click()
# select_lang = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
# select_lang.select_by_visible_text("English (Indian)")
# driver.find_element(By.ID,
#                     "login-button").click()
#
# driver.find_element(By.XPATH, "//div[text()='Patient']").click()
# driver.find_element(By.XPATH, "//div[text()='New/Search']").click()
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='pat']"))
#
# driver.find_element(By.ID, "form_fname").send_keys("Ravi")
# driver.find_element(By.ID, "form_lname").send_keys("Patel")
# driver.find_element(By.ID, "form_DOB").send_keys("2023-03-01")
# driver.find_element(By.XPATH, "//option[text()='Male']").click()
# driver.find_element(By.ID, "create").click()
# driver.switch_to.default_content()
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
# driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()
# driver.switch_to.default_content()
# time.sleep(10)
# alert_text = driver.switch_to.alert.textprint(alert_text)
# driver.switch_to.alert.accept()
# driver.find_element(By.XPATH, "//div[@class='closeDlgIframe']").click()
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='pat']"))
# print(driver.find_element(By.XPATH, "//h2[contains(text(),'Medical Record Dashboard')]").text)
# driver.switch_to.default_content()
# time.sleep(10)
# driver.quit()
