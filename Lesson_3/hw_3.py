import time
from selenium import webdriver

# Инициализировать драйвер
driver = webdriver.Chrome()
# Открыть любую страницу, например: vk.com
driver.get("https://vk.com")
# Получить и вывести title в консоль.
print(driver.title)
# Открыть любую другую страницу, например: google.com
driver.get("https://www.google.com/")
# Получить и вывести title в консоль
print(driver.title)
# Вернуться назад и, используя assert, убедиться, что вы точно вернулись обратно
driver.back()
assert "ВКонтакте | Добро пожаловать" in driver.title
print("OK")
# Сделать рефреш страницы
driver.refresh()
# Получить и вывести URL-адрес текущей страницы.
print(driver.current_url)
# Вернуться "вперед" на страницу из пункта 4.
driver.forward()
# Убедиться, что URL-адрес изменился.
print(driver.current_url)

time.sleep(3)
