import datetime
import logging
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

from lesson11.utils.logger import Logger


class MyListener(AbstractEventListener):
    def __init__(self, logfile):
        super()
        self.filename = logfile

    def before_find(self, by, value, driver):
        info = "INFO", "Trying to find {} {}".format(by, value)
        logging.log(3, info)
        Logger.write_logs(self.filename, info)

    def after_find(self, by, value, driver):
        info = "INFO", "{} {} founded!".format(by, value)
        logging.log(3, info)
        Logger.write_logs(self.filename, info)

    def on_exception(self, exception, driver):
        current_time = datetime.datetime.now()
        logging.log(1, exception)
        Logger.write_logs(self.filename, exception)
        logger_time = "{} {}:{}:{}".format(current_time.date(),
                                           current_time.hour, current_time.minute, current_time.second)
        driver.save_screenshot("screenshots/{}".format(logger_time))
