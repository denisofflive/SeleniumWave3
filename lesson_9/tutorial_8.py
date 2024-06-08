import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://demoqa.com/selectable")
time.sleep(3)

# Подход через лямбду, с помощью неё передаём похожие локаторы
item_locator = lambda text: ("xpath", f"//li[text()='{text}']")

driver.find_element(*item_locator("Cras justo odio")).click()
driver.find_element(*item_locator("Morbi leo risus")).click()

time.sleep(3)

