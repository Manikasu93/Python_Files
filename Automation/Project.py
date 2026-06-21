from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://www.tranktechnologies.com/")    
    vrt=page.locator('(//a[text()="Verticals"])[1]')
    tcngy=page.locator('(//a[text()="Technologies"])[1]')


    # vrt_Locators
    td=page.locator('//strong[text()="Trading"]')
    rande=page.locator('//strong[text()="Retail and Ecommerce"]')
    hc=page.locator('//strong[text()="Healthcare"]')
    ft=page.locator('//strong[text()="Fintech"]')
    sg=page.locator('//strong[text()="Custom App"]')

    # td X path
    st=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
    pt=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
    ct=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
    tadm=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
    at=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
    cts=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
    wpt=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        #rande Xpath
    ecw=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
    eca=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

    # hc Xpaths 
    dandn=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
    hta=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

    #ft Xpaths
    psd=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
    cta=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

    # sg Xpaths
    dad=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
    hd=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
    tl=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
    dtd=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
    crmd=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
    crm=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
    ead=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
    el=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
    re=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')


    v_l=[st,pt,ct,tadm,at,cts,wpt]
    rande_l=[eca]
    h_l = [dandn , hta]
    ft_l=[psd,cta]
    sg_l=[dad,hd,tl,dtd,crmd,crm,ead,el,re]

        

    for i in v_l:
        vrt.hover()
        td.hover()
        i.click()
        page.wait_for_timeout(2000)
        page.go_back()

    
    for j in rande_l:
        vrt.hover()
        rande.hover()
        # page.wait_for_timeout(1000)
        j.click()
        page.wait_for_timeout(1000)


    for i in h_l:
        vrt.hover()
        hc.hover()
        i.click()
        page.wait_for_timeout(2000)
        page.go_back()

    for i in ft_l:
        vrt.hover()
        ft.hover()
        i.click()
        page.wait_for_timeout(1000)
    
    for i in sg_l:
        vrt.hover()
        sg.hover()
        i.click()
        page.wait_for_timeout(1000)


    # tec_locators
    ecd=page.locator('//strong[text()="eCommerce Development"]')
    mad=page.locator('//strong[text()="Mobile App Development"]')
    ai=page.locator('//strong[text()="Artificial Intelligence"]')

    #ecd_Xpath
    magent0_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
    codeigniter_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
    big_comm=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
    cs_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
    open_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
    word_press=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
    shopify_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
    Node_Js=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')

    # map_Xpaths
    react_native=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
    enterprise_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
    xamarin_App=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
    kotlin_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
    flutter_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
    ionic_app=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')

    ecd_l=[magent0_dev,codeigniter_dev,big_comm,cs_cart,open_cart,word_press,shopify_dev,Node_Js]

    for i in ecd_l:
        tcngy.hover()
        ecd.hover()
        i.click()
        page.wait_for_timeout(1000)

    mad_l=[react_native,enterprise_mobile,xamarin_App,kotlin_mobile,flutter_mobile,ionic_app]
    for i in mad_l:
        tcngy.hover()
        mad.hover()
        i.click()
        page.wait_for_timeout(2000)


    # blog_LOcator
    blg=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
    # contact_Locator
    contactus=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')




    #XPaths for blog
    ad=page.locator('//a[@href="/blog/category/app-development/"]')
    wd=page.locator('//a[@href="/blog/category/web-development/"]')
    sd=page.locator('//a[@href="/blog/category/software-development/"]')
    dm=page.locator('//a[@href="/blog/category/digital-marketing/"]')
    ai=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
    ud=page.locator('//a[@href="/blog/category/ui-ux-design/"]')



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




