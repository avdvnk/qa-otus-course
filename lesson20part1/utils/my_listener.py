import logging

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

from lesson20part1.utils.my_logger import MyLogger


class MyListener(AbstractEventListener):

    def __init__(self, db_name):
        self.db_name = db_name

    def before_find(self, by, value, driver):
        output = "Trying to find [{}:{}]".format(by, value)
        logging.log(3, output)
        MyLogger.write_to_db(self.db_name, output, MyLogger.get_datetime())

    def after_find(self, by, value, driver):
        output = "[{}:{}] found".format(by, value)
        logging.log(3, output)
        MyLogger.write_to_db(self.db_name, output, MyLogger.get_datetime())

    def on_exception(self, exception, driver):
        time = MyLogger.get_datetime()
        logging.log(1, exception)
        MyLogger.write_to_db(self.db_name, exception, time)
        driver.save_screenshot("screenshots/{}.png".format(time))
