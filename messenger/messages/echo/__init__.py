from messenger.messages.repository import send_message_response
from messenger.component import sender_action


def echo_service(messaging: dict):
    recipient_id = messaging["sender"]["id"]
    message_text = messaging["message"].get("text")

    if message_text:
        sender_action.mark_seen(recipient_id)
        sender_action.typing_on(recipient_id)
        send_message_response(recipient_id, {"text": message_text})
        sender_action.typing_off(recipient_id)
