from playwright.sync_api import Playwright
import json

# payload must be a valid Python dict (was JS-like syntax)
orderspayload = {
    "orders": [
        {"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}
    ]
}

class ApiUtils:
    def gettoken(self, playwright: Playwright, user_credentials):
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_req_context.post(
            "/api/ecom/auth/login",
            data=json.dumps({"userEmail": user_credentials["username"], 
                             "userPassword": user_credentials["password"]}),
            headers={"content-type": "application/json"},
        )
        assert response.ok
        responsebody = response.json()
        responsebodytoken = responsebody["token"]
        return responsebodytoken

    def createoder(self, playwright: Playwright, user_credentials):
        token = self.gettoken(playwright, user_credentials)
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_req_context.post(
            "/api/ecom/order/create-order",
            data=json.dumps(orderspayload),
            headers={"Authorization": token, "content-type": "application/json"},
        )
        response_body = response.json()
        orderid = response_body.get("orders", [None])[0]
        return orderid