from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lesson11.models.locator import AdminPageLocators, DashboardLocators
from lesson11.models.locator import MainPageLocators, ProductPageLocators
from lesson11.models.page import BasePage


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


class DashboardPage(BasePage):

    def get_add_nav_bar(self):
        try:
            return self.driver.find_element(*DashboardLocators.ADD_MENU)
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def click_menu_item(self, nav_menu, item_name, delay):
        try:
            WebDriverWait(nav_menu, delay).until(EC.presence_of_element_located(DashboardLocators.DROPDOWN_MENU))
            menu = self.driver.find_element(*DashboardLocators.DROPDOWN_MENU)
            items = menu.find_elements(*DashboardLocators.MENU_ITEMS)
            for item in items:
                if item.text == item_name:
                    item.click()
                    break
        except (NoSuchElementException, TimeoutException):
            raise AssertionError("Item not founded!")

    def set_product_name(self, product_name):
        try:
            input_field = self.driver.find_element(*DashboardLocators.PRODUCT_NAME_INPUT)
            self._clear_element_(input_field)
            input_field.send_keys(product_name)
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def get_nav_bar(self):
        try:
            return self.driver.find_element(*DashboardLocators.NAV_BAR)
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def open_nav_bar_element(self, nav_bar, element_name):
        nav_items = nav_bar.find_elements(*DashboardLocators.MENU_ITEMS)
        for item in nav_items:
            if item.text == element_name:
                item.click()

    def set_product_code(self, product_code):
        try:
            product_code_field = self.driver.find_element(*DashboardLocators.PRODUCT_MODEL_INPUT)
            self._clear_element_(product_code_field)
            product_code_field.send_keys(product_code)
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def click_add_image_btn(self):
        try:
            self.driver.find_element(*DashboardLocators.ADD_IMAGE_BUTTON).click()
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def set_product_image(self, image_number, image_path, delay):
        try:
            images_table = self.driver.find_element(*DashboardLocators.IMAGES_TABLE)
            images = images_table.find_elements(*DashboardLocators.TABLE_ROWS)
            if image_number > len(images):
                raise AssertionError("Wrong image number!")
            images[image_number].find_element(*DashboardLocators.IMAGE_TAG).click()
            self.driver.find_element(*DashboardLocators.EDIT_IMAGE_BUTTON).click()
            WebDriverWait(self.driver, delay).\
                until(EC.presence_of_element_located(DashboardLocators.UPLOAD_IMAGE_BUTTON))
            self.driver.find_element(*DashboardLocators.UPLOAD_IMAGE_BUTTON).send_keys(image_path)
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def click_save_btn(self):
        try:
            self.driver.find_element(*DashboardLocators.SAVE_BUTTON).click()
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def click_btn_menu(self):
        try:
            self.driver.find_element(*DashboardLocators.MENU_BUTTON).click()
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def get_catalog_menu(self):
        try:
            return self.driver.find_element(*DashboardLocators.CATALOG_MENU).click()
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def click_catalog_item(self, catalog, item_name):
        items = catalog.find_elements(*DashboardLocators.MENU_ITEMS)
        for item in items:
            if item.text == item_name:
                item.click()
                break

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

    def _get_product_list(self, delay):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(ProductPageLocators.PRODUCT_TABLE))
            return self.driver.find_element(*ProductPageLocators.PRODUCT_TABLE)
        except NoSuchElementException:
            return False

    def get_left_menu(self):
        try:
            return self.driver.find_element(*DashboardLocators.LEFT_MENU)
        except NoSuchElementException:
            raise AssertionError("Element not founded!")

    def get_design_subsection(self):
        try:
            return self.driver.find_element(*DashboardLocators.MENU_DESIGN)
        except NoSuchElementException:
            return False

    def click_subsection_item(self, subsection, item_name, delay):
        WebDriverWait(subsection, delay).until(EC.presence_of_element_located(DashboardLocators.MENU_ITEMS))
        items = subsection.find_elements(*DashboardLocators.MENU_ITEMS)
        for item in items:
            if item.text == item_name:
                item.click()
                break

    def select_category(self, category_name, delay):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(DashboardLocators.CATEGORY_ITEMS))
            categories = self.driver.find_elements(*DashboardLocators.CATEGORY_ITEMS)
            print(len(categories))
            for category in categories:
                if category_name in category.text:
                    return category
            return False
        except TimeoutException:
            raise AssertionError("Element not founded!")

    def drag_and_drop_element(self, element, x, y):
        ActionChains(self.driver).drag_and_drop_by_offset(element, x, y).perform()

    def get_element_y(self, element):
        return element.location.get("y")

    def get_element_x(self, element):
        return element.location.get("x")

    def set_download_name(self, download_name):
        self.driver.find_element(*DashboardLocators.DOWNLOAD_NAME).send_keys(download_name)

    def set_download_mask(self, download_mask):
        self.driver.find_element(*DashboardLocators.DOWNLOAD_MASK).send_keys(download_mask)

    def add_download_file(self, file_path):
        upload_btn = self.driver.find_element(*DashboardLocators.DOWNLOAD_BUTTON).send_keys(file_path)
        self.driver.execute_script("HTMLInputElement.prototype.click = function(){"
                                   "    if(this.type != 'file') HTMLElement.prototype.click.call(this);"
                                   "};")
        inputs = upload_btn.find_element_by_name("file")
        print(inputs.text)
