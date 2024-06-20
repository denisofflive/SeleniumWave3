import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# экшн.кликни.перемести.подожди.заверши

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
actions = ActionChains(driver)

driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")
time.sleep(3)

SOURCE_LOCATOR = ("xpath", "//div[@class='grid__item'][1]")
TARGET_LOCATOR = ("xpath", "//div[@class='drop-area']//div[@class='drop-area__item'][1]")

source = driver.find_element(*SOURCE_LOCATOR)
target = driver.find_element(*TARGET_LOCATOR)

actions.click_and_hold(source) \
    .pause(2) \
    .move_to_element(target) \
    .release() \
    .perform()

time.sleep(5)
