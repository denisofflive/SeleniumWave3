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

wait.until(EC.number_of_windows_to_be(tab_count + 1))

for window_handle in driver.window_handles: # ["123", "321"]
    if window_handle != original_tab:
        driver.switch_to.window(window_handle)
        break

driver.find_element("xpath", "//div[@class='example']//h3[text()='New Window']").click()
time.sleep(3)