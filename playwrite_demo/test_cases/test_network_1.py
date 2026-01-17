from playwright.sync_api import Page

fake_response = {"data":[],"message":"No Orders"}
def intercepted_response(route):
    route.fulfill(json=fake_response)

def test_network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercepted_response)
    page.locator("#userEmail").fill("sergioaguero@gmail.com")
    page.locator("#userPassword").fill("Abcd@1234")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.locator(".mt-4").get_by_text("You have No Orders to show").is_visible()