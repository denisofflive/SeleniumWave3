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

def move_slider(slider, target_point, current_position, step):
    if target_point < current_position:
        offset = int((current_position - target_point) / step)
        slider.send_keys(Keys.ARROW_LEFT * offset)
    else:
        offset = int((target_point - current_position) / step)
        slider.send_keys(Keys.ARROW_RIGHT * offset)

def set_range(s1, s2, target_points: list, current_point_attr_name, step=1):
    slider_1 = driver.find_element(*s1)
    slider_2 = driver.find_element(*s2)

    current_position_1 = int(slider_1.get_attribute(current_point_attr_name))
    current_position_2 = int(slider_2.get_attribute(current_point_attr_name))

    move_slider(slider_1, target_points[0], current_position_1, step)
    move_slider(slider_2, target_points[1], current_position_2, step)

    assert int(slider_1.get_attribute(current_point_attr_name)) == target_points[0]
    assert int(slider_2.get_attribute(current_point_attr_name)) == target_points[1]

S1_LOCATOR = ("xpath", "(//div[@id='example-2']//div[@role='slider'])[1]")
S2_LOCATOR = ("xpath", "(//div[@id='example-2']//div[@role='slider'])[2]")

time.sleep(3)
set_range(S1_LOCATOR, S2_LOCATOR, target_points=[200, 700], current_point_attr_name="aria-valuenow", step=5)
time.sleep(5)
