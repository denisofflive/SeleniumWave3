import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://demoqa.com/checkbox")
time.sleep(3)

SPAN_CHECKBOX_LOCATOR = ("xpath", "//span[@class ='rct-checkbox']")
CHECKBOX_STATUS_LOCATOR = ("xpath", "//input[@id ='tree-node-home']")
checkbox_status = driver.find_element(*CHECKBOX_STATUS_LOCATOR)

print(checkbox_status.is_selected())
driver.find_element(*SPAN_CHECKBOX_LOCATOR).click()
print(checkbox_status.is_selected())

time.sleep(3)

