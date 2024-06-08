import time
import pickle
import os
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://www.freeconferencecall.com/ru/ru/login")


LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

# Вход в аккаунт
driver.get("https://www.freeconferencecall.com/ru/ru/login")


driver.delete_all_cookies()
cookies = pickle.load(
    open(
        os.path.join(os.getcwd(), "cookies", "cookies.pkl"),
        "rb"
    )
)

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(3)
