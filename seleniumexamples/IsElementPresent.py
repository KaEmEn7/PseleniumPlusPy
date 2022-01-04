import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# funkce pro hledání prvku podle key; value
def is_element_present(id):
    try:
        driver.find_element(By.ID, "identifierId")
        return True
    except NoSuchElementException:
        return False

def is_element_present(xpath):
    try:
        driver.find_element(By.XPATH, value=xpath)
        return True
    except NoSuchElementException:
        return False

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://gmail.com/")
driver.implicitly_wait(2)

print(driver.find_element(By.ID, "identifierId").is_displayed())

print(is_element_present("identifierId"))

time.sleep(10)
driver.quit()