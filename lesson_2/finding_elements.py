import time
from selenium import webdriver

driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")

## Примеры

# print (driver.find_element(By.CLASS_NAME, "MuiAvatar-img css-1hy9t21"))
# print(driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input"))
# print(driver.find_element(By.TAG_NAME, "form"))

# driver.find_element("id", "Wikipedia1_wikipedia-search-input")
# elements = driver.find_elements("tag name", "button")
# for element in elements:
#     element.click()
#     time.sleep(2)

driver.get("https://the-internet.herokuapp.com/download")
time.sleep(3)
elements = driver.find_elements("tag name", "a")
del elements[0]

for element in elements:
    # element.click()
    print(element.text)
    # time.sleep(1)


