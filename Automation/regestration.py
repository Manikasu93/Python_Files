from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page =browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    page.locator('//a[@href="Register.html"]').click()
    page.locator('//input[@placeholder="First Name"]').fill('Manikanta')
    page.locator('//input[@placeholder="Last Name"]').fill('kasu')
    page.locator('//textarea[@ng-model="Adress"]').fill('andhra pradesh,' \
    'West godavari' \
    'kallamandalam 534236')
    page.locator('//input[@ng-model="EmailAdress"]').fill('manikasu77y@gmail.com')
    page.locator('//input[@ng-model="Phone"]').fill('9381862130')
    page.locator('//input[@value="Male"]').click()
    page.locator('//input[@value="Cricket"]').click()
    page.locator('//div[@class="ui-autocomplete-multiselect ui-state-default ui-widget"]')
    page.locator('(//a[@style="text-decoration:none"])[1]')
    page.locator('(//a[@style="text-decoration:none"])[1]')
    
    page.wait_for_timeout(2500)