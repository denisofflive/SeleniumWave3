import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://demoqa.com/selectable")


"""ДО КЛИКА И ПОСЛЕ КЛИКА"""

# Нажать на вкладку Grid
DEMO_GRID_TAB = ("xpath", "//a[@id='demo-tab-grid']")
driver.find_element(*DEMO_GRID_TAB).click()
time.sleep(3)

ONE_ELEMENT = ("xpath", "//li[text()='One']")
TWO_ELEMENT = ("xpath", "//li[text()='Two']")

# ПЕРВЫЙ ЭЛЕМЕНТ
one_element = driver.find_element(*ONE_ELEMENT)
# Выводим на экран значение по class
print(one_element.get_attribute("class"))
# Проверяем, что "active" отсутствует
assert "active" not in one_element.get_attribute("class")
print("Active is none")
# Кликаем на элемент
one_element.click()
# Выводим на экран значение по class
print(one_element.get_attribute("class"))
# Проверяем, что "active" присутствует
assert "active" in one_element.get_attribute("class")
print("Active is here")

# ВТОРОЙ ЭЛЕМЕНТ
two_element = driver.find_element(*TWO_ELEMENT)
# Выводим на экран значение по class
print(two_element.get_attribute("class"))
# Проверяем, что "active" отсутствует
assert "active" not in two_element.get_attribute("class")
print("Active is none")
# Кликаем на элемент
two_element.click()
# Выводим на экран значение по class
print(two_element.get_attribute("class"))
# Проверяем, что "active" присутствует
assert "active" in two_element.get_attribute("class")
print("Active is here")

"""ВОЗВРАЩЕНИЕ В ИСХОДНОЕ СОСТОЯНИЕ"""

# ПЕРВЫЙ ЭЛЕМЕНТ
one_element = driver.find_element(*ONE_ELEMENT)
# Выводим на экран значение по class
print(one_element.get_attribute("class"))
# Проверяем, что "active" присутствует
assert "active" in one_element.get_attribute("class")
print("Active is here")
# Кликаем на элемент
one_element.click()
# Выводим на экран значение по class
print(one_element.get_attribute("class"))
# Проверяем, что "active" отсутствует
assert "active" not in one_element.get_attribute("class")
print("Active is none")

# ВТОРОЙ ЭЛЕМЕНТ
two_element = driver.find_element(*TWO_ELEMENT)
# Выводим на экран значение по class
print(two_element.get_attribute("class"))
# Проверяем, что "active" присутствует
assert "active" in two_element.get_attribute("class")
print("Active is here")
# Кликаем на элемент
two_element.click()
# Выводим на экран значение по class
print(two_element.get_attribute("class"))
# Проверяем, что "active" отсутствует
assert "active" not in two_element.get_attribute("class")
print("Active is none")
