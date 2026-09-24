\# Playwright Python Framework — UI and API Tests



A hand-written test framework using Playwright (Python) and pytest, covering a web UI across three browsers and a stateful REST API, running in GitHub Actions on every push.



\## What is tested



| Layer | Target | Covers |

| --- | --- | --- |

| UI | SauceDemo | Valid login, wrong password, locked-out user, product listing, cart badge on add and remove, price sorting |

| API | Restful-Booker | Create, read back, update with auth token, unauthorised update, delete, and a 404 case |



14 tests: 8 UI (run on Chromium, Firefox and WebKit, so 24 executions) and 6 API.



\## Why these tests



\- \*\*Login\*\*: the locked-out user and wrong-password cases assert on the real error message, so a blank or broken page fails instead of passing on a URL check.

\- \*\*Cart\*\*: the cart is asserted empty before anything is added, then checked after adding \*and\* after removing, so a broken remove button cannot hide behind a passing add test.

\- \*\*Sorting\*\*: prices are read from the page and compared against a sorted copy, so the test fails if the dropdown changes but the products do not reorder.

\- \*\*API\*\*: every test verifies stored state, not just the response. After an update it re-fetches the booking; after a delete it expects 404. The unauthorised update asserts both the 403 and that the stored value is unchanged.



\## Structure



\- `pages/` — page objects (`LoginPage`, `InventoryPage`): locators and actions in one place

\- `api/booker\_client.py` — one method per endpoint, returning the raw response so tests can assert on status codes

\- `conftest.py` — fixtures: `login\_page`, `logged\_in\_page`, `booker`, `token` (session-scoped), `sample\_booking`

\- `tests/ui/`, `tests/api/` — the tests

\- `tools/` — an experimental AI draft generator, not part of the test run

\- `.github/workflows/tests.yml` — CI



\## Running it locally



Requires Python 3.11+.



git clone https://github.com/Bhagyashree5995/playwright-ai-framework.git

cd playwright-ai-framework

python -m venv .venv

.venv\\Scripts\\activate

pip install -r requirements.txt

playwright install chromium firefox webkit

pytest -v





Cross-browser run:





\## CI



GitHub Actions runs the API tests and the UI tests on all three browsers on Ubuntu, and uploads HTML reports as artifacts on every run, including failures.



\## Design notes



\- No explicit waits. Playwright locators auto-wait for elements to be attached, visible and actionable, which removes most of the timing code a Selenium suite needs.

\- Locators prefer user-facing queries (`get\_by\_role`, `get\_by\_placeholder`) and the application's own `data-test` attributes over CSS paths or XPath.

\- `get\_by\_text("Products")` was tried first and matched several elements; Playwright's strict mode surfaced the ambiguity, and it was replaced with `\[data-test="title"]`.

\- The auth token is fetched once per session; booking data is a fresh dictionary per test, so no test can alter another test's data.



\## Known limitations



\- Restful-Booker is a shared public sandbox. Data created by other users is visible, so tests only assert on bookings they create themselves.

\- No visual, accessibility or performance checks yet.

\- Checkout is not covered; the UI tests stop at the cart.





