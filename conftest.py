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


from api.booker_client import BookerClient


@pytest.fixture(scope="session")
def booker():
    return BookerClient()


@pytest.fixture(scope="session")
def token(booker):
    response = booker.create_token()
    assert response.status_code == 200, "Could not get an auth token"
    return response.json()["token"]


@pytest.fixture
def sample_booking():
    return {
        "firstname": "Bhagyashree",
        "lastname": "Manjithaya",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-10-01", "checkout": "2026-10-05"},
        "additionalneeds": "Breakfast",
    }