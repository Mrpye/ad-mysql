"""Module for events classes. """
#Change this to be your activities and your imports


from activities_python.actions.MySqlSelectQuery import MySqlSelectQuery
from activities_python.actions.verify_target import VerifyTargetQuery
from activities_python.constants.basic_constants import BasicConstants


def resolve_event(event_type, options):
    """Return the proper handler based on the event type. """

    if event_type == BasicConstants.VERIFY_TARGET_TYPE:
        handler = VerifyTargetQuery()
    elif event_type == BasicConstants.SELECT_TYPE:
        handler = MySqlSelectQuery()
    else:
        return None
    handler.create_logger(options)
    return handler
