from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

actions = ActionChains(driver)

driver.get("https://jqueryui.com/resources/demos/slider/default.html")
driver.maximize_window()
driver.implicitly_wait(1)

slider = driver.find_element(By.XPATH, "//*[@id=\"slider\"]/span")

MainSlider = driver.find_element(By.ID, "slider")

location = MainSlider.location
size = MainSlider.size

w,h = size['width'], size['height']
print(location)
print(size)
print(w,h)

ActionChains(driver).drag_and_drop_by_offset(slider, w/2, 0).perform()


time.sleep(50)

driver.quit()
