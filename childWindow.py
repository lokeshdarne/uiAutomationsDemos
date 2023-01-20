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

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

windowOpened = driver.window_handles # this retrives the list of windows opened in the current session
driver.switch_to.window(windowOpened[1]) #it is used to switch to the dected tab
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close() #close child window 
driver.switch_to.window(windowOpened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)