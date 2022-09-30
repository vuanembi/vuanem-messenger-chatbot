import re

from messenger.message import debug
from messenger.component import quick_reply


def handler(messaging):
    message_text = messaging.get("message", {}).get("text", "")

    quick_reply.phone_number.handler(messaging)

    debug_match = re.search("\/debug (\w*)", message_text)

    if debug_match:
        debug.handler(messaging)

    return True
