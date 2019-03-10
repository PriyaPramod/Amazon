from selenium import webdriver
from source.utilities import const
from source.utilities import helpers


def create_driver(browser_name, url):
    driver = None
    hub_url = "http://192.168.88.2:4444/wd/hub"
    chrome_capability = {"platform":"windows",
                         "browserName":"chrome"}
    
    ff_capability = {"platform":"windows",
                         "browserName":"firefox"}
    
    if browser_name == "Chrome":
        driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=chrome_capability)
    elif browser_name == "ff":
        driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=ff_capability)
    
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(helpers.get_itime())
    
    return driver