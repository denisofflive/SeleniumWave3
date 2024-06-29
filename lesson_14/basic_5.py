import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dphandler import DatePickerHandler

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

ACCEPT_COOKIES = ("xpath", "//button[@id='onetrust-accept-btn-handler']")
# Ссылка на Datepicker - выбор даты в календаре
driver.get("https://www.booking.com/")
wait.until(EC.element_to_be_clickable(ACCEPT_COOKIES)).click()
time.sleep(5)

datepicker = DatePickerHandler(driver)
datepicker.open()
datepicker.set_date(21, 11, 2024)
datepicker.set_date(15, 3, 2025)
datepicker.plus_minus(7)

time.sleep(3)
