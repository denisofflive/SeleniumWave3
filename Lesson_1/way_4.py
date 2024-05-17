# 4 способ инициализации

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(ChromeDriverManager(driver_version="114.0.5735.16").install())
driver = webdriver.Chrome(service=service)

