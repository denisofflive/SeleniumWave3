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
driver.find_element(*LOGIN_FIELD).send_keys("protest@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("1")
driver.find_element(*SUBMIT_BUTTON).click()

time.sleep(3)

pickle.dump(
    driver.get_cookies(),
    open(
        os.path.join(os.getcwd(), "cookies", "cookies.pkl"),
        "wb"
    )
)


time.sleep(3)
