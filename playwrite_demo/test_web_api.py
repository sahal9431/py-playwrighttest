from playwright.sync_api import Playwright, sync_playwright
# dynamically import ApiUtils to avoid static import resolution issues in editors/linters
from importlib import import_module
# file is named `apiBase.py` so import with the same casing
ApiUtils = import_module("utils.apiBase").ApiUtils

def test_web_e2e_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Perform API operations
    api_utils = ApiUtils()
    #api_utils.gettoken(playwright)
    oder_id = api_utils.createoder(playwright)
    #Login via UI
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("sergioaguero@gmail.com")
    page.locator("#userPassword").fill("Abcd@1234")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    row = page.locator("tr").filter(has_text=oder_id)
    row.get_by_role("button", name="View").click()
    assert page.locator(".tagline").text_content() == "Thank you for Shopping With Us"


