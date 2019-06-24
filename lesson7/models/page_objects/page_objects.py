from lesson7.models.locator import MainPageLocators, ProductPageLocators
from lesson7.models.page import BasePage
from lesson7.models.locator import AdminPageLocators


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

    def get_catalog(self):
        return self.driver.find_element(*AdminPageLocators.CATALOG)

    def get_subselection(self, parent_selection, text):
        items = parent_selection.find_elements(*AdminPageLocators.MENU_ITEMS)
        for item in items:
            if item.text == text:
                return item
        return False


class ProductPage(BasePage):

    def get_window_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")

    def click_add_btn(self):
        self.driver.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def set_product_name(self, product_name):
        self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(product_name)

    def get_meta_tag(self):
        meta_tag = self.driver.find_elements(*ProductPageLocators.META_TAG)
        if len(meta_tag) == 0:
            return False
        return meta_tag[0]

    def set_meta_tag(self, meta_tag):
        scroll_step = self.get_window_height() / 10
        start = 0
        end = scroll_step
        for i in range(10):
            meta_tag_element = self.get_meta_tag()
            if meta_tag_element:
                meta_tag_element.send_keys(meta_tag)
                break
            else:
                self.driver.execute_script("window.scrollTo({}, {})".format(start, end))
                start = end
                end += scroll_step

    def set_model(self, model_name):
        self.driver.find_element(*ProductPageLocators.MODEL).send_keys(model_name)

    def open_tab(self, tab_name):
        nav_bar = self.driver.find_element(*ProductPageLocators.NAV_BAR)
        tabs = nav_bar.find_elements(*ProductPageLocators.NAV_TABS)
        for tab in tabs:
            if tab.text == tab_name:
                tab.click()
                break

    def click_save(self):
        self.driver.find_element(*ProductPageLocators.SAVE_BUTTON).click()

    def get_product_list(self):
        return self.driver.find_element(*ProductPageLocators.PRODUCT_TABLE)

    def get_product(self, product_name):
        tbody = self.get_product_list().find_element(*ProductPageLocators.TABLE_BODY)
        products = tbody.find_elements(*ProductPageLocators.TABLE_ROW)
        for item in products:
            column_name = item.find_elements(*ProductPageLocators.ROW_COLUMN)[2]
            if column_name.text == product_name:
                return item
        return False
