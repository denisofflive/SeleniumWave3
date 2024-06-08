import time
# для работы с DropDown
from selenium.webdriver.support.select import Select
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://the-internet.herokuapp.com/dropdown")

SELECT_LOCATOR = ("xpath", "//select")

dropdown = Select(driver.find_element(*SELECT_LOCATOR))
# Перебор элементов по тексту
all_options = dropdown.options

options_value = []
for option in all_options:
    options_value.append(option.text)

# Проверка "Option 2", что оно есть
assert "Option 2" in options_value

