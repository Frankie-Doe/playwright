#To figure out where exactly on a patch of code has an issue using the try catch method
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try :
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://demo.automationtesting.in/Selectable.html')
        #Capture below code with error to see if terminal captures the error
        page.locator("xpath=//a[@href='#Serialize' and @data-toggle='tab']").click()
        page.wait_for_timeout(2000)

        #<b> tag in HTML is used to store and show lists.To select all the list under the HTML element <b> tag in a site
        elements = page.query_selector_all('b')
        #To print size of the list
        print(len(elements))
        #to print each content in the list
        for i in elements:
        #to take a text from the web element by use of text_content
            print(i.text_content())
    
        #<a> (attribute tag)tag used to store link tags (a href)
        variable = page.query_selector_all('a')
        print(len(variable))
        for v in variable:
         print(v.get_attribute('href'))
    
        page.wait_for_timeout(2000)
    except Exception as e:
        print(str(e))
    finally:
        print('Code executed despite error')
