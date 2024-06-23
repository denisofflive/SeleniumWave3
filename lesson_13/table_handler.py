from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class TableHandler:

    TABLE_LOCATOR = ("xpath", "//div[@role='grid']")
    ROWS_LOCATOR = ("xpath", ".//div[@class='oxd-table-card']//div[@role='row']")
    CELLS_LOCATOR = ("xpath", ".//div[@role='cell']")
    DELETE_LOCATOR = ("xpath", ".//div[@class='oxd-table-cell-actions']//button[.//i[contains(@class, 'bi-trash')]]")
    EDIT_LOCATOR = ("xpath", ".//div[@class='oxd-table-cell-actions']//button[.//i[contains(@class, 'bi-pencil-fill')]]")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    @property
    def _table(self):
        return self.driver.find_element(*self.TABLE_LOCATOR)

    @property
    def _rows(self) -> list[WebElement]:
        table = self._table
        return table.find_elements(*self.ROWS_LOCATOR)

    @property
    def row_count(self):
        return len(self._rows)

    def get_cell_content(self, row_number, column_number):
        row = self._rows[row_number - 1]
        cell = row.find_elements(*self.CELLS_LOCATOR)[column_number - 1]
        return cell.text

    def get_row_content(self, row_number):
        row = self._rows[row_number - 1]
        # content = []
        # for cell in row.find_elements(*self.CELLS_LOCATOR):
        #     content.append(cell.text)
        # return content
        return [cell.text for cell in row.find_elements(*self.CELLS_LOCATOR)]

    def get_column_content(self, column_number):
        column_content = []
        rows = self._rows

        # for row in self._rows:
        #     column_content.append(self.get_cell_content(rows.index(row) + 1, column_number))
        # return column_content

        for row in self._rows:
            cells = row.find_elements(*self.CELLS_LOCATOR)
            column_content.append(cells[column_number - 1].text)
        return column_content

    def select_row(self, row_number):
        row = self._rows[row_number - 1]
        cell = row.find_elements(*self.CELLS_LOCATOR)[0]
        cell.click()

    def select_row2(self, row_number):
        row = self._rows[row_number - 1]
        if "Admin" in self.get_row_content(row_number):
            raise AssertionError ("YOU SHALL NOT PASS")
        else:
            cell = row.find_elements(*self.CELLS_LOCATOR)[0]
            cell.click()

    def edit_row(self, row_number):
        row = self._rows[row_number - 1]
        row.find_element(*self.EDIT_LOCATOR).click()

    def delete_row(self, row_number):
        row = self._rows[row_number - 1]
        row.find_element(*self.DELETE_LOCATOR).click()

    def delete_row2(self, row_number):
        row = self._rows[row_number - 1]
        if "Admin" in self.get_row_content(row_number):
            raise AssertionError("YOU SHALL NOT PASS")
        else:
            row.find_element(*self.DELETE_LOCATOR).click()

    def edit_row_by_username(self, username):
        rows = self._rows
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                cell = row.find_elements(*self.EDIT_LOCATOR)[0]
                cell.click()

