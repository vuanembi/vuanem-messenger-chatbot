import json

from messenger.message_response.repository import send_message_response


def debug_send_message_response(messaging):
    send_message_response(messaging["sender"]["id"], {"text": json.dumps(messaging)})
    return True
