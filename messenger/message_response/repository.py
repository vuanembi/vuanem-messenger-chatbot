from messenger.repository import send_message


def send_message_response(recipient_id: str, message: dict) -> dict:
    payload = {
        "messaging_type": "RESPONSE",
        "message": message,
    }
    return send_message(recipient_id, payload)
