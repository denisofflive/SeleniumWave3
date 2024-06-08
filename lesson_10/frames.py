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

driver.get("https://testautomationpractice.blogspot.com/")

WIDGET_IFRAME_LOCATOR = ("xpath", "//div[@class='widget-content']//frame")
widget_iframe = driver.find_element(*WIDGET_IFRAME_LOCATOR)

# Переключение на iframe
driver.switch_to.frame(widget_iframe)

driver.find_element("xpath", "//input[@id='RESULT_TextField-0']").send_keys("Denis")

time.sleep(3)

