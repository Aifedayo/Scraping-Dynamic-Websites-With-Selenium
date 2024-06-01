import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
input_element = driver.get_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("Data Science Jobs in Nigeria")

time.sleep(10)

driver.quit()