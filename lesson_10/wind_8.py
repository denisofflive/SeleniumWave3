import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

# Открытие сайта

driver.get("https://the-internet.herokuapp.com/windows")
# Первая вкладка
first_tab = driver.current_window_handle

driver.switch_to.new_window("window")
# Вторая вкладка
second_tab = driver.current_window_handle
driver.get("https://ya.ru")
print(driver.title)

# Переключаемся на первую вкладку
driver.switch_to.window(first_tab)
driver.get("https://vk.com")
time.sleep(3)

