import re

from messenger.messages import debug, echo
from messenger.component import quick_reply


def handler(messaging):
    message_text = messaging.get("message", {}).get("text", "")

    quick_reply.phone_number.handler(messaging)

    debug_match = re.search("\/debug (\w*)", message_text)

    if debug_match:
        debug.debug_service(messaging)
    else:
        echo.echo_service(messaging)

    return True
