from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

actions = ActionChains(driver)

driver.get("https://deluxe-menu.com/popup-mode-sample.html")
driver.maximize_window()
driver.implicitly_wait(1)

rightclick = driver.find_element(By.XPATH, "//tbody/tr/td[3]/p[2]/img")

menu = actions.context_click(rightclick).perform()

step1 = driver.find_element(By.XPATH, "//*[@id=\"dm2m1i1tdT\"]")
actions.move_to_element(step1).perform()

step2 = driver.find_element(By.XPATH, "//*[@id=\"dm2m2i1tdT\"]")
actions.move_to_element(step2).perform()

step3 = driver.find_element(By.XPATH, "//*[@id=\"dm2m3i1tdT\"]")
actions.move_to_element(step3).perform()

step3.click()

time.sleep(5)

driver.quit()
