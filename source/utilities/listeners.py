from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from source.utilities import helpers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Listen(AbstractEventListener):
    
    def after_find(self, by, value, driver):
        wait = WebDriverWait(driver, helpers.get_etime())
        wait.until(ec.element_to_be_clickable((by, value)), "Element is not visible or disabled")

    def before_change_value_of(self, element, driver):
        element.clear()

    def after_quit(self, driver):
        print("*****Test Ended*****")

    def on_exception(self, exception, driver):
        helpers.attach_screen_shot(driver, exception)
