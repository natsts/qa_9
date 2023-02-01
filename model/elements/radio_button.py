from selene.support.shared import browser
from selene import have


def gender(selector, value):
    browser.all(selector).element_by(have.value(value)).element('..').click()
