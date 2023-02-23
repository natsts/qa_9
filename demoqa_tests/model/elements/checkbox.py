import selene
from selene import have


class Checkbox:
    def __init__(self, element: selene.Element):
        self.element = element

    def select_hobby(self, value):
        self.element.element_by(have.text(value)).click()
