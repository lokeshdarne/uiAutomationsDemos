import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

serivce_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serivce_obj)

driver.get('https://rahulshettyacademy.com/client/auth/login')
time.sleep(10)
# driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234") #Parent to child travel using CSS
# driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()







