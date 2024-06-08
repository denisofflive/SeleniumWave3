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

# Текущее окно (вкладка)
original_tab = driver.current_window_handle
tab_count = len(driver.window_handles)
# Проверяем, что у нас одна вкладка
assert tab_count == 1
# assert len(driver.window_handles) == 1

driver.find_element("xpath", "//div[@class='example']//a").click()
tabs = driver.window_handles
# Переключаемся на вторую вкладку
driver.switch_to.window(tabs[1])
time.sleep(3)
driver.close()
time.sleep(3)
# Переключаемся на первую вкладку
driver.switch_to.window(tabs[0])
driver.find_element("xpath", "//div[@class='example']//a").click()
time.sleep(3)
