import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

VISIBLE_AFTER_5_SECONDS_BUTTON = ("xpath", "//button[@id='visibleAfter']")
# Неявное ожидание 10 секунд - не рекомендуется его использовать (10 секунд будет ждать все элементы)
driver.implicitly_wait(10)
driver.get("https://demoqa.com/dynamic-properties")

driver.find_element(*VISIBLE_AFTER_5_SECONDS_BUTTON)
# time.sleep(3)
