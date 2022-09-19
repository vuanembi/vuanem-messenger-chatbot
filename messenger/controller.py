import re

from flask import Blueprint, request

from messenger.verify.service import verify_service
from messenger.message_response.router import message_response_router

messenger_controller = Blueprint("messenger", __name__)


@messenger_controller.get("/")
def verify_controller():
    query = request.args
    return verify_service(query)


@messenger_controller.post("/")
def webhook_controller():
    data = request.get_json(silent=True)

    [handle_entry(entry) for entry in data["entry"]]

    return ("EVENT_RECEIVED", 200)


def handle_entry(entry):
    messaging = entry["messaging"].pop()

    if messaging.get('messages'):
        handler = message_response_router
    else:
        handler = lambda _: True

    return handler(messaging)
