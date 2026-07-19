from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.kamera-express.nl/', wait_until='domcontentloaded')
    print('loaded', page.url)
    page.locator('//button[@class="is--regular"]').click()
    login = page.locator('(//span[text()="Log in"])[2]')
    print('login count', login.count())
    login.hover()
    page.locator('(//button[@class="sf-button"])[2]').click()
    page.locator('//input[@name="username"]').fill('manikasu777@gmail.com')
    page.locator('//input[@name="password"]').fill('Mk@123')
    page.locator('//input[@id="btn_login"]').click()
    page.wait_for_load_state('networkidle', timeout=30000)
    print('after login url', page.url)
    print('title', page.title())
    for sel in [
        '(//font[@_msttexthash="117832"])[1]',
        'text=My account',
        'text=Account',
        'text=Mijn account',
        'a:has-text("account")',
        'button:has-text("Account")',
        'button:has-text("Mijn account")',
        'text=Logout',
        'text=Log out'
    ]:
        try:
            loc = page.locator(sel)
            count = loc.count()
            print(sel, 'count=', count)
            if count:
                print('first text', loc.first.text_content())
        except Exception as e:
            print(sel, 'ERR', e)
    browser.close()
