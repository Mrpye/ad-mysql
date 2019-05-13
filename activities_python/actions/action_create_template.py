"""Module for the sample adapter classes. """

from activities_python.common.action_support.base import BaseAction
from activities_python.pythonutils.models.template_launch_params import MySqlLaunchParams
from activities_python.pythonutils.models.MySqlTarget import MySqlTarget
from activities_python.pythonutils.models.MySqluser import MySqlUser
from activities_python.pythonutils.MySqlAdapter import MySqlAdapter
from activities_python.pythonutils.MySqlError import MySqlError
from activities_python.pythonutils.utils import check_input_params


class ActionQuery2(BaseAction):
    """Sample Class for creating some template using post request with template_name parameter."""

    TEMPLATE_NAME = "template_name"

    def invoke(self, data, context):
        """Invoke this action class. """
        self.logger.info('Invoked ActionQuery2')
        check_input_params(data, self.TEMPLATE_NAME)
        template_name = data[self.TEMPLATE_NAME]
        target = MySqlTarget(data)
        user = MySqlUser(data)
        params = MySqlLaunchParams(data)
        template_adapter = MySqlAdapter(target, self.logger)
        try:
            token = template_adapter.get_auth_token(user, self.proxies)
            info = template_adapter.create_template(token, template_name, params, self.proxies)
            return info
        except MySqlError as e:
            self.logger.error("Action failed. Status=%s, Response=%s", e.status_code, e.response)
            self.raise_action_error(e.status_code, e.message)
