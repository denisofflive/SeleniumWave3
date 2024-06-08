import time

from selenium.webdriver import Keys
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://demoqa.com/select-menu")

MULTI_SELECT = ("xpath", "//input[@id = 'react-select-4-input']")

driver.find_element(*MULTI_SELECT).send_keys("Black", Keys.TAB, Keys.ESCAPE)
driver.find_element(*MULTI_SELECT).send_keys("Green", Keys.TAB, Keys.ESCAPE)
print(driver.find_element(*MULTI_SELECT).get_attribute("value"))
driver.find_element(*MULTI_SELECT).send_keys(Keys.BACKSPACE*2)
time.sleep(3)
