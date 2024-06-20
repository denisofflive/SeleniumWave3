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

driver.find_element("xpath", "//a[@href='#example-1']").click()

def move_slider(slider_locator: tuple, current_point_atr_name: str, target_point: int):
    """
    Данная функция перемещает горизонтальный слайдер
    :param slider_locator: Локатор слайдера
    :param current_point_atr_name: Имя атрибута, отвечающего за текущую позицию
    :param target_point: Конечная точка сдвига
    :return:
    """
    slider = driver.find_element(*slider_locator)
    current_position = int(slider.get_attribute(current_point_atr_name))

    if target_point < 0 or target_point > 20:
        raise AssertionError("Нельзя так")
    elif target_point > current_position:
        offset = target_point - current_position
        slider.send_keys(Keys.ARROW_RIGHT * offset)
    elif target_point < current_position:
        offset = current_position - target_point
        slider.send_keys(Keys.ARROW_LEFT * offset)

SLIDER_LOCATOR = ("xpath", "(//div[@id='example-1']//div[@role='slider'])[1]")
time.sleep(3)
move_slider(SLIDER_LOCATOR, current_point_atr_name="aria-valuenow", target_point=23)
time.sleep(5)
