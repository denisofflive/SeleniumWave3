import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
actions = ActionChains(driver)

driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")
time.sleep(3)

SOURCE_LOCATOR = ("xpath", "//div[@class='grid__item'][1]")

target_x = 112
target_y = 251

source = driver.find_element(*SOURCE_LOCATOR)
current_location = source.location
current_x = current_location["x"]
current_y = current_location["y"]

offset_x = target_x - current_x
offset_y = target_y - current_y

actions.click_and_hold(source) \
    .move_by_offset(offset_x, offset_y) \
    .pause(2) \
    .perform()


time.sleep(5)
