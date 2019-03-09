'''
Created on 09-Mar-2019

@author: PriyaPramod
'''
from source.pages.dashboard_page import DashBoardPage
from source.pages.login_page import LoginPage

def get_dashboard_page(driver):
    return DashBoardPage(driver)

def get_login_page(driver):
    return LoginPage(driver)