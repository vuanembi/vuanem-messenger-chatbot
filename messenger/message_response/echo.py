import json
from message_response.repository import send_message_response
from messenger.sender_action.repository import send_sender_action


def echo(messaging: dict) -> dict:
    send_sender_action("mark_seen")
    send_sender_action("typing_on")
    return send_message_response(messaging["sender"]["id"], {"text": json.dumps(messaging)})
