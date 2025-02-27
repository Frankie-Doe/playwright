from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    # Radio button -same essence as drop down select button
    radio_button = page.query_selector('//input[@value= "Male"]')
    #click and check
    # radio_button.click()
    radio_button.check()

    if radio_button.is_checked():
        print ('Passed')
    else:
        print ('Try again')    
    
    #Check box
    Checkbox = page.query_selector('//input[@value= "Movies"]')
    # Checkbox.click()
    Checkbox.check()

    if Checkbox.is_checked():
        print ('Passed')
    else:
        print ('Try again')

    page.wait_for_timeout(5000)

