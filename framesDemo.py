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

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr") #first switch to frame to automate its content
#perform action on the frame
driver.find_element(By.CSS_SELECTOR, "p").clear()
driver.find_element(By.CSS_SELECTOR, "p").send_keys("I am Lokesh")

driver.switch_to.default_content() #switch back to the main window

print(driver.find_element(By.CSS_SELECTOR, "h3").text)
