from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page =browser.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.wait_for_timeout(2000)

    page.locator('//input[@name="username"]').fill("Admin")

    page.locator('//input[@name="password"]').fill("admin123")

    #screenshots

    page.screenshot(path="D://PlayWrite//screenshot//s1.png")

    page.locator('//button[@type="submit"]').click()
    # page.screenshot(path="D://PlayWrite//screenshot//s1.png")

    page.wait_for_timeout(2000)

    #navigation cmds

    page.go_back()

    page.wait_for_timeout(2000)

    page.go_forward()

    page.wait_for_timeout(2000)

    page.reload()

    page.wait_for_timeout(2000)