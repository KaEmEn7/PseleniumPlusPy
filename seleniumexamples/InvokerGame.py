from selenium.webdriver.remote import webelement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

actions = ActionChains(ActionChains)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.invokergame.com/")
driver.maximize_window()
# driver.implicitly_wait(1)

# click on clasic
driver.find_element(By.XPATH, "//*[@id=\"GameMenu\"]/div/table/tbody/tr[3]/td[1]/input").click()
# click on without steam
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id=\"LoginNotification\"]/div/table/tbody/tr/td[3]/a/span[1]/sub").click()
# start game
time.sleep(1)


def is_element_present(xpath):
    try:
        driver.find_element(By.XPATH, value=xpath)
        return True
    except NoSuchElementException:
        return False


print("START!!!")
count = 0
for i in range(0, 10):
    if is_element_present('//nobr/table/tbody/tr/td[@id="Spell_0"]/img'):
        print("start snap")
        ActionChains(driver).send_keys('qqqr').perform()
        count += 1
        print("end SNAAP" + "  Spell counter counter: ", count)
        continue
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_1"]/img'):
        print("start walk")
        ActionChains(driver).send_keys('qqwr').perform()
        # driver.send_keys("QQWR")
        count += 1
        print("end WALK" + "  Spell counter counter: ", count)
        continue
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_2"]/img'):
        print("start wall")
        ActionChains(driver).send_keys('qqer').perform()
        # driver.send_keys("QQER")
        count += 1
        print("end WALL" + "  Spell counter counter: ", count)
        continue
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_3"]/img'):
        print("start emp")
        ActionChains(driver).send_keys('wwwr').perform()
        # driver.send_keys("WWWR")
        count += 1
        print("end EMP" + "  Spell counter counter: ", count)
        continue
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_4"]/img'):
        print("start tornado")
        ActionChains(driver).send_keys('wwqr').perform()
        # driver.send_keys("WWQR")
        count += 1
        print("end TORNADO" + "  Spell counter counter: ", count)
        continue
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_5"]/img'):
        print("start alacrity")
        ActionChains(driver).send_keys('wwer').perform()
        # driver.send_keys("WWER")
        count += 1
        print("end ALACRITY" + "  Spell counter counter: ", count)
        continue
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_6"]/img'):
        print("start sunstrike")
        ActionChains(driver).send_keys('eeer').perform()
        # driver.send_keys("EEER")
        count += 1
        print("Send UN STRIKE" + "  Spell counter counter: ", count)
        continue
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_7"]/img'):
        print("start FORGE SPIRIT")
        ActionChains(driver).send_keys('eeqr').perform()
        # driver.send_keys
        count += 1
        print("end FORGE SPIRIT" + "  Spell counter counter: ", count)
        continue
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_8"]/img'):
        print("start CHAOS METEOR")
        ActionChains(driver).send_keys('eewr').perform()
        # driver.send_keys("EEWR")
        count += 1
        print("end CHAOS METEOR!" + "  Spell counter counter: ", count)
        continue
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_9"]/img'):
        print("start DEFEANING BLAST")
        ActionChains(driver).send_keys('qwer').perform()
        # driver.send_keys("QWER")
        count += 1
        print("end DEFEANING BLAST!!" + "  Spell counter counter: ", count)
        continue
print("STOP" + "  Spell counter counter: ", count)
# x = driver.find_element(By.XPATH, "//*[@id=\"StatsScreen\"]/div/div[1]")
time.sleep(1)
driver.quit()
