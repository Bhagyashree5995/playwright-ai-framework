# 🎭 Playwright AI Framework

An AI-powered test automation framework that generates and runs Playwright tests from plain English user stories.

## What it does

Type a user story → AI generates a complete Playwright test → It runs automatically → Shows Pass/Fail

## Tech Stack

- Python 3.11
- Playwright (browser automation)
- pytest (test runner)
- Groq API / LLaMA 3.3 (AI test generation)
- python-dotenv (environment management)

## How it works

1. You provide a plain English user story
2. The AI (via Groq API) generates a complete Python Playwright test
3. The test runs automatically against a real browser
4. Pass/Fail result is returned

## Setup

1. Clone the repo
2. Install Python 3.11
3. Install dependencies:

pip3.11 install -r requirements.txt
python3.11 -m playwright install chromium

4. Create .env file:

GROQ_API_KEY=your_groq_api_key_here

5. Run tests:

python3.11 -m pytest tests/test_playwright.py -v -s

## Example

User Story:
As a user, I want to login to saucedemo with valid credentials so that I can access the inventory page

Result: PASSED

## Author

Bhagyashree Manjithaya — QA Engineer
LinkedIn: https://linkedin.com/in/bhagyashree-manjithaya
GitHub: https://github.com/Bhagyashree5995