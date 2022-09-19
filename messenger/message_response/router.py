import re

from messenger.message_response.debug import service as debug_service

def message_response_router(messaging):
    message_text = messaging.get("messages", {}).get("text", "")

    debug_match = re.search("\/debug (\w*)", message_text)

    if debug_match:
        return debug_service.debug(messaging)

    return True
