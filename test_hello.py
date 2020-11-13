# python -m pytest -x -s --alluredir=test_results/ test_hello.py
# allure serve test_results
import pytest
from base_case import BaseCase
from lib.Request.request import Request
from lib.assetions_helper import AssertionsHelper
import allure


class TestHello(BaseCase):
    @allure.description("Check hello w/o a name")
    def _test_hello_without_name(self):
        response = Request.get(self.get_url() + "hello", {}, {}, {})
        AssertionsHelper.assert_code_status(response, 200, "Bad code")
        AssertionsHelper.assert_response_text(response, "Hello, someone", "Bad response text")

    @allure.description("Check hello with a name")
    @pytest.mark.parametrize('name', ["Vitalii", "Bella", "Olga", "Svetlana"])
    def test_hello_with_name(self, name):
        response = Request.get(self.get_url() + "hello", {'name': name}, {}, {})
        AssertionsHelper.assert_code_status(response, 200, "Bad code")
        AssertionsHelper.assert_response_text(response, f'Hello, {name}', "Bad response text")



