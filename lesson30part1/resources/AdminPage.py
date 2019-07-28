from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC

from locator import AdminPageLocators, ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait

DRIVER_PATH = "D:\\drivers\\"


class AdminPage:

    def __init__(self):
        self.driver = None

    def set_browser(self, browser_name="firefox"):
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

    def close_browser(self):
        self.driver.quit()

    def input_username(self, username):
        self.driver.find_element(*AdminPageLocators.USERNAME).send_keys(username)
        self.driver.save_screenshot("./reports/input_username.png")

    def input_password(self, password):
        self.driver.find_element(*AdminPageLocators.PASSWORD).send_keys(password)
        self.driver.save_screenshot("./reports/input_password.png")

    def click_submit_button(self):
        self.driver.find_element(*AdminPageLocators.LOGIN_BTN).click()
        self.driver.save_screenshot("./reports/click_submit_button.png")

    def open_page(self, address):
        self.driver.get(address)
        self.driver.save_screenshot("./reports/open_{}.png".format(address))

    def click_catalog(self, delay=20):
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(AdminPageLocators.CATALOG))
        self.driver.find_element(*AdminPageLocators.CATALOG).click()
        self.driver.save_screenshot("./reports/click_catalog.png")

    def click_products(self):
        self.driver.find_element(*AdminPageLocators.PRODUCTS).click()
        self.driver.save_screenshot("./reports/click_products.png")

    def click_add_product(self):
        self.driver.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.driver.save_screenshot("./reports/click_add_product.png")

    def input_product_name(self, name):
        self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(name)
        self.driver.save_screenshot("./reports/input_product_name.png")

    def input_product_tag(self, tag):
        self.driver.find_element(*ProductPageLocators.META_TAG).send_keys(tag)
        self.driver.save_screenshot("./reports/input_product_tag.png")

    def click_data_tab(self):
        self.driver.find_element(*ProductPageLocators.DATA_TAB).click()
        self.driver.save_screenshot("./reports/click_data_tab.png")

    def input_product_model(self, model):
        self.driver.find_element(*ProductPageLocators.MODEL).send_keys(model)
        self.driver.save_screenshot("./reports/input_product_model.png")

    def click_save_button(self):
        self.driver.find_element(*ProductPageLocators.SAVE_BUTTON).click()
        self.driver.save_screenshot("./reports/click_save_button.png")

    def select_product(self, model):
        products = self.driver.find_elements(*ProductPageLocators.PRODUCTS)
        for product in products:
            if product.find_elements(*ProductPageLocators.ROW_COLUMN)[3].text == model:
                product.find_elements(*ProductPageLocators.ROW_COLUMN)[0].click()
                self.driver.save_screenshot("./reports/select_product.png")
                break

    def click_remove_button(self):
        self.driver.find_element(*ProductPageLocators.REMOVE_BUTTON).click()
        self.driver.save_screenshot("./reports/click_remove_button.png")

    def confirm_remove(self, delay=10):
        WebDriverWait(self.driver, float(delay)).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        self.driver.save_screenshot("./reports/confirm_remove.png")
        sleep(3)
