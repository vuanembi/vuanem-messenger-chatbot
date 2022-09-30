import re

from messenger.message import debug
from messenger.component.quick_reply import phone_number, ice_breaker


def handler(messaging):
    message_text = messaging.get("message", {}).get("text", "")

    phone_number.handler(messaging)
    ice_breaker.handler(messaging)

    debug_match = re.search("\/debug (\w*)", message_text)

    if debug_match:
        debug.handler(messaging)

    return True
