from selenium import webdriver
from source.utilities import const
from source.utilities import helpers


def create_driver(browser_name, url):
    driver = None
    if browser_name == "Chrome":
        driver = webdriver.Chrome(executable_path=const.CHROME_VALUE)
    elif browser_name == "ff":
        driver = webdriver.Firefox(executable_path=const.FF_VALUE)
    
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(helpers.get_itime())
    
    return driver