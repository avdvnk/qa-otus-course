from lesson5.models.locator import MainPageLocators
from lesson5.models.page import BasePage
from lesson6.models.locator import AdminPageLocators


class MainPage(BasePage):

    def get_dashboard(self):
        return self.driver.find_element(*MainPageLocators.DASHBOARD).text


class AdminPage(BasePage):

    def login(self, username, password):
        input_login = self.driver.find_element(*AdminPageLocators.USERNAME)
        input_password = self.driver.find_element(*AdminPageLocators.PASSWORD)
        login_btn = self.driver.find_element(*AdminPageLocators.LOGIN_BTN)
        input_login.send_keys(username)
        input_password.send_keys(password)
        login_btn.click()

    def get_dashboard(self):
        dashboard = self.driver.find_elements(*AdminPageLocators.DASHBOARD)
        if len(dashboard) == 0:
            return False
        return dashboard[0]

    def get_customers(self):
        customers = self.driver.find_elements(*AdminPageLocators.CUSTOMERS)
        if len(customers) == 0:
            return False
        return customers[0]

    def get_menu_count(self):
        extension = self.driver.find_element(*AdminPageLocators.EXTENSION)
        extension.click()
        extension_items = extension.find_elements(*AdminPageLocators.MENU_ITEMS)
        return len(extension_items)

    def get_username(self):
        username = self.driver.find_elements(*AdminPageLocators.USERNAME)
        if len(username) == 0:
            return False
        return username

    def get_attributes(self):
        attributes = self.driver.find_elements(*AdminPageLocators.ATTRIBUTES)
        if len(attributes) == 0:
            return False
        return attributes

    def get_recent_activity(self):
        recent_activity = self.driver.find_elements(*AdminPageLocators.RECENT_ACTIVITY)
        if len(recent_activity) == 0:
            return False
        return recent_activity
