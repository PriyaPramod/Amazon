'''
Created on 09-Mar-2019

@author: PriyaPramod
'''
from selenium.webdriver.common.by import By

from source.pages.base_page import BasePage
from source.utilities.selenium_actions import move_to_element


class DashBoardPage(BasePage):
    
    __your_order = (By.XPATH, "//span[text()='Hello, Sign in']/../span[2]")
    __sing_in = (By.XPATH, "(//span[@class='nav-action-inner'])[1]")

    def click_on_sing_in(self):
        move_to_element(self.driver, self.find_element(*self.__your_order))
        self.click(*self.__sing_in)
