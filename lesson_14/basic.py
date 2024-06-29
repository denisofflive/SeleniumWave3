import time
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# для авторизации добавляем к ссылке admin:admin@
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)

