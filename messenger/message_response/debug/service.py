import json
import re

from messenger.message_response.repository import send_message_response
from messenger.message_response.echo import echo

def debug_send_message_response(messaging):
    send_message_response(messaging["sender"]["id"], {"text": json.dumps(messaging)})
    return True

def debug_echo(messaging):
    echo(messaging)
    return True