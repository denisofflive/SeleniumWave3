import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

ACCEPT_COOKIES = ("xpath", "//button[@id='onetrust-accept-btn-handler']")
# Ссылка на Datepicker - выбор даты в календаре
driver.get("https://www.booking.com/")
wait.until(EC.element_to_be_clickable(ACCEPT_COOKIES)).click()
time.sleep(5)

class DatePickerHandler:
    DATEPICKER_TRIGGER_BUTTON = ("xpath", "//button[@data-testid = 'date-display-field-end']")
    DATEPICKER = ("xpath", "//div[@id='calendar-searchboxdatepicker']")
    CALENDAR_MONTH_AND_YEAR = ("xpath", ".//h3[1]")
    NEXT_MONTH_BUTTON = ("xpath", "//div[@id='calendar-searchboxdatepicker']//button[@aria-label='Следующий месяц']")
    DAY_LOCATOR = ("xpath", ".//div[table][1]//td[.//span]")
    PM_DAYS = ("xpath", "//div[@data-testid='flexible-dates-container']//label[./input]")
    PM_STATUS = ("xpath", ".//input")


    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.find_element(*self.DATEPICKER_TRIGGER_BUTTON).click()
        time.sleep(3)

    def set_date(self, day, month, year):
        datepicker = self.driver.find_element(*self.DATEPICKER)
        target_month_year = f"{month} {year}"
        while target_month_year not in datepicker.find_element(*self.CALENDAR_MONTH_AND_YEAR).text:
            self.next_month()
            time.sleep(0.5)
        days = datepicker.find_elements(*self.DAY_LOCATOR)
        for element in days:
            if str(day) in element.text:
                element.click()
                break

    def plus_minus(self, days):
        elements = self.driver.find_elements(*self.PM_DAYS)
        for element in elements:
            if str(days) in element.text:
                element.click()
                element.find_element(*self.PM_STATUS).is_selected()
                break

    def next_month(self):
        datepicker = self.driver.find_element(*self.DATEPICKER)
        datepicker.find_element(*self.NEXT_MONTH_BUTTON).click()


datepicker = DatePickerHandler(driver)
datepicker.open()
datepicker.set_date(21, "декабрь", 2024)
datepicker.set_date(15, "март", 2025)
datepicker.plus_minus(7)

time.sleep(3)

