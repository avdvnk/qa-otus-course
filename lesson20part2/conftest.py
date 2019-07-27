import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from lesson20part2.models.page_objects.page_objects import AdminPage, DashboardPage

DRIVER_PATH = "D:\\drivers\\"
DB_CONNECT = [{"host": "192.168.0.108", "port": 3306,
               "username": "username", "password": "password",
               "db_name": "opencart"}]
COUPONS = [{"name": "TestName", "code": "9999", "type": "P", "discount": 0.0,
            "logged": 0, "shipping": 1, "total": 100.0, "date_start": "2019-07-11",
            "date_end": "2019-07-22", "uses_total": 10, "uses_customers": 10,
            "status": 0, "date_added": "2019-07-01 23:43:17"}]


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
        firefox_options = FirefoxOptions()
        # firefox_options.add_argument("-headless")
        execute_path = DRIVER_PATH + "geckodriver.exe"
        wd = webdriver.Firefox(options=firefox_options, executable_path=execute_path)
    else:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        execute_path = DRIVER_PATH + "chromedriver.exe"
        wd = webdriver.Chrome(options=chrome_options, executable_path=execute_path)
    wd.maximize_window()
    yield wd
    wd.quit()


@pytest.fixture()
def admin_address(request):
    return request.config.getoption("address") + "/opencart/admin"


@pytest.fixture()
def admin_data(request):
    return request.config.getoption("login"), request.config.getoption("password")


@pytest.fixture(params=DB_CONNECT)
def db_info(request):
    return request.param


@pytest.fixture(params=COUPONS)
def coupon(request):
    return request.param


@pytest.fixture()
def delay(request):
    return float(request.config.getoption("delay"))


@pytest.fixture()
def dashboard_page(driver, admin_address, admin_data):
    page = AdminPage(driver)
    page.driver.get(admin_address)
    page.login(admin_data[0], admin_data[1])
    return DashboardPage(page.driver)
