from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("https://www.okx.com/balance/overview")
    page.screenshot(path="example2.png")
    print ('Chrome successfuly opened')
    browser.close()
