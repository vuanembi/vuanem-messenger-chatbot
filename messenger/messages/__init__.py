import re

from messenger.messages import debug, echo
from messenger.component import quick_reply


def handler(messaging):
    message_text = messaging.get("message", {}).get("text", "")

    quick_reply.phone_number.handler(messaging)

    debug_match = re.search("\/debug (\w*)", message_text)

    if debug_match:
        return debug.debug_service.debug(messaging)
    else:
        return echo.echo_service.echo(messaging)
