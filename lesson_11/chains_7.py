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

driver.get("https://demoqa.com/droppable")

DRAGGABLE_LOCATOR = ("xpath", "//div[@id='draggable']")
DROPPABLE_LOCATOR = ("xpath", "//div[@id='droppable']")

# source - что мы перетаскиеваем
source = driver.find_element(*DRAGGABLE_LOCATOR)
# source - куда мы перетаскиеваем
target = driver.find_element(*DROPPABLE_LOCATOR)

time.sleep(2)

actions.drag_and_drop(source, target).perform()

time.sleep(5)

