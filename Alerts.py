import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

serivce_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serivce_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Lokesh"
driver.find_element(By.XPATH, "//input[@placeholder= 'Enter Your Name']").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "input[value= 'Alert']").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
#alert.dismiss()

time.sleep(2)
