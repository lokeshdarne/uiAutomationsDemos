import time
from selenium import webdriver
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

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, "input[type = 'search']").send_keys("ber")
time.sleep(2)

# list validation
expected_product_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_product_list = []

results = driver.find_elements(By.XPATH, "//div[@class = 'products']/div") #list of products
time.sleep(2) #As above list is the only exception for the implicit wait 
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click() #chaining of web element
    actual_product_list.append(result.find_element(By.XPATH, "h4").text)
assert expected_product_list == actual_product_list

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)

#sum validation of product prices
prices = driver.find_elements(By.XPATH, "//td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
total_amount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
assert sum == int(total_amount)


driver.find_element(By.CSS_SELECTOR, ".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#Explicit wait
wait = WebDriverWait(driver, 10)  #wait object
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo"))) #condition for wait
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

#total amount after discount validation
total_discounted_amount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
assert float(total_discounted_amount) < float(total_amount)





