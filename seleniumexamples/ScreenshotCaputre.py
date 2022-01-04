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


def screenshot_capture(d, path):
    file_name = path+ "screenshot_" + time.asctime().replace(":", "_") + ".png"
    d.save_screenshot(file_name)
    print("Screenshot captured")

driver.get("https://medium.com/swlh/why-gerkin-cucumber-specflow-always-failed-with-ui-test-automation-c85a8030c07d")
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


driver.save_screenshot("./Screenshots/error.jpg")


screenshot_capture(driver, "./Screenshots/")

time.sleep(2)
driver.quit()
