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

# # Создаём цикл и выбираем его по тексту
# for option in all_options:
#     time.sleep(2)
#     dropdown.select_by_visible_text(option.text)

# # Создаём цикл и выбираем его по индексу
# for option in all_options:
#     time.sleep(2)
#     dropdown.select_by_index(all_options.index(option))

# Создаём цикл и выбираем его по value (значению)
for option in all_options:
    time.sleep(2)
    dropdown.select_by_value(option.get_attribute("value"))
