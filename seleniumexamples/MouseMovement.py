from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

actions = ActionChains(driver)

driver.get("https://www.way2automation.com/")
driver.maximize_window()
driver.implicitly_wait(2)

menu = driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div/nav/div/ul/li[2]/a/span[2]")

actions.move_to_element(menu).perform()
driver.find_element(By.XPATH, "//*[@id=\"menu-item-27595\"]/a/span[2]").click()

time.sleep(50)

driver.quit()
