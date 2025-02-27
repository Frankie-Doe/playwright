from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    # implement CSS Selector use of id #, class . , attribute tagname[attribute = "value"]

   #emailtxtbox = page.wait_for_selector('#email')
   #emailtxtbox.type('lihandafranklin@gmail.com')
   #buttonlogin = page.wait_for_selector('#enterimg')
   #buttonlogin.click()

    

    #attribute tagname[attribute = "value"]
    username = page.wait_for_selector('input[name="username"]')
    username.type('Admin')
    password = page.wait_for_selector('input[type="password"]')
    password.type('admin123')
    loginbutton = page.wait_for_selector('button[type="submit"]')
    loginbutton.click()

    page.wait_for_timeout(3000)
    print ('Its all good')