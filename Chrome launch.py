from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://test1-master.staging.shipsticks.com/')
    print('chrome successfully opened')
    title = page.title()
    print("Page Title:", title)
    page.wait_for_timeout(2000)
    browser.close()