from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://test1-master.staging.shipsticks.com/')
    # Prints all the cookies on the site
    my_cookies = page.context.cookies()
    print(my_cookies)

    #clear all cookies from site
    page.context.clear_cookies()

    #To set up new cookies on the site
    #new_cookies = {
        #'name' : 'Anonny'
        #'value': 'Guru247'
    #}
    #To add the new cookies to the site
    #page.context.add_cookies()

    #Taking a screenshot and naming the screenshot.png 
    page.screenshot(path='2025.png',full_page=True)
    