from selene.support.shared import browser

def type_by_id(id, value):
    browser.element(id).type(value)
