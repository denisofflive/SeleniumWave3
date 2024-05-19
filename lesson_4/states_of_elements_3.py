import time

from selenium import webdriver
from selenium.webdriver import Keys

TARGET_FIELD = ("xpath", "//input[@id='target']")

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/key_presses")
time.sleep(2)
driver.find_element(*TARGET_FIELD).send_keys(Keys.SHIFT)
time.sleep(2)
