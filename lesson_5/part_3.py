import time
import os
from selenium import webdriver

prefs = {
    "download.default_directory": os.path.join(os.getcwd(), "downloads"),
    "download.prompt_for_download": False,
    "safebrowsing.enabled": False
}
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/upload-download")

DOWNLOAD_BUTTON = ("xpath", "//a[@id='downloadButton']")
# Скачивание файла
driver.find_element(*DOWNLOAD_BUTTON).click()
time.sleep(3)
if os.path.exists("downloads/sampleFile.jpeg"):
    print("Файл загружен")
