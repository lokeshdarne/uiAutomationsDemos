import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#use headless mode to run the automation without opening the browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
#use below line to ignore SSL site certificates
chrome_options.add_argument("--ignore-certificate-errors")

serivce_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serivce_obj, options=chrome_options) #add options to use headless mode
driver.maximize_window()

#implicit wait
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);") #use javascript code to scroll the webpage
driver.get_screenshot_as_file("sc.png") # take screenshots
time.sleep(2)