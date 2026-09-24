import pytest

from pages.login_page import LoginPage

STANDARD_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def logged_in_page(login_page, page):
    login_page.login(STANDARD_USER, PASSWORD)
    return page