from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium import webdriver
import driver as driver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# PREFERENCES:
# headless mode activated

actions = ActionChains(driver)

driver.get("https://www.lambdatest.com/blog/selenium-best-practices-for-web-testing/")
driver.maximize_window()
driver.implicitly_wait(1)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll' +X)

driver.set_window_size(S('Width'), S('Height'))

# HEADLESS MODE NEEDED FOR FULL PAGE SCREENSHOT
time.sleep(3)
driver.find_element(By.TAG_NAME, "body").screenshot('./Screenshots/selenium-best-practices-for-web-testing.png')
print("Full page screenshot captured")
time.sleep(1)
driver.quit()
