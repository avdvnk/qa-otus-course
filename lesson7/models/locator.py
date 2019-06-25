from selenium.webdriver.common.by import By


class BaseLocators(object):
    PRIMARY_BUTTON = (By.CLASS_NAME, "btn.btn-primary")


class MainPageLocators(object):
    DASHBOARD = (By.XPATH, "//a[@href='http://192.168.0.108/opencart/index.php?route=common/home']")


class AdminPageLocators:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@class='btn btn-primary']")
    DASHBOARD = (By.CSS_SELECTOR, "a.navbar-brand")
    CUSTOMERS = (By.ID, "menu-customer")
    MENU = (By.ID, "menu")
    EXTENSION = (By.ID, "menu-extension")
    MENU_ITEMS = (By.TAG_NAME, "li")
    ATTRIBUTES = (By.XPATH, "//a[@href='http://192.168.0.108/opencart/admin/#collapse1-4']")
    RECENT_ACTIVITY = (By.CSS_SELECTOR, "div.panel panel-default")
    CATALOG = (By.ID, "menu-catalog")
    PRODUCTS = (By.XPATH, "//a[href='']")


class ProductPageLocators:
    ADD_BUTTON = (By.XPATH, "//a[@data-original-title='Add New']")
    PRODUCT_NAME = (By.XPATH, "//input[@placeholder='Product Name']")
    META_TAG = (By.XPATH, "//input[@placeholder='Meta Tag Title']")
    NAV_BAR = (By.XPATH, "//ul[@class='nav nav-tabs']")
    MODEL = (By.XPATH, "//input[@placeholder='Model']")
    SAVE_BUTTON = (By.XPATH, "//button[@data-original-title='Save']")
    PRODUCT_TABLE = (By.XPATH, "//table[@class='table table-bordered table-hover']")
    TABLE_BODY = (By.TAG_NAME, "tbody")
    NAV_TABS = (By.TAG_NAME, "li")
    TABLE_ROW = (By.TAG_NAME, "tr")
    ROW_COLUMN = (By.TAG_NAME, "td")
    REMOVE_BUTTON = (By.XPATH, "//button[@data-original-title='Delete']")
    DESCRIPTION_FIELD = (By.XPATH, "//div[@class='note-editable panel-body']")
