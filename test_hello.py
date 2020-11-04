# python -m pytest -s --alluredir=test_results/ test_headers.py
# allure serve test_results
from base_case import BaseCase
from lib.Request.request import Request
import requests
import allure


class TestHello(BaseCase):
    @allure.description("Check hello w/o a name")
    def test_hello_without_name(self):
        response = Request.get(self.get_url() + "hello", {}, {}, {})
        self.Logger.add(response)
        self.assertion_helper.assert_code_status(response, 200, "Bad code")
        self.assertion_helper.assert_response_text(response, "Hello, someone", "Bad response text")

    @allure.description("Check hello with a name")
    def test_hello_with_name(self):
        # todo add dataprovider
        name = "Vitalii"
        response = Request.get(self.get_url() + "hello", {'name': name}, {}, {})
        self.assertion_helper.assert_code_status(response, 200, "Bad code")
        self.assertion_helper.assert_response_text(response, f'Hello, {name}', "Bad response text")



