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

# Если есть кука, то загрузи и прочитай куку
if os.path.exists(os.path.join(os.getcwd(), "cookies", "cookies.pkl")):
    driver.delete_all_cookies()
    cookies = pickle.load(open(os.path.join(os.getcwd(), "cookies", "cookies.pkl"), "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
# Есл куки нет, то мы логинимся, создаём и сохраняем куку
else:
    driver.find_element(*LOGIN_FIELD).send_keys("protest@ya.ru")
    driver.find_element(*PASSWORD_FIELD).send_keys("1")
    driver.find_element(*SUBMIT_BUTTON).click()
    time.sleep(2)

    pickle.dump(driver.get_cookies(), open(os.path.join(os.getcwd(), "cookies", "cookies.pkl"), "wb"))

