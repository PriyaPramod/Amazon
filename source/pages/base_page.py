from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        
    @allure.step   
    def verify_title(self, title):
        flag = False
        wait = WebDriverWait(self.driver, 30)
        try:
            flag = wait.until(ec.title_contains(title), 
                              "Verifying the title: "+title)
            return flag
        except TimeoutException:
            print("Title is not loaded: ",title)
            return flag

    def find_element(self, By, attribute_value):
        web_element = None
        try:
            web_element = self.driver.find_element(By, attribute_value)
        except NoSuchElementException:
            print("Web element not found: ", NoSuchElementException)
        
        return web_element
    
    def click(self, By, attribute_value):
        try:
            web_element = self.find_element(By, attribute_value)
            web_element.click()
        except Exception:
            print("Unable to click on the web element: ", Exception)
        
    def send_keys(self, By, attribute_value, value_to_enter):
        try:
            web_element = self.find_element(By, attribute_value)
            web_element.send_keys(str(value_to_enter))
        except Exception:
            print("Unable to enter the value to the web element: ", Exception)
            
            
    
    
    
