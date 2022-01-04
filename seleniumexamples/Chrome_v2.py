import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.gmail.com")
# will wait for element to appear for 20s
driver.implicitly_wait(20)
# title = driver.title
# username = driver.find_element_by_id("identifierId").send_keys("panbonker@gmail.com")
username = driver.find_element(By.ID, "identifierId")
username.send_keys("panbonker@gmail.com")

#WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable(By.XPATH, "jehoxpath"))

username = driver.find_element(By.XPATH, "//*[@id=\"identifierNext\"]/div/button/span").click()


time.sleep(200)
#driver.quit()

#assert "Seznam" in title
#print(title)