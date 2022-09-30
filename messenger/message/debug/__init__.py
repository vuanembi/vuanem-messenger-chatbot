import json

from messenger.repository import send_message_response
from messenger.component import converse


def handler(messaging: dict):
    converse(debug_service, messaging)


def debug_service(messaging: dict):
    send_message_response(messaging["sender"]["id"], {"text": json.dumps(messaging)})
