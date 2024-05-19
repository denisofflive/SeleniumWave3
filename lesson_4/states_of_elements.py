import time

from selenium import webdriver

STATE_INPUT_FIELD = ("xpath", "//form[@id='input-example']/input")
ENABLE_BUTTON = ("xpath", "//form[@id='input-example']/button")
ADD_BUTTON = ("xpath", "//button[text()='Add']")

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# # is_enabled  - проверяет состояние элемента, если активный True, иначе False
# print(driver.find_element(*STATE_INPUT_FIELD).is_enabled())
# driver.find_element(*ENABLE_BUTTON).click()
# time.sleep(5)
# print(driver.find_element(*STATE_INPUT_FIELD).is_enabled())

# is_displayed - отображается ли кнопка на странице
driver.find_element(*ADD_BUTTON).is_displayed()



