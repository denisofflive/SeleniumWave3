from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")

# Проверяем, что данной куки изначально нет
print("Кука username:", driver.get_cookie("username"))

# Удаляем все куки
driver.delete_all_cookies()

# Добавляем свою куку
driver.add_cookie(
    {
        "name": "username",
        "value": "user123"
    }
)

# Выводим куку
print("Кука username:", driver.get_cookie("username"))

# Удаляем куку
print("Кука username:", driver.delete_cookie("username"))

# Обновляем страницу
driver.refresh()

# Убеждаемся что такой куки нет
print("Кука username:", driver.get_cookie("username"))
