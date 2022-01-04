from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager

driver = webdriver.Opera(executable_path=OperaDriverManager().install())

driver.get("https://www.google.com")
title = driver.title

driver.quit()

assert "Google" in title
print(title)