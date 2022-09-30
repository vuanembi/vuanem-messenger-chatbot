from messenger.repository import send_message_response
from messenger.component import template


def send_store_location(messaging):
    send_message_response(
        messaging["sender"]["id"],
        {"attachment": template.store_location_attachment()},
    )
