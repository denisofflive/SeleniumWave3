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
# Выбрать по видимому тексту
time.sleep(2)
dropdown.select_by_visible_text("Option 1")
time.sleep(2)
# Выбрать по индексу
dropdown.select_by_index(2)
time.sleep(2)
# Выбрать по value (ЛУЧШИЙ ВАРИАНТ ПО ЗНАЧЕНИЮ)
dropdown.select_by_value("1")
time.sleep(2)



