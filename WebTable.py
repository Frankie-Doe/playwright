from playwright.sync_api import sync_playwright, TimeoutError

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        page.goto(
            'https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html',
            wait_until="networkidle",
            timeout=60000
        )
    except TimeoutError:
        print("Page did not load within the specified timeout.")

    # Proceed if the page loaded
    table = page.wait_for_selector('//table[@id="customers"]')
    rows = table.query_selector_all('tr')
    print("Number of rows:", len(rows))
    cells = table.query_selector_all('td')
    print("Number of cells:", len(cells))

    page.wait_for_timeout(3000)
    browser.close()
