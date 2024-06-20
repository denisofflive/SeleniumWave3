import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
# Явное ожидание
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
actions = ActionChains(driver)

driver.get("https://seiyria.com/bootstrap-slider")
time.sleep(2)

driver.find_element("xpath", "//a[@href='#example-2']").click()

def move_slider(slider_locator, current_point_atr_name, target_point, step):

    slider = driver.find_element(*slider_locator)
    current_position = int(slider.get_attribute(current_point_atr_name))

    if target_point < current_position:
        offset = int((current_position - target_point) / step)
        slider.send_keys(Keys.ARROW_LEFT * offset)
    else:
        offset = int((target_point - current_position) / step)
        slider.send_keys(Keys.ARROW_RIGHT * offset)


SLIDER_LOCATOR = ("xpath", "(//div[@id='example-2']//div[@role='slider'])[1]")
time.sleep(3)
move_slider(SLIDER_LOCATOR, current_point_atr_name="aria-valuenow", target_point=400, step=5)
time.sleep(5)
