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

driver.get("https://demoqa.com/sortable")
time.sleep(3)


def sort_elements(source_index, target_index):
    SOURCE_ELEMENT = driver.find_element("xpath", f"//div[contains(@class, 'vertical-list')]//div[{source_index}]")
    TARGET_ELEMENT = driver.find_element("xpath", f"//div[contains(@class, 'vertical-list')]//div[{target_index}]")
    actions.drag_and_drop(SOURCE_ELEMENT,TARGET_ELEMENT).perform()
    time.sleep(2)

sort_elements(source_index=1, target_index=4)
sort_elements(source_index=3, target_index=6)
time.sleep(3)
