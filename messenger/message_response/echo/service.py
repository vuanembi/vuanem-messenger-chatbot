from messenger.message_response.repository import send_message_response
from messenger.sender_action.service import mark_seen, typing_on, typing_off


def echo(messaging: dict):
    recipient_id = messaging["sender"]["id"]
    message_text = messaging["message"].get("text")

    if message_text:
        mark_seen(recipient_id)
        typing_on(recipient_id)
        send_message_response(recipient_id, {"text": message_text})
        typing_off(recipient_id)

    return True
