# Mouse Hover Part

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page =browser.new_page()
    page.goto("https://uncodemy.com/")
    cat=page.locator('//span[@id="categoriesBtn"]')
    # page.wait_for_timeout(5000)

    fsd=page.locator('//a[text()="Full-Stack-Development"]')
    ds=page.locator('//a[text()="Data Science"]')
    st=page.locator('//menuitem[@class="SEt"]/a[text()="Software Testing"]')
    ct=page.locator('//a[text()="Cloud Tools"]')
    dm=page.locator('//a[text()="Digital Marketing"]')
    jt=page.locator('//a[text()="Java Technology"]')
    nm=page.locator('//a[text()="Network & Security"]')
    pl=page.locator('//a[text()="Programming Language"]')
    cadl=page.locator('//a[text()="CAD Training"]')
    gd=page.locator('//a[text()="Graphic Designing"]')


    # l=[fsd,ds,st,ct,dm,jt,nm,pl,cadl,gd,fsdns,pfs,jfsur]
    # for i in l:
    #     i.hover()
    # page.wait_for_timeout(1000)

# Fsd sub locators XPath
    fsnj = page.locator('//a[text()="Full Stack With NodeJs"]')
    pfs = page.locator('//a[text()="Python Full Stack"]')
    jfr = page.locator('(//a[@href="/course/full-stack-with-nodejs-training-course-in-noida"])[1]')
    wd = page.locator('//a[text()="Web Designing"]')
    wdev = page.locator('//a[@href="/course/web-designing-training-course-in-noida""]')
    fe = page.locator('//a[text()="Frontend"]')
    ang = page.locator('//a[text()="Angular"]')
    rjs = page.locator('//a[text()="ReactJs"]')
    dsa = page.locator('//a[@href="/course/data-structure-and-algorithm-training-course-in-noida"]')
    m = page.locator('//a[text()="Mean"]')
    mr = page.locator('//a[text()="Mern"]')

# DS XPath

    ba= page.locator('//a[text()="Business Analytics"]')
    py = page.locator('//a[text()="Python"]')
    dap = page.locator('//menuitem[@label="Test 2"]/a[@href="/course/data-analytics-using-python-training-course-in-noida"]')
    dsml = page.locator('//a[text()="Data Science & Machine Learning using Python"]')
    mlp = page.locator('//a[text()="Machine Learning using Python"]')
    aip = page.locator('//a[text()="AI Using Python"]')


#ST

    stt = page.locator('//menuitem [@label = "Test 1"][a[text()="Software Testing"]]')
    mt = page.locator('//a[text()="Manual Testing"]')
    at = page.locator('//a[text()="Automation Testing"]')
    istqb = page.locator('//a[text()="ISTQB Training"]')
    ms = page.locator('//a[text()="Manual + Selenium"]')


# CT

    msa = page.locator('//a[text()="Microsoft Azure"]')
    devops = page.locator('//a[text()="DevOps"]')
    aws = page.locator('//a[text()="Amazon Web Services (AWS)"]')
    cld = page.locator('//a[text()="Cloud Computing"]')
    sf = page.locator('//a[text()="Salesforce"]')


# DM
    dm = page.locator('//menuitem[@class="SEt"]/a[text()="Digital Marketing"]')
    adm = page.locator('//menuitem[@label="Test 1"]/a[@href="/course/advance-digital-marketing-training-course-in-noida"]')
    seo = page.locator('//menuitem[@label="Test 1"]/a[@href="/course/seo-training-course-in-noida"]')

# JT
    java = page.locator('//a[text()="Java"]')
    jbig = page.locator('//menuitem[@label="Test 1"]/a[@href="/course/java-for-beginners-training-course-in-noida"]')
    jexp = page.locator('//a[text()="Java Expert"]')
    sb = page.locator('//menuitem[@label="Test 1"]/a[@href="/course/spring-boot-microservices-security-with-hibernate-training-course-in-noida"]')


# nm
    eh = page.locator('//a[text()="Ethical Hacking"]')
    cs = page.locator('//a[text()="Cyber Security"]')
    ccnp = page.locator('//a[text()="CCNP"]')
    mcsa = page.locator('//a[text()="MCSA"]')
    vmw = page.locator('//a[text()="Vmware"]')


# pl
    cds = page.locator('//menuitem[@label="Test 1"]/a[@href="/course/c-with-data-structure-and-algorithm-training-course-in-noida"]')
    oods = page.locator('//menuitem[@label="Test 1"]/a[@href="/course/cpptraining-training-course-in-noida"]')
    dotnet = page.locator('//menuitem[@label="Test 1"]/a[@href="/course/net-4-months-training-course-in-noida"]')
    dnetfs = page.locator('//menuitem[@label="Test 1"]/a[@href="/course/dotnet-full-stack-training-course-in-noida"]')
    rpr = page.locator('//a[text()="R Programming"]')

# cadl

    acad = page.locator('//a[text()="AUTOCAD"]')
    cncp = page.locator('//a[text()="CNC Programming"]')
# gd

    gd = page.locator('//menuitem[@label="Test 1"]/a[text()="Graphic Designing"]')
    uiux = page.locator('//menuitem[@label="Test 1"]/a[@href="/course/uiux-training-course-in-noida"]')



    fsd_l=[fsnj,pfs,jfr,wd,fe,ang,rjs,dsa,m,mr]
    ds_lst = [ba,py,dap,dsml,mlp,aip]
    st_lst = [stt,mt,at,istqb,ms]
    ct_lst = [msa,devops,aws,cld,sf]
    dm_lst = [dm,adm,seo]
    jt_lst = [java,jbig,jexp,sb]
    ns_lst = [eh,cs,ccnp,mcsa,vmw]
    pl_lst = [cds,oods,dotnet,dnetfs,rpr]
    cad_lst = [acad,cncp]
    gd_lst = [gd,uiux]

    for i in fsd_l:
        cat.hover()
        fsd.click()
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()

        
   
    for i in ds_lst:
         cat.hover()
         ds.hover()
         i.click()    
         page.wait_for_timeout(1000)

    for i in st_lst:
         cat.hover()
         st.hover()
         i.click()    
         page.wait_for_timeout(1000)

    for i in ct_lst:
         cat.hover()
         ct.hover()
         i.click()    
         page.wait_for_timeout(1000)
   
    for i in dm_lst:
         cat.hover()
         dm.hover()
         i.click()    
         page.wait_for_timeout(1000)
  
    for i in jt_lst:
         cat.hover()
         jt.hover()
         i.click()    
         page.wait_for_timeout(1000)
 
    for i in ns_lst:
         cat.hover()
         nm.hover()
         i.click()    
         page.wait_for_timeout(1000)
    for i in pl_lst:
         cat.hover()
         pl.hover()
         i.click()    
         page.wait_for_timeout(1000)

    for i in cad_lst:
         cat.hover()
         cadl.hover()
         i.click()    
         page.wait_for_timeout(1000)

    for i in gd_lst:
         cat.hover()
         gd.hover()
         i.click()    
         page.wait_for_timeout(1000)     


