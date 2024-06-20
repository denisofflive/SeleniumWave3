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
time.sleep(3)

driver.find_element("xpath", "//a[@href='#example-3']").click()

RED_SLIDER_LOCATOR = ("xpath", "(//div[@id='RC']//div[@role='slider'])[1]")
BLUE_SLIDER_LOCATOR = ("xpath", "(//div[@id='RC']//div[@role='slider'])[1]")
GREEN_SLIDER_LOCATOR = ("xpath", "(//div[@id='GC']//div[@role='slider'])[1]")
FINAL_COLOR_LOCATOR = ("xpath", "//div[@id='RGB']")


def move_slider(slider, target_point, current_point):
    if 0 <= target_point < current_point:
        offset = current_point - target_point
        slider.send_keys(Keys.ARROW_LEFT * offset)
    elif 255 >= target_point > current_point:
        offset = target_point - current_point
        slider.send_keys(Keys.ARROW_RIGHT * offset)

def set_rgb(red: int, green: int, blue: int):
    # Слайдеры для каждого цвета
    red_slider = driver.find_element(*RED_SLIDER_LOCATOR)
    green_slider = driver.find_element(*GREEN_SLIDER_LOCATOR)
    blue_slider = driver.find_element(*BLUE_SLIDER_LOCATOR)

    # Текущие позиции слайдера
    red_slider_position = int(red_slider.get_attribute("aria-valuenow"))
    green_slider_position = int(green_slider.get_attribute("aria-valuenow"))
    blue_slider_position = int(blue_slider.get_attribute("aria-valuenow"))

    # Смещение
    move_slider(red_slider, red, red_slider_position)
    move_slider(green_slider, green, green_slider_position)
    move_slider(blue_slider, blue, blue_slider_position)

    final_color = driver.find_element(*FINAL_COLOR_LOCATOR).get_attribute("style")
    assert f"rgb({red}, {green}, {blue})" in final_color

time.sleep(5)
set_rgb(red=255, green=0, blue=188)
time.sleep(3)
