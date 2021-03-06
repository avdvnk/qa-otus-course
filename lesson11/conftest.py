import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from lesson11.utils.my_listener import MyListener

DRIVER_PATH = "D:\\drivers\\"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--address", action="store", default="http://192.168.0.108/", help="Opencart address")
    parser.addoption("--login", action="store", default="admin", help="Admin login")
    parser.addoption("--password", action="store", default="qwerty", help="Admin password")
    parser.addoption("--delay", action="store", default=25, help="Waiting delay")
    parser.addoption("--logfile", action="store", default="log_info.txt", help="Logger filename")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    log_filename = request.config.getoption("--logfile")
    if browser == "firefox":
        firefox_options = FirefoxOptions()
        # firefox_options.add_argument("-headless")
        execute_path = DRIVER_PATH + "geckodriver.exe"
        wd = webdriver.Firefox(options=firefox_options, executable_path=execute_path)
    else:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        execute_path = DRIVER_PATH + "chromedriver.exe"
        wd = webdriver.Chrome(options=chrome_options, executable_path=execute_path)
    wd = EventFiringWebDriver(wd, MyListener(log_filename))
    wd.maximize_window()
    yield wd
    wd.quit()
