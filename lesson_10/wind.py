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
driver.get("https://demoqa.com/radio-button")

# # Открыть новую вкладку
# driver.switch_to.new_window("tab")

# Открыть новое окно
driver.switch_to.new_window("window")

driver.get("https://the-internet.herokuapp.com")

driver.find_element("xpath", "//div[@id='content']//a").click()

time.sleep(3)

# SELECT_LOCATOR = ("xpath", "//select")