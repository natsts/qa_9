import selene
from selene.support.shared import browser
from selene import have


class Dropdown:
    def __init__(self, element: selene.Element):
        self.element = element

    def select_state_or_city(self, value):
        self.element.click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

