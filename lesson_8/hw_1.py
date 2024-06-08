from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")
print(driver.get_cookie("username"))

driver.add_cookie(
    {
        "name": "username",
        "value": "user123"
    }
)
print(driver.get_cookie("username"))
driver.refresh()
print(driver.get_cookie("username"))
