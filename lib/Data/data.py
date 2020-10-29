class Data:
    url = '???'

    def get_url(self):
        if self.url == '???':
            raise Exception("Cannot detect ENV")
        else:
            return self.url
