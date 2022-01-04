from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

driver.get("https://www.google.com")
title = driver.title

driver.quit()

# assert "Seznam" in title
print(title)
