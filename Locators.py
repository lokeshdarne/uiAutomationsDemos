import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

serivce_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serivce_obj)
driver.maximize_window()

# ID, Xpath, CSSSelector, Classname, Name, LinkText
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("abc@gamil.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath: //tagname[@attribute='value']
# CSS: tagname[attribute = 'value'] OR use #ID OR .classname
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Lokesh")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)


driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("Hello There")
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()
time.sleep(10)




