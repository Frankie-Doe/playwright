from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # taking a Video and declaring its directory of storage
    context = browser.new_context(record_video_dir= './videos')
    page = context.new_page() 
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.wait_for_selector('//input[@name="username"]').fill('Admin')
    page.wait_for_selector('//input[@name="password"]').fill('admin123')
    # Taking a Screenshot and path of storage
    page.screenshot(path="./Snapchat/loginpage.png")
    page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(3000)
    page.screenshot(path="./Snapchat/homepage.png")
    page.wait_for_timeout(3000)
    context.close()
