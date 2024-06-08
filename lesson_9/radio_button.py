import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://demoqa.com/radio-button")

YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")
YES_RADIO_LABEL_BUTTON = ("xpath", "//label[@for='yesRadio']")
IMPRESSIVE_RADIO_BUTTON = ("xpath", "//input[@id='impressiveRadio']")
NO_RADIO_BUTTON = ("xpath", "//input[@id='noRadio']")

radio_button = lambda id:  ("xpath", f"//input[@id='{id}']")
label_for = lambda radio_id: ("xpath", f"//label[@for='{radio_id}']")

time.sleep(3)
driver.find_element(*label_for("yesRadio")).click()
# Проверяем выбрана ли кнопка radio_button (получение статуса кнопки radio button)
print(driver.find_element(*radio_button("yesRadio")).is_selected())
time.sleep(3)
