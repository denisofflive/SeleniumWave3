import time
import os
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/upload-download")

UPLOAD_FIELD = ("xpath", "//input[@type='file']")
# Загрузка файла
driver.find_element(*UPLOAD_FIELD).send_keys(os.path.join(os.getcwd(), "bmw.jpg"))
time.sleep(3)
