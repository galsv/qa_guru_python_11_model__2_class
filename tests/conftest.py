import pytest
from selene.support.shared import browser

@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.timeout = 10
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
