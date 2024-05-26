import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

REMOVE_BUTTON = ("xpath", "//button[@onclick='swapCheckbox()']")

wait.until(EC.element_to_be_clickable(REMOVE_BUTTON)).click()
wait.until(
    EC.text_to_be_present_in_element(REMOVE_BUTTON, "QWE"),
    message="Add button didn't change text on 'QWE'"
)
# time.sleep(3)
