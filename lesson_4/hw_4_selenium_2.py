import time
from selenium import webdriver

USER_NAME = ("xpath", "//input[@id='username']")
PASSWORD = ("xpath", "//input[@id='password']")
LOGIN_BUTTON = ("xpath", "//button[@type='submit']")
LOGOUT_BUTTON = ("xpath", "//i[text()=' Logout']")

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(3)

# User Name
user_name = driver.find_element(*USER_NAME)
# clear - очистить поле
user_name.clear()
# проверка, что поле пустое
assert user_name.get_attribute("value") == ""
# Ввести фамилию, имя
user_name.send_keys("tomsmith")
# проверка, что в поле указано tomsmith
assert user_name.get_attribute("value") == "tomsmith"
print(user_name.get_attribute("value"))

# Password
password = driver.find_element(*PASSWORD)
# clear - очистить поле
password.clear()
# проверка, что поле пустое
assert password.get_attribute("value") == ""
# Ввести Password
password.send_keys("SuperSecretPassword!")
# проверка, что в поле указано SuperSecretPassword!
assert password.get_attribute("value") == "SuperSecretPassword!"
print(password.get_attribute("value"))

# Нажать на кнопку LOGIN
login_button = driver.find_element(*LOGIN_BUTTON)
login_button.click()

# Проверка отображения кнопки Logout
logout_button = driver.find_element(*LOGOUT_BUTTON).is_displayed()
assert logout_button == True
print("Logout button is displayed")

time.sleep(3)
