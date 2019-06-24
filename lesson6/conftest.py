import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions

DRIVER_PATH = "D:\\drivers\\"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--address", action="store", default="http://192.168.0.108/", help='Opencart address')


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("-headless")
        execute_path = DRIVER_PATH + "geckodriver.exe"
        wd = webdriver.Firefox(options=firefox_options, executable_path=execute_path)
    elif browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        execute_path = DRIVER_PATH + "chromedriver.exe"
        wd = webdriver.Chrome(options=chrome_options, executable_path=execute_path)
    else:
        ie_options = IEOptions()
        wd = webdriver.Ie()
    wd.maximize_window()
    yield wd
    wd.quit()
