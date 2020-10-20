# python -m pytest --alluredir=test_results/ test_auth.py
# allure serve test_results
from base_case import BaseCase
import requests
import allure


class TestAuth(BaseCase):
    @allure.description("Check getting auth cookie and making request with they")
    def test_auth_cookie(self):
        response = requests.post(self.main_url + "get_auth_cookie", {'login': "secret_login", 'password': "secret_pass"})
        self.assertion_helper.assert_code_status(response, 200, "Bad code")
        cookie = self.get_cookie(response, "auth_cookie")
        response = requests.post(self.main_url + "check_auth_cookie", {}, cookies=cookie)
        self.assertion_helper.assert_code_status(response, 200, "Bad code")
        self.assertion_helper.assert_response_text(response, "You are authorized", "Bad response text")

