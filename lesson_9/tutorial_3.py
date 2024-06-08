import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://the-internet.herokuapp.com/checkboxes")
CHECKBOX_1_LOCATOR = ("xpath", "(//input[@type='checkbox'])[1]")
checkbox = driver.find_element(*CHECKBOX_1_LOCATOR)
# Проверяем выбран ли чекбокс (получение статуса чекбокса)
print(checkbox.is_selected())
checkbox.click()
# Проверяем выбран ли чекбокс получение статуса чекбокса
print(checkbox.is_selected())
time.sleep(3)

