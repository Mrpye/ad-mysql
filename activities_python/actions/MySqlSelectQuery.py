"""Module for the sample adapter classes. """

from activities_python.common.action_support.base import BaseAction
from activities_python.pythonutils.MySqlError import MySqlError
from activities_python.pythonutils.utils import check_input_params
from activities_python.pythonutils.MySqlAdapter import MySqlAdapter
from activities_python.pythonutils.models.MySqluser import MySqlUser
from activities_python.pythonutils.models.MySqlTarget import MySqlTarget


class MySqlSelectQuery(BaseAction):
    """Sample Class to demonstrator input and output parameters."""

    SELECTQUERY ="select_query"
    RETURNQUERY="return_query"
    ROWCOUNT="row_count"

    def invoke(self, data, context):
        """Invoke this action class. """
        self.logger.info('Invoked MySqlSelect Activity: {}'.format(data))
        check_input_params(data,self.SELECTQUERY)
        sql=data[self.SELECTQUERY]

        target=MySqlTarget(data)
        user=MySqlUser(data)
        adapter=MySqlAdapter(data)

        result = {}

        try:
            connection= adapter.connect_to_mysql(user)
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result[self.RETURNQUERY]=cursor.fetchall()
                result[self.ROWCOUNT] = len(result[self.RETURNQUERY])
                self.logger.info("Returning {} to Result Engine".format(result))

            return result
        except MySqlError as e:
            self.logger.error("Action failed. Cause=%s, Response=%s",  e.__cause__)
            self.raise_action_error("102" , e.__cause__)
        finally:
            connection.close()
