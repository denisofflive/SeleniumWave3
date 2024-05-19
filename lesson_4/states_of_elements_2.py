import time

from selenium import webdriver

FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(1)
first_name = driver.find_element(*FIRST_NAME_FIELD)
time.sleep(1)
# проверка, что поле пустое
assert first_name.get_attribute("value") == ""
first_name.send_keys("Denis")
# проверка, что в поле указан Denis
assert first_name.get_attribute("value") == "Denis"
print(first_name.get_attribute("value"))
# clear - очистить поле
first_name.clear()
# проверка, что поле пустое
assert first_name.get_attribute("value") == ""
