from flask import Blueprint, request

from messenger import verify, message, referral, postback

messenger_controller = Blueprint("messenger", __name__)


@messenger_controller.get("/")
def verify_controller():
    query = request.args

    response = verify.verify_service(query)
    return response if response else ("ok", 200)


@messenger_controller.post("/")
def webhook_controller():
    data = request.get_json(silent=True)

    print(data)

    [handle_entry(entry) for entry in data["entry"]]

    return ("EVENT_RECEIVED", 200)


def handle_entry(entry):
    messaging = entry["messaging"].pop()

    if messaging.get("message"):
        handler = message.handler

    elif messaging.get("referral"):
        handler = referral.handler

    elif messaging.get("postback"):
        handler = postback.handler
        
    else:
        handler = lambda _: True

    return handler(messaging)
