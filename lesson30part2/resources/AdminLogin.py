from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from locator import AdminPageLocators
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = "D:\\drivers\\"


class AdminLogin:

    def __init__(self):
        self.driver = None

    @keyword("AdminPage.Set Webdriver")
    def admin_set_webdriver(self, browser_name="firefox"):
        if browser_name == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("-headless")
            execute_path = DRIVER_PATH + "geckodriver.exe"
            wd = webdriver.Firefox(options=firefox_options, executable_path=execute_path)
        else:
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")
            execute_path = DRIVER_PATH + "chromedriver.exe"
            wd = webdriver.Chrome(options=chrome_options, executable_path=execute_path)
        wd.maximize_window()
        self.driver = wd

    @keyword("AdminPage.Open Opencart")
    def admin_open_opencart(self, address):
        url = "{}/opencart/admin".format(address)
        self.driver.get(url)

    @keyword("AdminPage.Close Browser")
    def admin_close_browser(self):
        self.driver.quit()

    @keyword("AdminPage.Input Username")
    def admin_input_username(self, username):
        self.driver.find_element(*AdminPageLocators.USERNAME).send_keys(username)

    @keyword("AdminPage.Input Password")
    def admin_input_password(self, password):
        self.driver.find_element(*AdminPageLocators.PASSWORD).send_keys(password)

    @keyword("AdminPage.Click Submit Button")
    def admin_click_submit_button(self):
        self.driver.find_element(*AdminPageLocators.LOGIN_BTN).click()

    @keyword("AdminPage.Check Admin Dashboard")
    def admin_check_admin_dashboard(self, delay=10):
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(AdminPageLocators.NAVIGATION))
        dashboard = self.driver.find_element(*AdminPageLocators.NAVIGATION).text
        if dashboard not in "Navigation":
            assert AssertionError("Dashboard element not found!")
