from messenger.repository import send_message_response
from messenger.component import converse


def handler(messaging: dict):
    recipient_id = messaging["sender"]["id"]
    message_text = messaging["message"].get("text")
    send_message_response(recipient_id, {"text": message_text})


def echo_service(messaging: dict):
    message_text = messaging["message"].get("text")

    if message_text:
        converse(handler, messaging)
