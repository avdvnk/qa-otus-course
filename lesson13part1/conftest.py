import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from lesson12.utils.my_listener import MyListener

DRIVER_PATH = "C:\\PyProjects\\drivers\\"
LOG_FILENAME = "my_log.txt"
GRID_HOST = "http://localhost:4444/wd/hub"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--address", action="store", default="http://192.168.0.108/", help="Opencart address")
    parser.addoption("--login", action="store", default="admin", help="Admin login")
    parser.addoption("--password", action="store", default="qwerty", help="Admin password")
    parser.addoption("--delay", action="store", default=25, help="Waiting delay")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        desired_capabilities = {
            "browserName": "firefox"
        }
    else:
        desired_capabilities = {
            "browserName": "chrome"
        }
    wd = webdriver.Remote(command_executor=GRID_HOST, desired_capabilities=desired_capabilities)
    wd = EventFiringWebDriver(wd, MyListener(LOG_FILENAME))
    wd.maximize_window()
    yield wd
    wd.quit()
