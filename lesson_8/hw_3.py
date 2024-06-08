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

time.sleep(3)

# Очистка всех cookies
driver.delete_all_cookies()

cookies = pickle.load(
    open(
        os.path.join(os.getcwd(), "product_cookies", "cookies.pkl"),
        "rb"
    )
)

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(3)

# Если есть кука, то загрузи её и прочитай куку
if os.path.exists(os.path.join(os.getcwd(), "product_cookies", "cookies.pkl")):
    driver.delete_all_cookies()
    cookies = pickle.load(open(os.path.join(os.getcwd(), "product_cookies", "cookies.pkl"), "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
# Если куки нет, то создаём и сохраняем куку
else:
    pickle.dump(driver.get_cookies(), open(os.path.join(os.getcwd(), "product_cookies", "cookies.pkl"), "wb"))

time.sleep(3)
