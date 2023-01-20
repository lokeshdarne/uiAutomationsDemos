import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

serivce_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serivce_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected() #is selected is boolean to check if the checkbox is selected or not
        break

time.sleep(2)

radiobuttons = driver.find_elements(By.XPATH, "//input[@type = 'radio']")

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        break

time.sleep(2)

# is_displayed explained below
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

