import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(3)
CHECKBOX_1_LOCATOR = ("xpath", "(//input[@type='checkbox'])[1]")
checkbox = driver.find_element(*CHECKBOX_1_LOCATOR)
print(checkbox.get_attribute("checked"))
# Проверяем, что чекбокс не установлен
assert checkbox.get_attribute("checked") is None
checkbox.click()

time.sleep(3)
print(checkbox.get_attribute("checked"))

# Проверяем, что чекбокс установлен
assert checkbox.get_attribute("checked") is not None