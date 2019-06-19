from selenium.webdriver.common.by import By


class BaseLocators(object):
    PRIMARY_BUTTON = (By.CLASS_NAME, "btn.btn-primary")


class MainPageLocators(object):

    DASHBOARD = (By.XPATH, "//h1[@class='panel-title']")
