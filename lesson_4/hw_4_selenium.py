import time
from selenium import webdriver

FULL_NAME_FIELD = ("xpath", "//input[@id='userName']")
EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
PERMANENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='permanentAddress']")
SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")

NAME = ("xpath", "//p[@id='name']")
EMAIL = ("xpath", "//p[@id='email']")
CURRENT_ADDRESS = ("xpath", "//p[@id='currentAddress']")
PERMANENT_ADDRESS = ("xpath", "//p[@id='permanentAddress']")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(3)

# Full Name
full_name = driver.find_element(*FULL_NAME_FIELD)
# clear - очистить поле
full_name.clear()
# проверка, что поле пустое
assert full_name.get_attribute("value") == ""
# Ввести фамилию, имя
full_name.send_keys("Denisov Denis")
# проверка, что в поле указано Denisov Denis
assert full_name.get_attribute("value") == "Denisov Denis"
print(full_name.get_attribute("value"))

# Email
email_field = driver.find_element(*EMAIL_FIELD)
# clear - очистить поле
email_field.clear()
# проверка, что поле пустое
assert email_field.get_attribute("value") == ""
# Ввести email
email_field.send_keys("test@test.com")
# проверка, что в поле указано test@test.com
assert email_field.get_attribute("value") == "test@test.com"
print(email_field.get_attribute("value"))

# Current Address
current_address_field = driver.find_element(*CURRENT_ADDRESS_FIELD)
# clear - очистить поле
current_address_field.clear()
# проверка, что поле пустое
assert current_address_field.get_attribute("value") == ""
# Ввести адрес
current_address_field.send_keys("Moscow City")
# проверка, что в поле указано test@test.com
assert current_address_field.get_attribute("value") == "Moscow City"
print(current_address_field.get_attribute("value"))

# Permanent Address
permanent_address_field = driver.find_element(*PERMANENT_ADDRESS_FIELD)
# clear - очистить поле
permanent_address_field.clear()
# проверка, что поле пустое
assert permanent_address_field.get_attribute("value") == ""
# Ввести адрес
permanent_address_field.send_keys("77 77 77")
# проверка, что в поле указано test@test.com
assert permanent_address_field.get_attribute("value") == "77 77 77"
print(permanent_address_field.get_attribute("value"))

# Нажать на кнопку Submit
submit_button = driver.find_element(*SUBMIT_BUTTON)
submit_button.click()
time.sleep(3)
