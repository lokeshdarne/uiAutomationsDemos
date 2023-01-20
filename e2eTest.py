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

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT, "Shop").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click() #click on checkout
driver.find_element(By.ID, "country").send_keys("ind")

wait = WebDriverWait(driver, 10)  #wait object
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".suggestions"))) #condition for wait

driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, ".checkbox ").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

successText = driver.find_element(By.CLASS_NAME, "alert").text
assert "Success! Thank you!" in successText
driver.close()





