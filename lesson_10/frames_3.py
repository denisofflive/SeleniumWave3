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
# Переключаемся на iframe
driver.switch_to.frame(top_parent_frame)
driver.find_element("xpath", "//frameset[@name='frameset-middle']").click()
time.sleep(3)
