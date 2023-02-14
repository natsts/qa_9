from model.elements.radio_button import gender
from selene.support.shared import browser
from model.elements.dropdown import select_option
from model.elements.datepicker import date_of_birth
from model.elements.check_box import hobby
from utils.path import path
from selene import have, command


def open_form():
    browser.open('https://demoqa.com/automation-practice-form')

    ads = browser.all('[id^=google_ads_][id$=container__]')
    google_uploads = browser.all("[id^=google_uploaded_]")

    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)
    if google_uploads.wait.until(have.size_greater_than_or_equal(1)):
        google_uploads.perform(command.js.remove)


def fill_contact_fields(name, last_name, email, phone):
    browser.element('#firstName').click().type(name)
    browser.element('#lastName').click().type(last_name)
    browser.element('#userEmail').click().type(email)
    browser.element('#userNumber').click().type(phone)


def select_gender(value):
    gender('[name=gender]', value)


def select_subject(value):
    browser.element('#subjectsInput').type(value).press_enter()


def select_state(value):
    select_option('#state', value)


def select_city(value):
    select_option('#city', value)


def select_year(year):
    browser.element('#dateOfBirthInput').click()
    date_of_birth('.react-datepicker__year-select', year)


def select_month(month):
    date_of_birth('.react-datepicker__month-select', month)


def select_day(day):
    browser.element(f'.react-datepicker__day--0{day}').click()


def select_hobby(value):
    hobby('[for^=hobbies-checkbox]', value)


def add_image(image):
    path('#uploadPicture', image)


def add_address(value):
    browser.element('#currentAddress').type(value)


def submit():
    browser.element('#submit').press_enter()


def check_header(text):
    browser.element('#example-modal-sizes-title-lg').should(have.text(text))


def check_data(*items):
    browser.all('.table-responsive td:nth-child(2)').should(have.exact_texts(*items))


