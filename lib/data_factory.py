import os
from lib.Data.data import Data
from lib.Data.dev_data import DevData
from lib.Data.prod_data import ProdData


class DataFactory:
    @staticmethod
    def get() -> Data:
        if 'API_ENV' not in os.environ:
            raise Exception("Cannot get API_ENV variable")

        if os.environ['API_ENV'] in ['dev', 'devel']:
            return DevData()
        elif os.environ['API_ENV'] in ['prod', 'production']:
            return ProdData()
        else:
            val = os.environ['API_ENV']
            raise Exception(f"No data for API_ENV={val}")
