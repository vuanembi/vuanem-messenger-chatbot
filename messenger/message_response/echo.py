import json
from message_response.repository import send_message_response

def echo(messaging: dict) -> dict:
    return send_message_response(messaging["sender"]["id"], {"text": json.dumps(messaging)})