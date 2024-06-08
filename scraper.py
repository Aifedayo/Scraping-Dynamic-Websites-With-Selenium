import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Wait for an element to load before proceeding    

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

# Crash the program after 5 seconds if the element does not exist
WebDriverWait(driver, 5).until(
    EC.presense_of_element_located((By.CLASS_NAME, "gLFyf")))

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear() # clear first before inputting text
input_element.send_keys("Data Science Jobs in Nigeria" + Keys.ENTER)

time.sleep(10)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Data Science") # use LINK_TEXT if you want exact match
# Use find_elements to  return an array that you can iterate over
link.click()

driver.quit()