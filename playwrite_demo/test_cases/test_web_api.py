from playwright.sync_api import Playwright, sync_playwright
# dynamically import  to avoid static import resolution issues in editors/linters
from importlib import import_module
#from utils.apibase import ApiUtils
# file is named `apiBase.py` so import with the same casing
ApiUtils = import_module("utils.apiBase").ApiUtils
LoginPage = import_module("pages.loginpage").LoginPage
import json
import pytest

#json credentials
with open("data/credentials.json") as file:
    data = json.load(file)
    print(data)
    user_credentials_list = data["usercredentials"]

@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_web_e2e_api(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Perform API operations
    api_utils = ApiUtils()
    #api_utils.gettoken(playwright)
    oder_id = api_utils.createoder(playwright, user_credentials)

    #Login via UI
    loginpage = LoginPage(page)
    loginpage.navigate()
    loginpage.login(user_credentials)
    page.get_by_role("button", name="ORDERS").click()
    row = page.locator("tr").filter(has_text=oder_id)
    row.get_by_role("button", name="View").click()
    assert page.locator(".tagline").text_content() == "Thank you for Shopping With Us"
    page.close()
    context.close()


