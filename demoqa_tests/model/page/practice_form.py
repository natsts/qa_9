import datetime
from selene import have, command
from selene.support.shared import browser
from demoqa_tests.utils.path import Path
from demoqa_tests.model.elements.datepicker import Datepicker
from demoqa_tests.model.elements.dropdown import Dropdown
from demoqa_tests.model.elements.radiobutton import Radiobutton
from demoqa_tests.model.elements.checkbox import Checkbox


def open_form():
    browser.open('https://demoqa.com/automation-practice-form')

    ads = browser.all('[id^=google_ads_][id$=container__]')
    google_uploads = browser.all("[id^=google_uploaded_]")

    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)
    if google_uploads.wait.until(have.size_greater_than_or_equal(1)):
        google_uploads.perform(command.js.remove)


class PracticeForm:
    def __init__(self, user):
        self.user = user

    def fill_form(self):

        browser.element('#firstName').click().type(self.user.name)
        browser.element('#lastName').click().type(self.user.last_name)
        browser.element('#userEmail').click().type(self.user.email)
        browser.element('#userNumber').click().type(self.user.phone)
        browser.element('#currentAddress').type(self.user.address)
        browser.element('#subjectsInput').type(self.user.subject).press_enter()

        gender = Radiobutton(browser.all('[name=gender]'))
        gender.select_gender(self.user.gender)

        state = Dropdown(browser.element('#state'))
        state.select_state_or_city(self.user.state)

        city = Dropdown(browser.element('#city'))
        city.select_state_or_city(self.user.city)

        birthday = Datepicker(browser.element('#dateOfBirthInput'))
        birthday.set_date(datetime.date(self.user.year, self.user.month, self.user.day))

        hobby = Checkbox(browser.all('[for^=hobbies-checkbox]'))
        hobby.select_hobby(self.user.hobby)

        path = Path(browser.element('#uploadPicture'))
        path.input_path(self.user.image)

        browser.element('#submit').press_enter()

    def assert_fields(self):
        browser.element('.table').all('td').even.should(have.texts(
            f'{self.user.name} {self.user.last_name}',
            self.user.email,
            self.user.gender,
            self.user.phone,
            f'{self.user.day} May,{self.user.year}',
            self.user.subject,
            self.user.hobby,
            self.user.image,
            self.user.address,
            f'{self.user.state} {self.user.city}'

        ))
