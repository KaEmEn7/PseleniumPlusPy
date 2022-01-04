from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import driver as driver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# PREFERENCES:
# headless mode activated
chrome_options.headless = True

actions = ActionChains(driver)

# URL
driver.get("https://deluxe-menu.com/popup-mode-sample.html")

# Maximized Window
driver.maximize_window()

# Implicit wait for every action (make test run longer)
driver.implicitly_wait(1)

time.sleep(10)

driver.quit()
