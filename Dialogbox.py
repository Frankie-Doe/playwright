from playwright.sync_api import sync_playwright
text_alert = []


def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    #xpath locator syntax ('//tagname[@attribute= "value"]/button)-single slash means direct child from tagname

    #page.wait_for_selector('//div[@id="OKTab"]/button').click()
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(3000)
    # controling the dialog box-telling the box to print whats in the pop up dialog box
    page.on("dialog",handle_dialog)
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    page.wait_for_timeout(2000)
    print (text_alert[0])