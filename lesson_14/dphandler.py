import time
from selenium.webdriver.chrome.webdriver import WebDriver

months = {
    1: "январь",
    2: "февраль",
    3: "март",
    4: "апрель",
    5: "май",
    6: "июнь",
    7: "июль",
    8: "август",
    9: "сентябрь",
    10: "октябрь",
    11: "ноябрь",
    12: "декабрь"
}

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
        target_month_year = f"{months[month]} {year}"
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
