from source.pages import page_managers as pm
from source.utilities import excel 
from source.utilities import const

def test_tc001_invalid_login(request):
    valid_user_name = excel.read_excel_data(const.EXCEL_PATH, "Setting", 0, "Phone_Email")
    invalid_user_name = excel.read_excel_data(const.EXCEL_PATH, "data", 0, "UserName")
    invalid_password = excel.read_excel_data(const.EXCEL_PATH, "data", 0, "Password")
    expected_user_error = excel.read_excel_data(const.EXCEL_PATH, "data", 0, "UserNameError")
    expected_Pass_error = excel.read_excel_data(const.EXCEL_PATH, "data", 0, "PasswordError")
    
    dash = pm.get_dashboard_page(request.node.driver)
    dash.click_on_sing_in()
    login = pm.get_login_page(request.node.driver)
    login.set_user_name(invalid_user_name)
    
    actual_user_error = login.get_login_error_message()
    
    assert expected_user_error == actual_user_error, "Actual error and expected error message for user name text box is not matching"
    login.set_user_name(valid_user_name)
    
    login.set_password(invalid_password)
    actual_pass_error = login.get_login_error_message()
    
    assert expected_Pass_error == actual_pass_error, "Actual error and expected error message for password text box is not matching"
    