"""Module for the sample adapter classes."""

from activities_python.common.action_support.base import BaseAction
from activities_python.pythonutils.models.MySqlTarget import MySqlTarget
from activities_python.pythonutils.models.MySqluser import MySqlUser
from activities_python.pythonutils.MySqlAdapter import MySqlAdapter
from activities_python.pythonutils.MySqlError import MySqlError


class VerifyTargetQuery(BaseAction):
    """Sample Class for verifying target."""

    def invoke(self, data, context):
        """Invoke this action class. """
        self.logger.info('Invoked VerifyTargetQuery')

        # Put your code here to get/parse some adapter properties.
        # Sample:
        target = MySqlTarget(data)
        user = MySqlUser(data)
        adapter = MySqlAdapter(target, self.logger)

        try:
            # Verify target here: (check password/token/etc , try to connect).
            # Sample:
            connection = adapter.connect_to_mysql(user)

            return {
                'verified': True,
            }
        except MySqlError as e:
            self.logger.error("Failed to verify target.Cause=%s", e.status_code, e.__cause__)
            self.raise_action_error(e.status_code, e.__cause__)
