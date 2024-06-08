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

first_tab = driver.current_window_handle
print(first_tab)
driver.find_element("xpath", "//div[@class='example']//a").click()

updates_tabs = driver.window_handles

# Переключиться на вторую вкладку (где New Window)
driver.switch_to.window(updates_tabs[1])
second_tab = driver.current_window_handle
print(second_tab)

# Проверяем, что вкладки не равны т.е. находимся на новом дискрипторе
assert first_tab != second_tab
driver.find_element("xpath", "//div[@class='example']//h3[text()='New Window']").click()
time.sleep(3)
