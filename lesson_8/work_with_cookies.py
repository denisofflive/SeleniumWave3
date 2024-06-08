from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")
# print(driver.get_cookies())
# print(driver.get_cookie("1P_JAR"))
print(driver.get_cookie("QA"))
driver.add_cookie(
    {
        "name": "QA",
        "value": "PROKA4"
    }
)
print(driver.get_cookie("QA"))
driver.refresh()
print(driver.get_cookie("QA"))
