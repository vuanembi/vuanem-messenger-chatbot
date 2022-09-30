import json

from messenger.repository import send_message_response


def debug_service(messaging):
    send_message_response(messaging["sender"]["id"], {"text": json.dumps(messaging)})
