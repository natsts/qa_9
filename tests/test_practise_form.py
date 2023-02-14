from model.page import practice_form


def test_practise_form(size_browser):
    practice_form.open_form()

    practice_form.fill_contact_fields('Test', 'Testovych', 'test123@mail.ru', '9617778558')

    practice_form.select_gender('Female')

    practice_form.select_year('1996')
    practice_form.select_month('May')
    practice_form.select_day('20')

    practice_form.select_subject('English')

    practice_form.select_hobby('Reading')

    practice_form.add_image('\media\cat.jpg')

    practice_form.add_address('Moscow')

    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')

    practice_form.submit()

    practice_form.check_header('Thanks for submitting the form')
    practice_form.check_data(
        'Test Testovych',
        'test123@mail.ru',
        'Female',
        '9617778558',
        '20 May,1996',
        'English',
        'Reading',
        'cat.jpg',
        'Moscow',
        'NCR Delhi'
    )
