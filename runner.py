import pytest
import os
from datetime import datetime
from source.utilities import const


class MyClass():
    
    def pytest_sessionfinish(self):
        time_stamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        allure_command = "allure generate " +const.JSON_PATH+ " --output " +const.HTML_PATH + time_stamp
        os.popen(allure_command)

commands = ['-n', '2', '--alluredir', const.JSON_PATH]
pytest.main(commands, plugins=[MyClass()])
