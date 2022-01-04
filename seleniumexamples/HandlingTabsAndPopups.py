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

driver.get("https://www.way2automation.com/")
driver.maximize_window()
driver.implicitly_wait(1)

windows = driver.window_handles
print("click on \"Member Login\"")
driver.find_element(By.XPATH, "//*[@id=\"menu-item-27625\"]/a/span[2]").click()
print("Fill email")

#driver.switch_to.default_content() - zmeni na default okno

windows

for window in windows:
    print(window)

"""
For switch window:

for window in windows:
    print(window)
    driver.switch_to.window(window) - = posledni ulozene window
    
    driver.switch_to.windows(driver.window_hanldes[0]) - index okna pro switch

"""

driver.find_element(By.XPATH, "//*[@id=\"email\"]").send_keys("somerandom@email.com")
# ActionChains(driver).send_keys('somerandom@email.com').perform()
print("Fill password")
driver.find_element(By.XPATH, "//*[@id=\"password\"]").send_keys("Randompassword123")
print("Close")
driver.close() # - zavře focus okno
# driver.close()
# xpath = '//*[@id="elementor-popup-modal-26600"]/div/div[4]/i'
# popup = driver.find_element(By.XPATH, xpath)
#
#
# def is_element_present(xpath):
#     try:
#         driver.find_element(By.XPATH, value=xpath)
#         return True
#     except NoSuchElementException:
#         return False
#
#
# if is_element_present(xpath) == True:
#     # time.sleep(2)
#     popup.click()
#     print("popup clicked")
#
# frames = driver.find_elements(By.TAG_NAME, "iframe")
# for frame in frames:
#     print(frame.get_attribute("id"))
# xframes = len(frames)
# print("Počet framů = ", xframes)
#
# # time.sleep(3)
# # print("3 secs waited")
# print("Switch?")
# # jede .switch_to.frame přestože by nemělo podle dokumentace? :O
# driver.switch_to.frame("iframeResult")
# print("switched, going to click Try It button")
# driver.find_element(By.XPATH, "/html/body/button").click()
# print("Already clicked")
time.sleep(5)
# print("Done!")
driver.quit()
