"""Module containting the template adapter classes.  """

import pymysql.cursors

class MySqlAdapter(object):
    """The Template Adapter class. """

    def __init__(self, target, logger):
        self.target = target
        self.logger = logger

    def connect_to_mysql(self,user):
        user_info = user.get_params()
        db_info = self.target.get_params()

        connection = pymysql.Connection(host=db_info['host'],
            password=user_info['password'],
            user=user_info['password'],
            db=db_info['db'],
            charset=db_info['charset'], cursorclass=db_info['cursor'])


    