from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.kamera-express.nl/")
    page.locator('//button[@class="is--regular"]').click()
    login=page.locator('(//span[text()="Log in"])[2]')
    login.hover()
    page.locator('(//button[@class="sf-button"])[2]').click()
    page.locator('//input[@name="username"]').fill("manikasu777@gmail.com")
    page.locator('//input[@name="password"]').fill("Mk@123")
    page.wait_for_timeout(2000)
    page.locator('//input[@id="btn_login"]').click()
    page.wait_for_load_state(state="load")
    
