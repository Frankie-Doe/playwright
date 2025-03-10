from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.wait_for_timeout(7000)
    #xpath - syntax used to navigate throug elements and attributes
    #xpath syntax using attribute - //tagname[@attributename ="value"]



    username_element = page.wait_for_selector('//input[@name= "username"]')
    username_element.type('Admin')
    password_element = page.wait_for_selector('//input[@type= "password"]')
    password_element.type('admin123')
    login_element = page.wait_for_selector('//button[@type= "submit"]')
    login_element.click()
    page.wait_for_timeout(5000)
    

    #xpath syntax using text - //tagname[text()= "text"]
    #page.wait_for_selector('//p[text()="Forgot your password? "]').click()
    #page.wait_for_timeout(3000)
    






 

