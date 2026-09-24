# Playwright Python Framework — UI and API Tests

Hand-written Playwright (Python) and pytest framework covering a web UI across three browsers and a stateful REST API, running in GitHub Actions on every push.

## What is tested

| Layer | Target | Covers |
| --- | --- | --- |
| UI | SauceDemo | Valid login, wrong password, locked-out user, product listing, cart badge on add and remove, price sorting |
| API | Restful-Booker | Create, read back, update with auth token, unauthorised update, delete, 404 case |

14 tests: 8 UI (run on Chromium, Firefox and WebKit, so 24 executions) and 6 API.

## Why these tests

- **Login**: the locked-out and wrong-password cases assert on the real error message, so a blank page fails instead of passing a URL check.
- **Cart**: asserted empty before adding, then checked after adding and after removing, so a broken remove button cannot hide behind a passing add test.
- **Sorting**: prices are read from the page and compared against a sorted copy, so the test fails if the dropdown changes but products do not reorder.
- **API**: every test verifies stored state, not just the response. After an update it re-fetches the booking; after a delete it expects 404. The unauthorised update asserts both the 403 and that the stored value is unchanged.

## Structure

- `pages/` — page objects (LoginPage, InventoryPage)
- `api/booker_client.py` — one method per endpoint, returning the raw response
- `conftest.py` — fixtures: login_page, logged_in_page, booker, token (session-scoped), sample_booking
- `tests/ui/`, `tests/api/` — the tests
- `tools/` — experimental AI draft generator, not part of the test run
- `.github/workflows/tests.yml` — CI

## Running it locally

Requires Python 3.11+.

    git clone https://github.com/Bhagyashree5995/playwright-ai-framework.git
    cd playwright-ai-framework
    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    playwright install chromium firefox webkit
    pytest -v

Cross-browser run:

    pytest tests/ui --browser chromium --browser firefox --browser webkit -v

## CI

GitHub Actions runs the API tests and the UI tests on all three browsers on Ubuntu, uploading HTML reports as artifacts on every run, including failures.

## Design notes

- No explicit waits. Playwright locators auto-wait for elements to be attached, visible and actionable.
- Locators prefer user-facing queries (get_by_role, get_by_placeholder) and the application's own data-test attributes over CSS paths or XPath.
- get_by_text("Products") was tried first and matched several elements; Playwright's strict mode surfaced the ambiguity, and it was replaced with [data-test="title"].
- The auth token is fetched once per session; booking data is a fresh dictionary per test, so no test can alter another test's data.

## Known limitations

- Restful-Booker is a shared public sandbox, so tests only assert on bookings they create themselves.
- No visual, accessibility or performance checks yet.
- Checkout is not covered; the UI tests stop at the cart.