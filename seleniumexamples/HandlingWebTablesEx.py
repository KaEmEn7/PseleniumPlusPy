from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium import webdriver
import driver as driver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# PREFERENCES:
# headless mode activated
chrome_options.headless = False

# Maximized Window
driver.maximize_window()

# Implicit wait for every action (make test run longer)
driver.implicitly_wait(1)

actions = ActionChains(driver)

# URL
driver.get("https://www.espncricinfo.com/series/ipl-2021-1249214/points-table-standings")

xpath = '//*[@id="onetrust-close-btn-container"]/button'
cookies = driver.find_element(By.XPATH, xpath)

def is_element_present(xpath):
    try:
        driver.find_element(By.XPATH, value=xpath)
        return True
    except NoSuchElementException:
        return False


if is_element_present(xpath) == True:
    # time.sleep(2)
    cookies.click()
    print("Cookies clicked")

xpath2 = '//*[@id="wzrk-cancel"]'
wait = WebDriverWait(driver, 15)
news_wait = wait.until(EC.presence_of_element_located((By.XPATH, xpath2)))
news = driver.find_element(By.XPATH, xpath2)

# for i in range (0, 20):
#     print("Time: ", i)
#     time.sleep(1)
if is_element_present(xpath2) == True:
    news.click()
    print("News clicked 'NO'")

rows = driver.find_elements(By.XPATH, "//tbody/tr")
total_rows = len(rows)
print(total_rows)

cols = driver.find_elements(By.XPATH, "//tbody/tr[1]/td")
total_cols = len(cols)

print(total_cols)
print("Total rows are: ", total_rows, " and total cols are: ", total_cols)

for row in rows:
    print(row.text)

print("----------------- Second way-------------------")

start_xpath = "//tbody/tr["
mid_xpath = "]/td["
end_xpath = "]"

xpath3 = (start_xpath+str(row)+mid_xpath+str(cols)+end_xpath)
print(xpath3)

for row in range(1, total_rows+1):
    for col in range(1, total_cols+1):
        print(driver.find_element(By.XPATH, start_xpath+str(row)+mid_xpath+str(col)+end_xpath).text, end=" ")
print()

time.sleep(10)
driver.quit()
