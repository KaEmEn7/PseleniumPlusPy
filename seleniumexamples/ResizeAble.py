from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

actions = ActionChains(driver)

driver.get("https://jqueryui.com/resources/demos/resizable/default.html")
driver.maximize_window()
driver.implicitly_wait(1)

resizable = driver.find_element(By.XPATH, "//*[@id=\"resizable\"]/div[3]")


location = resizable.location
size = resizable.size

w,h = size['width'], size['height']
print(location)
print(size)
print(w,h)

ActionChains(driver).drag_and_drop_by_offset(resizable, 400, 400).perform()
location = resizable.location
size = resizable.size

w,h = size['width'], size['height']
print(location)
print(size)
print(w,h)

time.sleep(5)

driver.quit()
