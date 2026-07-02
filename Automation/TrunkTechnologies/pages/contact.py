from conftest import page
from config import url
class contact:
    def __init__(self,page):
        self.page = page
        self.contactus=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.contactus.click()

        self.name=page.locator('(//input[@placeholder="Your Name"])[2]').fill("ManiKasu")
        self.mail=page.locator('(//input[@type="email"])[2]').fill('maniksu77@gmail.com')
        self.company=page.locator('(//input[@placeholder="Your Company"])[2]').fill('zeebronix')
        self.service=page.locator('(//select[@name="service"])[2]').select_option('App Development')
        self.phone=page.locator('(//input[@placeholder="Your Phone"])[2]').fill('2211335455')
        self.message=page.locator('(//textarea[@placeholder="Message"])[2]').fill('manikantakasu')

    def click_elements(self):
        self.list=[self.name,self.mail,self.company,self.service,self.phone,self.message]
        for i in self.list:
            i.click()
            self.page.wait_for_load_state(state="load")
            print("successfully clicked on the element")