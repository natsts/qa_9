import datetime
import sys
import selene
import demoqa_tests.config
from selenium.webdriver.common.keys import Keys


class Datepicker:

    def __init__(self, element: selene.Element):
        self.element = element

    def set_date(self, date: datetime.date):
        modifier_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        self.element.send_keys(
            modifier_key + 'a' + Keys.NULL,
            date.strftime(demoqa_tests.config.datetime_input_format)
            ).press_enter()

