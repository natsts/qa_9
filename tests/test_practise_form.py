import allure
from allure_commons.types import Severity
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from demoqa_tests.model.page.practice_form import PracticeForm, open_form
from demoqa_tests.model.user import test_user
from demoqa_tests.utils import attach


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "natsts")
def test_practise_form(size_browser):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver


with allure.step('Ореn practice form'):
    def test_practice_form(size_browser):
        user_data = PracticeForm(test_user)
        open_form()
        user_data.fill_form()
        user_data.assert_fields()


    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
