#Social Media pages

from config import url
from conftest import page

class about:

    def __init__(self,page):
        self.page=page
        self.aboutus = page.locator('(//a[text()="About us"])[1]')


        self.cmsWebsite=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.customWebPortaDev=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.mobileAppDesign=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.responsiveWebDesig=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brandIdentityDesign=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')
        self.iosAppDev=page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.hybridMobileapp=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.crossPlatfromApp=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.progressiveWebApp=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')
        self.logodesign=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.bannerdesign=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packgingDesign=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.cardDesign=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')

        print("Sub Elements Social Media pages")

    def click_social_media_pages(self):
        self.socail_list=[self.cmsWebsite,self.customWebPortaDev,self.mobileAppDesign,self.responsiveWebDesig,self.brandIdentityDesign,self.iosAppDev,self.hybridMobileapp,self.crossPlatfromApp,self.progressiveWebApp,self.logodesign,self.bannerdesign,self.packgingDesign,self.cardDesign] 

        # for i in self.socail_list:
        #     self.aboutus.click()
        #     self.cmsWebsite.click()
        #     i.click()
        #     self.page.wait_for_load_state(state="load")
        #     print("successfully clicked on the element")   
     
        for index,locator in enumerate(self.socail_list,start=1):
            locator.click()
            self.page.wait_for_load_state(state="load")
            self.page.go_back()
            # Print before clicking to know what the script is attempting
            print(f"[{index}/{len(self.socail_list)}] Clicking locator: {locator}")
            
            locator.click()
            self.page.wait_for_load_state(state="load")
            
            print(f"Successfully loaded page for locator {index}. Navigating back...")
            self.page.go_back()
            
        print("All pages processed successfully!")

        self.arrow1=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]').click()
        self.page.wait_for_load_state(state="load")
        print("click arrow1")
        with self.page.context.expect_page() as new_page_info:
            self.page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]').click()
            print("clicked website")
        new_tab = new_page_info.value
        new_tab.wait_for_load_state()
        self.page.bring_to_front()
        self.page.wait_for_load_state(state="load")

        self.arrow2=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]').click()
        self.page.wait_for_load_state(state="load")
        print("Clcked Arrow2")
        with self.page.context.expect_page() as new_page_info:
            self.androidAppDev=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]').click()
            print("clicked android")
        new_tab = new_page_info.value
        new_tab.wait_for_load_state()
        self.page.bring_to_front()
        self.page.wait_for_load_state(state="load")

        self.arrow3=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[3]').click()
        with self.page.context.expect_page() as new_page_info:
            self.appDeve=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]').click()
            print("clicked company")

        new_tab = new_page_info.value
        new_tab.wait_for_load_state()
        self.page.bring_to_front()
        self.page.wait_for_load_state(state="load")


