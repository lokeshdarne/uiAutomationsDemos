import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

serivce_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serivce_obj)
driver.maximize_window()

#implicit wait
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, "input[type = 'search']").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class = 'products']/div") #list of products
time.sleep(2) #As above list is the only exception for the implicit wait
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click() #chaining of web element

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)





