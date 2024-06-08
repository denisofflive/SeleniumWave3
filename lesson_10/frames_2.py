import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

# Открытие сайта
driver.get("https://testautomationpractice.blogspot.com/")

# Переключение на iframe по id
driver.switch_to.frame(0)

driver.find_element("xpath", "//input[@id='RESULT_TextField-0']").send_keys("Denis")
time.sleep(3)
print(driver.title)

# Вернуться на страницу - выйти из iframe
driver.switch_to.default_content()
driver.find_element("xpath", "//a[contains(text(), 'open cart')]").click()
print(driver.title)
time.sleep(3)