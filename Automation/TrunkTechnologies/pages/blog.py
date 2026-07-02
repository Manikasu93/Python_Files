from conftest import page
from config import url

class blog:
    def __init__(self,page):
        self.page = page    
        self.blg=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        self.ad=page.locator('//a[@href="/blog/category/app-development/"]')
        self.wd=page.locator('//a[@href="/blog/category/web-development/"]')
        self.sd=page.locator('//a[@href="/blog/category/software-development/"]')
        self.dm=page.locator('//a[@href="/blog/category/digital-marketing/"]')
        self.ai=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
        self.ud=page.locator('//a[@href="/blog/category/ui-ux-design/"]')

    

    def click_elements(self):
        self.list = [self.ad, self.wd, self.sd, self.dm, self.ai, self.ud]
        for i in self.list:
            self.blg.click()
            # self.ad.click()
            i.click()
            self.page.wait_for_timeout(2000)
            print("successfully clicked on the element")