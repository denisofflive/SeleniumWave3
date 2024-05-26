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

driver.get("http://the-internet.herokuapp.com/download")

# Находим все ссылки на скачивание файлов на странице
download_links = driver.find_elements("xpath", "//a[contains(@href,'download')]")

# Цикл для скачивания файлов
for link in download_links:
    link.click()
    # time.sleep(2)  # Даем немного времени, чтобы файл скачался

driver.quit()
