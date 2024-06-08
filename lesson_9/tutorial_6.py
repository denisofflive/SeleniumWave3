import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://demoqa.com/selectable")
time.sleep(3)

ITEM_LOCATOR = ("xpath", "//li[text()='Dapibus ac facilisis in']")

item = driver.find_element(*ITEM_LOCATOR)
# проверка статуса
assert "active" not in item.get_attribute("class")
item.click()
# проверка статуса
assert "active" in item.get_attribute("class")

time.sleep(3)

