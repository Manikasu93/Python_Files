from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://demoqa.llq.vn/automation-practice-form") 

    fNaame=page.locator('//input[@placeholder="First Name"]').fill("Manikanta")
