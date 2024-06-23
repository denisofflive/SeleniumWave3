import time
from selenium import webdriver
from table_handler import TableHandler

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

table = TableHandler(driver)

driver.get("https://demoqa.com/webtables")
time.sleep(3)


print(table.row_count)
print(table.get_cell_content(1, 2))
print(table.get_row_content(2))
print(table.get_column_content(3))
# table.edit_row(1)
# table.delete_row(1)
time.sleep(3)
