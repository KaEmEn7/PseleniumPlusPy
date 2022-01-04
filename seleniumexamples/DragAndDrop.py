from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

actions = ActionChains(driver)

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.maximize_window()
driver.implicitly_wait(1)

drag = driver.find_element(By.XPATH, "//*[@id=\"draggable\"]")
drop = driver.find_element(By.XPATH, "//*[@id=\"droppable\"]")
# No By.XPATH/ID !!!
ActionChains(driver).move_by_offset(200, 200).perform()

time.sleep(5)

driver.quit()
