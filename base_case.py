from requests import Response
from lib.data_factory import DataFactory
from lib.assetions_helper import AssertionsHelper
import allure


class BaseCase:
    assertion_helper = None

    def setup(self):
        # todo remove allure folder
        self.assertion_helper = AssertionsHelper()
        pass

    def teardown(self):
        pass

    @allure.step('Getting cookie {cookie_name}')
    def get_cookie(self, response: Response, cookie_name):
        cookies = {cookie_name: response.cookies[cookie_name]}
        return cookies

    def get_url(self) -> str:
        return DataFactory.get().get_url()
