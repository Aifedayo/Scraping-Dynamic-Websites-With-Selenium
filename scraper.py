import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear() # clear first before inputting text
input_element.send_keys("Data Science Jobs in Nigeria" + Keys.ENTER)


time.sleep(10)

driver.quit()