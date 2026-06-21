from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page =browser.new_page()
    page.goto("https://www.globalsqa.com/demo-site/draganddrop/#google_vignette")

    frame=page.frame_locator('(//iframe[@class="demo-frame"])[1]')

    img1=frame.locator('//img[@src="images/high_tatras_min.jpg"]')
    img2=frame.locator('//img[@src="images/high_tatras2_min.jpg"]')
    img3=frame.locator('//img[@src="images/high_tatras3_min.jpg"]')
    img4=frame.locator('//img[@src="images/high_tatras4_min.jpg"]')

    trash=frame.locator('//div[@id="trash"]')
    
    list=[img1,img2,img3,img4]
    for i in list:
        i.drag_to(trash)
        page.wait_for_timeout(2000)
