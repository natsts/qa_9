import selene
import os
import tests


class Path:
    def __init__(self, element: selene.Element):
        self.element = element

    def input_path(self, image):
        self.element.send_keys(os.path.abspath((os.path.dirname(tests.__file__) + '\media\\' + image)))
