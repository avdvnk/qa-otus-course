from selenium.webdriver.common.by import By


class BaseLocators(object):
    PRIMARY_BUTTON = (By.CLASS_NAME, "btn.btn-primary")


class MainPageLocators(object):

    DASHBOARD = (By.XPATH, "//a[@href='http://192.168.0.108/opencart/index.php?route=common/home']")
