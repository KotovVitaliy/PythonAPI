# python -m pytest -s --alluredir=test_results/ test_headers.py
# allure serve test_results
from base_case import BaseCase
from lib.Request.request import Request
from lib.assetions_helper import AssertionsHelper
import allure


class TestHeaders(BaseCase):
    @allure.description("Check getting auth cookie and making request with they")
    def test_auth_cookie(self):
        response = Request.post(self.get_url() + "get_auth_cookie", {'login': "secret_login", 'password': "secret_pass"}, {}, {})

        AssertionsHelper.assert_code_status(response, 200, "Bad code")
        AssertionsHelper.assert_response_has_cookie(response, 'auth_cookie')
        cookie = self.get_cookie(response, "auth_cookie")

        response = Request.post(self.get_url() + "check_auth_cookie", {}, {}, cookie)

        AssertionsHelper.assert_code_status(response, 200, "Bad code")
        AssertionsHelper.assert_response_text(response, "You are authorized", "Bad response text")

    def test_headers(self):
        response = Request.post(self.get_url() + "show_all_headers", {}, {'ololo': '123'}, {})
        assert "X-THIS_IS_TEST" in response.text, "Cannot find test header amongst all headers in the response"

