import datetime
import os
from requests import Response


class Logger:
    instance = None
    path = "logger.txt"
    data = ""

    def __init__(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def __del__(self):
        # todo почему-то не вызывается
        self.write_log_to_file()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def add(self, response: Response):
        # todo add testname
        # os.environ.get('PYTEST_CURRENT_TEST')

        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_to_add = f"\n-----\nResponse code: {response.status_code}\n"
        data_to_add += f"Response text: {response.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += "\n-----\n"

        self.data += data_to_add

    def show_all_data(self):
        if len(self.data) > 0:
            print("\n\nSTART OF LOG")
            print(self.data)
            print("END OF LOG\n\n")

    def write_log_to_file(self):
        with open(self.path, 'a', encoding='utf-8') as logger_file:
            logger_file.write(f'{str(datetime.datetime.now())}\n')
            logger_file.write(self.data)
