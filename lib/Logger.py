from requests import Response


class Logger:
    data = ""

    def add(self, response: Response):
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

