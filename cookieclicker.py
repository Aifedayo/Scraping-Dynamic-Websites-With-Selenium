import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Instantiate the service
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

def cookie_clicker():
    cookie_id = "bigCookie"

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
    )
    language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
    language.click()

    cookie = driver.find_element(By.ID, cookie_id)
    cookie.click()


if __name__ == "__main__":
    cookie_clicker()
