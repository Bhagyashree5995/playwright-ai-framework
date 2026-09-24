from app import generate_playwright_test, run_test

def test_login():
    user_story = "As a user, I want to login to saucedemo with valid credentials so that I can access the inventory page"
    
    test_code = generate_playwright_test(user_story)
    print("\nGenerated Test Code:")
    print(test_code)
    
    result = run_test(test_code)
    print("\nTest Output:")
    print(result.stdout)
    
    if result.returncode != 0:
        print("Errors:")
        print(result.stderr)
    
    assert result.returncode == 0, f"Test failed with errors:\n{result.stderr}"