import time
import os
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/upload")

UPLOAD_FIELD = ("xpath", "//input[@id='file-upload' and @type='file']")
# Загрузка файла
# driver.find_element(*UPLOAD_FIELD).send_keys(f"{os.getcwd()}/bmw.jpg")
driver.find_element(*UPLOAD_FIELD).send_keys(os.path.join(os.getcwd(), "bmw.jpg"))
time.sleep(3)
