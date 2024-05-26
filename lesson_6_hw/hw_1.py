import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

CHANGE_TEXT_TO_SELENIUM_WEBDRIVER = ("xpath", "//button[@id='populate-text']")
SITE_TEXT = ("xpath", "//h2[@id='h2']")

DISPLAY_BUTTON_AFTER_10_SECONDS = ("xpath", "//button[@id='display-other-button']")
ENABLED_BUTTON = ("xpath", "//button[text()='Enabled']")

ENABLE_BUTTON_AFTER_10_SECONDS = ("xpath", "//button[@id='enable-button']")
BUTTON = ("xpath", "//button[text()='Button']")

CLICK_ME_TO_OPEN_AN_ALERT_AFTER_5_SECONDS = ("xpath", "//button[@id='alert']")

# 1. Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
wait.until(EC.element_to_be_clickable(CHANGE_TEXT_TO_SELENIUM_WEBDRIVER)).click()
wait.until(EC.text_to_be_present_in_element(SITE_TEXT, "Selenium Webdriver"))
print("Selenium Webdriver")

# 2. Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
wait.until(EC.element_to_be_clickable(DISPLAY_BUTTON_AFTER_10_SECONDS)).click()
wait.until(EC.presence_of_element_located(ENABLED_BUTTON))
print("Enabled")

# 3. Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON_AFTER_10_SECONDS)).click()
wait.until(EC.element_to_be_clickable(BUTTON)).click()
print("Button")

# 4. Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта
wait.until(EC.element_to_be_clickable(CLICK_ME_TO_OPEN_AN_ALERT_AFTER_5_SECONDS)).click()
print("I got opened after 5 seconds")
wait.until(EC.alert_is_present()).accept()
print("Ok")

time.sleep(3)
