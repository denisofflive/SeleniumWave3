import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-playground.com")
# получение ссылки страницы
print(driver.current_url)
# получение заголовка
print(driver.title)
# получение содержимой всей html-страницы
print(driver.page_source)

# проверка, что "QA Playground" присутствует на странице
assert "QA Playground" in driver.page_source
time.sleep(3)



