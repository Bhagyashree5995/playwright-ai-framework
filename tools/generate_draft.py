import subprocess
import tempfile
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_playwright_test(user_story):
    prompt = f"""You are a Playwright test automation expert.
Write a complete Python Playwright test for this user story:

{user_story}

Rules:
- Use playwright.sync_api
- Test against https://www.saucedemo.com
- Login with username: standard_user, password: secret_sauce
- Use sync_playwright context manager
- Return ONLY the Python code, no explanation, no markdown, no backticks

Start with: from playwright.sync_api import sync_playwright"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def run_test(test_code):
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(test_code)
        temp_path = f.name
    
    result = subprocess.run(
        ["/usr/local/bin/python3.11", temp_path],
        capture_output=True,
        text=True
    )
    os.unlink(temp_path)
    return result