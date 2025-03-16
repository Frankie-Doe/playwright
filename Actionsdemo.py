from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://test1-master.staging.shipsticks.com/')

    # Mouse Actions
    # Hover the dropdown
    page.wait_for_selector("//a[@class='main-nav-link uline' and @href='https://www.shipsticks.com/blog/']").hover()
 #  Click on element
    page.wait_for_selector("//a[@class='main-nav-link uline' and @href='https://www.shipsticks.com/blog/']").click()
 #    Double Click
    page.wait_for_selector("//a[@class='main-nav-link uline' and @href='https://www.shipsticks.com/blog/']").dblclick()
 #   Right on Element
    page.wait_for_selector("//a[@class='main-nav-link uline' and @href='https://www.shipsticks.com/blog/']").click(button="right")
 #   Shift Click
    page.wait_for_selector("//a[@class='main-nav-link uline' and @href='https://www.shipsticks.com/blog/']").click(modifiers=["Shift"])

  # Keyboard
    page.wait_for_selector("//a[@class='main-nav-link uline' and @href='https://www.shipsticks.com/blog/']").press("A")
  # Backquote, Minus, Equal, Backslash, Backspace, Tab, Delete, Escape,
# ArrowDown, End, Enter, Home, Insert, PageDown, PageUp, ArrowRight,
# ArrowUp, F1 - F12, Digit0 - Digit9, KeyA - KeyZ, etc.
    page.wait_for_selector('//a[text()="SwitchTo"]').press("$")