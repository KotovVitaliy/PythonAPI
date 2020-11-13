import requests
from lib.logger import Logger


class Request:
    @staticmethod
    def post(URL: str, data: dict, headers: dict, cookies: dict):
        return Request._send(URL, data, headers, cookies, 'post')

    @staticmethod
    def get(URL: str, data: dict, headers: dict, cookies: dict):
        return Request._send(URL, data, headers, cookies, 'get')

    @staticmethod
    def _send(URL: str, data: dict, headers: dict, cookies: dict, method: str):
        additional_header = {'X-THIS_IS_TEST': 'True'}
        headers.update(additional_header)

        if method == 'get':
            response = requests.get(URL, params=data, headers=headers, cookies=cookies)
        elif method == 'post':
            response = requests.post(URL, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f'Bad HTTP method "{method}" was received')

        Logger.get_instance().add(response)
        return response