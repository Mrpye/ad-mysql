"""Module for the adapter target classes. """

from activities_python.pythonutils.utils import check_input_params
from activities_python.pythonutils.utils import get_optional_value
import pymysql.cursor

class MySqlTarget(object):
    """Class representing the adapter target. """

   
    HOST = "host"
    DB ="db"
    CHARSET="charset"

    def fill_host(self, data):
        """Set the target host. """
        check_input_params(data, self.HOST)
        self.host = data[self.HOST]

    def fill_db(self,data):
        check_input_params(data, self.DB)
        self.db = data[self.DB]

    def fill_charset(self,data):
        check_input_params(data, self.DB)
        self.charset = get_optional_value(data,self.CHARSET,"utf8mb4")


    def __init__(self, data):
        self.fill_host(data)
        self.fill_charset(data)
        self.fill_db(data)
        self.cursor=pymysql.cursors.DictCursor