from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://demoqa.llq.vn/automation-practice-form") 

    fname=page.locator('//input[@placeholder="First Name"]').fill("Manikanta")
    lname=page.locator('//input[@placeholder="Last Name"]').fill("Kasu")
    email=page.locator('//input[@placeholder="name@example.com"]').fill("manikanta.kasu@email.com")
    gender=page.locator('//label[@for="gender-radio-1"]').click()
    pnumber=page.locator('//input[@placeholder="Mobile Number"]').fill("9381862130")
    dob_input = page.locator('//input[@id="dateOfBirthInput"]')
    dob_input.click()
    dob_input.clear()
    dob_input.fill("10/10/1999")   
    page.keyboard.press('Escape')
    page.wait_for_timeout(500)
    sub=page.locator('//select[@id="subjectsInput"]').select_option("Maths")


    page.wait_for_load_state(state="load")

