from playwright.sync_api import sync_playwright

def download_handle(download):
    file_location = './files/test.zip'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/FileDownload.html')
    page.on('download', download_handle)

    page.query_selector('//a[@id="link-to-download"]').click