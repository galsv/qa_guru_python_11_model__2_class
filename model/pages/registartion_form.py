from selene import command, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss
from model.controls import input, dropdown, modal, upload
from model import google
from typing import Tuple
from tests.test_data.users import Subject, Hobby
from model.controls.datepicker import DatePicker
from model.controls.dropdown import DropDown


class RegistrationForm:
    def __init__(self):
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))

    def given_opened(self):
        browser.open('/automation-practice-form')
        google.remove_ads(amount=3, timeout=6)
        google.remove_ads(amount=1, timeout=2)
        return self

    def set_first_name(self, value: str):
        input.type_by_id('#firstName', value)
        return self

    def set_last_name(self, value: str):
        input.type_by_id('#lastName', value)
        return self

    def set_email(self, value: str):
        input.type_by_id('#userEmail', value)
        return self

    def set_gender(self, value: str):
        browser.element(f'[id^=gender-radio][value={value}]').perform(command.js.click)
        return self

    def set_user_number(self, value: str):
        input.type_by_id('#userNumber', value)
        return self

    def set_date_of_birthday(self, value: str):
        self.birthday.set_date(value)
        return self

    def add_subjects(self, values: Tuple[Subject]):
        for subject in values:
            browser.element('#subjectsInput').type(subject.value).press_enter()
        return self

    def select_hobbies_cb(self, values: Tuple[Hobby]):
        for hobby in values:
            browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
                '..'
            ).click()
        return self

    def upload_picture(self, value: str):
        upload.picture_up('#uploadPicture', value)
        return self

    def set_current_address(self, value: str):
        input.type_by_id('#currentAddress', value)
        return self

    def scroll_to_bottom(self):
        browser.element('#state').perform(command.js.scroll_into_view)
        return self

    def set_state(self, value: str):
        DropDown(browser.element('#state')).select(value)
        return self

    def set_city(self, value: str):
        DropDown(browser.element('#city')).select(value)
        return self

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def should_have_submitted(self, data):
        rows = modal.dialog.all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
        return self
