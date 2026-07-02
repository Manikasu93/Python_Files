from conftest import page
from config import url

class portfo:
    def __init__(self, page):
        self.page = page
        # main portfolio nav/link
        self.portfol = page.locator('(//a[@href="https://www.tranktechnologies.com/portfolio"])[1]')

    def click_portfolio(self):
        self.portfol.click()
        self.page.wait_for_timeout(1000)
