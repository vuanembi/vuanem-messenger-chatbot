import re

from messenger.message_response.debug import service as debug_service
from messenger.message_response.echo import service as echo_service

def message_response_router(messaging):
    message_text = messaging.get("message", {}).get("text", "")

    debug_match = re.search("\/debug (\w*)", message_text)

    if debug_match:
        return debug_service.debug(messaging)
    else:
        return echo_service.echo(messaging)
