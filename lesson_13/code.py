import time
from selenium import webdriver
from table_handler import TableHandler

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

table = TableHandler(driver)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# Login
USERNAME_LOCATOR = ("xpath", "//input[@name='username']")
PASSWORD_LOCATOR = ("xpath", "//input[@name='password']")
SUBMIT_BUTTON_LOCATOR = ("xpath", "//button[@type='submit']")

driver.find_element(*USERNAME_LOCATOR).send_keys("Admin")
driver.find_element(*PASSWORD_LOCATOR).send_keys("admin123")
driver.find_element(*SUBMIT_BUTTON_LOCATOR).click()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
time.sleep(3)

# print(table.row_count)
# print(table.get_cell_content(2, 3))
# print(table.get_row_content(2))
# print(table.get_column_content(3))
print(table.select_row(3))
# print(table.select_row2(1))
# table.edit_row(1)
# table.delete_row(1)
# table.delete_row2(1)
table.edit_row_by_username("Admin")
time.sleep(3)

# TABLE_LOCATOR = ("xpath", "//div[@role='table']")
# ROWS_LOCATOR = ("xpath", ".//div[@class='oxd-table-card']//div[@role='row']")
#
# table = driver.find_element(*TABLE_LOCATOR)
# rows = table.find_elements(*ROWS_LOCATOR)
