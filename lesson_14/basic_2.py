import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Ссылка на Datepicker - выбор даты в календаре
driver.get("https://material.angular.io/components/datepicker/overview")
time.sleep(1)
DATEPICKER_LOCATOR = ("xpath", "//input[@id='mat-input-0']")
driver.find_element(*DATEPICKER_LOCATOR).send_keys("8/20/2027")

time.sleep(3)

