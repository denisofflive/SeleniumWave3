import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://www.freeconferencecall.com/ru/ru/login")

print(driver.get_cookie("_freeconferencecall_session"))

driver.delete_cookie("_freeconferencecall_session")
driver.add_cookie(
    {
        "name": "_freeconferencecall_session",
        "value": "ttwBF0l8P0WorTdBfu1qHJghuIsqVblsFzw2gcCGHYhIK8kCmHLdTu6SBkokkzg4NhQ9IlSEHLq5Wws5B6q8TQvi9vlZDgHbo4MOYmGyPqLURyBo2eVJ8CJ%2BxyKYCBswto1yfgl3Uiy76Q8%2BX%2BRq0i4DdeaDqbNqDu73x9KBveyaSx8bZTTp9p%2B1V12Dl%2BsMrjky26NFmf4969mNpFsclZOtPxqBuINiXBEx6Q9W7WA4VtXnV9WnTPnXYwPhUoYS6jbq1SLFbaszxo3R2QSlrt%2FIcgFB%2BiNyGYrwBEcNwSMsU1KkUESP70Qvi1bYRbWbcjH5Q%2BCCtM84EYzmzqsZOJXQ4dftfSLbvGr5rh9%2BAKqMKIIcTrDCYeDGllWSs3bhLakQHm6POKUYYYuHDpdvnDcOFrCDJQYpY9FIlB5tz7Ey5k4qbvE0kt2GVmL2sJE%3D--gpyEM7aI29GQN9Vo--RBoN7MFddlQae2zKxkHIaw%3D%3D"
    }
)

print(driver.get_cookie("_freeconferencecall_session"))
driver.refresh()
time.sleep(5)
