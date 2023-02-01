from selene.support.shared import browser
import os
import tests


def path(selector, image):
    browser.element(selector).send_keys(os.path.abspath((os.path.dirname(tests.__file__) + image)))
