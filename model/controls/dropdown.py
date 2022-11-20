import selene
from selene import have
from selene.support.shared import browser


class DropDown:
    def __init__(self, element: selene.Element):
        self.element = element
        self.input = element.element('[id^=react-select][id$=-input]')
        self.options = browser.all('[id^=react-select][id*=-option-]')

    def option(self, text: str):
        return self.options.by(have.exact_text(text)).first

    def open(self):
        self.element.click()
        return self

    def choose(self, option: str):
        self.option(option).click()
        return self

    def select(self, option: str):
        return self.open().choose(option)
