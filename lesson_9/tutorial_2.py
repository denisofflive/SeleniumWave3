import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://the-internet.herokuapp.com/checkboxes")
CHECKBOX_1_LOCATOR = ("xpath", "(//input[@type='checkbox'])[1]")
checkbox = driver.find_element(*CHECKBOX_1_LOCATOR)
time.sleep(3)

# Если чекбокс не проставлен, то кликни по нему
if checkbox.get_attribute("checked") is None:
    checkbox.click()
    assert checkbox.get_attribute("checked") is not None
else:
    pass

time.sleep(3)

