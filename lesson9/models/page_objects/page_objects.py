from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lesson9.models.locator import AdminPageLocators
from lesson9.models.locator import MainPageLocators, ProductPageLocators
from lesson9.models.page import BasePage


class MainPage(BasePage):

    def get_dashboard(self):
        return self.driver.find_element(*MainPageLocators.DASHBOARD).text


class AdminPage(BasePage):

    def login(self, username, password):
        try:
            input_login = self.driver.find_element(*AdminPageLocators.USERNAME)
            input_password = self.driver.find_element(*AdminPageLocators.PASSWORD)
            login_btn = self.driver.find_element(*AdminPageLocators.LOGIN_BTN)
            input_login.send_keys(username)
            input_password.send_keys(password)
            login_btn.click()
        except NoSuchElementException:
            return False

    def get_catalog(self):
        try:
            return self.driver.find_element(*AdminPageLocators.CATALOG)
        except NoSuchElementException:
            return False

    def get_subselection(self, parent_selection, text):
        items = parent_selection.find_elements(*AdminPageLocators.MENU_ITEMS)
        for item in items:
            if item.text == text:
                return item
        return False


class ProductPage(BasePage):

    def _get_window_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")

    def _click_add_btn(self):
        try:
            self.driver.find_element(*ProductPageLocators.ADD_BUTTON).click()
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def _set_product_name(self, product_name):
        try:
            self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(product_name)
        except NoSuchElementException:
            raise AssertionError("Can't edit the element!")

    def _get_meta_tag(self):
        meta_tag = self.driver.find_elements(*ProductPageLocators.META_TAG)
        if len(meta_tag) == 0:
            return False
        return meta_tag[0]

    def _set_meta_tag(self, meta_tag):
        scroll_step = self._get_window_height() / 10
        start = 0
        end = scroll_step
        for i in range(10):
            meta_tag_element = self._get_meta_tag()
            if meta_tag_element:
                meta_tag_element.send_keys(meta_tag)
                break
            else:
                self.driver.execute_script("window.scrollTo({}, {})".format(start, end))
                start = end
                end += scroll_step

    def _set_model(self, model_name):
        try:
            model_field = self.driver.find_element(*ProductPageLocators.MODEL)
            self._clear_element_(model_field)
            model_field.send_keys(model_name)
        except NoSuchElementException:
            raise AssertionError("Can't get the element!")

    def _open_tab(self, tab_name):
        try:
            nav_bar = self.driver.find_element(*ProductPageLocators.NAV_BAR)
            tabs = nav_bar.find_elements(*ProductPageLocators.NAV_TABS)
            for tab in tabs:
                if tab.text == tab_name:
                    tab.click()
                    break
        except NoSuchElementException:
            raise AssertionError("Navigation bar not founded!")

    def _click_save_btn(self):
        try:
            self.driver.find_element(*ProductPageLocators.SAVE_BUTTON).click()
        except NoSuchElementException:
            raise AssertionError("Save button not founded!")

    def _click_remove_btn(self):
        try:
            self.driver.find_element(*ProductPageLocators.REMOVE_BUTTON).click()
        except NoSuchElementException:
            raise AssertionError("Remove button not founded!")

    def _get_product_list(self, delay):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(ProductPageLocators.PRODUCT_TABLE))
            return self.driver.find_element(*ProductPageLocators.PRODUCT_TABLE)
        except NoSuchElementException:
            return False

    def get_product(self, product_name, delay):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(ProductPageLocators.TABLE_BODY))
            tbody = self._get_product_list(delay).find_element(*ProductPageLocators.TABLE_BODY)
            products = tbody.find_elements(*ProductPageLocators.TABLE_ROW)
            for item in products:
                WebDriverWait(item, delay).until(EC.presence_of_element_located(ProductPageLocators.ROW_COLUMN))
                column_name = item.find_elements(*ProductPageLocators.ROW_COLUMN)[2]
                if column_name.text == product_name:
                    return item
            return False
        except (NoSuchElementException, TimeoutException):
            return False

    def _select_product(self, product):
        product.find_elements(*ProductPageLocators.ROW_COLUMN)[0].click()

    def _confirm_remove(self, delay):
        try:
            WebDriverWait(self.driver, float(delay)).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            sleep(3)
        except (TimeoutException, NoSuchElementException):
            raise AssertionError("Element not founded!")

    def _click_edit_btn(self, product):
        try:
            product.find_elements(*ProductPageLocators.ROW_COLUMN)[7].click()
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def _get_product_model(self, product):
        return product.find_elements(*ProductPageLocators.ROW_COLUMN)[3].text

    def _click_dropdown_toggle(self):
        try:
            self.driver.find_element(*ProductPageLocators.DROPDOWN_TOGGLE).click()
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def _get_dropdown_headers(self, delay):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(ProductPageLocators.DROPDOWN_HEADER))
            dropdown_headers = self.driver.find_elements(*ProductPageLocators.DROPDOWN_HEADER)
            if len(dropdown_headers) == 0:
                return False
            return dropdown_headers
        except (NoSuchElementException, TimeoutException):
            return False

    def add_product(self, product_name, meta_tag, product_model):
        self._click_add_btn()
        self._set_product_name(product_name)
        self._set_meta_tag(meta_tag)
        self._open_tab("Data")
        self._set_model(product_model)
        self._click_save_btn()

    def edit_product_model(self, product_element, new_model):
        self._click_edit_btn(product_element)
        self._open_tab("Data")
        self._set_model(new_model)
        self._click_save_btn()

    def remove_product(self, product_element, delay):
        self._select_product(product_element)
        self._click_remove_btn()
        self._confirm_remove(delay)

    def open_dropdown_toggle(self, delay):
        self._click_dropdown_toggle()
        return self._get_dropdown_headers(delay)
