from lib.Data.data import Data
from lib.Data.dev_data import DevData
from lib.Data.prod_data import ProdData


class DataFactory:
    @staticmethod
    def get() -> Data:
        # todo add ENV
        return ProdData()

