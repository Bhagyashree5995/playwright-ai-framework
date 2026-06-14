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

## Project Structure