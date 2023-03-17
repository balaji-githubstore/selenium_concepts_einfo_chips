from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select  import Select


opt = webdriver.ChromeOptions()
dictionary = {"download.default_directory":"D:\\Shefali"}
opt.add_experimental_option("prefs", dictionary)
driver = webdriver.Chrome(executable_path='C:\\Users\\112552\\Downloads\\chromedriver_win32\\chromedriver.exe', options=opt)
# driver = webdriver.Edge(executable_path='C:\\Users\\112552\\Downloads\\edgedriver_win64\\msedgedriver.exe')
# driver.get("https://www.selenium.dev/downloads/")
# driver.find_element(By.XPATH,"//a[text()='4.8.1']").click()
