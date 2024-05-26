import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

driver.get("https://hyperskill.org/")

PRICING_LINK = ("xpath", "//nav//a[text()='Pricing']")
wait.until(EC.element_to_be_clickable(PRICING_LINK)).click()

wait.until(EC.url_changes("https://hyperskill.org/"))
time.sleep(3)
