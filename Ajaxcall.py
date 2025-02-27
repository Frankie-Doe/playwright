from playwright.sync_api import sync_playwright

#settting up the response of the code to fetch the status/text and then print
def handle_rejex(response):
    if 'https://www.plus2net.com/php_tutorial/dd-ajax.php?' in response.url:
        status = response.status
        data = response.text()
        print(f'status:{status},data:{data}')


with sync_playwright() as p:
    browser = p.chromium.launch()
    #context is used to store multiple pages in the url
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php')

    select = page.wait_for_selector('//select[@id="s1"]')
    page.on('response', lambda response : handle_rejex(response))
    select.select_option('3')
    page.wait_for_timeout(2000)