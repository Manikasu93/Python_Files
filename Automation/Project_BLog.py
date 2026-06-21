from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://www.tranktechnologies.com/")    
    vrt=page.locator('(//a[text()="Verticals"])[1]')

# Locators
    ##Blog##
    # blg=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
    contactus=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')

#XPaths for blog
    # ad=page.locator('//a[@href="/blog/category/app-development/"]')
    # wd=page.locator('//a[@href="/blog/category/web-development/"]')
    # sd=page.locator('//a[@href="/blog/category/software-development/"]')
    # dm=page.locator('//a[@href="/blog/category/digital-marketing/"]')
    # ai=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
    # ud=page.locator('//a[@href="/blog/category/ui-ux-design/"]')
#Xpaths For Contact us
    contactus.click()
    name=page.locator('(//input[@placeholder="Your Name"])[2]').fill("ManiKasu")
    page.wait_for_timeout(1000)
    mail=page.locator('(//input[@type="email"])[2]').fill('maniksu77@gmail.com')
    page.wait_for_timeout(1000)
    ycmpn=page.locator('(//input[@placeholder="Your Company"])[2]').fill('zeebronix')
    page.wait_for_timeout(1000)
    cas=page.locator('(//select[@name="service"])[2]').select_option('App Development')
    page.wait_for_timeout(1000)
    phone=page.locator('(//input[@placeholder="Your Phone"])[2]').fill('2211335455')
    page.wait_for_timeout(1000)
    msg=page.locator('(//textarea[@placeholder="Message"])[2]').fill('manikantakasu')
    page.wait_for_timeout(1000)





    # b_l=[ad,wd,sd,dm,ai,ud]
    # for i in b_l:
    #     vrt.hover()
    #     blg.click()
    #     i.click()
    #     page.wait_for_timeout(2000)
    #     page.reload()
    #     page.go_back()
        # print("ALL ARE SUCCESSFULLY DONE")
