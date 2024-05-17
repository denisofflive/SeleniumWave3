# 2 Первый способ инициализации

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

