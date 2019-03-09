import allure

from source.utilities import const
from source.utilities import excel


def get_itime():
    itime = excel.read_excel_data(const.EXCEL_PATH, "Setting", 0, "Iwait")
    return int(itime)

def get_etime():
    etime = excel.read_excel_data(const.EXCEL_PATH, "Setting", 0, "Ewait")
    return int(etime)   

def get_url():
    url = excel.read_excel_data(const.EXCEL_PATH, "Setting", 0, "URL")
    return url

def attach_screen_shot(driver, name):
    allure.attach(driver.get_screenshot_as_png(), name,
                      attachment_type=allure.attachment_type.PNG )