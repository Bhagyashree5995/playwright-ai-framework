from conftest import STANDARD_USER, LOCKED_USER, PASSWORD


def test_valid_login_reaches_inventory(login_page, page):
    login_page.login(STANDARD_USER, PASSWORD)
    assert "inventory.html" in page.url
    assert page.get_by_text("Products").is_visible()


def test_invalid_password_shows_error(login_page):
    login_page.login(STANDARD_USER, "wrong_password")
    assert "Username and password do not match" in login_page.error_message()


def test_locked_out_user_is_blocked(login_page):
    login_page.login(LOCKED_USER, PASSWORD)
    assert "Sorry, this user has been locked out" in login_page.error_message()