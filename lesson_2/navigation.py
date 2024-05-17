import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(3)

# Обновление страницы
driver.refresh()
time.sleep(3)

# назад стрелка страницы
driver.back()
time.sleep(5)

# вперёд стрелка страницы
driver.forward()
time.sleep(5)

