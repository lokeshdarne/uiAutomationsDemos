import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

serivce_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serivce_obj)
driver.maximize_window()

#implicit wait
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

windowsList = driver.window_handles
driver.switch_to.window(windowsList[1])

redText = driver.find_element(By.XPATH, "//p[@class = 'im-para red']").text
emailId = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", redText)

driver.switch_to.window(windowsList[0])

driver.find_element(By.ID, "username").send_keys(emailId)
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

print(driver.find_element(By.CSS_SELECTOR, ".alert").text)

