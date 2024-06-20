import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


# экшн.кликни.перемести.подожди.заверши

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
actions = ActionChains(driver)

driver.get("https://demoqa.com/buttons")

CLICK_ME_BUTTON_LOCATOR = ("xpath", "//button[text()='Click Me']")
button = driver.find_element(*CLICK_ME_BUTTON_LOCATOR)
actions.click(button).perform()

time.sleep(2)

