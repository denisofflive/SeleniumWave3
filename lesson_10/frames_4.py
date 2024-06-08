import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

# Открытие сайта
driver.get("https://the-internet.herokuapp.com/nested_frames")

top_parent_frame = driver.find_element("xpath", "//frame[@name='frame-top']")
# Переключаемся на iframe - родитель для 3-х фреймов
driver.switch_to.frame(top_parent_frame)
time.sleep(3)

# Переключаемся на middle Frame
middle_frame = driver.find_element("xpath", "//frame[@name='frame-middle']")
driver.switch_to.frame(middle_frame)
print(driver.find_element("xpath", "//div[@id='content']").text)
time.sleep(3)


# Возвращаемся в родительский top_parent_frame из текущего
driver.switch_to.parent_frame()
driver.find_element("xpath", "//frameset[@name='frameset-middle']").click()

# Переключение на right frame из parent frame
right_frame = driver.find_element("xpath", "//frame[@name='frame-right']")
driver.switch_to.frame(right_frame)
time.sleep(3)
print(driver.find_element("xpath", "//body").text)
