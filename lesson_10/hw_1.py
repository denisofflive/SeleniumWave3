import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

# Первая вкладка Hyperskill
driver.get("https://hyperskill.org/login")
# Первая вкладка
first_tab = driver.current_window_handle
print("Hyperskill")
time.sleep(3)

# Открыть новое окно
driver.switch_to.new_window("tab")

# Вторая вкладка Avito
second_tab = driver.current_window_handle
driver.get("https://www.avito.ru/")
print("Avito")
time.sleep(3)

# Открыть новое окно
driver.switch_to.new_window("tab")

# Третья вкладка Vk
third_tab = driver.current_window_handle
driver.get("https://www.vk.com/")
print("VK")

# Переключаемся на первую вкладку Hyperskill и выводим title
driver.switch_to.window(first_tab)
print(driver.title)
time.sleep(1)

# Переключаемся на вторую вкладку Avito и выводим title
driver.switch_to.window(second_tab)
print(driver.title)
time.sleep(1)

# Переключаемся на третью вкладку VK и кликнуть по logo
driver.switch_to.window(third_tab)
print(driver.title)

vk_logo = driver.find_element("xpath", "//a[@class='TopHomeLink ']")
vk_logo.click()
print("Click VK Logo")
time.sleep(1)

# Переключаемся на вторую вкладку Avito и кликнуть по logo
driver.switch_to.window(second_tab)

avito_logo = driver.find_element("xpath", "//div[@class='index-logo-K90gi']")
avito_logo.click()
print("Click Avito Logo")
time.sleep(1)

# Переключаемся на первую вкладку Hyperskill и кликнуть по logo
driver.switch_to.window(first_tab)

hyperskill_logo = driver.find_element("xpath", "//div[contains(@class, 'text-logo')]")
hyperskill_logo.click()
print("Click Hyperskill Logo")
time.sleep(1)
