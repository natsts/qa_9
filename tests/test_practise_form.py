from demoqa_tests.model.page.practice_form import PracticeForm, open_form
from demoqa_tests.model.user import test_user


def test_practice_form(size_browser):
    user_data = PracticeForm(test_user)
    open_form()
    user_data.fill_form()
    user_data.assert_fields()
