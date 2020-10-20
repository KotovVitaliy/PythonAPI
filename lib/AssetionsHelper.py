import allure
from requests import Response


class AssertionsHelper:
    @allure.step('Asserting code response')
    def assert_code_status(self, response: Response, expected_code: int, message: str):
        assert response.status_code == expected_code, \
            f'Expected status code {expected_code}, but got {response.status_code}. {message}'

    @allure.step('Asserting response text')
    def assert_response_text(self, response: Response, expected_text: str, message: str):
        assert response.text == expected_text, \
            f'Expected response text {expected_text}, but got {response.text}. {message}'

    def assert_response_has_cookie(self, response: Response, name):
        pass
