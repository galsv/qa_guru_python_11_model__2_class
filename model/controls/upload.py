from selene.support.shared import browser
from utils import path


def picture_up(element: str, picture: str):
    browser.element(element).send_keys(path.to_resource(picture))