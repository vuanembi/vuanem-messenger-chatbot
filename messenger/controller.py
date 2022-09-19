from flask import Blueprint, request

from messenger.verify.service import verify_service
from messenger.message_response.router import message_response_router

messenger_controller = Blueprint("messenger", __name__)


@messenger_controller.get("/")
def verify_controller():
    query = request.args

    response = verify_service(query)
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
        handler = message_response_router
    else:
        handler = lambda _: True

    return handler(messaging)
