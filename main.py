from playwright.sync_api import sync_playwright

url1 = 'https://instagram.com'
url2 = 'https://www.youtube.com/@pdpuz/videos'
def instagram():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = browser.new_page()
        page.goto(url1)
        page.get_by_label('Phone number, username, or email').fill('your_username')
        page.get_by_label('Password').fill('your_password')
        page.click('button[type=submit]')
        page.get_by_role('button', name='Not Now', exact=True).click()
        page.get_by_role('button', name='Not Now', exact=True).click()
        page.get_by_text('Profile').click()


def youtube():
    with sync_playwright() as play:
        browser = play.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url2)
        dates = page.query_selector_all('#video-discription')

        j=1
        for i in dates[:5]:
            print(f'{j} vedio malumoti >> {i.text_content()}')
            j+=1

        page.wait_for_timeout(100000)