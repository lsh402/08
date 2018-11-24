from selenium import webdriver


def init_driver():
    driver = webdriver.Firefox()
    driver.get("http://www.yhd.com/")
    driver.implicitly_wait(10)
    return driver
