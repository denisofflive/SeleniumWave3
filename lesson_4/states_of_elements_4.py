import time
import platform
from selenium import webdriver
from selenium.webdriver import Keys

# запуск на разных ОС системах для CTRL или Command
os_name = platform.system()
CMD_CTRL = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL

TARGET_FIELD = ("xpath", "//div[@id='example-target']//input")

driver = webdriver.Chrome()
driver.get("https://clipboardjs.com/")
time.sleep(2)

field = driver.find_element(*TARGET_FIELD)
field.send_keys(CMD_CTRL + "A")
time.sleep(2)
field.send_keys(CMD_CTRL + "X")
time.sleep(2)
assert field.get_attribute("value") == ""
field.send_keys("Denis")
time.sleep(2)
