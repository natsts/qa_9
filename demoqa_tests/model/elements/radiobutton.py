import selene
from selene import have


class Radiobutton:
    def __init__(self, element: selene.Element):
        self.element = element

    def select_gender(self, value):
        self.element.element_by(have.value(value)).element('..').click()
