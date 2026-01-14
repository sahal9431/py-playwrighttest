from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time

# def test_playwrightBasics(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     browser_context = browser.new_context()
#     page = browser_context.new_page()
#     page.goto("https://www.google.com/")
#     page.wait_for_timeout(3000)
#     browser_context.close()

# def test_playwrightshortcut(page):
#     '''
#     it uses chromium by default in headless mode in 
#     single context and single page
#     '''
#     page.goto("https://www.google.com/")

# def test_coreLocators(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     #browser = playwright.firefox.launch(headless=False)
#     browser_context = browser.new_context()
#     page = browser_context.new_page()
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
#     username = page.get_by_label("Username").fill("rahulshettyacademy")
#     password = page.get_by_label("Password").fill("learning")
#     page.get_by_role("combobox").select_option("teach")
#     time.sleep(5)
#     page.locator("#terms").check()
#     #page.locator("text=Sign In").click()  alternative way to click                         
#     # for cssselector if there is id #then id  for class .then class
#     #page.get_by_role("link", name="Terms & Conditions").click()
#     page.get_by_role("button", name="Sign In").click()
#     #expect(page.get_by_text("Incorrect")).to_be_visible()
#     #expect(page.locator(".alert-danger")).to_contain_text("Incorrect")
#     iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
#     iphoneProduct.locator("text=Add").click()
#     nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
#     nokiaProduct.locator("text=Add").click()
#     time.sleep(5)
#     checkoutButton = page.get_by_text("Checkout").click()
#     time.sleep(5)
#     expect(page.locator(".media-body")).to_have_count(2)

# def test_childPageTest(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     browser_context = browser.new_context()
#     page = browser_context.new_page()
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
#     with page.expect_popup() as new_page_info:
#         page.locator(".blinkingText").click()
#         time.sleep(5)
#         child_page = new_page_info.value
#         text = child_page.locator(".red").text_content()
#         print(text)
#         word = text.split("at")
#         Email = word[1].strip().split(" ")[0]
#         assert Email == "mentor@rahulshettyacademy.com"
#         assert "mentor@rahulshettyacademy.com" in text

def test_ui_Validation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    browser_context = browser.new_context()
    page = browser_context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # page.get_by_placeholder("Hide/Show Example").is_visible()
    # page.get_by_role("button", name="Hide").click()
    # assert page.get_by_placeholder("Hide/Show Example").is_hidden()

    # #Alert Handling
    # page.get_by_role("button", name="Confirm").click()
    # time.sleep(10)
    # page.on("dialog", lambda dialog: dialog.accept())
    # #lambda fuction is used to create small anonymous function at runtime in single line

    # #Mouse Hovering
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

    
    # #Frames Handling
    # pageFrame = page.frame_locator("#courses-iframe")
    # pageFrame.get_by_role("link", name="All Access plan").click()
    # expect(pageFrame.locator("h2")).to_contain_text(" Happy Subscibers!")

    # page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # for index in range(page.locator("th").count()):
    #     if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
    #         pricecolmvalue = index
    #         break
    # riceRow = page.locator("tr").filter(has_text="Rice")
    # price = riceRow.locator("td").nth(pricecolmvalue).text_content()
    # assert price == "37"












