from selene.support.shared import browser
from selene import have


def date_of_birth(selector, value):
    browser.element(selector).click().all('option').element_by(have.exact_text(value)).click()
