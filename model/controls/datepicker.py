import sys

from selene.support.shared import browser
from selenium.webdriver import Keys
from selene import Element


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select_date(self, year: str, month: str, day: str):
        self.element.click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(
            f'.react-datepicker__day--0{day}'
            f':not(.react-datepicker__day--outside-month)'
        ).click()

    def set_date(self, date: str):
        modifier_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        self.element.send_keys(modifier_key + 'a').type(date).press_enter()
        return self
