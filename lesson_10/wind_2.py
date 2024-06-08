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
current_tab = driver.current_window_handle
# print(current_tab)

all_tabs = driver.window_handles
print(all_tabs)

driver.find_element("xpath", "//div[@class='example']//a").click()

updates_tabs = driver.window_handles
# Получение всех tabs
print(len(updates_tabs))

time.sleep(3)

# driver.find_element("xpath", "//div[@class='example']//h3[text()='New Window']").click()
# time.sleep(3)
