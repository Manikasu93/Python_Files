from conftest import page
from config import url

class vertical:
    def __init__(self, page):
        self.page=page
        self.vrt=page.locator('(//a[text()="Verticals"])[1]')

        # vrt_Locators
        self.td=page.locator('//strong[text()="Trading"]')
        self.rande=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.hc=page.locator('//strong[text()="Healthcare"]')
        self.ft=page.locator('//strong[text()="Fintech"]')
        self.sg=page.locator('//strong[text()="Custom App"]')

        # td X path
        self.st = page.locator('div#trading a[href*="stock-trading-mobile-app-development-company"]')
        self.pt = page.locator('div#trading a[href*="paper-trading-app-development-company"]')
        self.ct = page.locator('div#trading a[href*="cfd-trading-app-development-company"]')
        self.tadm = page.locator('div#trading a[href*="stock-trading-development-in-massachusetts"]')
        self.at = page.locator('div#trading a[href*="algo-trading-app-development-company"]')
        self.cts = page.locator('div#trading a[href*="custom-trading-software-development-company"]')
        self.wpt = page.locator('div#trading a[href*="webportal-trading-development"]')

        # rande Xpath
        # self.ecw = page.locator('div#retailEcommerce a[href*="ecommerce-web-development-company"]')
        self.eca = page.locator('div#retailEcommerce a[href*="ecommerce-app-development"]')

            # # hc Xpaths 
        self.dandn=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.hta=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        # #ft Xpaths
        self.psd=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.cta=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        # # sg Xpaths
        self.dad=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hd=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.tl=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.dtd=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.crmd=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.crm=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.ead=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.el=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.re=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')



    def mouse_hover(self):
        self.list = [self.td, self.rande, self.hc, self.ft, self.sg]
        for i in self.list:
            self.vrt.hover()
            i.hover()
            self.page.wait_for_timeout(2000)
            print("successfully hovered on the element")

    def trading(self):
        self.list1 = [self.st, self.pt, self.ct, self.tadm, self.at, self.cts, self.wpt]
        for i in self.list1:
            self.vrt.hover()
            self.td.hover()  # Hover over Trading to reveal its links
            self.page.wait_for_timeout(500)
            i.click()
            print("successfully clicked trading link")
            self.page.go_back()

    def retail(self):
        self.list2 = [self.eca]
        for i in self.list2:
            self.vrt.hover()
            self.rande.hover()
            self.page.wait_for_timeout(500)
            i.click()
            print("successfully clicked retail link")
            self.page.go_back()

    def healthcare(self):
        self.list3 = [self.dandn, self.hta]
        for i in self.list3:
            self.vrt.hover()
            self.hc.hover()            
            self.page.wait_for_timeout(500)
            i.click()
            print("successfully clicked healthcare link")
            self.page.go_back()        

    def fintech(self):
        self.list4 = [self.psd, self.cta]
        for i in self.list4:
            self.vrt.hover()
            self.ft.hover()
            self.page.wait_for_timeout(500)
            i.click()
            print("successfully clicked fintech link")
            self.page.go_back()

    def custom_app(self):
        self.list5 = [self.dad, self.hd, self.tl, self.dtd, self.crmd, self.crm, self.ead, self.el, self.re]
        for i in self.list5:
            self.vrt.hover()
            self.page.wait_for_timeout(500)
            self.sg.hover()  # Hover to reveal custom app links
            i.click()  
            self.page.wait_for_timeout(2000)
            print("successfully clicked custom app link")
            self.page.go_back()     

            
        