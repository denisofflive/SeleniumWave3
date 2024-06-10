import time
import pickle
import os

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие сайта
driver.get("https://www.wildberries.ru/catalog/elektronika/avtoelektronika")
time.sleep(1)

# Добавление товаров в корзину
add_to_carts = driver.find_elements("xpath", "//span[text()='Завтра']")

# Добавление только первых 3 товаров в корзину
for i in range(3):
    add_to_carts[i].click()
    time.sleep(1)

# Клик по корзине
cart = driver.find_element("xpath", "(//span[contains(@class, 'icon--basket')])[1]")
cart.click()

# Сохранение состояния корзины (cookies)
cookies = driver.get_cookies()
print(cookies)

# Сохранение куков в папку product_cookies
pickle.dump(
    driver.get_cookies(),
    open(
        os.path.join(os.getcwd(), "product_cookies", "cookies.pkl"),
        "wb"
    )
)

# Чистим куки + перезагрузка страницы = очистка корзины
driver.delete_all_cookies()
driver.refresh()
time.sleep(3)

# Добавляем куки
driver.delete_all_cookies()
cookies = pickle.load(
    open(
        os.path.join(os.getcwd(), "product_cookies", "cookies.pkl"),
        "rb"
    )
)

for cookie in cookies:
    driver.add_cookie(cookie)

# Перезагрузка страницы для применения новых куков
driver.refresh()
time.sleep(3)
