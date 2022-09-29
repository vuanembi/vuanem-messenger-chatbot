from messenger.repository import send_message


def send_sender_action(sender_action: str):
    def _send(recipient_id: str) -> dict:
        payload = {"sender_action": sender_action}
        return send_message(recipient_id, payload)

    return _send


mark_seen = send_sender_action("mark_seen")

typing_on = send_sender_action("typing_on")

typing_off = send_sender_action("typing_off")
