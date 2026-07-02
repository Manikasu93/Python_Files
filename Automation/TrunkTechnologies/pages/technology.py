from conftest import page
from config import url

class technology:
    def __init__(self,page):
        self.page=page
        self.tec=page.locator('(//a[text()="Technologies"])[1]')

        #Xpath
        self.ecd=page.locator('//strong[text()="eCommerce Development"]')
        self.mad=page.locator('//strong[text()="Mobile App Development"]')
        self.ai=page.locator('//strong[text()="Artificial Intelligence"]')

        #e_cmm Xpath
        self.magent_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.codeigniter_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.big_comm=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.cs_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.open_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.word_press=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.shopify_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.Node_Js=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')

    # # map_Xpaths
        self.react_native=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.enterprise_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xamarin_App=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kotlin_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.flutter_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.ionic_app=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')

    def mouse_hover(self):
        self.list=[self.ecd,self.mad,self.ai]
        for i in self.list:
            self.tec.hover()
            i.hover()
            self.page.wait_for_timeout(2000)
            print("successfully hovered on the element")

    def click_on_ecommerce(self):
        self.list2=[self.magent_dev,self.codeigniter_dev,self.big_comm,self.cs_cart,self.open_cart,self.word_press,self.shopify_dev,self.Node_Js]
        for i in self.list2:
            self.tec.hover()
            self.ecd.hover()
            # self.page.wait_for_timeout(500)
            i.click()
            self.page.wait_for_timeout(2000)
            print("successfully clicked on the element")

    def click_on_mobile(self):
        self.list3=[self.react_native,self.enterprise_mobile,self.xamarin_App,self.kotlin_mobile,self.flutter_mobile,self.ionic_app]
        for i in self.list3:
            self.tec.hover()
            self.mad.hover()
            # self.page.wait_for_timeout(500)
            i.click()
            self.page.wait_for_timeout(2000)
            print("successfully clicked on the element")
