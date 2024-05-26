import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

VISIBLE_AFTER_5_SECONDS_BUTTON = ("xpath", "//button[@id='visibleAfter']")
ENABLE_AFTER_5_SECONDS_BUTTON = ("xpath", "//button[@id='enableAfter']")
# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")
# "Жди.пока не не выполнится(отображение элемента)"
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_5_SECONDS_BUTTON))
button = wait.until(EC.element_to_be_clickable(ENABLE_AFTER_5_SECONDS_BUTTON))
button.click()

driver.find_element(*VISIBLE_AFTER_5_SECONDS_BUTTON)
# time.sleep(3)
