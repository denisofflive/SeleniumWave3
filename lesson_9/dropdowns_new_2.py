import time
# для работы с DropDown
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://demoqa.com/select-menu")

INPUT_LOCATOR = ("xpath", "//input[@id = 'react-select-3-input']")
time.sleep(2)
driver.find_element(*INPUT_LOCATOR).send_keys("Ms.", Keys.ENTER)
# Получение атрибута
print(driver.find_element(*INPUT_LOCATOR).get_attribute("value"))
time.sleep(2)



