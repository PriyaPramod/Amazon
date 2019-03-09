from selenium.webdriver.common.by import By

from source.pages.base_page import BasePage


class LoginPage(BasePage):
    
    __user_name_tb = (By.ID, "ap_email")
    __continue_button = (By.ID, "continue")
    __login_error = (By.XPATH, "//span[@class='a-list-item']")
    __password_tb = (By.ID, "ap_password")
    __login_button = (By.ID, "signInSubmit")
    
        
    def set_user_name(self, email_phone):
        self.send_keys(*self.__user_name_tb, email_phone)
        self.click(*self.__continue_button)
        
    def get_login_error_message(self):
        ele = self.find_element(*self.__login_error)
        return ele.text
    
    def set_password(self, password):
        self.send_keys(*self.__password_tb, password)
        self.click(*self.__login_button)
        
    
    