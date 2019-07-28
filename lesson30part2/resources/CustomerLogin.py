from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locator import CustomerPageLocators

DRIVER_PATH = "D:\\drivers\\"


class CustomerLogin:

    def __init__(self):
        self.driver = None

    @keyword("CustomerPage.Set Webdriver")
    def customer_set_webdriver(self, browser_name="firefox"):
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

    @keyword("CustomerPage.Open Opencart")
    def customer_open_opencart(self, address):
        url = "{}/opencart/".format(address)
        self.driver.get(url)

    @keyword("CustomerPage.Close Browser")
    def customer_close_browser(self):
        self.driver.quit()

    @keyword("CustomerPage.Check Dashboard Page")
    def customer_check_dashboard_page(self, delay=10):
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(CustomerPageLocators.DASHBOARD))
        dashboard = self.driver.find_element(*CustomerPageLocators.DASHBOARD).text
        if dashboard not in "Your Store":
            assert AssertionError("Wrong dashboard")

