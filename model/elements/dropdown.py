from selene.support.shared import browser
from selene import have


def select_option(selector, value):
    browser.element(selector).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

