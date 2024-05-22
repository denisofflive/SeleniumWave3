import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Создаём объект опций
options = Options()
# # Стратегия загрузки страницы (normal, eager, none)
# options.page_load_strategy = "normal"
## Безголовый режим (new)
# options.add_argument("--headless=new")

## Инкогнито режим
# options.add_argument("--incognito")

# # Отключения кэширования режим
# options.add_argument("--disable-cache")

# # Игнорирование сертификата режим
# options.add_argument("--ignore-certificate-errors")

# Опция высоты и ширины экрана - ЛУЧШИЙ ВАРИАНТ
options.add_argument("--window-size=1920,1080")

# Инициализация драйвера, используя Options
driver = webdriver.Chrome(options=options)
# # установка высоты и ширины экрана
# driver.set_window_size(1920,1080)
# # установка полного экрана
# driver.maximize_window()
start = time.time()
driver.get("https://www.google.com/")
end = time.time()
result = end - start
print(result)
# time.sleep(3)
