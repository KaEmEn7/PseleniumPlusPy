from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import driver as driver
import time

chrome_options = webdriver.ChromeOptions()

#headless mode activated
chrome_options.headless = True


# druha varianta je přes import
#  from selenium.webdriver.chrome.options import Options
#chrome_options = Options

prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

actions = ActionChains(driver)

driver.get("https://www.redbus.in/")
print("Page open")
driver.maximize_window()
print("window maximized")
driver.implicitly_wait(1)

print(driver.title)
time.sleep(5)

driver.quit()
print("Done")