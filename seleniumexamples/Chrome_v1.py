from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path="C:\\Users\\Kamil\\PycharmProjects\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://way2automation.com")
title = driver.title
driver.quit()

print(title)
assert "Selenium" in title