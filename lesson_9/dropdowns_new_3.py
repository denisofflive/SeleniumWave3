import time
# для работы с DropDown
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://demoqa.com/select-menu")

SELECT_LOCATOR = ("xpath", "//div[@id='selectOne']")
SELECT_OPTIONS = ("xpath", "//div[@id='selectOne']//div[contains(@class, 'option')]")


# Функция выбирает по тексту элемент через цикл
def choose_option_by_text(text):
    elements = driver.find_elements(*SELECT_OPTIONS)
    for element in elements:
        if text == element.text:
            return element

driver.find_element(*SELECT_LOCATOR).click()
time.sleep(2)
choose_option_by_text("Prof.").click()
time.sleep(2)



