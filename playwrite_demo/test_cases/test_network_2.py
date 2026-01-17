from playwright.sync_api import Playwright, expect 
from importlib import import_module
import json
# file is named `apiBase.py` so import with the same casing
ApiUtils = import_module("utils.apiBase").ApiUtils

def intercept_response(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fbo")

def test_network2(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_response)
    page.locator("#userEmail").fill("sergioaguero@gmail.com")
    page.locator("#userPassword").fill("Abcd@1234")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    page.locator(".blink_me").get_by_text("You are not authorize to view this order").is_visible()
    page.close()

def test_session_storage(playwright: Playwright):
    api_token = ApiUtils().gettoken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Inject token into localStorage before any page loads; JSON-escape the token
    page.add_init_script(f"window.localStorage.setItem('token', {json.dumps(api_token)});")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    # Assert the Orders view is visible
    expect(page.get_by_text("Your Orders")).to_be_visible()
    page.close()