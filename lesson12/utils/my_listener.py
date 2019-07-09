import logging

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

from lesson12.utils.my_logger import MyLogger


class MyListener(AbstractEventListener):

    def __init__(self, filename):
        self.filename = filename

    def before_find(self, by, value, driver):
        output = "Trying to find [{}:{}]".format(by, value)
        logging.log(3, output)
        MyLogger.write_to_file(self.filename, output, MyLogger.get_datetime())

    def after_find(self, by, value, driver):
        output = "[{}:{}] found".format(by, value)
        logging.log(3, output)
        MyLogger.write_to_file(self.filename, output, MyLogger.get_datetime())

    def on_exception(self, exception, driver):
        time = MyLogger.get_datetime()
        logging.log(1, exception)
        MyLogger.write_to_file(self.filename, exception, time)
        driver.save_screenshot("screenshots/{}.png".format(time))
