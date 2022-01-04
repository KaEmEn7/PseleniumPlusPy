from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import driver as driver
import time

firefox_options = webdriver.FirefoxOptions()

# headless mode activated
firefox_options.headless = False

# prefs = {
#     "profile.default_content_setting_values.notifications": 2}
# lze nahradit:
firefox_options.set_preference("dom.webnotification.enable", False)
# firefox_options.add_experimental_option("prefs", prefs)

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

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
