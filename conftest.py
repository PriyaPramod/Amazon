import os

import pytest
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from source.utilities import const
from source.utilities import helpers
from source.utilities import webdriver_manager
from source.utilities.listeners import Listen


@pytest.fixture(scope='session', autouse=True)
def set_environ():
    os.environ[const.CHROME_KEY] = const.CHROME_VALUE 
    os.environ[const.FF_KEY] = const.FF_VALUE
    
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_"+rep.when, rep)
    return rep
    
@pytest.fixture(scope="function", params=['Chrome'], autouse=True)
def set_up_test(request):
    url = helpers.get_url()  
    web_driver = webdriver_manager.create_driver(request.param, url)
    driver = EventFiringWebDriver(web_driver, Listen())
    request.node.driver = driver
    yield
    if request.node.rep_call.failed:
        helpers.attach_screen_shot(driver, request.function.__name__)
    web_driver.close()
