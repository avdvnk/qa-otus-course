from lesson5.models.locator import MainPageLocators
from lesson5.models.page import BasePage


class MainPage(BasePage):

    def get_dashboard(self):
        return self.driver.find_element(*MainPageLocators.DASHBOARD).text
