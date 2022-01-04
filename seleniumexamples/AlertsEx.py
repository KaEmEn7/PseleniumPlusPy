from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium import webdriver
import driver as driver
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
actions = ActionChains(driver)

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.implicitly_wait(1)

signup = driver.find_element(By.XPATH, "//div[2]/div[2]/div[2]/input[2]").click()

# musí být u alertu jinak mi to nejede lol
alert = Alert(driver)
# alert = driver.switch_to.alert je to same jako alert = Alert(driver)
print(alert.text)
time.sleep(3)
alert.accept()

time.sleep(5)

driver.quit()
