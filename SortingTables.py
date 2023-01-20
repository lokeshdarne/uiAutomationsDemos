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

BrowserSortedList = [] #initialize one blank list

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click() #click on the element to sort the list on browser level
VeggieList = driver.find_elements(By.XPATH, "//tr/td[1]") #extract the list from browser elements

for elements in VeggieList:
    BrowserSortedList.append(elements.text) #store the list

originalBrowserSortedList = BrowserSortedList.copy() #make a original copy

BrowserSortedList.sort() #sort the second copy

assert BrowserSortedList == originalBrowserSortedList #compare original and second copy