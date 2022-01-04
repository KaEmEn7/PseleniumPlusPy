from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
driver.implicitly_wait(2)

# funkce pro hledání prvku podle key; value


def is_element_present2(what):
    if len(driver.find_elements(By.XPATH, value=what)) == 0:
        return False
    else:
        return True


i = 1
print(i)
x = "\"//div[4]/input["+str(i)+"]\""
print(x)
# driver.find_element(By.XPATH, "//div[4]/input["+str(i)+"]").click()

# x = "\"//div[4]/input["+str(i)+"]\""

# # Varianta 1
# # x nelze zadat, musí to být jak je níže, nevím proč, ale takhle to jede
# while is_element_present2("//div[4]/input["+str(i)+"]"):
#     print(i)
#     print(x, "while loop", i)
#     driver.find_element(By.XPATH, "//div[4]/input["+str(i)+"]").click()
#     i += 1

print("Total checkbox count is ", i-1)
# # Varianta 2

# # 2.1 (only block of checkboxes) -
block = driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]")
checkboxes = block.find_elements(By.NAME, "sports")

print(len(checkboxes))

for checkbox in checkboxes:
    print("Before clicking ", checkbox.is_selected())
    checkbox.click()
    print("After clicking", checkbox.is_selected())


# # one by one checkbox
# # //div[4]/input[1]
# driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]/input[1]").click()
# # //div[4]/input[2]
# driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]/input[2]").click()
# # //div[4]/input[3]
# driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]/input[3]").click()
# # //div[4]/input[4]
# driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]/input[4]").click()

time.sleep(10)

driver.quit()
