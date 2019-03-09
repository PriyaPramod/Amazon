from selenium.webdriver.common.action_chains import ActionChains


def move_to_element(driver, element):
    action = ActionChains(driver)
    action.move_to_element(element)
    action.pause(2)
    action.perform()