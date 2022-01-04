from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium import webdriver
import driver as driver
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

actions = ActionChains(driver)

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")
driver.maximize_window()
driver.implicitly_wait(1)

xpath = '//*[@id="accept-choices"]'
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

frames = driver.find_elements(By.TAG_NAME, "iframe")
for frame in frames:
    print(frame.get_attribute("id"))
xframes = len(frames)
print("Počet framů = ", xframes)

# time.sleep(3)
# print("3 secs waited")
print("Switch?")
# jede .switch_to.frame přestože by nemělo podle dokumentace? :O
driver.switch_to.frame("iframeResult")

print("switched, going to click Try It button")
# driver.find_element(By.XPATH, "/html/body/button").click()

# najdu si element pomocí id a zavolám na něm javascript funkci + highlight ten element
driver.execute_script("myFunction()")
elem = driver.find_element(By.ID, "mySubmit")
driver.execute_script("arguments[0].style.border='3px solid red'", elem)

driver.save_screenshot("./Screenshots/error.jpg")
elem.screenshot("./Screenshots/elem.png")

print("Already clicked")
print("Done!")

time.sleep(2)
driver.quit()
