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

driver.switch_to.new_window("window")
tabs = driver.window_handles
driver.get("https://ya.ru")
print(driver.title)

driver.switch_to.window(tabs[0])
driver.get("https://vk.com")
time.sleep(3)

