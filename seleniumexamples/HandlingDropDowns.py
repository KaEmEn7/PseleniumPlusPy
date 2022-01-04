import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://echoecho.com/htmlforms11.htm")
# will wait for element to appear for 20s
driver.find_element(By.XPATH, "/html/body/div[2]/table[9]/tbody/tr/td[4]/table/tbody/tr/td/div/span/form/table[1]/tbody/tr/td/table/tbody/tr[2]/td[3]/select").send_keys("Cheese")
# driver.implicitly_wait(2)
driver.get("https://wikipedia.org")
driver.find_element(By.XPATH, "//*[@id=\"searchLanguage\"]").send_keys("et")

"""
DROPDOWN SELECT

dropdown = driver.find_element(By.XY, "XYvalue")
select = Select(dropdown) #prida import
select.select_by_visible_text("text")
select.select_by_value("VALUE")

"""
options = driver.find_elements(By.TAG_NAME, "option")
for option in options:
    print("Text is", option.text, "Lang is " + option.get_attribute("lang"))
print("total dropdown values are", len(options))
# total count of the link on wikipedia.org
# every class link or js110n = link
links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    a=+1
    print("text is ",link.text,"<<<--- URL is: "+link.get_attribute("href"))

print("Number of link on page wikipedia.org is: ", len(links))

time.sleep(10)
