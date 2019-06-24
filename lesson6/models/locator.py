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
