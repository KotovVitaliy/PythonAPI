from requests import Response


class Logger:
    data = ""

    def add(self, response: Response):
        data_to_add = f"Response code: {response.status_code}\n"
        data_to_add += f"Response text: {response.text}\n"
        # data_to_add += f"Response headers: {response.headers}\n"
        # data_to_add += f"Response cookies: {response.cookies}\n"
        data_to_add += "\n-----\n"

        self.data += data_to_add

    def show_all_data(self):
        print(self.data)
        print("End of log")
