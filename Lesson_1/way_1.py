# 1 Первый способ инициализации
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ya.ru")
time.sleep(5)
