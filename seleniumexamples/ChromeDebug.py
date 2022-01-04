from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

"""
Udělat složku s chromedata a v cmd najit chrome dir,

chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Kamil\PycharmProjects\PySelenium\chromedata

"""
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# driver.get("http://gmail.com")
# driver.maximize_window()

# @ dela ctr+v clipboardu lol
driver.find_element(By.ID, "identifierId").send_keys("panbonker@gmail.com")
